import pygame

from classes.Comment import Comment
from helpers import screen
from buttons import *


class Post:
    def __init__(self, username, location, description):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []
        self.comments_display_index = 0

    def display(self):
        self.display_discription()
        self.display_likes()
        self.display_location()
        self.display_username()
        self.display_comments()

    def add_like(self):
        self.likes_counter += 1

    def add_comments(self, text):
        self.comments.append(Comment(text))

    def display_likes(self):
        font = pygame.font.SysFont('chalkduster.ttf', 18)
        text_like = font.render(f"Liked by {self.likes_counter} users", True, BLACK)
        screen.blit(text_like, [LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS])

    def display_username(self):
        font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        user_text = font.render(self.username, True, BLACK)
        screen.blit(user_text, [USER_NAME_X_POS, USER_NAME_Y_POS])

    def display_location(self):
        font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        user_text = font.render(self.location, True, LIGHT_GRAY)
        screen.blit(user_text, [LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS])

    def display_discription(self):
        font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        user_text = font.render(self.description, True, BLACK)
        screen.blit(user_text, [DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS])

    def display_comments(self):
        position_index = self.comments_display_index
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more = comment_font.render("view more comments",
                                            True, GREY)
            screen.blit(view_more, (VIEW_MORE_COMMENTS_X_POS,
                                    VIEW_MORE_COMMENTS_Y_POS))
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break
