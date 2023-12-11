"""
game that finds mouse position, if position matches box position, you win, round 2 etc.
"""

import pygame
import random
import math
import time
import sys
import colorama
import pyautogui
import os


os.system('cls' if os.name == 'nt' else 'clear')
while True:
    touching_square = False
    square_x = random.randint(0, 1000)
    square_y = random.randint(0, 1000)
    print(square_x, square_y)
    print(pyautogui.position())
    while not touching_square:
        mouse_x, mouse_y = pyautogui.position()
        if mouse_x >= square_x and mouse_x <= square_x + 100 and mouse_y >= square_y and mouse_y <= square_y + 100:
            touching_square = True
    to_output = str(pyautogui.position())
    for letter in to_output:
        #possible_colors = [Fore.RED,Fore.GREEN,Fore.YELLOW,Fore.BLUE,Fore.MAGENTA,Fore.CYAN]
        #letter = random.choice(possible_colors) + letter
        sys.stdout.write(letter)
        sys.stdout.flush()
    time.sleep(0.001)
    sys.stdout.write('\r' + ' ' * len(to_output) + '\r')