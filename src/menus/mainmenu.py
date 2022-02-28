import pygame

from src.menus.buttons import PlayButton, SettingButton, QuitButton
from src.menus import Settings
from src.utils import get_font
from src.core import Game
from src.utils.freequit import freeExit


class MainMenu:
    def __init__(self):
        self.img_bg = pygame.image.load("assets/menu/Background.png")
        self.display_menu = True
        self.game = Game()
        self.y = self.game.screen.get_height()
        self.x = self.game.screen.get_width()

    def disp(self):
        play_btn = PlayButton(self.game.screen, (self.x / 2 - self.y / 4, 200, 370, 109), self.game.run)
        setting_btn = SettingButton(self.game.screen, (self.x / 2 - self.y / 4, 350, 370, 109), None)
        quit_btn = QuitButton(self.game.screen, (self.x / 2 - self.y / 4, 500, 370, 109), freeExit)
        list_bnt = [play_btn, setting_btn, quit_btn]

        while self.display_menu:
            self.game.screen.blit(self.img_bg, (0, 0))
            menu_text = get_font(100).render("Irale", True, "#b68f40")
            menu_rect = menu_text.get_rect(center=((self.x / 2), (self.y / 5)))
            self.game.screen.blit(menu_text, menu_rect)
            for button in list_bnt:
                button.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    freeExit()
                if setting_btn.click(event):
                    Settings.run(self, MainMenu(), self.game.screen)
                for button in list_bnt:
                    if button.click(event):
                        if button.func is not None:
                            button.func()
                    button.hover(event)
            pygame.display.flip()
