from Zadanie1 import *
import unittest


class TestIterator(unittest.TestCase):
    """Test functions using iterators"""

    def test_pierwsze(self):
        self.assertEqual(pierwsze_iterator(40), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])

    def test_doskonale(self):
        self.assertEqual(list(doskonale_iterator(10000)), [6, 28, 496, 8128])


if __name__ == "__main__":
    unittest.main()
