import pygame
import sys
from src.sql.database import add_user,check_user_exists


def run_login(screen):
    WIDTH, HEIGHT = screen.get_size()

    # Colors
    BG_COLOR = (66, 37, 112)
    WHITE = (255, 255, 255)
    YELLOW = (255, 235, 59)
    GREEN = (16, 185, 129)
    GRAY = (100, 100, 100)
    PINK = (236, 72, 153)
    BLUE_VIOLET = (99, 102, 241)
    YELLOW_TEXT = (255, 235, 59)
    BOX_FILL_COLOR = (255, 255, 255, 30)
    BOX_BORDER_COLOR = (255, 255, 255, 80)
    PLACEHOLDER_COLOR = (200, 200, 200)

    # Fonts
    font_title = pygame.font.SysFont("Arial", 80, bold=True)
    font_subtitle = pygame.font.SysFont("Arial", 30)
    font_input = pygame.font.SysFont("Arial", 40)
    font_button = pygame.font.SysFont("Arial", 40, bold=True)

    # State variables
    username = ""
    error_msg = ""
    clock = pygame.time.Clock()

    def draw_text_centered(text, font, color, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, y))
        screen.blit(text_surface, text_rect)

    running = True
    while running:
        screen.fill(BG_COLOR)
        mouse_pos = pygame.mouse.get_pos()

        # --- Events Management ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pseudo_input = username.strip()

                    if btn1_rect.collidepoint(event.pos):
                        if len(pseudo_input) >= 3:
                            if check_user_exists(pseudo_input):
                                return pseudo_input
                            else:
                                error_msg = "Compte inexistant ! Créez-en un."
                        else:
                            error_msg = "Pseudo trop court !"
                    elif btn2_rect.collidepoint(event.pos):
                        if len(pseudo_input) >= 3:
                            if add_user(pseudo_input):
                                return pseudo_input
                            else:
                                error_msg = "Ce pseudo existe déjà"
                        else:
                            error_msg = "Pseudo trop court !"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                    error_msg = ""
                elif event.key == pygame.K_RETURN:
                    if len(username.strip()) >= 3:
                        return username.strip()  # <--- Return pseudo into main
                    error_msg = "Le pseudo doit contenir au moins 3 caractères"
                elif event.unicode.isprintable() and len(username) < 20:
                    username += event.unicode
                    error_msg = ""

        # --- Interface Design ---

        # Header (Icon + Titles)
        icon_center = (WIDTH // 2, 220)
        pygame.draw.circle(screen, WHITE, icon_center, 42, width=3)
        pygame.draw.circle(screen, PINK, icon_center, 40)
        pygame.draw.circle(screen, WHITE, (icon_center[0], icon_center[1] - 10), 10, width=2)
        pygame.draw.arc(screen, WHITE, (icon_center[0] - 15, icon_center[1], 30, 20), 0, 3.14, 2)

        draw_text_centered("QUIZ ÉDUCATIF", font_title, WHITE, 100)
        draw_text_centered("Apprends en t'amusant", font_subtitle, YELLOW, 150)

        # Card
        draw_text_centered("CONNEXION", font_button, WHITE, 300)
        draw_text_centered("Entre ton pseudo pour commencer", font_subtitle, YELLOW_TEXT, 350)
        draw_text_centered("TON PSEUDO", font_subtitle, WHITE, 420)

        # Input Box
        input_rect = pygame.Rect(WIDTH // 4 + 50, 450, WIDTH // 2 - 100, 80)
        input_surf = pygame.Surface((input_rect.width, input_rect.height), pygame.SRCALPHA)
        pygame.draw.rect(input_surf, BOX_FILL_COLOR, (0, 0, input_rect.width, input_rect.height), border_radius=15)
        pygame.draw.rect(input_surf, BOX_BORDER_COLOR, (0, 0, input_rect.width, input_rect.height), width=3,
                         border_radius=15)
        screen.blit(input_surf, (input_rect.x, input_rect.y))

        # Text in input field
        txt_display = username if username else "Ex: SuperJoueur123"
        txt_col = WHITE if username else PLACEHOLDER_COLOR
        surf_txt = font_input.render(txt_display, True, txt_col)
        screen.blit(surf_txt, surf_txt.get_rect(center=input_rect.center))

        if error_msg:
            draw_text_centered(error_msg, font_subtitle, (255, 100, 100), 540)

        # --- Button 1 : Log In ---
        btn1_rect = pygame.Rect(WIDTH // 4 + 50, 580, WIDTH // 2 - 100, 80)
        is_hover1 = btn1_rect.collidepoint(mouse_pos)
        btn_color1 = (20, 210, 150) if is_hover1 else GREEN
        pygame.draw.rect(screen, btn_color1, btn1_rect, border_radius=15)

        btn1_text = font_button.render("→ SE CONNECTER",True,WHITE)
        screen.blit(btn1_text, btn1_text.get_rect(center=btn1_rect.center))

        # --- Button 2 : CREATE  ---
        btn2_rect = pygame.Rect(WIDTH // 4 + 50, 680, WIDTH // 2 - 100, 100)
        is_hover2 = btn2_rect.collidepoint(mouse_pos)
        btn_color2 = (120, 130, 255) if is_hover2 else BLUE_VIOLET
        pygame.draw.rect(screen, btn_color2, btn2_rect, border_radius=15)

        btn2_text = font_button.render("+ CRÉER UN COMPTE", True, WHITE)
        screen.blit(btn2_text, btn2_text.get_rect(center=btn2_rect.center))

        # --- Logic Clic ---
        if pygame.mouse.get_pressed()[0]:
            if is_hover1:
                if len(username.strip()) >= 3:
                    return username.strip()
                error_msg = " Trop court !"
            elif is_hover2:
                print("Action : Créer un compte")
        draw_text_centered("Version 1.0 - Jeu interactif", font_subtitle, GRAY, 850)

        pygame.display.flip()
        clock.tick(60)