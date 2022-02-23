import sys
import pygame

from src.utils.get_font import get_font


class Settings:

    def __init__(self):
        super().__init__()

    def options(self):
        while True:

            option_mous_pos = pygame.mouse.get_pos()
            self.game.screen.fill("white")
            option_txt = get_font(50).render("This is the OPTIONS screen.", True, "Black")
            option_rect = option_txt.get_rect(center=((self.x / 2), 260))
            self.game.screen.blit(option_txt, option_rect)
            option_back = Button(image=None, pos=((self.x / 2), 460), text_input="BACK", font=get_font(75),
                                 base_color="Black", hovering_color="Green")
            option_back.changeColor(option_mous_pos)
            option_back.update(self.game.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if option_back.checkForInput(option_mous_pos):
                        disp()

            pygame.display.update()
