from Post import *
from helpers import *


class TextPost(Post):
    def __init__(self, username, location, description, text, text_color, background_color):
        super().__init__(username, location, description)
        self.text_array = from_text_to_array(text)
        self.text_color = text_color
        self.background_color = background_color

    def display(self):
        super().display()
        self.display_text()

    def display_text(self):
        square = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.background_color, square)
        for i in range(len(self.text_array)):
            text_font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE)
            text_display = text_font.render(self.text_array, True, self.text_color)
            x = center_text(len(self.text_array), text_display, i)
            screen.blit(text_display, x)
