import pygame
import sys
from datetime import datetime

pygame.init()
WIDTH, HEIGHT = 1200, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Score Statistics")
clock = pygame.time.Clock()

BG_COLOR = (66, 37, 112)
WHITE = (255, 255, 255)
YELLOW = (253, 224, 71)
BLUE_GRAD = [(59, 130, 246), (37, 99, 235)]
GREEN_GRAD = [(16, 185, 129), (5, 150, 105)]
PURPLE_GRAD = [(168, 85, 247), (126, 34, 206)]

# --- Polices ---
font_title = pygame.font.SysFont("Arial", 60, bold=True)
font_subtitle = pygame.font.SysFont("Arial", 32)
font_huge = pygame.font.SysFont("Arial", 70, bold=True)
font_medium = pygame.font.SysFont("Arial", 28, bold=True)
font_small = pygame.font.SysFont("Arial", 20)

results = [
    {"id": 1, "theme": "animaux", "difficulty": "facile", "score": 8, "totalQuestions": 10, "timePerQuestion": [3, 2, 4], "date": "2026-03-01"},
    {"id": 2, "theme": "informatique", "difficulty": "difficile", "score": 5, "totalQuestions": 10, "timePerQuestion": [8, 5, 6], "date": "2026-03-02"},
]


# --- Fonctions utilitaires ---
def draw_rounded_rect(surface, rect, color, corner_radius):
    """Dessine un rectangle arrondi"""
    pygame.draw.rect(surface, color, rect, border_radius=corner_radius)


def draw_text_centered(text, font, color, center_pos, surface=screen):
    text_obj = font.render(text, True, color)
    rect = text_obj.get_rect(center=center_pos)
    surface.blit(text_obj, rect)


def calculate_stats(data):
    totalGames = len(data)
    if totalGames == 0:
        return 0, 0

    totalScorePerc = sum((r['score'] / r['totalQuestions']) * 100 for r in data)
    avgScore = totalScorePerc / totalGames

    totalTime = sum(sum(r['timePerQuestion']) / len(r['timePerQuestion']) for r in data)
    avgTime = totalTime / totalGames

    return avgScore, avgTime

