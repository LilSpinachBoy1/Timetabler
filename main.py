"""
WELCOME TO TIMETABLER!
See README.md for more information on the project.
This is main.py, the initial file to run for the project, it will house initial boot info and the main menu of the application.
"""

# Library imports
import sys
import time
import pygame
from pygame.locals import *

# Local imports
from SCRIPTS import util

# Initialise libraries where required
pygame.init()

# Constants
BG_COLOUR = (199, 202, 255)  # Pastel light blue
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 500
FPS = 60

# Setup window
fpsClock = pygame.time.Clock()
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Timetabler: Login')


# Class to manage menu scenes
class MainMenu:
    def __init__(self):
        self.scene = "login"

    def login(self):
        login_running = True

        # Game loop
        while login_running:
            # Get events for quitting
            for event in pygame.event.get():
                if event.type == QUIT:  # If quit is pressed
                    pygame.quit()
                    sys.exit()

            # Render elements
            WINDOW.fill(BG_COLOUR)
            pygame.display.update()
            fpsClock.tick(FPS)

    def manager(self):
        while True:
            if self.scene == "login": self.login()


# Create object of class and begin
run = MainMenu()
run.manager()
