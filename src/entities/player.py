import pygame

from src.animations.anim_new import AnimateNew
from src.entities import Entity


class Player(Entity):

    def __init__(self):
        super().__init__("player", 0, 0)
        self.hp_anim = AnimateNew("hearts")
        self.reg = 0
        self.hp = 100
        self.mp = 100

    def get_hp(self): return self.hp

    def regen_mp(self):
        self.reg += self.speed * 5
        if self.reg >= 100:
            self.reg = 0
            if self.mp < 100:
                self.mp += 1

    def dammage(self, amount): self.hp -= amount

    def heal(self, amount):
        if ((self.mp - amount) > 0) & ((self.hp + amount) < 101):
            self.hp += amount
            self.mp -= amount

    def update_hp(self, screen):
        hp_color = (255, 0, 0)
        hp_back_color = (0, 0, 0)
        screen_x = screen.get_width() / 40
        screen_y = screen.get_height() / 30

        #             [x, y, width, height]
        hp_position = [screen_x, screen_y, self.hp, 10]
        hp_back_position = [screen_x, screen_y, 100, 10]
        pygame.draw.rect(screen, hp_back_color, hp_back_position)
        pygame.draw.rect(screen, hp_color, hp_position)

    def update_mp(self, screen):
        mp_color = (0, 0, 230)
        mp_back_color = (0, 0, 0)
        screen_x = screen.get_width() / 40
        screen_y = screen.get_height() / 30

        mp_position = [screen_x, screen_y * 1.5, self.mp, 10]
        mp_back_position = [screen_x, screen_y * 1.5, 100, 10]
        pygame.draw.rect(screen, mp_back_color, mp_back_position)
        pygame.draw.rect(screen, mp_color, mp_position)

    def update_bar(self, screen):
        self.regen_mp()
        self.update_hp(screen)
        self.update_mp(screen)
        self.hp_anim.change_anim_svg()

