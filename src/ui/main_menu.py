import pygame
import sys


class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()

        # Couleurs du design
        self.WHITE = (255, 255, 255)
        self.YELLOW = (253, 224, 71)
        self.BTN_GREEN = (16, 185, 129)
        self.BTN_BLUE = (59, 130, 246)
        self.BTN_PINK = (168, 85, 247)
        self.BTN_EXIT = (40, 40, 40)

        #Chargement des polices
        self.font_title = pygame.font.SysFont('Arial', 50,bold=True)
        self.font_subtitle = pygame.font.SysFont('Arial', 30)
        self.font_btn = pygame.font.SysFont('Arial', 35,bold=True)

        #Chargement du fond
        try:
            self.bg = pygame.transform.scale(self.bg,(self.width,self.height))
        except:
            self.bg = None

    def draw_button(self,text,y_pos,color,mouse_pos):
        width,height = 500,80
        x_pos = (self.width - width) // 2
        rect = pygame.Rect(x_pos,y_pos,width,height)

        # Aide IA pour le hovered
        is_hovered = rect.collidepoint(mouse_pos)
        draw_rect = rect.inflate(20,10) if is_hovered else rect
        draw_color = tuple(min(c + 20, 255) for c in color) if is_hovered else color

        # Dessin de l'ombre et du bouton
        pygame.draw.rect(self.screen, (0, 0, 0, 100), draw_rect.move(4, 4), border_radius=15)
        pygame.draw.rect(self.screen, draw_color, draw_rect, border_radius=15)
        pygame.draw.rect(self.screen, self.WHITE, draw_rect, width=3, border_radius=15)

        # Texte
        text_surf = self.font_btn.render(text, True, self.WHITE)
        text_rect = text_surf.get_rect(center=draw_rect.center)
        self.screen.blit(text_surf, text_rect)

        return rect
    def run (self):
        """Boucle d'affichage du menu"""
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()

            if self.bg:
                self.screen.blit(self.bg, (0, 0))
            else:
                self.screen.fill((30,0,50))


            title_surf = self.font_title.render("QUIZ ÉDUCATIF ", True, self.WHITE)
            self.screen.blit(title_surf, (self.width // 2 - title_surf.get_width() // 2, 100))

            subtitle_surf = self.font_subtitle.render("⚡ Testez vos connaissances ⚡", True, self.YELLOW)
            self.screen.blit(subtitle_surf, (self.width // 2 - subtitle_surf.get_width() // 2, 200))

            btn_play = self.draw_button("JOUER MAINTENANT",300, self.BTN_GREEN, mouse_pos)
            btn_stats = self.draw_button("SCORES & STATS",400,self.BTN_BLUE, mouse_pos)
            btn_add = self.draw_button("AJOUTER QUESTIONS",500,self.BTN_PINK, mouse_pos)
            btn_exit = self.draw_button("QUITTER",620,self.BTN_EXIT, mouse_pos)

            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if btn_play.collidepoint(event.pos):
                        print("Action: Lancer Jeu")
                        return "GAME"
                    if btn_stats.collidepoint(event.pos):
                        print("Action: Voir Stats")
                    if btn_add.collidepoint(event.pos):
                        print("Action: Ajouter Question")
                    if btn_exit.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()