import pygame
import sys

def run_game_menu(screen,quiz_data):
    WIDTH, HEIGHT = screen.get_size()
    clock = pygame.time.Clock()

    # Colors and Fonts
    BG_COLOR = (66, 37, 112)
    WHITE = (255, 255, 255)
    GREEN = (16, 185, 129)
    RED = (239, 68, 68)

    font_q = pygame.font.SysFont("Arial", 40, bold=True)
    font_btn = pygame.font.SysFont("Arial", 30)

    #  Game Status
    current_question_index = 0
    score = 0
    time_limit = 20000 # 20 seconds
    start_time = pygame.time.get_ticks()

