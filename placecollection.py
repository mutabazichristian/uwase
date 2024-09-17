from place import Place
from operator import attrgetter
import csv


class PlaceCollection:
    def __init__(self):
        self.places = []

    def load(self, filename):
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                name, country, priority, visited = row
                self.add(Place(name, country, int(priority), visited.lower() == "true"))

    def save(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for place in self.places:
                writer.writerow(
                    [place.name, place.country, place.priority, place.visited]
                )

    def add(self, place):
        self.places.append(place)

    def get_number_unvisited(self):
        return sum(1 for place in self.places if not place.visited)

    def sort(self, key):
        self.places.sort(key=attrgetter(key, "priority"))

    def __str__(self):
        return f"{len(self.places)} places in collection"
