from Zadanie2 import *
import unittest


class TestPierwiastek(unittest.TestCase):
    """Test pierwiastek function."""

    def test_pierwiastek(self):
        self.assertEqual(pierwiastek(1), 1)
        self.assertEqual(pierwiastek(2), 1)
        self.assertEqual(pierwiastek(4), 2)
        self.assertEqual(pierwiastek(15), 3)
        self.assertEqual(pierwiastek(17), 4)
        self.assertEqual(pierwiastek(101), 10)


if __name__ == "__main__":
    unittest.main()
