import sys, pygame

from src.menus import Settings
from src.utils import Button, get_font
from src.core import Game

class MainMenu:
    def __init__(self):
        self.img_bg = pygame.image.load("assets/menu/Background.png")
        self.display_menu = True
        self.game = Game()
        self.settings = Settings()
        self.y = self.game.screen.get_height()
        self.x = self.game.screen.get_width()

    def disp(self):
        while self.display_menu:
            self.game.screen.blit(self.img_bg, (0, 0))
            mouse_pos = pygame.mouse.get_pos()
            menu_text = get_font(100).render("Irale", True, "#b68f40")
            menu_rect = menu_text.get_rect(center=((self.x/2), (self.y/5)))
            play_btn = Button(image=pygame.image.load("assets/menu/Play Rect.png"), pos=((self.x/2), (self.y/5)*2),
                              text_input="PLAY", font=get_font(75), base_color="#00ff00", hovering_color="White")
            stg_btn = Button(image=pygame.image.load("assets/menu/Options Rect.png"), pos=((self.x/2), (self.y/5)*3),
                                 text_input="OPTIONS", font=get_font(75), base_color="#0000ff",
                                 hovering_color="White")
            quit_btn = Button(image=pygame.image.load("assets/menu/Quit Rect.png"), pos=((self.x/2), (self.y/5)*4),
                              text_input="QUIT", font=get_font(75), base_color="#ff0000", hovering_color="White")
            self.game.screen.blit(menu_text, menu_rect)

            for button in [play_btn, stg_btn, quit_btn]:
                button.changeColor(mouse_pos)
                button.update(self.game.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_btn.checkForInput(mouse_pos):
                        self.game.run()
                    if stg_btn.checkForInput(mouse_pos):
                        Settings.run(self, MainMenu(), self.game.screen)
                    if quit_btn.checkForInput(mouse_pos):
                        pygame.quit()
                        sys.exit()
    
            pygame.display.update()
