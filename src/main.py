import pygame
from ui.main_menu import MainMenu

def main():

    pygame.init()

    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("QUIZ ÉDUCATIF")

    menu = MainMenu(screen)

    menu.run()

if __name__ == "__main__":
    main()