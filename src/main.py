import pygame
from ui.main_menu import MainMenu
from ui.game_menu import run_game_menu
from ui.score_statistics import run_statistics
from ui.login_page import run_login
from ui.game_quiz import run_game_quiz
def main():

    pygame.init()
    screen = pygame.display.set_mode((1200, 900))
    pygame.display.set_caption("QUIZ ÉDUCATIF")

    pseudo = run_login(screen)
    current_state = "MAIN_MENU"
    running = True
    from sql.database import get_user_id_by_pseudo
    current_user_id = get_user_id_by_pseudo(pseudo)


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
                if len(questions_quiz) > 0:
                    theme_id = questions_quiz[0]["themes_id"]
                else:
                    theme_id = 1  # Value to default if empty

                stats_partie = run_game_quiz(screen,questions_quiz)

                from sql.database import save_game_result
                save_game_result(
                    users_id=current_user_id,
                    themes_id=theme_id,
                    final_score=stats_partie["score"],
                    total_time=stats_partie["total_time"]
                )
                current_state = "MAIN_MENU"
        elif current_state == "SCORES_STATS":
            from sql.database import get_user_stats
            real_results = get_user_stats(current_user_id)
            action = run_statistics(screen, real_results)
            if action == "BACK":
                current_state = "MAIN_MENU"
            else:
                print(f"Quiz lancé avec : {resultat}")
                current_state = "MAIN_MENU"

    pygame.quit()

if __name__ == "__main__":
    main()