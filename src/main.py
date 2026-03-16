import pygame
from ui.main_menu import MainMenu
from ui.game_menu import run_game_menu
from ui.score_statistics import run_statistics
from ui.login_page import run_login
def main():

    pygame.init()
    screen = pygame.display.set_mode((1200, 900))
    pygame.display.set_caption("QUIZ ÉDUCATIF")

    run_login(screen)
    current_state = "MAIN_MENU"
    running = True

    menu = MainMenu(screen)

    while running:
        if current_state == "MAIN_MENU":
            action = menu.run()
            if action == "GAME":
                current_state = "GAME_MENU"
            elif action == "STATS":
                current_state = "SCORES_STATS"
            elif action == "QUIT":
                running = False

        elif current_state == "GAME_MENU":
            resultat = run_game_menu(screen)
            if resultat == "MAIN_MENU":
                current_state = "MAIN_MENU"
            elif isinstance(resultat,dict):

                questions_quiz = resultat["questions"]
                run_game_quiz(screen, questions_quiz)
                current_state = "MAIN_MENU"
        elif current_state == "SCORES_STATS":
            action = run_statistics(screen,[])
            if action == "BACK":
                current_state = "MAIN_MENU"
            else:
                print(f"Quiz lancé avec : {resultat}")
                current_state = "MAIN_MENU"

    pygame.quit()

if __name__ == "__main__":
    main()