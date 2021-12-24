from AC3 import AC3
from backtrack import recursive_backtrack_algorithm
from sudoku import Sudoku
from utils import convert

def solve(grid):
    sudoku = Sudoku(grid)
    AC3_result = AC3(sudoku)
    if not AC3_result:
        print("No solution")
    else:
        if sudoku.isFinished():
            for cell in sudoku.possibilities:
                sudoku.possibilities[cell] = sudoku.possibilities[cell][0]
            result3 = result(sudoku)
            return result3
        else:
            print("{}/{} : AC3 finished, Backtracking starting...")
            assignment = {}
            for cell in sudoku.cells:
                if len(sudoku.possibilities[cell]) == 1:
                    assignment[cell] = sudoku.possibilities[cell][0]
            assignment = recursive_backtrack_algorithm(assignment, sudoku)
            for cell in sudoku.possibilities:
                sudoku.possibilities[cell] = assignment[cell]
            if assignment:
               result3=result(sudoku)
               return  result3
def result(self):
        su=[[],[],[],[],[],[],[],[],[]]
        index=0
        for i in range(9):
            for j in range(9):
                temp=self.possibilities[self.cells[index]]
                su[i].append(temp)
                index = index + 1
        return su
def SolverSudoku(sudoku):
    listr = convert(sudoku)
    result4 = solve(listr)
    return result4