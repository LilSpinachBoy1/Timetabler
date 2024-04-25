"""
SCENE: CREATING A NEW TIMETABLE
"""

from SCRIPTS import colourLib
from SCRIPTS import util
import pygame
import sys


def scene(screen: pygame.display):
    pygame.display.set_caption("Timetabler: New Timetable")
    tempClock = pygame.time.Clock()
    running = True

    # Create page elements
    title_text = util.Text("Create a new Timetable:", 35, (20, 10))
    ttNameInp = util.InputField("Timetable Name: ", 25, (15, 75), box_width=260)

    # Game loop
    while running:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # If esc pressed
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False  # Return out a scene

        # PROCESSING
        ttNameInp.check_inps()

        screen.fill(colourLib.blue)
        ttNameInp.out(screen)
        title_text.out(screen)
        pygame.display.update()
        tempClock.tick(60)
