import sys
def is_different(cell_i, cell_j):
    result = cell_i != cell_j
    return result
def number_of_conflicts(sudoku, cell, value):
    count = 0
    for related_c in sudoku.related_cells[cell]:
        if len(sudoku.possibilities[related_c]) > 1 and value in sudoku.possibilities[related_c]:
            count += 1
    temp = count
    return count


def is_consistent(sudoku, assignment, cell, value):
    is_consistent = True
    for current_cell, current_value in assignment.items():
        if current_value == value and current_cell in sudoku.related_cells[cell]:
            is_consistent = False
            break;
    return is_consistent
def assign(sudoku, cell, value, assignment):
    assignment[cell] = value
    if sudoku.possibilities:
        forward_check(sudoku, cell, value, assignment)


def unassign(sudoku, cell, assignment):
    if cell in assignment:
        for (coord, value) in sudoku.pruned[cell]:
            sudoku.possibilities[coord].append(value)
        sudoku.pruned[cell] = []
        del assignment[cell]

def forward_check(sudoku, cell, value, assignment):
    for related_c in sudoku.related_cells[cell]:
        if related_c not in assignment:
            if value in sudoku.possibilities[related_c]:
                sudoku.possibilities[related_c].remove(value)
                sudoku.pruned[cell].append((related_c, value))
def fetch_sudokus(input):
    DEFAULT_SIZE = 81
    if (len(input) % DEFAULT_SIZE) != 0:
        print("Error : the string must be a multiple of {}".format(DEFAULT_SIZE))
        sys.exit()
    else:
        formatted_input = input.replace("X", "0").replace("#", "0").replace("@", "0")
        if not formatted_input.isdigit():
            print("Error : only the following characters are allowed: [1,9], 'X', '#' and '@'")
            sys.exit()
        else:
            return [formatted_input[i:i + DEFAULT_SIZE] for i in range(0, len(formatted_input), DEFAULT_SIZE)]
def convert(sudoku):
    liststr=""
    defaulsize=9
    for i in range(defaulsize):
        for j in range(defaulsize):
            liststr+=str(sudoku[i][j])
    return liststr
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
def str_to_puzzle(s):
    puzzleSolution = []
    for i in range(len(s)):
        if i % 9 == 0:
            temp = []
            for j in s[i:i + 9]:
                temp.append(int(j))
            puzzleSolution.append(temp)
    return puzzleSolution
class StaticClass:
    temp=[[],[],[],[],[],[],[],[],[]]