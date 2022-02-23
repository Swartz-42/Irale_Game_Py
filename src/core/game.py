import pygame

from src.entities.player import Player
from src.utils.dialog import DialogBox
from src.core.map import MapManager

global running


class Game:

    def __init__(self):

        global running

        # creer la fenetre du jeu
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Irale - Le jeux video")
        running = True

        # generer le joueur
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)
        self.dialog_box = DialogBox()

    # definir control
    def handle_input(self):

        global running
        pressed = pygame.key.get_pressed()
        up = pressed[pygame.K_z]
        down = pressed[pygame.K_s]
        right = pressed[pygame.K_d]
        left = pressed[pygame.K_q]
        esc = pressed[pygame.K_ESCAPE]

        if up & right:
            self.player.move_up()
            self.player.move_right()
        elif up & left:
            self.player.move_up()
            self.player.move_left()
        elif down & right:
            self.player.move_down()
            self.player.move_right()
        elif down & left:
            self.player.move_down()
            self.player.move_left()
        elif down:
            self.player.move_down()
        elif right:
            self.player.move_right()
        elif left:
            self.player.move_left()
        elif up:
            self.player.move_up()
        elif esc:
            running = False

    def update(self):
        self.map_manager.update()

    def run(self):

        global running
        clock = pygame.time.Clock()
        # boucle du jeu

        while running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            self.dialog_box.render(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        self.map_manager.check_npc_collisions(self.dialog_box)

            clock.tick(60)
        self.disp()
