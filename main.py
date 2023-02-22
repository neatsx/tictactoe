import tkinter as tk
from tkinter import *
from playsound import playsound
from PIL import Image, ImageDraw, ImageTk



root = tk.Tk()
canvas = Canvas()


root.geometry("500x500")
root.resizable(False, False)

#board
#squares
square_1 = tk.Button(root, text=".", height=10, width=15,bg='#fff', command= lambda t= 0: game(t))
square_2 = tk.Button(root, text=".", height=10, width=15,bg='#fff', command= lambda t= 1: game(t))
square_3 = tk.Button(root, text=".", height=10, width=15,bg='#fff', command= lambda t= 2: game(t))
square_4 = tk.Button(root, text=".", height=10, width=15,bg='#fff', command= lambda t= 3: game(t))
square_5 = tk.Button(root, text=".", height=10, width=15,bg='#fff', command= lambda t= 4: game(t))
square_6 = tk.Button(root, text=".", height=10, width=15,bg='#fff', command= lambda t= 5: game(t))
square_7 = tk.Button(root, text=".", height=10, width=15,bg='#fff', command= lambda t= 6: game(t))
square_8 = tk.Button(root, text=".", height=10, width=15,bg='#fff', command= lambda t= 7: game(t))
square_9 = tk.Button(root, text=".", height=10, width=15,bg='#fff', command= lambda t= 8: game(t))

gameLabel = tk.Label(root, text="Ready?", font=('calibre', 15, 'bold'))
gameLabel2 = tk.Label(root, text="", font=('calibre', 35, 'bold'))
gameLabel3 = tk.Label(root, text="Turn: X", font=('calibre', 25, 'bold'))

restartButton = tk.Button(root, text="Restart?", command= lambda t = 12: restart_game())


squares = [square_1, square_2, square_3, square_4, square_5, square_6, square_7, square_8, square_9]

#organization
square_1.grid(row=0, column=0)
square_2.grid(row=0, column=1)
square_3.grid(row=0, column=2)
square_4.grid(row=1, column=0)
square_5.grid(row=1, column=1)
square_6.grid(row=1, column=2)
square_7.grid(row=2, column=0)
square_8.grid(row=2, column=1)
square_9.grid(row=2, column=2)
gameLabel.grid(row=0, column=3)
gameLabel3.grid(row=1, column=3)
restartButton.grid(row=2, column=3)

#player possesions
player_1 = []
player_2 = []

check_squares = []

turn = 0

#functions
def game(button_press):
    global turn
    global squares
    global player_1
    global player_2
    global gameLabel
    global check_squares
    global win
    #if the button is pressed, get that button and check which one was pressed, then change the display of it to X or O depending on if turn = 0 or turn = 1
    #When turn = 2, that means the game has been won, so the else: statement at the bottom makes it so nothing else can be changed after a player has won
    for i in range(9):
        if turn == 0:
            if i == button_press:
                player_1.append(button_press)
                squares[i].config(text="X")
                turn=1
                gameLabel.config(text="Player 2's Turn")
                gameLabel3.config(text="Turn: O")
        elif turn == 1:
            if i == button_press:
                turn=0
                player_2.append(button_press)
                squares[i].config(text="O")
                gameLabel.config(text="Player 1's Turn")
                gameLabel3.config(text="Turn: X")
        elif turn > 1:  
            if i == button_press:
                if squares[i].cget('text') == "X":
                    squares[i].config(text="X")
                    print(squares[i].cget('text'))
                if squares[i].cget('text') == "O":
                    print(squares[i].cget('text'))
                    squares[i].config(text="O")
                elif squares[i].cget('text') == ".":
                    squares[i].config(text=".")
                    print(squares[i].cget('text'))
    checkWin2()
    checkTie()

winning_values_1 = [0,1,2]
winning_values_2 = [3,4,5]
winning_values_3 = [6,7,8]
winning_values_4 = [0,3,6]
winning_values_5 = [1,4,7]
winning_values_6 = [2,5,8]
winning_values_7 = [0,4,8]
winning_values_8 = [2,4,6]

user_winning_values = []

all_winning_values = [winning_values_1,winning_values_2,winning_values_3,winning_values_4,winning_values_5,winning_values_6,winning_values_7,winning_values_8]

tie = 0

def checkWin2():
    #checks every turn if someone filled up the squares with winning moves.
    global squares
    global gameLabel
    global turn
    global player_1
    global player_2
    global all_winning_values
    global check_squares
    global user_winning_values

    for i in range(8):
        if all(value in player_1 for value in all_winning_values[i]):
            gameLabel.config(text="Player 1 Wins!")
            user_winning_values.append(all_winning_values[i])
            print(user_winning_values)
            turn == 3
            squares[user_winning_values[0][0]].config(bg='#3D9140')
            squares[user_winning_values[0][1]].config(bg='#3D9140')
            squares[user_winning_values[0][2]].config(bg='#3D9140')
            print(user_winning_values)
            turn = 2
            gameLabel2.config(text="")
            gameLabel3.config(text="")
        elif all(value in player_2 for value in all_winning_values[i]):
            squares[i].config(bg="#fff")
            gameLabel.config(text="Player 2 Wins!")
            print(user_winning_values[0][0])
            turn = 2
            gameLabel2.config(text="")
            user_winning_values.append(all_winning_values[i])
            squares[user_winning_values[0][0]].config(bg='#3D9140')
            squares[user_winning_values[0][1]].config(bg='#3D9140')
            squares[user_winning_values[0][2]].config(bg='#3D9140')
            print(user_winning_values)
            gameLabel3.config(text="")
    

    
def checkTie():
    global turn
    global squares
    global player_1
    global player_2
    global gameLabel
    global check_squares
    global tie
    for y in range(9):
        check_squares.append(squares[y].cget('text'))
        print(check_squares)
    if not "." in check_squares and turn < 2:
        gameLabel.config(text="Tie!")
        tie = 1
        print(check_squares)
        gameLabel2.config(text="")
        gameLabel3.config(text="")
        for i in range(9):
            squares[i].config(bg="#9A32CD")
    if "." in check_squares:
        check_squares = []
    


def restart_game():
    global turn
    global squares
    global player_1
    global player_2
    global gameLabel
    global check_squares
    global user_winning_values
    print("RESTARTED")
    player_1 = []
    player_2 = []
    check_squares = []
    user_winning_values = []
    gameLabel.config(text="Ready?")
    turn = 0
    for i in range(9):
        squares[i].config(text=".")
        squares[i].config(bg="#fff")

root.mainloop()