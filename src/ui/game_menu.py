import pygame
import sys
from src.logic.quiz_engine import get_random_quiz
def run_game_menu(screen):
    # --- Configuration ---
    WIDTH, HEIGHT = screen.get_size()
    clock = pygame.time.Clock()

    # Colors
    BG_COLOR = (66, 37, 112)
    WHITE = (255, 255, 255)
    YELLOW = (253, 224, 71)

    # Theme data
    THEMES = [
        {"id": 1, "name": "ANIMAUX", "emoji": "🐾", "color": (16, 185, 129)},
        {"id": 2 , "name": "DRAPEAUX", "emoji": "🏁", "color": (59, 130, 246)},
        {"id": 3 , "name": "INFORMATIQUE", "emoji": "💻", "color": (139, 92, 246)},
        {"id": 4, "name": "GEOGRAPHIE", "emoji": "🌍", "color": (6, 182, 212)},
        {"id": 5 , "name": "HISTOIRE", "emoji": "📚", "color": (245, 158, 11)},
        {"id": 6 , "name": "SCIENCES", "emoji": "🔬", "color": (236, 72, 153)},
    ]
    DIFFICULTIES = [
        {"id": "facile", "name": "FACILE", "color": (74, 222, 128)},
        {"id": "moyen", "name": "MOYEN", "color": (251, 191, 36)},
        {"id": "difficile", "name": "DIFFICILE", "color": (239, 68, 68)},
    ]

    # --- Fonts ---
    font_large = pygame.font.SysFont("Arial", 60, bold=True)
    font_medium = pygame.font.SysFont("Arial", 32, bold=True)
    font_small = pygame.font.SysFont("Arial", 20)
    font_button = pygame.font.SysFont("Arial", 25, bold=True)
    font_emoji = pygame.font.SysFont("Segoe UI Emoji", 50)

    # --- Status ---
    selected_theme = None
    selected_difficulty = None

    def draw_text_centered(text, font, color, y):
        text_obj = font.render(text, True, color)
        rect = text_obj.get_rect(center=(WIDTH // 2, y))
        screen.blit(text_obj, rect)

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

    def draw_button(rect, text, emoji, color, is_selected, hover=False):
        draw_rect = rect.inflate(20, 20) if is_selected else rect
        border_color = WHITE if (is_selected or hover) else (255, 255, 255, 50)
        bg_color = color if is_selected else (255, 255, 255, 20)
        shape_surf = pygame.Surface((draw_rect.width, draw_rect.height), pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, bg_color, (0, 0, draw_rect.width, draw_rect.height), border_radius=15)
        pygame.draw.rect(shape_surf, border_color, (0, 0, draw_rect.width, draw_rect.height), width=3, border_radius=15)
        screen.blit(shape_surf, draw_rect.topleft)
        y_offset = draw_rect.centery - 20
        if emoji:
            e_surf = font_emoji.render(emoji, True, WHITE)
            e_rect = e_surf.get_rect(center=(draw_rect.centerx, y_offset))
            screen.blit(e_surf, e_rect)
            y_offset += 50
        t_surf = font_medium.render(text, True, WHITE)
        t_rect = t_surf.get_rect(center=(draw_rect.centerx, y_offset + 10))
        screen.blit(t_surf, t_rect)

    # --- Main function loop ---
    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check the return button
                back_rect = pygame.Rect(30, 30, 150, 60)
                if back_rect.collidepoint(mouse_pos):
                    return "MAIN_MENU"

                # Check Themes
                for i, theme in enumerate(THEMES):
                    col, row = i % 3, i // 3
                    rect = pygame.Rect(150 + col * 320, 250 + row * 160, 280, 140)
                    if rect.collidepoint(mouse_pos):
                        selected_theme = theme['id']

                # Check Difficulties
                for i, diff in enumerate(DIFFICULTIES):
                    rect = pygame.Rect(150 + i * 320, 620, 280, 120)
                    if rect.collidepoint(mouse_pos):
                        selected_difficulty = diff['id']

                # Check Button Start
                if selected_theme and selected_difficulty:
                    start_rect = pygame.Rect(WIDTH // 2 - 200, 780, 400, 80)
                    if start_rect.collidepoint(mouse_pos):

                        print(f"Lancement du quiz : {selected_theme} - {selected_difficulty}")

                        # Call function get_random_quiz
                        quiz_questions = get_random_quiz(themes_id=selected_theme,limit=8)

                        return {
                            "theme": selected_theme,
                            "difficulty": selected_difficulty,
                            "questions": quiz_questions
                        }

        # --- Rendering ---
        screen.fill(BG_COLOR)
        draw_text_centered("CHOISIS TON QUIZ", font_large, WHITE, 80)
        draw_text_centered("Sélectionne un thème et un niveau", font_small, YELLOW, 150)
        draw_text_centered("THÈME", font_medium, WHITE, 210)

        for i, theme in enumerate(THEMES):
            col, row = i % 3, i // 3
            rect = pygame.Rect(150 + col * 320, 250 + row * 160, 280, 140)
            is_sel = selected_theme == theme['id']
            is_hov = rect.collidepoint(mouse_pos)
            draw_button(rect, theme['name'], theme['emoji'], theme['color'], is_sel, is_hov)

        draw_text_centered("DIFFICULTÉ", font_medium, WHITE, 580)
        for i, diff in enumerate(DIFFICULTIES):
            rect = pygame.Rect(150 + i * 320, 620, 280, 120)
            is_sel = selected_difficulty == diff['id']
            is_hov = rect.collidepoint(mouse_pos)
            draw_button(rect, diff['name'], None, diff['color'], is_sel, is_hov)

        if selected_theme and selected_difficulty:
            start_rect = pygame.Rect(WIDTH // 2 - 200, 780, 400, 80)
            hover_start = start_rect.collidepoint(mouse_pos)
            color_start = (234, 179, 8) if not hover_start else (245, 158, 11)
            pygame.draw.rect(screen, color_start, start_rect, border_radius=20)
            pygame.draw.rect(screen, WHITE, start_rect, width=4, border_radius=20)
            draw_text_centered("C'EST PARTI !", font_medium, WHITE, 820)

        draw_back_button(mouse_pos)
        pygame.display.flip()
        clock.tick(60)