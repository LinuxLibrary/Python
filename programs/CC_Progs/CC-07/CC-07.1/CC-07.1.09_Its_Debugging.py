#!/usr/bin/python

from random import randint
board = []
for x in range(0,5):
    board.append(["O"] * 5)
def print_board(board):
    for row in board:
        print " ".join(row)
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)
ship_row = random_row(board)
ship_col = random_col(board)
# Add your code below!
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))
    
print ship_row
print ship_col
