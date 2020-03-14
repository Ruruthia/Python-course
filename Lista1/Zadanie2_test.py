from Zadanie2 import *
import unittest


class TestMinCoin(unittest.TestCase):
    """Test min_coin function"""

    def test_min_coins(self):
        self.assertEqual(min_coins([1, 2, 5, 10], 123), (14, [1, 2, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
        self.assertEqual(min_coins([1, 2, 5], 123),
                         (26, [1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
        self.assertEqual(min_coins([3, 10], 77), (14, [3, 3, 3, 3, 3, 3, 3, 3, 3, 10, 10, 10, 10, 10]))

if __name__ == "__main__":
    unittest.main()
