#!/usr/bin/python

from random import randint
# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
guesses_left = 3
# Start your game!
while guesses_left <=3:
    random_number = randint(1,10)
    print random_number
    guess = int(raw_input("Please input your guess : "))
    if guess == random_number :
        print "You win!"
        break
        guesses_left -=1
#    else:
#        print "Try again _/\_"
#        break
else: 
    print "You lose!"
