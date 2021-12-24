from utils import StaticClass

def draw(puzzle):
    for r in range(len(puzzle)):
        for c in range(len(puzzle[r])):
            if puzzle[r][c] != 0:
                StaticClass.temp[r].append(puzzle[r][c])


def str_to_puzzle(s):
    puzzleSolution = []
    for i in range(len(s)):
        if i % 9 == 0:
            temp = []
            for j in s[i:i + 9]:
                temp.append(int(j))
            puzzleSolution.append(temp)
    return puzzleSolution


def same_row(i, j):
    if i // 9 == j // 9:
        return True
    return False


def same_col(i, j):
    if i % 9 == j % 9:
        return True
    return False


def same_block(i, j):
    if ((i // 9) // 3 == (j // 9) // 3) & ((i % 9) // 3 == (j % 9) // 3):
        return True
    return False


def sudoku_brute_force(s):
    i = s.find('0')
    cannotuse = {s[j] for j in range(len(s)) if same_row(i, j) | same_col(i, j) | same_block(i, j)}
    every_possible_values = {str(i) for i in range(10)} - cannotuse
    for val in every_possible_values:
        s = s[0:i] + val + s[i + 1:]
        sudoku_brute_force(s)
        if s.find('0') == -1:
            draw(str_to_puzzle(s))

def Brute_Force(sudoku):
    s = ''.join(map(str, [''.join(map(str, i)) for i in sudoku]))
    StaticClass.temp = [[], [], [], [], [], [], [], [], []]
    sudoku_brute_force(s)
    return StaticClass.temp
