from Zadanie5 import *
import unittest


class TestKompresja(unittest.TestCase):
    """Test kompresja function."""

    def test_kompresja(self):
        self.assertEqual(kompresja("suuuuper"), "s4uper")
        self.assertEqual(kompresja("aaabttbabcc"), "3ab2tbab2c")


class TestDekompresja(unittest.TestCase):
    """Test dekompresja function."""

    def test_dekompresja(self):
        self.assertEqual(dekompresja("s4uper"), "suuuuper")
        self.assertEqual(dekompresja("3ab2tbab2c"), "aaabttbabcc")


if __name__ == "__main__":
    unittest.main()
