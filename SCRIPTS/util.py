"""
UTILITIES FOR APPLICATION
"""
import pygame
from SCRIPTS import colourLib

DEFAULT_ADDR = r"ASSETS/Fonts/TiltNeon-Regular.ttf"  # NOTE: This is relative to the script it is run from, not here (who knows why)


# Class to create text
class Text:
    # TAKES PARAMS:
    # Required: Text for screen, font size, position to draw to
    # Optional: font (address) and colour which will default to basic font in black
    def __init__(self, text: str, size: int, pos: tuple, colour: tuple = (0, 0, 0), font_adr: str = DEFAULT_ADDR) -> None:
        # Create font obj
        self.fontObj = pygame.font.Font(font_adr, size)
        self.textSurface = self.fontObj.render(text, True, colour)

        # Store other details
        self.position = pos

    # Function to be called to draw text to the screen
    def out(self, surface: pygame.Surface) -> None:
        surface.blit(self.textSurface, self.position)


# Class to create interactive buttons
class Button:
    # TAKES PARAMS:
    # Required: position (x, y)
    # Optional: width and height of button, background colour
    def __init__(self, pos: tuple, size: tuple = (425, 85), colour: tuple = colourLib.rust) -> None:
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.colour = colour
        self.state = "normal"

    def out(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, self.colour, self.rect, border_radius=5)
