from .canvas import printCanvas, clearConsole
from . import config
import logging

def add_guess(word: str):
    logging.info(f'Guessed Word: {word}')

    if not correctInput(word, config.current_word): 
        clearConsole()
        printCanvas()
        print("Not a correct input")
        getGuess()
        return

    config.previous_guesses.append(word.upper())
    for x in enumerate(word):
        if config.current_word[x[0]].upper() == x[1].upper():
            config.correct_letters[x[0]] = x[1]
            logging.info(f'Letter at index {x[0]} is correct.')

    printCanvas()
    if isWon(): print("You got the word, congratulations. The word was " + config.current_word.capitalize())
    elif len(config.previous_guesses) >= config.amount_of_guesses: print("Game Over The Word Was: " + config.current_word.capitalize())
    else: getGuess()





def isWon():
    for x in enumerate(config.current_word):
        if config.correct_letters[x[0]] == None : return False
        if str(config.correct_letters[x[0]]).upper() != x[1].upper(): return False
    
    logging.info(f'Game Won with word: {config.current_word}')
    return True

def correctInput(word: str, currentWord: str):
    if len(word) != len(currentWord): 
        logging.error(f'Input {word} was illegal.')
        return False

    return True

def getGuess():
    guess = str(input("What's your guess bucko? "))
    add_guess(guess)