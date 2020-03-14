from Zadanie4 import *
import unittest

sudoku = [[0, 0, 4, 0, 0, 0, 9, 1, 2],
           [6, 0, 2, 0, 9, 5, 0, 4, 8],
           [1, 0, 8, 3, 4, 2, 0, 6, 7],
           [8, 5, 9, 0, 6, 0, 4, 2, 0],
           [4, 0, 6, 8, 5, 0, 7, 9, 1],
           [7, 1, 0, 9, 2, 0, 8, 5, 6],
           [9, 6, 0, 5, 3, 7, 2, 8, 0],
           [2, 8, 7, 0, 1, 9, 6, 3, 0],
           [3, 0, 5, 2, 0, 6, 0, 7, 9]]

solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]

class TestSudoku(unittest.TestCase):
    """Test sudoku solving functions"""

    def test_is_sudoku_correct(self):
        self.assertTrue(is_sudoku_correct(solution))
        self.assertFalse(is_sudoku_correct(sudoku))

    def test_solve_sudoku(self):
        self.assertEqual(solve_sudoku(sudoku), solution)


if __name__ == "__main__":
    unittest.main()


