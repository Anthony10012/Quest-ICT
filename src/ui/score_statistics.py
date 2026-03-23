"""
 Project name: Pré-TPI Quest-ICT
 File : score_statistics.py
 description:
 Author : Anthony Simond
 Date : 2026/
 last modified : 2026/
 Version : 1.1

"""
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

# --- Fonts ---
font_title = pygame.font.SysFont("Arial", 60, bold=True)
font_subtitle = pygame.font.SysFont("Arial", 32)
font_huge = pygame.font.SysFont("Arial", 70, bold=True)
font_button = pygame.font.SysFont("Arial", 25, bold=True)
font_medium = pygame.font.SysFont("Arial", 28, bold=True)
font_small = pygame.font.SysFont("Arial", 20)

results = [
    {"id": 1, "theme": "animaux", "difficulty": "facile", "score": 8, "totalQuestions": 10, "timePerQuestion": [3, 2, 4], "date": "2026-03-01"},
    {"id": 2, "theme": "informatique", "difficulty": "difficile", "score": 5, "totalQuestions": 10, "timePerQuestion": [8, 5, 6], "date": "2026-03-02"},
]


# --- Utility functions ---
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
def draw_back_button(mouse_pos):
    rect = pygame.Rect(30, 30, 150, 60)
    is_hovered = rect.collidepoint(mouse_pos)
    color = (255, 255, 255, 50) if not is_hovered else (255, 255, 255, 100)
    shape_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    pygame.draw.rect(shape_surface, color, (0, 0, rect.width, rect.height), border_radius=10)
    pygame.draw.rect(shape_surface, WHITE, (0, 0, rect.width, rect.height), width=2, border_radius=10)
    screen.blit(shape_surface, rect.topleft)
    text_surface = font_button.render("← RETOUR", True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)
    return rect

# --- UI status ---
selected_tab = "history"
def run_statistics(screen, results):
    global selected_tab
    running = True

    back_rect = pygame.Rect(50,50,150,60)

    while running:
        mouse_pos = pygame.mouse.get_pos()

        # --- Event management ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(mouse_pos):
                    return "BACK"

                # Clicks on tabs (simulated)
                if pygame.Rect(100, 750, 300, 60).collidepoint(mouse_pos): selected_tab = "history"
                if pygame.Rect(450, 750, 300, 60).collidepoint(mouse_pos): selected_tab = "theme"
                if pygame.Rect(800, 750, 300, 60).collidepoint(mouse_pos): selected_tab = "difficulty"


        # --- Drawing ---
        screen.fill(BG_COLOR)

        # Back button
        draw_back_button(mouse_pos)

        # Title
        draw_text_centered("STATISTIQUES",font_title,WHITE,(WIDTH//2,80))
        draw_text_centered("Analyse de tes performances",font_subtitle,YELLOW,(WIDTH//2,140))

        # --- Overall Stats ---
        avgScore, avgTime = calculate_stats(results)

        #Parties
        draw_rounded_rect(screen,pygame.Rect(50,200,350,200),BLUE_GRAD[1],20)
        draw_text_centered("PARTIES JOUÉES", font_medium, WHITE, (225, 240))
        draw_text_centered(str(len(results)), font_huge, WHITE, (225, 300))

        # Score
        draw_rounded_rect(screen, pygame.Rect(425, 200, 350, 200), GREEN_GRAD[1], 20)
        draw_text_centered("SCORE MOYEN", font_medium, WHITE, (600, 240))
        draw_text_centered(f"{avgScore:.0f}%", font_huge, WHITE, (600, 300))

        # Time
        draw_rounded_rect(screen, pygame.Rect(800, 200, 350, 200), PURPLE_GRAD[1], 20)
        draw_text_centered("TEMPS MOYEN", font_medium, WHITE, (975, 240))
        draw_text_centered(f"{avgTime:.1f}s", font_huge, WHITE, (975, 300))

        # --- Tabs (Simulation) ---
        tab_y = 750
        draw_rounded_rect(screen, pygame.Rect(100, tab_y, 300, 60),
                          BLUE_GRAD[0] if selected_tab == "history" else (100, 100, 100), 10)
        draw_text_centered("HISTORIQUE", font_medium, WHITE, (250, tab_y + 30))

        draw_rounded_rect(screen, pygame.Rect(450, tab_y, 300, 60),
                          GREEN_GRAD[0] if selected_tab == "theme" else (100, 100, 100), 10)
        draw_text_centered("PAR THÈME", font_medium, WHITE, (600, tab_y + 30))

        draw_rounded_rect(screen, pygame.Rect(800, tab_y, 300, 60),
                          PURPLE_GRAD[0] if selected_tab == "difficulty" else (100, 100, 100), 10)
        draw_text_centered("PAR DIFFICULTÉ", font_medium, WHITE, (950, tab_y + 30))

        #--- Tabs Content ---
        content_rect = pygame.Rect(50,830,1100,50)
        if selected_tab == "history":
            if len(results) > 0:
                draw_text_centered(f"Dernière partie : {results[-1]['theme']} - {results[-1]['score']}/{results[-1]['totalQuestions']}", font_small, WHITE, content_rect.center)
            else:
                msg ="Aucun historique disponible pour le moment."
        elif selected_tab == "theme":
            draw_text_centered("Stats par thème non implémentées graphiquement", font_small, WHITE, content_rect.center)
        elif selected_tab == "difficulty":
            draw_text_centered("Stats par difficulté non implémentées graphiquement", font_small, WHITE, content_rect.center)

        pygame.display.flip()
        clock.tick(60)

# --- Boucle principale ---
if __name__ == "__main__":
    run_statistics(screen, results)