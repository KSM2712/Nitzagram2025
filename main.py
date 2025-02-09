import pygame
from helpers import screen
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from classes.Picture_post import *
from classes.Text_post import *

def main():
    # Set up the game display, clock and headline
    pygame.init()
    pygame.display.set_caption("Nitzagram")
    screen.fill((255, 255, 255))
    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    p1 = PicturePost("karin1", "Tel Aviv", ":)))", "Images/noa_kirel.jpg")
    p2 = PicturePost("Ira1", "haifa", "yayyy", "Images/ronaldo.jpg")
    p3 = TextPost("Esti1", "Eilat", "life quotes", "the sun is shining", [180, 74, 255], [250, 200, 72])



    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
