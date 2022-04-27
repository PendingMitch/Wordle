from .canvas import printCanvas
from . import config

def add_guess(word: str):

    if not correctInput(word, config.current_word): 
        print("Not a correct input")
        getGuess()
        return

    config.previous_guesses.append(word.upper())
    for x in enumerate(word):
        if config.current_word[x[0]] == x[1]:
            config.correct_letters[x[0]] = x[1]

    printCanvas()

    if isWon(): print("You got the word, congratulations.")
    elif len(config.previous_guesses) >= config.amount_of_guesses: print("Game Over The Word Was: " + config.current_word.capitalize())
    else: getGuess()





def isWon():
    for x in enumerate(config.current_word):
        if config.correct_letters[x[0]] != x[1]: return False
    return True

def correctInput(word: str, currentWord: str):
    if len(word) != len(currentWord): return False
    return True

def getGuess():
    guess = str(input("What's your guess bucko? "))
    add_guess(guess)