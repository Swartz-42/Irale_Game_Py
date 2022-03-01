import pygame

from src.control import Control
from src.entities import Player
from src.menus.buttons import QuitButton
from src.utils import DialogBox, get_font
from src.map import MapManager
from src.utils import freeExit


class Game:

    def __init__(self):
        super().__init__()

        # creer la fenetre du jeu
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Irale - Le jeux video")
        self.game_over = GameOver(self.screen)
        self.running = True

        # generer le joueur
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)
        self.dialog_box = DialogBox()

    def run(self):
        clock = pygame.time.Clock()
        self.running = True
        # boucle du jeu
        while self.running:
            self.update()
            if self.player.hp <= 0:
                self.running = False
                self.game_over.disp(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    freeExit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        self.player.dammage(10)
                        self.map_manager.check_npc_collisions(self.dialog_box)
                    if event.key == pygame.K_a:
                        self.player.heal(10)

            clock.tick(60)

    def update(self):
        self.player.save_location()
        self.running = Control().key_move(self.player)
        self.map_manager.update()
        self.map_manager.draw()
        self.dialog_box.render(self.screen)
        self.player.update_bar(self.screen)
        pygame.display.flip()


class GameOver:
    def __init__(self, screen):
        self.img_bg = pygame.image.load("assets/menu/Background.png")
        self.display = True
        self.y = screen.get_height()
        self.x = screen.get_width()

    def disp(self, screen):
        quit_btn = QuitButton(screen, (self.x / 2 - self.y / 4, 500, 370, 109), freeExit)
        list_bnt = [quit_btn]

        while self.display:
            screen.blit(self.img_bg, (0, 0))
            menu_text = get_font(100).render("GameOver", True, "#b68f40")
            menu_rect = menu_text.get_rect(center=((self.x / 2), (self.y / 5)))
            screen.blit(menu_text, menu_rect)

            for button in list_bnt:
                button.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    freeExit()
                for button in list_bnt:
                    if button.click(event):
                        if button.func is not None:
                            button.func()
                    button.hover(event)
            pygame.display.flip()
