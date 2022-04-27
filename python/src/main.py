from utils.game import startgame
from utils.canvas import clearConsole
import logging

logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s - %(filename)s:%(lineno)d")


if __name__ == "__main__":
    logging.info("File Started")
    while True:
        clearConsole()
        startgame()

        if input("Press Q to quit, press Enter to continue ").upper() == "Q": 
            clearConsole()
            logging.info("Game Quit")
            break