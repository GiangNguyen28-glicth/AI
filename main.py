from OnlyBacktracking import solve, print_board
from SolverSudoku import SolverSudoku
from input import sudoku
import os
import platform
import sys
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
    print("    3- Backtracking with MRV and degree heuristic")
    print("    4- Minimum conflicts local search\n")
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
    result = solve(sudoku)
    print_board(result)
elif option == 2:
    result =SolverSudoku(sudoku)
    print_board(result)
elif option == 3:
    temp=0
elif option == 4:
        sys.exit(0)
