from . import config as config

def printCanvas():
    print()
    for x in config.previous_guesses:
        for y in x:
            print('[' + y + '] ', end="")
        print()

    for x in range(config.amount_of_guesses - len(config.previous_guesses)):
        for y in range(len(config.current_word)):
            if config.correct_letters[y] != None: print('[' + config.correct_letters[y].upper() + ']', end=" ")
            else: print('[ ]', end=" ")

        print()