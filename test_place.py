import unittest
from place import Place


class TestPlace(unittest.TestCase):

    def setUp(self):
        self.place = Place("Test Name", "Test Country", 1)

    def test_init(self):
        self.assertEqual(self.place.name, "Test Name")
        self.assertEqual(self.place.country, "Test Country")
        self.assertEqual(self.place.priority, 1)
        self.assertFalse(self.place.visited)

    def test_str(self):
        self.assertEqual(
            str(self.place), "Test Name in Test Country, priority 1 (not visited)"
        )

    def test_mark_visited(self):
        self.place.mark_visited()
        self.assertTrue(self.place.visited)

    def test_mark_unvisited(self):
        self.place.mark_visited()
        self.place.mark_unvisited()
        self.assertFalse(self.place.visited)

    def test_is_important(self):
        self.assertTrue(self.place.is_important())
        self.place.priority = 3
        self.assertFalse(self.place.is_important())

    def test_lt(self):
        other_place = Place("Other", "Country", 2)
        self.assertTrue(self.place < other_place)
        self.assertFalse(other_place < self.place)


if __name__ == "__main__":
    unittest.main()
