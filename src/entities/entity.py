import pygame

from src.animations import AnimateSprite


class Entity(AnimateSprite):

    def __init__(self, name, nb_sprite, nb_face):
        super().__init__(name, nb_sprite, nb_face)
        self.image = self.get_svg(0, 1)
        self.image.set_colorkey(0, 0)
        self.rect = self.image.get_rect()
        self.position = [0, 0]
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()

    def save_location(self): self.old_position = self.position.copy()

    def move_up(self):
        self.change_animation("up")
        self.position[1] -= self.speed

    def move_down(self):
        self.change_animation("down")
        self.position[1] += self.speed

    def move_right(self):
        self.change_animation("right")
        self.position[0] += self.speed

    def move_left(self):
        self.change_animation("left")
        self.position[0] -= self.speed

    def move_up_right(self):
        self.change_animation("right")
        self.position[1] -= self.speed
        self.position[0] += self.speed

    def move_up_left(self):
        self.change_animation("left")
        self.position[1] -= self.speed
        self.position[0] -= self.speed

    def move_down_right(self):
        self.change_animation("right")
        self.position[1] += self.speed
        self.position[0] += self.speed

    def move_down_left(self):
        self.change_animation("left")
        self.position[1] += self.speed
        self.position[0] -= self.speed

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom
