from random import randint
from . import  config
from .canvas import printCanvas
from .guesses import getGuess

def startgame():
    while True:
        try:
            config.init()
            length = int(input("Input the length of the word that you would like: "))
            if length > 10: raise ValueError("Input was too large")

            config.current_word = getRandomWord(length)
            config.correct_letters = [None] * len(config.current_word)

            break
        except:
            print("There was an error try again")

    printCanvas()
    getGuess()

def getRandomWord(length: int):
    with open("dictionaries/dictionary"+str(length)+".txt", "r") as dictionary:
        words = dictionary.readlines()
        list_length = len(words)
        randomInt = randint(0, list_length)

        return words[randomInt].replace('\n', '')
