import pygame
from ui.main_menu import MainMenu
from ui.game_menu import run_game_menu

def main():

    pygame.init()
    screen = pygame.display.set_mode((1200, 900))
    pygame.display.set_caption("QUIZ ÉDUCATIF")

    current_state = "MAIN_MENU"
    running = True

    menu = MainMenu(screen)

    while running:
        if current_state == "MAIN_MENU":
            action = menu.run()
            if action == "GAME":
                current_state = "GAME_MENU"
            elif action == "QUIT":
                running = False
        elif current_state == "GAME_MENU":
            resultat = run_game_menu(screen)
            if resultat == "MAIN_MENU":
                current_state = "MAIN_MENU"
            else:
                print(f"Quiz lancé avec : {resultat}")
                current_state = "MAIN_MENU"

    pygame.quit()


if __name__ == "__main__":
    main()