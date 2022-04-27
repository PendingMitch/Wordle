from random import randint
from . import  config
from .canvas import printCanvas, clearConsole
from .guesses import getGuess
import logging


def startgame():
    while True:
        try:
            config.init()
            length = int(input("Input the length of the word that you would like: "))
            if length not in config.availableLengths: 
                logging.error("Length inputted was not correct.")
                raise ValueError("Length inputted was not correct.")

            config.current_word = getRandomWord(length)
            logging.info(f'New Word Generate: {config.current_word = }')
            config.correct_letters = [None] * len(config.current_word)

            break
        except:
            clearConsole()

            print("There was an error try again")
    printCanvas()
    getGuess()

def getRandomWord(length: int):
    with open("dictionaries/dictionary"+str(length)+".txt", "r") as dictionary:
        words = dictionary.readlines()
        list_length = len(words)
        randomInt = randint(0, list_length)

        return words[randomInt].replace('\n', '')
