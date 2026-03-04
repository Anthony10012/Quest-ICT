import pygame
import sys


# --- CONFIGURATION ---
pygame.init()
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ajouter une Question - Pygame Edition")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)
GREEN = (34, 197, 94)
BLUE_GRAD = (30, 58, 138)

# Fonts
font_title = pygame.font.SysFont("Arial", 50, bold=True)
font_ui = pygame.font.SysFont("Arial", 24)
font_small = pygame.font.SysFont("Arial", 18)

# --- Form Status ---
form_data = {
    "question":"",
    "explanation":"",
    "correct_answer": None,
    "answers": ["","","",""]
}
active_field = None # To find out which text field is selected

# --- Classes UI ---
class Button:
    def __init__(self, x, y, w, h, text, color, callback):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color
        self.callback = callback

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=12)
        pygame.draw.rect(surface, WHITE, self.rect, 2, border_radius=12)
        txt = font_ui.render(self.text, True, WHITE)
        surface.blit(txt, (self.rect.centerx - txt.get_width()//2, self.rect.centery - txt.get_height()//2))

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.callback()


class InputBox:
    def __init__(self, x, y, w, h, label, key):
        self.rect = pygame.Rect(x, y, w, h)
        self.label = label
        self.key = key

    def draw(self, surface):
        color = YELLOW if active_field == self.key else WHITE
        pygame.draw.rect(surface, color, self.rect, 2, border_radius=8)

        #Label
        label = font_small.render(self.label, True, WHITE)
        surface.blit(label,(self.rect.x,self.rect.y - 25))

        # Entered text
        value = form_data[self.key] if isinstance(form_data[self.key], str) else ""
        txt = font_ui.render(value[-30:], True, WHITE) #Displays the last 30 characters
        surface.blit(txt,(self.rect.x + 10, self.rect.y + 10))

