import pygame.image

from Post import *
class Picture(Post):
    def __init__(self,username, location,description, comments, image):
        super().__init__(username, location,description, comments)
        self.image = image


    def image_load(self):
        post_pic = pygame.image.load()
