from Zadanie1 import *
import unittest


class TestPierwsze(unittest.TestCase):
    """Test functions about generating prime numbers"""

    def test_imperatywna(self):
        self.assertEqual(pierwsze_imperatywna(40), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])

    def test_skladana(self):
        self.assertEqual(pierwsze_skladana(40), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])

    def test_funkcyjna(self):
        self.assertEqual(pierwsze_funkcyjna(40), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])




if __name__ == "__main__":
    unittest.main()
