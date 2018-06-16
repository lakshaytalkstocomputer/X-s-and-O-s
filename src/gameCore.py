from board import *


def check_win():
    win = False
    for i in range(1, 10, 3):
        if board[i-1] == board[i] == board[i+1]:
            return "Win : " + str(board[i-1])

    for i in range(1, 4):
        if board[i-1] == board[i+2] == board[i+5]:
            return "Win : " + str(board[i-1])

    if board[0] == board[4] == board[8]:
        return "Win : " + str(board[0])

    if board[2] == board[4] == board[6]:
        return "Win : " + str(board[2])

    return win


def turn(t):
    move = False

    while not move:
        choice = input("Enter Where you want to input : ")
        if board[int(choice)-1] in ["X", "O"]:
            print("Invalid Move Try Again !!")
        else:
            a = lambda: "O" if t % 2 == 0 else "X"
            board[int(choice)-1] = a()

            move = True
