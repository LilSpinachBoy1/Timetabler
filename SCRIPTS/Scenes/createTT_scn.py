"""
SCENE: CREATING A NEW TIMETABLE
"""

from SCRIPTS import colourLib
import pygame
import sys


def scene(SCREEN: pygame.display):
    pygame.display.set_caption("Timetabler: New Timetable")
    tempClock = pygame.time.Clock()
    running = True

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

        SCREEN.fill(colourLib.blue)
        pygame.display.update()
        tempClock.tick(60)
