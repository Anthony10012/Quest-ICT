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
