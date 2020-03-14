from Zadanie4 import *
import unittest

tekst = "Podział peryklinalny inicjałów wrzecionowatych \
kambium charakteryzuje się ścianą podziałową inicjowaną \
w płaszczyźnie maksymalnej."


class TestUproscZdanie(unittest.TestCase):
    """Test uprosc_zdanie function."""

    def test_uprosczdanie(self):
        words = uprosc_zdanie(tekst, 10, 5).split()
        maxlenght = max(len(word) for word in words)
        self.assertTrue(len(words) <= 5)
        self.assertTrue(maxlenght <= 10)

    def test_uprosctadeusz(self):
        f = open("pan-tadeusz.txt", "r")
        if f.mode == "r":
            words = uprosc_zdanie(f.read(), 10, 20).split()
            maxlenght = max(len(word) for word in words)
            self.assertTrue(len(words) <= 20)
            self.assertTrue(maxlenght <= 10)
        f.close()


if __name__ == "__main__":
    unittest.main()
