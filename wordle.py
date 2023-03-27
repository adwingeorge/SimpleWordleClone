import random
import sys
from termcolor import colored
import nltk
from nltk.corpus import words


def printMenu():
    print("Let's play the game")
    print('type a 5 letter word \n')


def readRandomWord():
    with open("words.txt")as f:
        words = f.read().splitlines()
        return random.choice(words)


playAgain = ""
while playAgain != "q":
    word = readRandomWord()

    for attempt in range(1, 7):
        guess = input().lower()

        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        for i in range(min(len(guess), 5)):
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end="")
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end="")
            else:
                print(guess[i], end="")

        print()

        if guess == word:
            print(colored(f"congrats! you got the wordle in {attempt}", 'red'))
            break

    playAgain = input("what to play again? Type q to exit.")
