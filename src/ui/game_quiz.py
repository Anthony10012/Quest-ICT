import pygame
import sys

def run_game_menu(screen,quiz_data):
    WIDTH, HEIGHT = screen.get_size()
    clock = pygame.time.Clock()

    # Couleurs et Polices
    BG_COLOR = (66, 37, 112)
    WHITE = (255, 255, 255)
    GREEN = (16, 185, 129)
    RED = (239, 68, 68)

    font_q = pygame.font.SysFont("Arial", 40, bold=True)
    font_btn = pygame.font.SysFont("Arial", 30)