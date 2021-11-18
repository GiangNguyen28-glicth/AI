import math
def IsSudoku(sudoku):
    for row in sudoku:
        for var in row:
            if var == 0:
                return False
    return True


def CheckConstraintSudoku(sudoku, row_i, col_j, value):
    for var in sudoku[row_i]:
        if value != 0 and var == value:
            return False
    for row in sudoku:
        if row[col_j] != 0 and row[col_j] == value:
            return False
    sqrt_n = int(math.sqrt(len(sudoku)))
    block_i = int(row_i / sqrt_n)
    block_j = int(col_j / sqrt_n)
    qs = range(sqrt_n)
    for i in [block_i * sqrt_n + q for q in qs]:
        for j in [block_j * sqrt_n + q for q in qs]:
            if (i, j) != (i, j) and sudoku[i][j] != 0 and sudoku[i][j] == value:
                return False
    return True