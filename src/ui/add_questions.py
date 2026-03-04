import pygame
import sys


# --- CONFIGURATION ---
pygame.init()
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ajouter une Question - Pygame Edition")

# Colors
BG_COLOR = (66, 37, 112)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)
GREEN = (34, 197, 94)
BLUE_GRAD = (30, 58, 138)

# Fonts
font_title = pygame.font.SysFont("Arial", 50, bold=True)
font_ui = pygame.font.SysFont("Arial", 24)
font_small = pygame.font.SysFont("Arial", 18)

# --- Form Status ---
form_data = {
    "question":"",
    "explanation":"",
    "correct_answer": None,
    "answers": ["","","",""]
}
active_field = None # To find out which text field is selected

# --- Classes UI ---
class Button:
    def __init__(self, x, y, w, h, text, color, callback):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color
        self.callback = callback

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=12)
        pygame.draw.rect(surface, WHITE, self.rect, 2, border_radius=12)
        txt = font_ui.render(self.text, True, WHITE)
        surface.blit(txt, (self.rect.centerx - txt.get_width()//2, self.rect.centery - txt.get_height()//2))

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.callback()


class InputBox:
    def __init__(self, x, y, w, h, label, key):
        self.rect = pygame.Rect(x, y, w, h)
        self.label = label
        self.key = key

    def draw(self, surface):
        color = YELLOW if active_field == self.key else WHITE
        pygame.draw.rect(surface, color, self.rect, 2, border_radius=8)

        #Label
        label = font_small.render(self.label, True, WHITE)
        surface.blit(label,(self.rect.x,self.rect.y - 25))

        # Entered text
        value = form_data[self.key] if isinstance(form_data[self.key], str) else ""
        txt = font_ui.render(value[-30:], True, WHITE) #Displays the last 30 characters
        surface.blit(txt,(self.rect.x + 10, self.rect.y + 10))

# --- Logic ---
def submit_form():
    if not form_data["question"] or form_data["correct_answer"] is None:
        print(" Formulaire incomplet !")
    else:
        print(f"Question ajoutée : {form_data['question']}")

buttons = [
    Button(WIDTH//2 - 150, 700, 300, 60, "AJOUTER", GREEN, submit_form)
]
inputs = [
    InputBox(100, 200, 1000, 50, "QUESTION", "question"),
    InputBox(100, 600, 1000, 50, "EXPLICATION", "explanation")
]

# Grid for the 4 answers
for i in range(4):
    row = i // 2
    column = i % 2


# --- Main Loop ---
running = True
while running:
    screen.fill(BG_COLOR)

    # Title
    title_surface = font_title.render("Ajouter une question", True, WHITE)
    screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, 50))

    # Drawing input and buttons
    for input in inputs:
        input.draw(screen)

    for button in buttons:
        button.draw(screen)

    # Correct answer selection area (1-4)
    instructions = font_small.render("Ajouter 4 images et coche la bonne réponses", True, YELLOW)
    screen.blit(instructions,(100,300))
    if form_data["correct_answer"] is not None:
        correct_answer = font_ui.render(f"Bonne réponse : {form_data["correct_answer"] + 1}", True, GREEN)
        screen.blit(correct_answer, (100, 330))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check focus sur inputs
            active_field = None
            for inp in inputs:
                if inp.rect.collidepoint(event.pos):
                    active_field = inp.key
            # Check boutons
            for btn in buttons:
                btn.check_click(event.pos)

        if event.type == pygame.KEYDOWN:
            if active_field:
                if event.key == pygame.K_BACKSPACE:
                    form_data[active_field] = form_data[active_field][:-1]
                elif event.key == pygame.K_RETURN:
                    active_field = None
                else:
                    form_data[active_field] += event.unicode


                    if event.key == pygame.K_F1: form_data["correct_answer"] = 0
                    if event.key == pygame.K_F2: form_data["correct_answer"] = 1
                    if event.key == pygame.K_F3: form_data["correct_answer"] = 2
                    if event.key == pygame.K_F4: form_data["correct_answer"] = 3


    pygame.display.flip()

pygame.quit()
sys.exit()