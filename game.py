import os
import time
from colorama import Fore, Back, Style

def clear():
    """
    Clears the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def load_game():
    """
    Loads the game and prints various messages using colorama library.
    """
    print(Fore.RED + "Hello World", Fore.RESET)
    clear()
    print(Back.GREEN + "Hello World", Back.RESET)
    clear()
    print(Style.DIM + "Hello World", Style.RESET_ALL)
    clear()
    print(Fore.GREEN, "Imports Ready...")
    time.sleep(1)
    clear()
    