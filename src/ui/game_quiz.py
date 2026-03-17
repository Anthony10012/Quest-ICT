import pygame
import sys
import os


def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        size = font.size(test_line)
        if size[0] <= max_width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]

    lines.append(' '.join(current_line))
    return lines
def run_game_quiz(screen,quiz_data):
    WIDTH, HEIGHT = screen.get_size()
    clock = pygame.time.Clock()

    # Colors and Fonts
    BG_COLOR = (66, 37, 112)
    WHITE = (255, 255, 255)
    YELLOW = (253, 224, 71)

    font_question = pygame.font.SysFont("Arial", 40, bold=True)
    font_btn = pygame.font.SysFont("Arial", 30)
    font_info = pygame.font.SysFont("Arial", 20, bold=True)

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

        # --- Title and Infos  ---
        info_text = f"{question_data.get('theme', 'QUIZ')} • {question_data.get('difficulty', 'NORMAL')}"
        info_surf = font_info.render(info_text, True, YELLOW)
        screen.blit(info_surf, (40, 30))

        # --- Question with automatic line break ---
        max_q_width = WIDTH - 100
        question_lines = wrap_text(question_data["question"], font_question, max_q_width)

        y_offset = 70
        for line in question_lines:
            line_surf = font_question.render(line, True, WHITE)
            screen.blit(line_surf, (40, y_offset))
            y_offset += 55  # Espace entre les lignes de texte

        # Ajuste le début de la grille des images selon le nombre de lignes
        # Si la question est longue, start_y descend pour ne pas cacher les images
        start_y = y_offset + 30

        # Timer
        timer_surface = font_question.render(f"Temps : {remaining}", True, WHITE)
        screen.blit(timer_surface, (WIDTH - 250, 50))

        # ---  Answers Grid ---
        answers_rectangles = []

        # Card dimensions
        card_w, card_h = 450, 320
        margin_x, margin_y = 40, 30
        start_x = (WIDTH - (card_w * 2 + margin_x)) // 2

        for i, answer in enumerate(question_data["answers"]):
            col = i % 2
            row = i // 2

            # Position of the background rectangle
            rect = pygame.Rect(start_x + col * (card_w + margin_x),
                               start_y + row * (card_h + margin_y),
                               card_w, card_h)
            # Card design
            pygame.draw.rect(screen, (255, 255, 255, 30), rect, border_radius=20)
            pygame.draw.rect(screen, (255, 255, 255, 80), rect, width=2, border_radius=20)

            # ---  Loading from the database via image_path ---
            # we retrieve the path store in  the Database (ex: "animals/lion.png")
            db_image_path = answer.get("image_path")

            if db_image_path:
                current_dir = os.path.dirname(os.path.abspath(__file__))
                project_root = os.path.abspath(os.path.join(current_dir,"..",".."))
                full_img_path = os.path.join(project_root, "assets", "images", db_image_path)

                try:
                    img = pygame.image.load(full_img_path).convert_alpha()
                    # Resizing
                    img = pygame.transform.smoothscale(img, (card_w - 60, card_h - 100))
                    img_rect = img.get_rect(center=rect.center)
                    screen.blit(img, img_rect)
                except Exception as e:
                    # If the image cannot be found, the response text is displayed
                    txt = font_btn.render(answer["response_text"], True, WHITE)
                    screen.blit(txt, txt.get_rect(center=rect.center))
            else:
                txt = font_btn.render(answer["response_text"], True, WHITE)
                screen.blit(txt, txt.get_rect(center=rect.center))
            answers_rectangles.append((rect, answer["is_correct"]))


        # --- Events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for rectangle, is_correct in answers_rectangles:
                    if rectangle.collidepoint(event.pos):
                        if is_correct:
                            score += 1
                        current_question_index += 1
                        start_time = pygame.time.get_ticks()

        pygame.display.flip()
        clock.tick(60)
    return score

