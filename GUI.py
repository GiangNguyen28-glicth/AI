import tkinter as tk
from tkinter import Entry, IntVar, Tk
def SquareCreate():
    sq = []
    for j in range(0, 9):
        for i in range(0, 9):
            data = IntVar()
            t = tk.Entry(main, textvariable=data, justify="center", font=("Arial", 16))
            ixtra = 0
            jxtra = 0
            if i > 2:
                ixtra = 4
            if i > 5:
                ixtra = 8
            if j > 2:
                jxtra = 4
            if j > 5:
                jxtra = 8
            t.place(x=i * 40 + 80 + ixtra, y=j * 40 + 80 + jxtra, width=40, height=40)
            t.delete(0)
            sq.append(data)
    return sq

def Chon():
    main.destroy()


def Backtracking():
    main.destroy()  # thuật toán


def Heuristic():
    main.destroy()  # thuật toán


def Thoat():
    main.destroy()


# mainprogramm
main = tk.Tk()
main.geometry("680x500")
main.resizable(width=0, height=0)
l = tk.Label(main, text="Welcome to the Game", fg="green", font=("Arial Bold", 20))
l.place(x=120, y=25)
button1 = tk.Button(main, text="New Game", fg="blue", font=("Arial Bold", 12), command=Chon)
button1.place(x=490, y=90)
button2 = tk.Button(main, text="Backtracking", fg="blue", font=("Arial Bold", 12), command=Backtracking)
button2.place(x=490, y=150)
button3 = tk.Button(main, text="Heuristic", fg="blue", font=("Arial Bold", 12), command=Heuristic)
button3.place(x=490, y=210)
button3 = tk.Button(main, text="Restart", fg="blue", font=("Arial Bold", 12), command=Thoat)
button3.place(x=490, y=270)
button4 = tk.Button(main, text="Sounds", fg="blue", font=("Arial Bold", 12), command=Thoat)
button4.place(x=490, y=330)
button4 = tk.Button(main, text="Quit Game", fg="blue", font=("Arial Bold", 12), command=Thoat)
button4.place(x=490, y=390)

SquareCreate()
main.mainloop()