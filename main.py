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
from SCRIPTS import colourLib
from SCRIPTS import Scenes as sc

# Initialise libraries where required
pygame.init()

# Constants
BG_COLOUR = colourLib.blue  # Light blue
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 500
FPS = 60

# Setup window
fpsClock = pygame.time.Clock()
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Timetabler')


# Class to manage menu scenes
class MainMenu:
    def __init__(self):
        self.scene = "menu"

    """
    FUNCTIONS FOR BUTTONS TO EXECUTE
    """
    @staticmethod
    def quit():
        pygame.quit()
        sys.exit()

    """
    THE MAIN MENU OF THE APPLICATION
    """
    def menu(self):
        login_running = True

        # Create text elements
        title_text = "Timetabler!"
        title_TXT = util.Text(title_text, 60, (100, 30))

        # Create button elements
        newButt = util.Button((35, 150))
        newButt.add_text("Create New Timetable", 30)
        viewButt = util.Button((35, 250))
        viewButt.add_text("View Timetable", 30)
        editButt = util.Button((35, 350))
        editButt.add_text("Edit Timetable", 30)
        quitButt = util.Button((35, 475))
        quitButt.add_text("Quit", 30)

        buttArr = [newButt, viewButt, editButt, quitButt]  # Button array for rendering

        # Game loop
        while login_running:
            # Get events for quitting
            for event in pygame.event.get():
                if event.type == QUIT:  # If quit is pressed
                    pygame.quit()
                    sys.exit()

            mousePos = pygame.mouse.get_pos()
            mousePressed = pygame.mouse.get_pressed()
            quitButt.press_check(mousePos, mousePressed[0], self.quit)

            # Render elements
            WINDOW.fill(BG_COLOUR)
            title_TXT.out(WINDOW)
            for butts in buttArr:
                butts.out(WINDOW)
            pygame.display.update()
            fpsClock.tick(FPS)

    def manager(self):
        while True:
            if self.scene == "menu":
                pygame.display.set_caption("Timetabler: Main Menu")
                self.menu()
            if self.scene == "newTT":
                pygame.display.set_caption("Timetabler: Timetable Creation")


# Create object of class and begin
run = MainMenu()
run.manager()
