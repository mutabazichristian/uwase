import unittest
from placecollection import PlaceCollection
from place import Place
import os


class TestPlaceCollection(unittest.TestCase):

    def setUp(self):
        self.collection = PlaceCollection()
        self.place1 = Place("Test1", "Country1", 1)
        self.place2 = Place("Test2", "Country2", 2, True)
        self.collection.add(self.place1)
        self.collection.add(self.place2)

    def test_add(self):
        self.assertEqual(len(self.collection.places), 2)

    def test_get_number_unvisited(self):
        self.assertEqual(self.collection.get_number_unvisited(), 1)

    def test_sort(self):
        self.collection.sort("name")
        self.assertEqual(self.collection.places[0].name, "Test1")
        self.assertEqual(self.collection.places[1].name, "Test2")

        self.collection.sort("country")
        self.assertEqual(self.collection.places[0].country, "Country1")
        self.assertEqual(self.collection.places[1].country, "Country2")

        self.collection.sort("priority")
        self.assertEqual(self.collection.places[0].priority, 1)
        self.assertEqual(self.collection.places[1].priority, 2)

    def test_load_save(self):
        filename = "test_places.csv"
        self.collection.save(filename)
        new_collection = PlaceCollection()
        new_collection.load(filename)
        self.assertEqual(len(new_collection.places), 2)
        self.assertEqual(new_collection.places[0].name, "Test1")
        self.assertEqual(new_collection.places[1].name, "Test2")
        os.remove(filename)

    def test_str(self):
        self.assertEqual(str(self.collection), "2 places in collection")


if __name__ == "__main__":
    unittest.main()
