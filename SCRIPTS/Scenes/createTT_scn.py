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
    title_text = util.Text("Create a new Timetable:", 25, (10, 10))
    inp1 = util.InputField("Hello: ", 25, (10, 300))

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

        screen.fill(colourLib.blue)
        inp1.out(screen)
        title_text.out(screen)
        pygame.display.update()
        tempClock.tick(60)
