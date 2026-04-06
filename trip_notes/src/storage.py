import json
import os
from .models import Destination, TripCollection

# Create data directory if it doesn't exist
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "trips.json")

def load_trips() -> TripCollection:
    collection = TripCollection()
    if not os.path.exists(DATA_FILE):
        return collection
    
    with open(DATA_FILE, "r") as f:
        try:
            data = json.load(f)
            for item in data:
                kwargs = {
                    "name": item["name"],
                    "country": item["country"],
                    "budget": item.get("budget", 0.0),
                }
                if "notes" in item: kwargs["notes"] = item["notes"]
                if "date_added" in item: kwargs["date_added"] = item["date_added"]
                if "visited" in item: kwargs["visited"] = item["visited"]
                dest = Destination(**kwargs)
                collection.add(dest)
        except json.JSONDecodeError:
            pass
            
    return collection

def save_trips(collection: TripCollection) -> None:
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        
    data = []
    for trip in collection.get_all():
        data.append({
            "name": trip.name,
            "country": trip.country,
            "budget": trip.budget,
            "notes": trip.notes,
            "date_added": trip.date_added,
            "visited": trip.visited
        })
        
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
