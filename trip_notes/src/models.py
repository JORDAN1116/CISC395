from dataclasses import dataclass, field
from datetime import date
from typing import List

@dataclass
class Destination:
    name: str
    country: str
    budget: float
    notes: List[str] = field(default_factory=list)
    date_added: str = field(default_factory=lambda: date.today().isoformat())
    visited: bool = False

    def add_note(self, note: str) -> None:
        self.notes.append(note)

class TripCollection:
    def __init__(self):
        self._trips: List[Destination] = []

    def __len__(self) -> int:
        return len(self._trips)

    def add(self, destination: Destination) -> None:
        self._trips.append(destination)

    def get_all(self) -> List[Destination]:
        return self._trips

    def search_by_country(self, query: str) -> List[Destination]:
        query_lower = query.lower()
        return [trip for trip in self._trips if trip.country.lower() == query_lower]

    def get_by_index(self, index: int) -> Destination:
        return self._trips[index]

    def get_wishlist(self) -> List[Destination]:
        return [trip for trip in self._trips if not trip.visited]

    def get_visited(self) -> List[Destination]:
        return [trip for trip in self._trips if trip.visited]

    def mark_visited(self, index: int) -> None:
        self._trips[index].visited = True
