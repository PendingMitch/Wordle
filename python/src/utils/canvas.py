from . import config as config
import os
import logging


def printCanvas():
    clearConsole()
    for x in config.previous_guesses:
        for y in x:
            print('[' + y + '] ', end="")
        print()

    for x in range(config.amount_of_guesses - len(config.previous_guesses)):
        for y in range(len(config.current_word)):
            if config.correct_letters[y] != None: print('[' + config.correct_letters[y].upper() + ']', end=" ")
            else: print('[ ]', end=" ")

        print()
    print()


    logging.info(f'Canvas printed. Current guessed letters: {config.correct_letters}')


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    logging.info("Console Cleared")