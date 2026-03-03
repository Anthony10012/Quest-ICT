import pygame
import sys

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
                elif event.key == pygame.K_RETURN:
                    # Pseudo validation
                    if len(username.strip()) < 3:
                        error_msg = "Le pseudo doit contenir au moins 3 caractères"
                    else:
                        print(f"Connexion réussie: {username}")
                        running = False

                else:
                    if len(username) < 50:
                        username += event.unicode