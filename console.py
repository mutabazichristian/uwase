from place import Place
from placecollection import PlaceCollection
import random


def main():
    print("Travel Tracker 1.0 - by [Your Name]")
    places = PlaceCollection()
    places.load("places.csv")
    print(f"{len(places.places)} places loaded from places.csv")

    while True:
        print("\nMenu:")
        print("L - List places")
        print("A - Add new place")
        print("M - Mark a place as visited")
        print("Q - Quit")
        choice = input(">>> ").upper()

        if choice == "L":
            display_places(places)
        elif choice == "A":
            add_place(places)
        elif choice == "M":
            mark_place(places)
        elif choice == "Q":
            places.save("places.csv")
            print(f"{len(places.places)} places saved to places.csv")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")


def display_places(places):
    places.sort("priority")
    for place in places.places:
        print(
            f"{place.name:40} in {place.country:20} {'(visited)' if place.visited else ''}"
        )
    print(f"{places.get_number_unvisited()} places still to visit")


def add_place(places):
    name = input("Name: ")
    country = input("Country: ")
    while True:
        try:
            priority = int(input("Priority: "))
            if priority <= 0:
                print("Priority must be > 0")
                continue
            break
        except ValueError:
            print("Invalid input; enter a valid number")
    places.add(Place(name, country, priority, False))
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker")


def mark_place(places):
    unvisited = [place for place in places.places if not place.visited]
    if not unvisited:
        print("No unvisited places")
        return
    display_places(PlaceCollection())  # Display only unvisited places
    while True:
        try:
            choice = int(
                input("Enter the number of the place to mark as visited\n>>> ")
            )
            if 1 <= choice <= len(unvisited):
                place = unvisited[choice - 1]
                place.mark_visited()
                print(f"{place.name} in {place.country} visited!")
                break
            else:
                print("Invalid place number")
        except ValueError:
            print("Invalid input; enter a valid number")


if __name__ == "__main__":
    main()
