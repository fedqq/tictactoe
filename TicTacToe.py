from tkinter import *
from tkinter import ttk

GAME_SIZE = 600
left = ['1', '2', '3']
middle = ['4', '5', '6']
right = ['7', '8', '9']
checked = []

player1 = True

def winGame(player):
    global canvas
    canvas.destroy()
    del canvas
    window.geometry("700x50")
    win_text = Label(window, text="Player {} Won The Game!".format(player[-1]), font = ("Arial", 30), bg = "#a8d44c", fg = "#ffffff")
    win_text.pack()

def checkColumn(column):
    if column[0] == column[1] == column[2]:
        winGame(column[0])

def checkRow(row):
    if left[row] == middle[row] == right[row]:
        winGame(left[row])

def updateTxt():
    str = ''
    if player1:
        str = '1'
    else:
        str = '2'
    label.config(text = "Player: {}".format(str))

def click(row, column):
    if (row, column) in checked:
        return
    else:
        checked.append((row, column))
    global player1
    if row == 1:
        if column == 1:
            if player1:
                topLeft.configure(image = XIMGFILE)
                left[0] = 'player1'
            else: 
                topLeft.configure(image = OIMGFILE)
                left[0] = 'player2'
        if column == 2:
            if player1:
                topMiddle.configure(image = XIMGFILE)
                middle[0] = 'player1'
            else: 
                topMiddle.configure(image = OIMGFILE)
                middle[0] = 'player2'
        if column == 3:
            if player1:
                topRight.configure(image = XIMGFILE)
                right[0] = 'player1'
            else: 
                topRight.configure(image = OIMGFILE)
                right[0] = 'player2'

    if row == 2:
        if column == 1:
            if player1:
                middleLeft.configure(image = XIMGFILE)
                left[1] = 'player1'
            else: 
                middleLeft.configure(image = OIMGFILE)
                left[1] = 'player2'
        if column == 2:
            if player1:
                middleMiddle.configure(image = XIMGFILE)
                middle[1] = 'player1'
            else: 
                middleMiddle.configure(image = OIMGFILE)
                middle[1] = 'player2'
        if column == 3:
            if player1:
                middleRight.configure(image = XIMGFILE)
                right[1] = 'player1'
            else: 
                middleRight.configure(image = OIMGFILE)
                right[1] = 'player2'

    if row == 3:
        if column == 1:
            if player1:
                bottomLeft.configure(image = XIMGFILE)
                left[2] = 'player1'
            else: 
                bottomLeft.configure(image = OIMGFILE)
                left[2] = 'player2'
        if column == 2:
            if player1:
                bottomMiddle.configure(image = XIMGFILE)
                middle[2] = 'player1'
            else: 
                bottomMiddle.configure(image = OIMGFILE)
                middle[2] = 'player2'
        if column == 3:
            if player1:
                bottomRight.configure(image = XIMGFILE)
                right[2] = 'player1'
            else: 
                bottomRight.configure(image = OIMGFILE)
                right[2] = 'player2'

    player1 = not player1
    updateTxt()

    checkColumn(left)
    checkColumn(middle)
    checkColumn(right)

    checkRow(0)
    checkRow(1)
    checkRow(2)

    if (left[0] == middle[1] == right[2]) or (left[2] == middle[1] == right[0]):
        winGame(middle[1])


window = Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)
window.configure(bg="#a8d44c")
window.geometry("{}x{}".format(GAME_SIZE, GAME_SIZE))
XIMGFILE = PhotoImage(file = "X.png")
OIMGFILE = PhotoImage(file = "O.png")
EMPTYIMGFILE = PhotoImage(file = "EMPTY.png")

canvas = Canvas(window, bg = "#a8d44c", width = GAME_SIZE, height = GAME_SIZE, bd = 0, relief=RAISED)


topLeft = Button(canvas, image = EMPTYIMGFILE, borderwidth = 0, command = lambda: click(1, 1))
topLeft.place(x = 75, y = 75)
topMiddle = Button(canvas, image = EMPTYIMGFILE, borderwidth = 0, command = lambda: click(1, 2))
topMiddle.place(x = 225, y = 75)
topRight = Button(canvas, image = EMPTYIMGFILE, borderwidth = 0, command = lambda: click(1, 3))
topRight.place(x = 375, y = 75)

middleLeft = Button(canvas, image = EMPTYIMGFILE, borderwidth = 0, command = lambda: click(2, 1))
middleLeft.place(x = 75, y = 225)
middleMiddle = Button(canvas, image = EMPTYIMGFILE, borderwidth = 0, command = lambda: click(2, 2))
middleMiddle.place(x = 225, y = 225)
middleRight = Button(canvas, image = EMPTYIMGFILE, borderwidth = 0, command = lambda: click(2, 3))
middleRight.place(x = 375, y = 225)

bottomLeft = Button(canvas, image = EMPTYIMGFILE, borderwidth = 0, command = lambda: click(3, 1))
bottomLeft.place(x = 75, y = 375)
bottomMiddle = Button(canvas, image = EMPTYIMGFILE, borderwidth = 0, command = lambda: click(3, 2))
bottomMiddle.place(x = 225, y = 375)
bottomRight = Button(canvas, image = EMPTYIMGFILE, borderwidth = 0, command = lambda: click(3, 3))
bottomRight.place(x = 375, y = 375)

label = Label(canvas, text="Player: 1", font = ("Arial", 30), bg = "#a8d44c", fg = "#ffffff")
label.place(x = 10, y = 10)


canvas.pack()


window.mainloop()