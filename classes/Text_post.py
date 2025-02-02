import pygame
from Post import *
from helpers import from_text_to_array


class Text(Post):
    def __init__(self, username, location, description, text, text_color, background_color):
        super().__init__(username, location, description)
        self.text_array = from_text_to_array(text)
        self.text_color = text_color
        self.background_color = background_color

    def display(self):
        super().display()
        self.display_text()

    def display_text(self):
        pass
