import pygame


class Control:

    def __init__(self):
        super().__init__()
        self.up = pygame.key.get_pressed()[pygame.K_z]
        self.down = pygame.key.get_pressed()[pygame.K_s]
        self.right = pygame.key.get_pressed()[pygame.K_d]
        self.left = pygame.key.get_pressed()[pygame.K_q]
        self.esc = pygame.key.get_pressed()[pygame.K_ESCAPE]
        self.up_right = self.up + self.right
        self.up_left = self.up + self.left
        self.down_right = self.down + self.right
        self.down_left = self.down + self.left

    def key_move(self, player):

        self.update()

        if self.up_right:
            player.move_up()
            player.move_right()
        elif self.up_left:
            player.move_up()
            player.move_left()
        elif self.up:
            player.move_up()
        elif self.down_right:
            player.move_down()
            player.move_right()
        elif self.down_left:
            player.move_down()
            player.move_left()
        elif self.down:
            player.move_down()
        elif self.right:
            player.move_right()
        elif self.left:
            player.move_left()
        elif self.esc:
            return False
        return True

    def update(self):
        self.up = pygame.key.get_pressed()[pygame.K_z]
        self.down = pygame.key.get_pressed()[pygame.K_s]
        self.right = pygame.key.get_pressed()[pygame.K_d]
        self.left = pygame.key.get_pressed()[pygame.K_q]
        self.esc = pygame.key.get_pressed()[pygame.K_ESCAPE]
        self.up_right = self.up & self.right
        self.up_left = self.up & self.left
        self.down_right = self.down & self.right
        self.down_left = self.down & self.left
