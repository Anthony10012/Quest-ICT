import pygame
import sys
import os
import time


def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = []
    for word in words:
        test_line = ' '.join(current_line + [word])
        if font.size(test_line)[0] <= max_width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    lines.append(' '.join(current_line))
    return lines


def run_game_quiz(screen, quiz_data):
    WIDTH, HEIGHT = screen.get_size()
    clock = pygame.time.Clock()

    # --- Couleurs ---
    BG_COLOR = (66, 37, 112)
    WHITE = (255, 255, 255)
    YELLOW = (253, 224, 71)
    GREEN = (34, 197, 94)
    RED = (239, 68, 68)
    CARD_BG = (255, 255, 255)

    # --- Polices ---
    font_question = pygame.font.SysFont("Arial", 45, bold=True)
    font_btn = pygame.font.SysFont("Arial", 28, bold=True)
    font_ui = pygame.font.SysFont("Arial", 24, bold=True)
    font_explanation = pygame.font.SysFont("Arial", 22, italic=True)

    # --- Game Status ---
    current_idx = 0
    score = 0
    start_time = time.time()
    selected_answer = None
    is_answered = False
    time_per_question = []

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, "..", ".."))

    while current_idx < len(quiz_data):
        question = quiz_data[current_idx]
        elapsed = int(time.time() - start_time) if not is_answered else elapsed

        screen.fill(BG_COLOR)

        # ---Question ---
        question_lines = wrap_text(question["question"], font_question, WIDTH - 100)
        y_ptr = 160
        for line in question_lines:
            txt = font_question.render(line, True, WHITE)
            screen.blit(txt, (50, y_ptr))
            y_ptr += 55

        # --- Header (Timer & Score) ---
        timer_txt = font_ui.render(f"Time :{elapsed}s", True, WHITE)
        score_txt = font_ui.render(f"{score}/{len(quiz_data)}", True, WHITE)
        screen.blit(timer_txt, (WIDTH - 150, 30))
        screen.blit(score_txt, (WIDTH - 150, 70))




        # --- Answer Grid ---
        answer_rects = []
        card_w, card_h = 420, 280
        start_x = (WIDTH - (card_w * 2 + 40)) // 2
        start_y = y_ptr + 30

        for i, answer in enumerate(question["answers"]):
            col, row = i % 2, i // 2
            r = pygame.Rect(start_x + col * (card_w + 40), start_y + row * (card_h + 30), card_w, card_h)

            # Color Logic
            color = CARD_BG
            if is_answered:
                if answer["is_correct"]:
                    color = GREEN
                elif i == selected_answer:
                    color = RED

            pygame.draw.rect(screen, color, r, border_radius=15)
            if i == selected_answer:
                pygame.draw.rect(screen, WHITE, r, width=4, border_radius=15)

            # Image or text
            image_drawn = False
            if answer.get("image_path"):
                path = os.path.normpath(os.path.join(project_root, "assets", "images", answer["image_path"]))
                if os.path.exists(path):
                    try:
                        img = pygame.image.load(path).convert_alpha()
                        img = pygame.transform.smoothscale(img, (card_w - 40, card_h - 60))
                        screen.blit(img, img.get_rect(center=r.center))
                        image_drawn = True
                    except:
                        pass

            if not image_drawn or is_answered:
                # On affiche le texte si pas d'image, ou par dessus si répondu pour aider
                txt_color = (66, 37, 112) if color == WHITE else WHITE
                txt = font_btn.render(answer["response_text"], True, txt_color)
                screen.blit(txt, txt.get_rect(center=(r.centerx, r.bottom - 30 if image_drawn else r.centery)))

            answer_rects.append((r, i))

        # --- Explanation and button Suivant ---
        if is_answered:
            # Text Explanation
            expl_lines = wrap_text(f"Note: {question.get('explanation', '')}", font_explanation, WIDTH - 100)
            ey = start_y + (card_h * 2) + 40
            for eline in expl_lines:
                screen.blit(font_explanation.render(eline, True, YELLOW), (50, ey))
                ey += 25

            # Button Suivant
            next_btn = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 80, 200, 60)
            pygame.draw.rect(screen, YELLOW, next_btn, border_radius=10)
            label = "TERMINER" if current_idx == len(quiz_data) - 1 else "SUIVANT"
            l_surf = font_btn.render(label, True, (0, 0, 0))
            screen.blit(l_surf, l_surf.get_rect(center=next_btn.center))
        else:
            next_btn = pygame.Rect(0, 0, 0, 0)  # disabled

        # --- Events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not is_answered:
                    for r, i in answer_rects:
                        if r.collidepoint(event.pos):
                            selected_answer = i
                            is_answered = True
                            time_per_question.append(time.time() - start_time)
                            if question["answers"][i]["is_correct"]:
                                score += 1
                elif next_btn.collidepoint(event.pos):
                    current_idx += 1
                    is_answered = False
                    selected_answer = None
                    start_time = time.time()

        pygame.display.flip()
        clock.tick(60)

    return {"score": score, "times": time_per_question}