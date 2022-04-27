from utils.game import startgame

if __name__ == "__main__":
    while True:
        startgame()
        if input("Press Q to quit, press Enter to continue").upper() == "Q": break