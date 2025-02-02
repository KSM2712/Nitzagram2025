import pygame
from Post import *

class Text(Post):
    def __init__(self, username, location, description, comments, text):
        super().__init__(username, location, description, comments)
        self.text = text
        self.text_color = (90, 250, 197)
        self.background_color = (0, 0, 0)

    def display_text(self):
        super().display_discription()
        super().display_likes()
        super().display_location()
        super().display_username()
        super().display_comments()


