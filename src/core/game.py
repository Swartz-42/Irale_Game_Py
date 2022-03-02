import pygame

from src.entities import Player
from src.utils import DialogBox
from src.map import MapManager
from src.utils import freeExit
from .control import Control


class Game:

    def __init__(self):

        super().__init__()

        # creer la fenetre du jeu
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Irale - Le jeux video")

        self.player = Player()
        self.control = Control()
        self.map_manager = MapManager(self.screen, self.player)
        self.dialog_box = DialogBox()
        self.running = True

    def update(self):
        self.player.save_location()
        self.running = self.control.move(self.player)
        self.map_manager.update()

    def run(self):
        clock = pygame.time.Clock()
        # boucle du jeu
        while self.running:

            #move de toute les entiters
            self.update()

            #mise a jour affichage
            self.map_manager.draw()
            self.dialog_box.render(self.screen)
            pygame.display.flip()

            #check event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    freeExit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        self.map_manager.check_npc_collisions(self.dialog_box)

            clock.tick(60)
