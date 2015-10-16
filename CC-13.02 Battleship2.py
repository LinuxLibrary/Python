#!/usr/bin/python
# Author : Arjun Shrinivas
# Import Modules
from random import randint
 
 
# Create an empty board
board1 = []
board2 = []
 
 
 
# Modify the board to  10x10
 
for x in range(10):
    board1.append(["O"] * 10)
    board2.append(["O"] * 10)
 
def plain_board(board1):
    for row in board1:
        print " ".join(row)
def failed_board(board2):
    for row in board2:
        print " ".join(row)
 
print "Let's play Battleship!"
plain_board
 
def random_row(board1):
    return randint(0, len(board2) - 1)
 
def random_col(board1):
    return randint(0, len(board2) - 1)
 
 
ship_row = random_row(board2)
ship_col = random_col(board2)
 
#print ship_row
#print ship_col
 
player1 = raw_input("Name of the first player: ")
player2 = raw_input("Name of the second player: ")
players = [player1,player2]
 
for player in players:
        print "Hi %s, try to locate the battleship.\n Please input 0-9 for row and column." % (player)
        for turn in range(3):
                guess_row = int(raw_input("Guess Row: "))
                guess_col = int(raw_input("Guess Col: "))
                turn += 1
                print "Guess %s of 3" %(turn)
                if guess_row == ship_row and guess_col == ship_col:
                        print "Congratulations! You sunk my battleship!"
                        plain_board(board1)
                        break
                else:
                        if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
                            print "Oops, that's not even in the ocean."
                        elif(board2[guess_row][guess_col] == "X"):
                            print "You guessed that one already."
                        else:
                            print "You missed my battleship!"
                            if turn == 3:
                                print "Game Over"
                board2[guess_row][guess_col] = "X"
                failed_board(board2)
                
  # END
