import os
from pathlib import Path

import chromadb
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer

GUIDES_DIR = "guides"
DB_PATH = "chroma_db"
COLLECTION = "trip_guides"
CHUNK_SIZE = 200
CHUNK_OVERLAP = 30

def read_file(path: str) -> str:
    path_obj = Path(path)
    text = ""
    try:
        if path_obj.suffix.lower() in [".txt", ".md"]:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
        elif path_obj.suffix.lower() == ".pdf":
            reader = PdfReader(path)
            pages = []
            for page in reader.pages:
                pages.append(page.extract_text() or "")
            text = "\n".join(pages)
    except Exception as e:
        print(f"Warning: could not read {path_obj.name}: {e}")
        return ""
        
    if not text.strip():
        print(f"Warning: {path_obj.name} has no extractable text (scanned PDF?), skipping.")
        return ""
        
    return text

def chunk_text(text: str, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP) -> list[str]:
    words = text.split()
    chunks = []
    if not words:
        return chunks
        
    step = max(1, chunk_size - overlap)
    for i in range(0, len(words), step):
        chunk = " ".join(words[i:i + chunk_size])
        if chunk:
            chunks.append(chunk)
            
    return chunks

def build_index(force: bool = False):
    guides_path = Path(GUIDES_DIR)
    if not guides_path.exists() or not guides_path.is_dir():
        print("Error: guides/ folder not found.")
        return
        
    client = chromadb.PersistentClient(path=DB_PATH)
    
    if force:
        try:
            client.delete_collection(name=COLLECTION)
        except Exception:
            pass
            
    collection = client.get_or_create_collection(name=COLLECTION)
    
    files = []
    for ext in [".txt", ".md", ".pdf"]:
        files.extend(guides_path.glob(f"*{ext}"))
        files.extend(guides_path.glob(f"*{ext.upper()}"))
        
    if not files:
        print("Warning: no supported files found in guides/.")
        return
        
    model = SentenceTransformer("all-MiniLM-L6-v2")
    
    total_chunks_added = 0
    files_with_chunks = 0
    
    for file_path in files:
        text = read_file(str(file_path))
        if not text:
            continue
            
        chunks = chunk_text(text)
        if not chunks:
            continue
            
        existing_ids = set()
        if not force:
            existing_data = collection.get()
            if existing_data and "ids" in existing_data:
                existing_ids = set(existing_data["ids"])
                
        ids_to_add = []
        documents_to_add = []
        
        for i, chunk in enumerate(chunks):
            chunk_id = f"{file_path.stem}_chunk_{i}"
            if not force and chunk_id in existing_ids:
                continue
            
            ids_to_add.append(chunk_id)
            documents_to_add.append(chunk)
            
        if ids_to_add:
            embeddings = model.encode(documents_to_add).tolist()
            collection.add(
                ids=ids_to_add,
                documents=documents_to_add,
                embeddings=embeddings
            )
            total_chunks_added += len(ids_to_add)
            files_with_chunks += 1
            
    print(f"Indexed {total_chunks_added} chunks from {files_with_chunks} files.")

def ensure_index() -> object:
    client = chromadb.PersistentClient(path=DB_PATH)
    collection = client.get_or_create_collection(name=COLLECTION)
    if collection.count() == 0:
        print("No index found. Building from guides/...")
        build_index()
    return collection

def search_guides(query: str, n_results: int = 3) -> list[str]:
    collection = ensure_index()
    count = collection.count()
    if count == 0:
        return []
        
    model = SentenceTransformer("all-MiniLM-L6-v2")
    vector = model.encode(query).tolist()
    
    n_results = min(n_results, count)
    results = collection.query(query_embeddings=[vector], n_results=n_results)
    
    if results and "documents" in results and results["documents"]:
        return results["documents"][0]
    return []

if __name__ == "__main__":
    build_index()