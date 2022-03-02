import sys, pygame

from src.utils import get_font
from src.menus.buttons import Button

class Settings:

    def __init__(self):
        super().__init__()

    def run(self, MainMenu, screen):
        while True:
            option_mous_pos = pygame.mouse.get_pos()
            screen.fill("white")
            option_txt = get_font(50).render("This is the OPTIONS screen.", True, "Black")
            option_rect = option_txt.get_rect(center=((self.x / 2), 260))
            screen.blit(option_txt, option_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
