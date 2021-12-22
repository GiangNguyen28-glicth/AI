from tkinter import *
from Brute_Force import Brute_Force
from OnlyBacktracking import solve_sudoku_backtrack
from SolverSudoku import SolverSudoku

from input import Load, sudoku1, sudoku2, sudoku3

root = Tk()
root.geometry('275x283')



def str_to_puzzle(s):
    puzzleSolution = []
    for i in range(len(s)):
        if i % 9 == 0:
            temp = []
            for j in s[i:i + 9]:
                temp.append(int(j))
            puzzleSolution.append(temp)
    return puzzleSolution



class SolveSudoku:
    def __init__(self):
        self.allZero()


    # Set the empty cells to 0
    def allZero(self):
        for i in range(9):
            for j in range(9):
                if savedNumbers[i][j].get() not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    savedNumbers[i][j].set(0)

    def startSolution(self, val2):
        for i in range(9):
            for j in range(9):
                savedNumbers[i][j].set(val2[i][j])
class LoadSudoku:
    def __init__(self):
        self.allZero()
    # Set the empty cells to 0
    def allZero(self):
        for i in range(9):
            for j in range(9):
                if savedNumbers[i][j].get() not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    savedNumbers[i][j].set(0)

    def startSolution(self, val1):
        for i in range(9):
            for j in range(9):
                # tem=savedNumbers[i][j].get()
                savedNumbers[i][j].set(val1[i][j])
class Launch():
    def __init__(self, master):
        self.master = master
        master.title("Sudoku Solver")
        font = ('Arial', 18)
        color = 'white'
        px, py = 0, 0
        # Front-end Grid
        self.__table = []
        for i in range(1, 10):
            self.__table += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
        for i in range(0, 9):
            for j in range(0, 9):
                if (i < 3 or i > 5) and (j < 3 or j > 5):
                    color = 'gray'
                elif i in [3, 4, 5] and j in [3, 4, 5]:
                    color = 'gray'
                else:
                    color = 'white'
                self.__table[i][j] = Entry(master, width=2, font=font, bg=color, cursor='arrow', borderwidth=0,
                                            highlightthickness=1, highlightbackground='black',
                                           textvar=savedNumbers[i][j])
                self.__table[i][j].grid(row=i, column=j)
        self.__table = []
        # Front-End Menu
        menu = Menu(master)
        master.config(menu=menu)
        menu1 = Menu(menu)
        menu2 = Menu(menu)
        file = Menu(menu)
        menu.add_cascade(label='File', menu=file)
        file.add_command(label='Exit', command=master.quit)
        # file.add_command(label='Solve', command=self.solveInput)
        file.add_command(label='Clear', command=self.clearAll)
        menu.add_cascade(label='Level', menu=menu1)
        menu1.add_command(label='Easy',command=self.loadInputEasy)
        menu1.add_command(label='Medium', command=self.loadInputMedium)
        menu1.add_command(label='Hard', command=self.loadInputHard)
        menu.add_cascade(label='Solve', menu=menu2)
        menu2.add_command(label='CSP',command=self.solveCSP)
        menu2.add_command(label='Backtracking',command=self.solveBacktracking)
        menu2.add_command(label='Brute Froce', command=self.solveInputBF)
    # Clear the Grid
    def clearAll(self):
        for i in range(9):
            for j in range(9):
                savedNumbers[i][j].set('')
    # Calls the class SolveSudoku
    def solveInputBF(self):
        f1 = open("de.txt", "r")
        data1 = f1.read()
        val1=str_to_puzzle(data1)
        print("Brute Force")
        result=Brute_Force(val1)
        solution = SolveSudoku().startSolution(result)

    def solveBacktracking(self):
        f1 = open("de.txt", "r")
        data1 = f1.read()
        val1 = str_to_puzzle(data1)
        result=solve_sudoku_backtrack(val1)
        print("Is BackTrack")
        solution = SolveSudoku().startSolution(result)

    def solveCSP(self):
        f1 = open("de.txt", "r")
        data1 = f1.read()
        val2 = str_to_puzzle(data1)
        result = SolverSudoku(val2)
        print("Is CSP")
        solution = SolveSudoku().startSolution(result)
    def loadInputEasy(self):
        solution1 = Load(sudoku1)
        f1 = open("de.txt", "r")
        data1 = f1.read()
        val1 = str_to_puzzle(data1)
        solution1 = LoadSudoku().startSolution(val1)
    # Calls the class SolveSudoku
    def loadInputMedium(self):
        solution2 = Load(sudoku2)
        f1 = open("de.txt", "r")
        data1 = f1.read()
        val1 = str_to_puzzle(data1)
        solution2 = LoadSudoku().startSolution(val1)
    # Calls the class SolveSudoku
    def loadInputHard(self):
        solution3 = Load(sudoku3)
        f1 = open("de.txt", "r")
        data1 = f1.read()
        val1 = str_to_puzzle(data1)
        solution3 = LoadSudoku().startSolution(val1)

savedNumbers = []
for i in range(1, 10):
    savedNumbers += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
for i in range(0, 9):
    for j in range(0, 9):
        savedNumbers[i][j] = StringVar(root)
app = Launch(root)
root.mainloop()