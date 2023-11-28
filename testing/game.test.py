// ```python
import unittest

from main import MainMenu


class TestMainMenu(unittest.TestCase):

    def test_init(self):
        # Test that the object is created correctly
        menu = MainMenu()
        self.assertEqual(menu.options, ["Continue Last Played Game", "Load Game", "New Game", "Credits", "Exit"])
        self.assertEqual(menu.selected, 0)
        self.assertTrue(menu.running)

    def test_menu(self):
        # Test that the menu is displayed correctly
        menu = MainMenu()
        menu.menu()
        expected_output = (
            Fore.GREEN + "Main Menu" + Fore.RESET + "\n"
            Fore.GREEN + "-----------" + Fore.RESET + "\n"
            Fore.GREEN + "Options:" + Fore.RESET + "\n"
            Fore.RED + "1. " + Fore.GREEN + "Continue Last Played Game" + Fore.RESET + "\n"
            Fore.RED + "2. " + Fore.GREEN + "Load Game" + Fore.RESET + "\n"
            Fore.RED + "3. " + Fore.GREEN + "New Game" + Fore.RESET + "\n"
            Fore.RED + "4. " + Fore.GREEN + "Credits" + Fore.RESET + "\n"
            Fore.RED + "5. " + Fore.GREEN + "Exit" + Fore.RESET + "\n"
            Fore.GREEN + "-----------" + Fore.RESET
        )
        self.assertEqual(printout, expected_output)

    def test_continue_game(self):
        # Test that the continue game function works correctly
        menu = MainMenu()
        menu.continue_game()
        expected_output = (
            Fore.RED + "No save file found, please load a game or start a new game" + Fore.RESET
        )
        self.assertEqual(printout, expected_output)

    def test_load_game(self):
        # Test that the load game function works correctly
        menu = MainMenu()
        menu.load_game()
        expected_output = (
            Fore.GREEN + "Load Game" + Fore.RESET
        )
        self.assertEqual(printout, expected_output)

    def test_new_game(self):
        # Test that the new game function works correctly
        menu = MainMenu()
        menu.new_game()
        expected_output = (
            Fore.GREEN + "New Game" + Fore.RESET
        )
        self.assertEqual(printout, expected_output)

    def test_show_credits(self):
        # Test that the show credits function works correctly
        menu = MainMenu()
        menu.show_credits()
        expected_output = (
            Fore.GREEN + "Credits" + Fore.RESET + "\n"
            Fore.GREEN + "Programming: Lewis" + Fore.RESET + "\n"
            Fore.GREEN + "Graphics: Lewis" + Fore.RESET + "\n"
            Fore.GREEN + "Story: Lewis" + Fore.RESET + "\n"
            Fore.GREEN + "Music: Lewis" + Fore.RESET + "\n"
            Fore.GREEN + "Sound Effects: Lewis" + Fore.RESET + "\n"
            Fore.GREEN + "Testing: Lewis" + Fore.RESET + "\n"
            Fore.GREEN + "Special Thanks: Lewis" + Fore.RESET
        )
        self.assertEqual(printout, expected_output)


if __name__ == "__main__":
    unittest.main()
// ```