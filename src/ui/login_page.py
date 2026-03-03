import pygame
import sys

from pygame_menu.utils import ShadowGenerator

pygame.init()



WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("QUIZ ÉDUCATIF - Connexion")


BG_COLOR = (66, 37, 112)
WHITE = (255, 255, 255)
YELLOW = (255, 235, 59)
GREEN = (16, 185, 129)
GRAY = (100, 100, 100)

# Fonts
font_title = pygame.font.SysFont("Arial", 80, bold=True)
font_subtitle = pygame.font.SysFont("Arial", 30)
font_input = pygame.font.SysFont("Arial", 40)
font_button = pygame.font.SysFont("Arial", 50, bold=True)

# State variables
username = ""
input_active = True
error_msg = ""
clock = pygame.time.Clock()

def draw_text_centered(text, font, color,y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH //2, y))
    screen.blit(text_surface, text_rect)


# --- Colors configuration  ---
BOX_FILL_COLOR = (255, 255, 255, 30)
BOX_BORDER_COLOR = (255, 255, 255, 80)
# Text color
PLACEHOLDER_COLOR = (200, 200, 200)


def draw_input_box():
    # Create the surface for the input area (with transparency)
    input_rect = pygame.Rect(WIDTH // 4 + 50, 450, WIDTH // 2 - 100, 80)
    input_surface = pygame.Surface((input_rect.width, input_rect.height), pygame.SRCALPHA)

    #Draw the filled background (semi-transparent)
    pygame.draw.rect(input_surface, BOX_FILL_COLOR, (0, 0, input_rect.width, input_rect.height), border_radius=15)

    # Draw the outline
    pygame.draw.rect(input_surface, BOX_BORDER_COLOR, (0, 0, input_rect.width, input_rect.height), width=3,
                     border_radius=15)

    #Display the area on the screen
    screen.blit(input_surface, (input_rect.x, input_rect.y))

    # Manage text (username or placeholder)
    if username == "":
        txt_to_show = "Ex: SuperJoueur123"
        color_to_use = PLACEHOLDER_COLOR
    else:
        txt_to_show = username
        color_to_use = WHITE

    # Centered text rendering in the box
    txt_surf = font_input.render(txt_to_show, True, color_to_use)
    txt_rect = txt_surf.get_rect(center=input_rect.center)
    screen.blit(txt_surf, txt_rect)

def main():
    global username, input_active, error_msg

    running = True
    while running:
        screen.fill(BG_COLOR)

        #--- Events Mangement ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                    error_msg = ""
                elif event.key == pygame.K_RETURN:
                    # Pseudo validation
                    if len(username.strip()) < 3:
                        error_msg = "Le pseudo doit contenir au moins 3 caractères"
                    else:
                        print(f"Connexion réussie: {username}")
                        running = False
                elif event.key == pygame.K_ESCAPE:
                    pass
                else:
                    if len(username) < 50:
                        username += event.unicode


            # --- Interface Design ---

            #Title
            draw_text_centered("QUIZ ÉDUCATIF", font_title, WHITE, 200)
            draw_text_centered("Apprends en t'amusant", font_subtitle, YELLOW, 280)

            #Connexion card (Rounded rectangle)
            card_rect = pygame.Rect(WIDTH // 4, 350, WIDTH // 2, 350)
            pygame.draw.rect(screen, (66, 37, 112), card_rect,border_radius=20)

            #Label Pseudo
            draw_text_centered("TON PSEUDO", font_subtitle,WHITE, 400)


            draw_input_box()

            # Error message
            if error_msg:
                draw_text_centered(error_msg, font_subtitle, (255, 100, 100), 530)

            # Button "C EST PARTI"
            btn_rect = pygame.Rect(WIDTH // 4 + 50, 580, WIDTH // 2 - 100, 80)
            mouse_pos = pygame.mouse.get_pos()

            #Animation hover
            if btn_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen,(20,210,150),btn_rect,border_radius=15)
                if pygame.mouse.get_pressed()[0]:# left click
                    if len(username.strip()) >= 3:
                        running = False
                    else:
                        error_msg = " Trop court !"
            else:
                pygame.draw.rect(screen,GREEN,btn_rect,border_radius=15)

            btn_text = font_button.render("C'EST PARTI !", True, WHITE)
            screen.blit(btn_text, btn_text.get_rect(center=btn_rect.center))

            # Footer
            draw_text_centered("Version 1.0 - Jeu interactif", font_subtitle, GRAY, 750)

            pygame.display.flip()
            clock.tick(60)
            # Transition vers le jeu
    print("Lancement du jeu...")

if __name__ == "__main__":
    main()

