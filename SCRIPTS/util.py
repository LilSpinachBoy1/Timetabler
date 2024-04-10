"""
UTILITIES FOR APPLICATION
"""
import pygame

# Function to get data surrounding login
def readLoginData() -> dict:
    file = open("../ASSETS/loginData.txt", "r")  # Open file to read from
    # Read data and store to list
    logins = file.readline()
    encryptedCode = file.readline()
    values = {"loginCount": logins, "encCode": encryptedCode}
    # Close file
    file.close()
    return values

# Class to create text
class Text:
    def __init__(self, text: str, size: int, pos: tuple, fontAdr = "../ASSETS/Fonts/TiltNeon-Regular.ttf", *colour: tuple):
        pass
