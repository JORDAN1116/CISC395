# GEMINI.md - Lab 05: Debugging, Data, and AI Analysis

## 🎯 Lab Overview
Lab 05 focuses on three core technical skills:
1. **Algorithmic Debugging:** Identifying and fixing intentional logic errors in Python.
2. **File Organization:** Cleaning up a "messy" workspace using script automation.
3. **AI-Assisted Research:** Leveraging LLMs to summarize technical academic papers.

## 📂 Directory Structure & Context
- `code/`: Contains Python scripts for practice.
    - `buggy_sort.py`: Five intentional logic bugs in Bubble Sort, Binary Search, and list utilities.
    - `calculator.py`: A library of verified math functions for reference.
- `data/`: CSV datasets for processing.
    - `student_grades.csv`: Grade tracking data (S001-S020) for 4 labs and 2 exams.
- `messy/`: A collection of poorly named files (drafts, backups, and untitled documents) intended for a file-organization script exercise.
- `papers/`: PDF research papers for summarization.
    - `1706.03762v7.pdf`: "Attention Is All You Need" (Transformer architecture).

## 🤖 Agent Guidelines (Instructions)

### 1. Debugging Workflow
- When asked to fix `buggy_sort.py`, explain the logic error (e.g., off-by-one, incorrect variable scope) before applying the fix.
- Ensure all functions pass their logic tests after modification.

### 2. Data Processing
- `student_grades.csv` columns: `StudentID, Name, Lab1, Lab2, Lab3, Lab4, Midterm, Final, Total, Grade`.
- Use this file for any data analysis or automated reporting requests.

### 3. File Cleanup
- For the `messy/` folder, prioritize organization by file type (e.g., `.txt`, `.csv`, `.py`) or by extracting semantic meaning from chaotic filenames (e.g., "assignment_submission", "notes", "hw1").
- Suggest a dry-run or a summary of proposed renames before moving/deleting files.

### 4. Paper Analysis
- Use the PDF in the `papers/` directory as the primary source for summarization tasks.
- Focus summaries on the **Introduction**, **Key Architecture (Transformers)**, and **Conclusion**.

---
*This file is a foundational mandate for the Lab 05 workspace. Do not ignore these context instructions.*
