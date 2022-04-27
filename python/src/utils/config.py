import logging
from configparser import ConfigParser
import os

def init():
    global current_word
    current_word = ""
    global completed
    completed = False
    global correct_letters
    correct_letters = [None]
    global previous_guesses
    previous_guesses = []
    global availableLengths
    availableLengths = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,29,31]



    ini_dir = os.path.join(os.getcwd(), 'config.ini')
    cfg = ConfigParser()
    cfg.read(ini_dir)

    global amount_of_guesses
    amount_of_guesses = int(cfg.get('Config', 'GuessAmount'))

    logging.info(f'Loaded config file - {ini_dir = }')