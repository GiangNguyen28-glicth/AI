from Brute_Force import Brute_Force
from OnlyBacktracking import solve_sudoku, solve_sudoku_backtrack
from SolverSudoku import SolverSudoku
from input import sudoku1, sudoku2, sudoku3
import os
import platform
import sys
from time import time
from utils import print_board
platform_system = platform.system()
def clear_screen():
    if platform_system == 'Linux':
        os.system('clear')
    elif platform_system == 'Windows':
        os.system('cls')
while True:
    clear_screen()
    print("Algorithms :")
    print("    1- Simple backtracking")
    print("    2- Backtracking with MRV heuristic")
    print("    3- Brute_Force")
    print("    0- Exit")
    try:
        option = int(input("Enter a number: "))
        if option < 0 or option > 4:
            raise Exception
    except:
        continue
    break
if option == 0:
    sys.exit(0)
result = None

if option == 1:
    t = time()
    result=solve_sudoku_backtrack(sudoku3)
    t1 = time() - t
    print(t1)
    print_board(result)
elif option == 2:
    t = time()
    result =SolverSudoku(sudoku1)
    t1 = time() - t
    print(t1)
    print_board(result)
elif option == 3:
    t = time()
    result=Brute_Force(sudoku3)
    t1 = time() - t
    print(t1)
    print_board(result)
elif option == 4:
    l = [1, 2, 3, 5, 0]
    print(any(l))

    l = [True,False, False]
    print(any(l))

    l = [0, False, 8]
    print(any(l))

    l = []
    print(any(l))
