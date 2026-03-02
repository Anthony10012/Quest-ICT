import pygame


# --- Configuration & Couleurs ---
pygame.init()
WIDTH, HEIGHT = 1200, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiz Selector")
clock = pygame.time.Clock()


BG_COLOR = (66, 37, 112)
WHITE = (255, 255, 255)
YELLOW = (253, 224, 71)
GRAY_OVERLAY = (255, 255, 255, 30)

# Données des thèmes
THEMES = [
    {"id": "animaux", "name": "ANIMAUX", "emoji": "🐾", "color": (16, 185, 129)},
    {"id": "drapeaux", "name": "DRAPEAUX", "emoji": "🏁", "color": (59, 130, 246)},
    {"id": "informatique", "name": "INFORMATIQUE", "emoji": "💻", "color": (139, 92, 246)},
    {"id": "geographie", "name": "GEOGRAPHIE", "emoji": "🌍", "color": (6, 182, 212)},
    {"id": "histoire", "name": "HISTOIRE", "emoji": "📚", "color": (245, 158, 11)},
    {"id": "sciences", "name": "SCIENCES", "emoji": "🔬", "color": (236, 72, 153)},
]

DIFFICULTIES = [
    {"id": "facile", "name": "FACILE", "color": (74, 222, 128)},
    {"id": "moyen", "name": "MOYEN", "color": (251, 191, 36)},
    {"id": "difficile", "name": "DIFFICILE", "color": (239, 68, 68)},
]

# --- Polices ---

try:
    font_large = pygame.font.SysFont("Arial", 60, bold=True)
    font_medium = pygame.font.SysFont("Arial", 32, bold=True)
    font_small = pygame.font.SysFont("Arial", 20)
    font_emoji = pygame.font.SysFont("Segoe UI Emoji", 50)
except:
    font_large = pygame.font.Font(None, 80)
    font_medium = pygame.font.Font(None, 40)
    font_small = pygame.font.Font(None, 25)
    font_emoji = pygame.font.Font(None, 60)

# --- État de l'application ---
selected_theme = None
selected_difficulty = None


def draw_text_centered(text, font, color, y, surface=screen):
    text_obj = font.render(text, True, color)
    rect = text_obj.get_rect(center=(WIDTH // 2, y))
    surface.blit(text_obj, rect)


def draw_button(rect, text, emoji, color, is_selected, hover=False):
    # Calcul de l'échelle (effet scale-110)
    draw_rect = rect.inflate(20, 20) if is_selected else rect
    border_color = WHITE if (is_selected or hover) else (255, 255, 255, 50)
    bg_color = color if is_selected else (255, 255, 255, 20)

    # Dessin du bouton (Approximation du glassmorphism/gradient)
    shape_surf = pygame.Surface((draw_rect.width, draw_rect.height), pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, bg_color, (0, 0, draw_rect.width, draw_rect.height), border_radius=15)
    pygame.draw.rect(shape_surf, border_color, (0, 0, draw_rect.width, draw_rect.height), width=3, border_radius=15)
    screen.blit(shape_surf, draw_rect.topleft)

    # Emoji & Texte
    y_offset = draw_rect.centery - 20
    if emoji:
        e_surf = font_emoji.render(emoji, True, WHITE)
        e_rect = e_surf.get_rect(center=(draw_rect.centerx, y_offset))
        screen.blit(e_surf, e_rect)
        y_offset += 50

    t_surf = font_medium.render(text, True, WHITE)
    t_rect = t_surf.get_rect(center=(draw_rect.centerx, y_offset + 10))
    screen.blit(t_surf, t_rect)


# --- Boucle principale ---
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check Thèmes
            for i, theme in enumerate(THEMES):
                col, row = i % 3, i // 3
                rect = pygame.Rect(150 + col * 320, 250 + row * 160, 280, 140)
                if rect.collidepoint(mouse_pos):
                    selected_theme = theme['id']

            # Check Difficultés
            for i, diff in enumerate(DIFFICULTIES):
                rect = pygame.Rect(150 + i * 320, 620, 280, 120)
                if rect.collidepoint(mouse_pos):
                    selected_difficulty = diff['id']

            # Check Bouton Start
            if selected_theme and selected_difficulty:
                start_rect = pygame.Rect(WIDTH // 2 - 200, 780, 400, 80)
                if start_rect.collidepoint(mouse_pos):
                    print(f"Lancement du quiz: {selected_theme} en {selected_difficulty}")

    # --- Rendu ---
    screen.fill(BG_COLOR)

    # Titres
    draw_text_centered("CHOISIS TON QUIZ", font_large, WHITE, 80)
    draw_text_centered("⚡ Sélectionne un thème et un niveau ⚡", font_small, YELLOW, 150)

    draw_text_centered("THÈME", font_medium, WHITE, 210)

    # Grille des thèmes
    for i, theme in enumerate(THEMES):
        col, row = i % 3, i // 3
        rect = pygame.Rect(150 + col * 320, 250 + row * 160, 280, 140)
        is_sel = selected_theme == theme['id']
        is_hov = rect.collidepoint(mouse_pos)
        draw_button(rect, theme['name'], theme['emoji'], theme['color'], is_sel, is_hov)

    # Difficultés
    draw_text_centered("DIFFICULTÉ", font_medium, WHITE, 580)
    for i, diff in enumerate(DIFFICULTIES):
        rect = pygame.Rect(150 + i * 320, 620, 280, 120)
        is_sel = selected_difficulty == diff['id']
        is_hov = rect.collidepoint(mouse_pos)
        draw_button(rect, diff['name'], None, diff['color'], is_sel, is_hov)

    # Bouton Start (C'EST PARTI)
    if selected_theme and selected_difficulty:
        start_rect = pygame.Rect(WIDTH // 2 - 200, 780, 400, 80)
        hover_start = start_rect.collidepoint(mouse_pos)
        color_start = (234, 179, 8) if not hover_start else (245, 158, 11)
        pygame.draw.rect(screen, color_start, start_rect, border_radius=20)
        pygame.draw.rect(screen, WHITE, start_rect, width=4, border_radius=20)
        draw_text_centered("C'EST PARTI !", font_medium, WHITE, 820)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

