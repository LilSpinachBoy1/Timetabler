"""
UTILITIES FOR APPLICATION
"""
import pygame

from SCRIPTS import colourLib

DEFAULT_ADDR = r"ASSETS/Fonts/TiltNeon-Regular.ttf"  # NOTE: This is relative to the script it is run from, not here (who knows why)
# The worlds best endurance event
# char_map = {pygame.K_a: ["a", "A"], pygame.K_b: ["b", "B"], pygame.K_c: ["c", "C"], pygame.K_d: ["d", "D"], pygame.K_e: ["e", "E"], pygame.K_f: ["f", "F"], pygame.K_g: ["g", "G"], pygame.K_h: ["h", "H"], pygame.K_i: ["i", "I"], pygame.K_j: }


# Class to create text
class Text:
    # TAKES PARAMS:
    # Required: Text for screen, font size, position to draw to
    # Optional: font (address) and colour which will default to basic font in black
    def __init__(self, text: str, size: int, pos: tuple, colour: tuple = (0, 0, 0), font_adr: str = DEFAULT_ADDR) -> None:
        # Create font obj
        self.fontObj = pygame.font.Font(font_adr, size)
        self.textSurface = self.fontObj.render(text, True, colour)
        self.textRect = self.textSurface.get_rect()

        # Store other details
        self.textRect.x = pos[0]
        self.textRect.y = pos[1]

    # Function to be called to draw text to the screen
    def out(self, surface: pygame.Surface) -> None:
        surface.blit(self.textSurface, self.textRect)


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

    def add_text(self, text: str, size: int, font_adr: str = DEFAULT_ADDR, colour: tuple = (0, 0, 0)) -> None:
        self.hasText = True
        self.fontObj = pygame.font.Font(font_adr, size)
        self.textSurface = self.fontObj.render(text, True, colour)

        self.textRectObj = self.textSurface.get_rect()

        # Calculation to find alignment to centre text
        boxWidth, boxHeight = self.rect.width, self.rect.height
        textWidth, textHeight = self.textRectObj.width, self.textRectObj.height
        horizontal_offset = (boxWidth // 2) - (textWidth // 2)
        vertical_offset = (boxHeight // 2) - (textHeight // 2)
        self.centred_pos = (self.rect.x + horizontal_offset, self.rect.y + vertical_offset)

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
        if self.hasText:
            surface.blit(self.textSurface, self.centred_pos)


# Code for an input field class
class InputField:
    # This takes a gazilion params so listen up
    # REQUIRED: Label (text to go with input), label size (text size), pos (position to draw to)
    # OPTIONAL: text_colour (colour of label), font_adr (address of font to use), box_colour (duh), box_width (how wide, height is determined by text size)
    def __init__(self, label: str, label_size: int, pos: tuple, text_colour: tuple = (0, 0, 0), font_adr: str = DEFAULT_ADDR, box_colour: tuple = (255, 255, 255), box_width: int = 200) -> None:
        # Create text
        self.fontObj = pygame.font.Font(font_adr, label_size)
        self.textSurface = self.fontObj.render(label, True, text_colour)
        self.textRect = self.textSurface.get_rect()
        self.textRect.x, self.textRect.y = pos[0], pos[1]

        # Create box
        self.rectColour = box_colour
        self.box_width = box_width
        self.pos_offset = self.textRect.width + 10
        self.text_box = pygame.Rect(pos[0] + self.pos_offset, pos[1], self.box_width, self.textRect.height)

        # Focus checks / input box logic
        self.isFocused = False
        self.boxText = ""

    # Check A: if box is focused, B: what text is entered
    def check_inps(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        # MOUSE FOCUS CHECK
        if self.text_box.x < mouse_pos[0] < (self.text_box.x + self.text_box.width):  # Check if in range X
            if self.text_box.y < mouse_pos[1] < (self.text_box.y + self.text_box.height):  # Check if in range Y
                # TOGGLE FOCUS
                if mouse_pressed[0] and self.isFocused:
                    self.isFocused = False
                elif mouse_pressed[0] and not self.isFocused:
                    self.isFocused = True

        # ESCAPE KEYS
        esc_keys = [pygame.K_ESCAPE, pygame.K_RETURN]
        # Listen for key presses
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key not in esc_keys:
                pass  # ADD WAY TO DETECT KEY AS STR

    def out(self, window: pygame.Surface) -> None:
        window.blit(self.textSurface, self.textRect)
        pygame.draw.rect(window, self.rectColour, self.text_box, border_radius=5)
