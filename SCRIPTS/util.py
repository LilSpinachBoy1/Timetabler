"""
UTILITIES FOR APPLICATION
"""
import pygame

DEFAULT_ADDR = r"ASSETS/Fonts/TiltNeon-Regular.ttf"  # NOTE: This is relative to the script it is run from, not here (who knows why)


# Class to create text
class Text:
    # TAKES PARAMS:
    # Text for screen, font size, position to draw to
    # Optional params of font (address) and colour which will default to basic font in black
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
    def __init__(self, size: tuple, pos: tuple, ) -> None:
        pass
