#!/usr/bin/env python3
import sys
import random
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

print(" Welcome to the party! Guess how many jelly beans are in the jar! Guess correctly and you get a prize! ")
number = random.randrange(1,50)
count = 0
guess = -1
while guess != number:
    count = count + 1
    guess = input(" Guess a number between 1 and 50! ")
    try:
        guess = int(guess)
        if guess != number:
            print(" Hmm not quite, try again! ")
    except:
        print("Please enter a number!")
print(" You got it! And it only took you " + str(count) + " tries! ")
print(" Your prize, this very jar of jelly beans! Congrats! Thanks for playing! ")    