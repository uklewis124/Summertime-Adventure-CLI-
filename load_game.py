import os
import time
import game
from colorama import Fore, Back, Style

print("Initializing Module Loaded")

def load():
    print(Fore.GREEN, "Initializing...", Fore.RESET)
    print

# DO NOT EDIT BELOW THIS LINE
if __name__ == "__main__":
    print("This file is not meant to be run directly.")
    print("Please run game.py instead.")
    input("Press Enter to continue...")
    save_file = game.MainMenu.continue_game(self=game.MainMenu)
    if save_file:
        directory = os.path.join(os.getcwd(), "save_games", save_file)
        with open(directory, "r") as f:
            # Chapter 0 = tutorial, 1 = chapter 1, etc.
            current_chapter = f.readline()
            xp_gained = f.readline() # Amount of xp gained (one single number)
            # Player relationships (one line, multiple numbers) (see player.py for more info)
            player_relationships = f.readline()
        if current_chapter == "":
            os.remove(directory)
            print(Fore.RED, "Save file is corrupted. Please start a new game.", Fore.RESET)
            print(Fore.RED, "Error Message: Missing Chapter ID", Fore.RESET)
        elif xp_gained  == "":
            os.remove(directory)
            print(Fore.RED, "Save file is corrupted. Please start a new game.", Fore.RESET)
            print(Fore.RED, "Error Message: Missing XP ID", Fore.RESET)
        elif player_relationships == "":
            os.remove(directory)
            print(Fore.RED, "Save file is corrupted. Please start a new game.", Fore.RESET)
            print(Fore.RED,
                    "Error Message: Missing Player Relationships",
                    Fore.RESET)
        else:  # Save file is not corrupted
            print(Fore.GREEN, f"Loading Chapter {current_chapter}", Fore.RESET)
            print(Fore.GREEN, f"You currently have {xp_gained} XP.", Fore.RESET)

