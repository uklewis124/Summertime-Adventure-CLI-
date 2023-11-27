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
    print(Fore.GREEN, "Loading Game...", Fore.RESET)
    time.sleep(1)
    clear()


load_game()

### Main Menu ###


class MainMenu:
    """
    Represents the main menu of the game.
    """

    def __init__(self):
        self.options = ["Continue Last Played Game", "Load Game", "New Game", "Credits", "Exit"]
        self.selected = 0
        self.running = True
        MainMenu.menu(self)
    def menu(self):
        print(Fore.GREEN, "Main Menu", Fore.RESET)
        print(Fore.GREEN, "-----------", Fore.RESET)
        print(Fore.GREEN, "Options:", Fore.RESET)
        for counter, option in enumerate(self.options, start=1):
            print(Fore.RED, f"{str(counter)}. ", Fore.GREEN, option, Fore.RESET)
        counter = 1
        print(Fore.GREEN, "-----------", Fore.RESET)
        # Finding out which option is selected
        try:
            self.selected = int(input(Fore.GREEN + "Select an option: " + Fore.RESET))
        except ValueError:
            print(Fore.RED, "Please enter a number between 1 and " + str(len(self.options)), Fore.RESET)
            input("Press Enter to continue...")
            clear()
            MainMenu.menu(self)
        if self.selected >= 1 and self.selected <= len(self.options):
            print(Fore.GREEN, "You selected: ", self.options[self.selected - 1], Fore.RESET)
            clear() # Remove for debugging
            if self.selected == 1:
                self.continue_game()
            elif self.selected == 2:
                self.load_game()
            elif self.selected == 3:
                self.new_game()
            elif self.selected == 4:
                self.credits()
            else:
                quit()
        else:
            print(Fore.RED, "Please enter a number between 1 and " + str(len(self.options)), Fore.RESET)
            input("Press Enter to continue...")
            clear()
            MainMenu.menu(self)
    def continue_game(self):
        print(Fore.GREEN, "Continue Game", Fore.RESET)
        input("Press Enter to continue...")
        clear()
        MainMenu.menu(self)
    def load_game(self):
        print(Fore.GREEN, "Load Game", Fore.RESET)
        input("Press Enter to continue...")
        clear()
        MainMenu.menu(self)
    def new_game(self):
        print(Fore.GREEN, "New Game", Fore.RESET)
        input("Press Enter to continue...")
        clear()
        MainMenu.menu(self)
    def credits(self):
        print(Fore.GREEN, "Credits", Fore.RESET)
        credits = ["Programming: Lewis", "Graphics: Lewis", "Story: Lewis", "Music: Lewis", "Sound Effects: Lewis", "Testing: Lewis", "Special Thanks: Lewis"]
        for credit in credits:
            print(Fore.GREEN, credit, Fore.RESET)
            time.sleep(0.5)
        input("Press Enter to continue...")
        clear()
        MainMenu.menu(self)


MainMenu()
