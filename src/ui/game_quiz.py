import pygame
import sys

def run_game_menu(screen,quiz_data):
    WIDTH, HEIGHT = screen.get_size()
    clock = pygame.time.Clock()

    # Colors and Fonts
    BG_COLOR = (66, 37, 112)
    WHITE = (255, 255, 255)
    GREEN = (16, 185, 129)
    RED = (239, 68, 68)

    font_question = pygame.font.SysFont("Arial", 40, bold=True)
    font_btn = pygame.font.SysFont("Arial", 30)

    #  Game Status
    current_question_index = 0
    score = 0
    time_limit = 20000 # 20 seconds
    start_time = pygame.time.get_ticks()

    while current_question_index < len(quiz_data):
        question_data = quiz_data[current_question_index]
        elapsed = pygame.time.get_ticks() - start_time
        remaining = max(0, (time_limit - elapsed) // 1000)

        # if times is up
        if elapsed > time_limit:
            current_question_index += 1
            start_time = pygame.time.get_ticks()
            continue

        screen.fill(BG_COLOR)

        # -- Drawing ---
        # Text question
        text_surface = font_question.render(question_data["question"], True, WHITE)
        screen.blit(text_surface, (100,100))

        # Timer
        timer_surface = font_question.render(f"Temps : {remaining}", True, WHITE)
        screen.blit(timer_surface, (WIDTH - 250, 50))

        # Answers button
        answers_rectangles = []
        for i, answer in enumerate(question_data["answers"]):
            rectangle = pygame.Rect(150, 300 + i * 120, 900, 80)
            pygame.draw.rect(screen,(255, 255, 255, 50), rectangle, border_radius=15)
            txt = font_btn.render(answer["response_text"], True, WHITE)
            screen.blit(txt,(180, 320 + i * 120))
            answers_rectangles.append((rectangle,answer["is_correct"]))



