import pygame.image

from Post import *


def display_images():
    BACKGROUND_IMAGE = pygame.image.load("images/background.png")
    BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE,[POST_WIDTH, POST_HEIGHT])
    RONALDO_IMAGE = pygame.image.load("images/ronaldo.png")
    RONALDO_IMAGE = pygame.transform.scale(RONALDO_IMAGE, [POST_WIDTH, POST_HEIGHT])
    NOA_IMAGE = pygame.image.load("images/noa_kirel.png")
    NOA_IMAGE = pygame.transform.scale(NOA_IMAGE, [POST_WIDTH, POST_HEIGHT])
    screen.blit(BACKGROUND_IMAGE, (POST_X_POS, POST_Y_POS))
    screen.blit(RONALDO_IMAGE, (POST_X_POS, POST_Y_POS))
    screen.blit(NOA_IMAGE, (POST_X_POS, POST_Y_POS))
    pygame.display.flip()


class Picture(Post):
    def __init__(self,username, location, description, comments, image_path):
        super().__init__(username, location,description, comments)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (POST_WIDTH, POST_HEIGHT))

    def display(self, surface, x, y):
        surface.blit(self.image, (x, y))
        super().display_discription()
        super().display_likes()
        super().display_location()
        super().display_username()
        super().display_comments()
        pygame.display.flip()

