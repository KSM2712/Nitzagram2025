from helpers import *
from constants import *


class Comment:
    def __init__(self):
        self.text = read_comment_from_user()

    def display(self, comment_num):
        COMMENT_X_POS = FIRST_COMMENT_X_POS
        COMMENT_Y_POS = (COMMENT_LINE_HEIGHT*comment_num)+FIRST_COMMENT_Y_POS
        screen.blit(self.text,[COMMENT_X_POS,COMMENT_Y_POS])
