import os
print("os Module Loaded")
import time
print("time Module Loaded")
import load_game as lg
print("load_game Module Loaded")
from colorama import Fore, Back, Style
print("colorama Module Loaded")

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


if __name__ == "__main__":
    load_game()


class MainMenu:
    """
    Represents the main menu of the game.
    """

    def __init__(self):
        self.options = ["Continue Last Played Game", "Load Game", "New Game", "Credits", "Exit"]
        self.selected = 0
        self.running = True
        self.error = True


    def menu(self):
        if self.error:
            print(Fore.RED, "An error may have just occured. Please report this to the developer.", Fore.RESET)
            self.error = True
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
            print(Fore.RED, f"Please enter a number between 1 and {str(len(self.options))}", Fore.RESET)
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
                self.show_credits()
            else:
                quit()
        else:
            print(Fore.RED, "Please enter a number between 1 and " + str(len(self.options)), Fore.RESET)
            input("Press Enter to continue...")
            clear()
            MainMenu.menu(self)

    def continue_game(self):
        current_save = "save_games/current_save.txt"
        # Grab the contents of the file, then find what file path is in the txt file and load that file as a save
        with open(current_save, "r") as f:
            save_file = f.read()
            if save_file == "":
                print(Fore.RED, "No save file found, please load a game or start a new game", Fore.RESET)
                input("Press Enter to continue...")
                clear()
                MainMenu.menu(self)
            elif save_file in os.listdir("save_games"):
                print(Fore.GREEN, "Loading save file: ", save_file, Fore.RESET)
                lg.load()
                input("Press Enter to continue...")
                clear()
                return save_file
            else:
                print(Fore.RED, "Save file corrupted. Please load a save manually.", Fore.RESET)
                with open(current_save, "w") as f:
                    f.write("")
                input("Press Enter to continue...")
                clear()
                MainMenu.menu(self)
            f.close()

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

    def show_credits(self):
        print(Fore.GREEN, "Credits", Fore.RESET)
        credit_list = ["Programming: Lewis", "Graphics: Lewis", "Story: Lewis", "Music: Lewis", "Sound Effects: Lewis", "Testing: Lewis", "Special Thanks: Lewis"]
        for credit in credit_list:
            print(Fore.GREEN, credit, Fore.RESET)
            time.sleep(0.5)
        input("Press Enter to continue...")
        clear()
        MainMenu.menu(self)


if __name__ == "__main__":
    initial_menu = MainMenu()
    initial_menu.error = False
    initial_menu.menu()
