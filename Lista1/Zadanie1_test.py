from Zadanie1 import *
import unittest

ZAKUPY = [0.2, 0.5, 4.59, 6]


class TestVatFaktura(unittest.TestCase):
    """Test vat_faktura function."""

    def test_vat(self):
        self.assertEqual(vat_faktura(ZAKUPY), 2.6)


class TestVatParagon(unittest.TestCase):
    """Test vat_paragon function."""

    def test_vat(self):
        self.assertEqual(vat_paragon(ZAKUPY), 2.61)


class TestVat(unittest.TestCase):
    """Test if both function return same/similar results."""

    def test_vat(self):
        self.assertFalse(vat_paragon(ZAKUPY) == vat_faktura(ZAKUPY))
        self.assertEqual(round(vat_paragon(ZAKUPY) - vat_faktura(ZAKUPY), 1), 0)


if __name__ == "__main__":
    unittest.main()
