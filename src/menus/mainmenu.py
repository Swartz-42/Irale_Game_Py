import sys
import pygame

from src.utils.button import Button
from src.core.game import Game


def get_font(size):
    return pygame.font.Font("assets/menu/font.ttf", size)


class MainMenu:
    def __init__(self):
        self.img_bg = pygame.image.load("assets/menu/Background.png")
        self.display_menu = True
        self.game = Game()
        self.y = self.game.screen.get_height()
        self.x = self.game.screen.get_width()

    def options(self):
        while True:
            option_mous_pos = pygame.mouse.get_pos()

            self.game.screen.fill("white")

            option_txt = get_font(50).render("This is the OPTIONS screen.", True, "Black")
            option_rect = option_txt.get_rect(center=((self.x/2), 260))
            self.game.screen.blit(option_txt, option_rect)

            option_back = Button(image=None, pos=((self.x/2), 460),
                                 text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

            option_back.changeColor(option_mous_pos)
            option_back.update(self.game.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if option_back.checkForInput(option_mous_pos):
                        self.disp()

            pygame.display.update()

    def disp(self):
        while self.display_menu:
            self.game.screen.blit(self.img_bg, (0, 0))
            mouse_pos = pygame.mouse.get_pos()
            menu_text = get_font(100).render("Irale", True, "#b68f40")
            menu_rect = menu_text.get_rect(center=((self.x/2), (self.y/5)))
            play_btn = Button(image=pygame.image.load("assets/menu/Play Rect.png"), pos=((self.x/2), (self.y/5)*2),
                              text_input="PLAY", font=get_font(75), base_color="#00ff00", hovering_color="White")
            opts_btn = Button(image=pygame.image.load("assets/menu/Options Rect.png"), pos=((self.x/2), (self.y/5)*3),
                                 text_input="OPTIONS", font=get_font(75), base_color="#0000ff",
                                 hovering_color="White")
            quit_btn = Button(image=pygame.image.load("assets/menu/Quit Rect.png"), pos=((self.x/2), (self.y/5)*4),
                              text_input="QUIT", font=get_font(75), base_color="#ff0000", hovering_color="White")
            self.game.screen.blit(menu_text, menu_rect)

            for button in [play_btn, opts_btn, quit_btn]:
                button.changeColor(mouse_pos)
                button.update(self.game.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_btn.checkForInput(mouse_pos):
                        self.game.run()
                    if opts_btn.checkForInput(mouse_pos):
                        self.options()
                    if quit_btn.checkForInput(mouse_pos):
                        pygame.quit()
                        sys.exit()
    
            pygame.display.update()
