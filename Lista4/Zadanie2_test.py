from Zadanie2 import *
import unittest


class TestDoskonale(unittest.TestCase):
    """Test functions about generating ideal numbers"""

    def test_imperatywna(self):
        self.assertEqual(doskonale_imperatywna(10000), [6, 28, 496, 8128])

    def test_skladana(self):
        self.assertEqual(doskonale_skladana(10000), [6, 28, 496, 8128])

    def test_funkcyjna(self):
        self.assertEqual(doskonale_funkcyjna(10000), [6, 28, 496, 8128])




if __name__ == "__main__":
    unittest.main()
