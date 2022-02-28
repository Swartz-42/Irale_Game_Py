import pygame

from src.control import Control
from src.entities import Player
from src.utils import DialogBox
from src.map import MapManager
from src.utils.freequit import freeExit


class Game:

    def __init__(self):

        super().__init__()

        # creer la fenetre du jeu
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Irale - Le jeux video")
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

            self.player.save_location()
            self.running = Control().key_pressed(self.player)
            self.update()
            self.map_manager.draw()
            self.dialog_box.render(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    freeExit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        self.map_manager.check_npc_collisions(self.dialog_box)

            clock.tick(60)

    def update(self):
        self.map_manager.update()
