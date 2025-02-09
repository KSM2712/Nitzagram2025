import pygame.image
from classes.Post import *


class PicturePost(Post):
    def __init__(self, username, location, description, image_path):
        super().__init__(username, location, description)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (POST_WIDTH, POST_HEIGHT))

    def display(self):
        super().display()
        self.display_images()

    def display_images(self):
        screen.blit(self.image, (POST_X_POS, POST_Y_POS))

