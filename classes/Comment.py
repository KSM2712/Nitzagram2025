from helpers import *
from constants import *


class Comment:
    def __init__(self, text):
        self.text = text

    def display(self, comment_num):
        comment_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        comment_to_display = comment_font.render(self.text,True, BLACK)
        COMMENT_X_POS = FIRST_COMMENT_X_POS
        COMMENT_Y_POS = (COMMENT_LINE_HEIGHT*comment_num)+FIRST_COMMENT_Y_POS
        screen.blit(comment_to_display,[COMMENT_X_POS,COMMENT_Y_POS])
