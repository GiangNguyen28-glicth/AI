from AC3 import AC3
from backtrack import recursive_backtrack_algorithm
from sudoku import Sudoku
from utils import fetch_sudokus, convert

def solve(grid,index,total):
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
            print("{}/{} : AC3 finished, Backtracking starting...".format(index, total))
            assignment = {}
            # for the already known values
            for cell in sudoku.cells:
                if len(sudoku.possibilities[cell]) == 1:
                    assignment[cell] = sudoku.possibilities[cell][0]
            # start backtracking
            assignment = recursive_backtrack_algorithm(assignment, sudoku)

            # merge the computed values for the cells at one place
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
    sudoku_queue = fetch_sudokus(listr)
    result4 = solve(listr, 1, len(sudoku_queue))
    return  result4