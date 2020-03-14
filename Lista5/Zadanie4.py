import itertools
import copy

possible = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def is_col_correct(j, sudoku):
    col = [row[j] for row in sudoku]
    for i in range(1, 10):
        if col.count(i) != 1:
            return False
    return True


def is_square_correct(k, sudoku):
    square = []
    for row in range(3 * (k // 3), 3 * (k // 3 + 1)):
        for col in range(3 * (k % 3), 3 * ((k % 3) + 1)):
            square.append(sudoku[row][col])
    for i in range(1, 10):
        if square.count(i) != 1:
            return False
    return True


def is_sudoku_correct(sudoku):
    for i in range(0, 9):
        if not (is_square_correct(i, sudoku) and is_col_correct(i, sudoku)):
            return False
    return True


def row_possible(m, sudoku):
    return possible - set(sudoku[m])


def insert_row(n, arg, sudoku):
    j = 0
    for i in range(0, 9):
        if sudoku[n][i] == 0:
            sudoku[n][i] = arg[j]
            j += 1


def solve_sudoku(sudoku_to_solve):
    temp = copy.deepcopy(sudoku_to_solve)
    possible_row0 = list(itertools.permutations(list(row_possible(0, temp))))
    possible_row1 = list(itertools.permutations(list(row_possible(1, temp))))
    possible_row2 = list(itertools.permutations(list(row_possible(2, temp))))
    possible_row3 = list(itertools.permutations(list(row_possible(3, temp))))
    possible_row4 = list(itertools.permutations(list(row_possible(4, temp))))
    possible_row5 = list(itertools.permutations(list(row_possible(5, temp))))
    possible_row6 = list(itertools.permutations(list(row_possible(6, temp))))
    possible_row7 = list(itertools.permutations(list(row_possible(7, temp))))
    possible_row8 = list(itertools.permutations(list(row_possible(8, temp))))
    possible_rows = itertools.product(possible_row0, possible_row1, possible_row2, possible_row3, possible_row4,
                                      possible_row5, possible_row6, possible_row7, possible_row8)
    while True:
        temp = copy.deepcopy(sudoku_to_solve)
        current_rows = next(possible_rows)
        for i in range(0, 9):
            insert_row(i, current_rows[i], temp)
        if is_sudoku_correct(temp):
            return temp


def print_sudoku(sudoku):
    for i in range(9):
        if i == 3 or i == 6:
            print("-----+------+-----")
        for j in range(9):
            if j == 2 or j == 5:
                print(str(sudoku[i][j]) + "|", end=" ")
            else:
                print(str(sudoku[i][j]), end=" ")
        print("")


sudoku = [[0, 0, 4, 0, 0, 0, 9, 1, 2],
           [6, 0, 2, 0, 9, 5, 0, 4, 8],
           [1, 0, 8, 3, 4, 2, 0, 6, 7],
           [8, 5, 9, 0, 6, 0, 4, 2, 0],
           [4, 0, 6, 8, 5, 0, 7, 9, 1],
           [7, 1, 0, 9, 2, 0, 8, 5, 6],
           [9, 6, 0, 5, 3, 7, 2, 8, 0],
           [2, 8, 7, 0, 1, 9, 6, 3, 0],
           [3, 0, 5, 2, 0, 6, 0, 7, 9]]

s = solve_sudoku(sudoku)
print_sudoku(s)
print("")
solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]
print_sudoku(solution)
