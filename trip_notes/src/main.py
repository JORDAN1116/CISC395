import sys
import os

# Add the project root to sys.path so that 'src' can be imported regardless of where main.py runs from
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from src.models import Destination
from src.storage import load_trips, save_trips
from src.ai_assistant import ask, TRAVEL_SYSTEM_PROMPT, generate_trip_briefing, rag_ask
from src.rag import build_index

def main():
    collection = load_trips()
    
    while True:
        print("\n=== Trip Notes ===")
        print("\n-- Data --")
        print("[1] Add destination")
        print("[2] View all destinations")
        print("[3] Search by country")
        print("[4] Add note to a destination")
        print("[5] Mark as Visited")
        print("[6] Wishlist / Visited Stats")
        print("\n-- AI --")
        print("[7] Trip Briefing")
        print("[8] Ask AI a travel question")
        print("[9] Search my guides")
        print("\n[R] Rebuild search index")
        print("[Q] Quit")
        
        choice = input("\nChoice: ")
        
        if choice.lower() == "q":
            print("Goodbye!")
            break
            
        elif choice == "1":
            name = input("Destination name: ")
            country = input("Country: ")
            budget_str = input("Budget (in USD): ")
            try:
                budget = float(budget_str) if budget_str else 0.0
            except ValueError:
                print("Invalid budget, defaulting to 0.")
                budget = 0.0
            
            dest = Destination(name=name, country=country, budget=budget)
            collection.add(dest)
            save_trips(collection)
            print(f"Added {name} to your trips!")
            
        elif choice == "2":
            trips = collection.get_all()
            if not trips:
                print("No destinations yet.")
                continue
            for idx, dest in enumerate(trips):
                status = "Visited" if dest.visited else "Wishlist"
                print(f"[{idx}] {dest.name}, {dest.country} | Budget: ${dest.budget:.2f} | Added: {dest.date_added} | {status}")
                if dest.notes:
                    for note in dest.notes:
                        print(f"    - {note}")
                        
        elif choice == "3":
            country = input("Country to search for: ")
            matches = collection.search_by_country(country)
            if not matches:
                print("No matches found.")
            else:
                for dest in matches:
                    status = "Visited" if dest.visited else "Wishlist"
                    print(f"- {dest.name}, {dest.country} | Budget: ${dest.budget:.2f} | {status}")
                    
        elif choice == "4":
            trips = collection.get_all()
            if not trips:
                print("No destinations to add notes to.")
                continue
            for idx, dest in enumerate(trips):
                print(f"[{idx}] {dest.name}, {dest.country}")
                
            idx_str = input("Enter destination index: ")
            try:
                idx = int(idx_str)
                dest = collection.get_by_index(idx)
                note = input("Enter your note: ")
                dest.add_note(note)
                save_trips(collection)
                print("Note added!")
            except (ValueError, IndexError):
                print("Invalid index.")
                
        elif choice == "5":
            trips = collection.get_all()
            unvisited_exist = False
            for idx, dest in enumerate(trips):
                if not dest.visited:
                    print(f"[{idx}] {dest.name}, {dest.country}")
                    unvisited_exist = True
            if not unvisited_exist:
                print("No active wishlist destinations to mark as visited.")
                continue
                
            idx_str = input("Enter index of destination to mark as visited: ")
            try:
                idx = int(idx_str)
                collection.mark_visited(idx)
                save_trips(collection)
                print("Marked as visited!")
            except (ValueError, IndexError):
                print("Invalid index.")
                
        elif choice == "6":
            wishlist = collection.get_wishlist()
            visited = collection.get_visited()
            print(f"\n--- Visited: {len(visited)} ---")
            for dest in visited:
                 print(f"  {dest.name}, {dest.country}")
            print(f"\n--- Wishlist: {len(wishlist)} ---")
            for dest in wishlist:
                 print(f"  {dest.name}, {dest.country}")
                 
        elif choice == "7":
            destinations = collection.get_all()
            if not destinations:
                print("No trips saved yet.")
                continue
                
            for i, dest in enumerate(destinations, 1):
                print(f"  [{i}] {dest.name}, {dest.country}")
                
            try:
                index = int(input("Select trip number: ")) - 1
                if index < 0 or index >= len(destinations):
                    print("Invalid selection.")
                    continue
                
                dest = destinations[index]
                print(f"Generating briefing for {dest.name}...")
                
                result = generate_trip_briefing(dest.name, dest.country, dest.notes)
                if result is None:
                    print("Briefing failed. Check your API connection.")
                    continue
                    
                print(f"\n--- {dest.name} Briefing ---")
                print(f"Overview:\n{result['overview']}")
                print(f"\nPacking List:\n{result['packing_list']}")
            except ValueError:
                print("Invalid selection.")
                
        elif choice == "8":
            question = input("Your question: ")
            result = ask(question, system_prompt=TRAVEL_SYSTEM_PROMPT)
            if result is None:
                print("Failed to get an answer from AI.")
                continue
            
            print("\n" + result + "\n")
            
            save_ans = input("Save this as a note on a trip? (y/n): ")
            if save_ans.lower() == "y":
                trips = collection.get_all()
                if not trips:
                    print("No trips saved yet.")
                    continue
                for idx, dest in enumerate(trips):
                    print(f"[{idx + 1}] {dest.name}, {dest.country}")
                
                try:
                    trip_num = int(input("Trip number: ")) - 1
                    dest = collection.get_by_index(trip_num)
                    dest.add_note(result)
                    save_trips(collection)
                    print(f"Saved as a note on {dest.name}.")
                except (ValueError, IndexError):
                    print("Invalid trip number.")
                    
        elif choice == "9":
            question = input("Your question: ")
            result = rag_ask(question)
            print("\n" + result + "\n")
            
        elif choice.lower() == "r":
            print("Rebuilding index from guides/...")
            build_index(force=True)
            print("Done. Use [9] to search your updated guides.")
                 
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
