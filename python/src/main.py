from utils.game import startgame
from utils.canvas import clearConsole

if __name__ == "__main__":
    while True:
        clearConsole()
        startgame()

        if input("Press Q to quit, press Enter to continue ").upper() == "Q": 
            clearConsole()
            break