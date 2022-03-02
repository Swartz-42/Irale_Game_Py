import pygame


class Control:

    def __init__(self):
        super().__init__()


    def move(self, entity):
        self.update()

        if self.up_right:
            entity.move_up()
            entity.move_right()
        elif self.up_left:
            entity.move_up()
            entity.move_left()
        elif self.down_right:
            entity.move_down()
            entity.move_right()
        elif self.down_left:
            entity.move_down()
            entity.move_left()
        elif self.up:
            entity.move_up()
        elif self.down:
            entity.move_down()
        elif self.right:
            entity.move_right()
        elif self.left:
            entity.move_left()
        elif self.esc:
            return False
        return True

    def update(self):
        self.up = pygame.key.get_pressed()[pygame.K_z]
        self.down = pygame.key.get_pressed()[pygame.K_s]
        self.right = pygame.key.get_pressed()[pygame.K_d]
        self.left = pygame.key.get_pressed()[pygame.K_q]
        self.up_right = self.up & self.right
        self.up_left = self.up & self.left
        self.down_right = self.down & self.right
        self.down_left = self.down & self.left
        self.esc = pygame.key.get_pressed()[pygame.K_ESCAPE]
