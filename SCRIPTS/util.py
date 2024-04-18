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
    # Optional: width and height of button, background colour, hover colour
    def __init__(self, pos: tuple, size: tuple = (425, 85), colour: tuple = colourLib.rust, hover_colour: tuple = colourLib.rust_hover) -> None:
        # Add font options to shut up interpreter
        self.centred_pos = None
        self.textRectObj = None
        self.textSurface = None
        self.fontObj = None

        # Set up everything else
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.boundX = (pos[0], pos[0] + size[0])
        self.boundY = (pos[1], pos[1] + size[1])
        self.current_colour = colour
        self.def_colour = colour
        self.hover_colour = hover_colour
        self.state = "normal"
        self.hasText = False

    # Does this work? Who knows
    def add_text(self, text: str, size: int, font_adr: str = DEFAULT_ADDR, colour: tuple = (0, 0, 0)) -> None:
        self.hasText = True
        self.fontObj = pygame.font.Font(font_adr, size)
        self.textSurface = self.fontObj.render(text, True, colour)

        self.textRectObj = self.textSurface.get_rect()

        # Calculation to find alignment to centre text
        boxWidth, boxHeight = self.rect.width, self.rect.height
        textWidth, textHeight = self.textRectObj.width, self.textRectObj.height
        horizontal_offset = (boxWidth % 2) - (textWidth % 2)
        vertical_offset = (boxHeight % 2) - (textHeight % 2)
        self.centred_pos = (horizontal_offset, vertical_offset)

    def press_check(self, mouse_pos: tuple, mouse_pressed: bool, func_to_run) -> None:
        # Within bounds
        if self.boundX[0] < mouse_pos[0] < self.boundX[1] and self.boundY[0] < mouse_pos[1] < self.boundY[1]:
            # Is pressed?
            if mouse_pressed:
                func_to_run()
            else:
                self.current_colour = self.hover_colour  # Change to hover colour if within bounds
        else:
            self.current_colour = self.def_colour  # Return to default colour if no criteria are met

    def out(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, self.current_colour, self.rect, border_radius=5)
        if self.hasText: surface.blit(self.textSurface, self.centred_pos)
