import pygame


# definir classe animation
class AnimateNew(pygame.sprite.Sprite):

    # init création entité
    def __init__(self, name):
        super().__init__()
        self.sprite_sheet = pygame.image.load(f'assets/{name}.svg')
        self.animation_index = 0
        self.clock = 0
        self.images = self.get_svgs(4)
        print(self.images)
        self.speed = 2
        self.animation = False

    def start_animation(self):
        self.animation = True

    def change_anim_svg(self):
        self.image = self.images[self.animation_index]
        self.image.set_colorkey(0, 0)
        self.clock += self.speed * 8

        if self.clock >= 100:
            self.animation_index += 1
            if self.animation_index >= len(self.images):
                self.animation_index = 0
            self.clock = 0

    def get_svgs(self, nb_sprite):
        images = []

        for i in range(0, nb_sprite):
            x = i * (self.sprite_sheet.get_width() / nb_sprite)
            image = self.get_svg(x)
            images.append(image)
        return images

    def get_svg(self, x):
        svg = pygame.Surface([x, self.sprite_sheet.get_height()])
        svg.blit(self.sprite_sheet, (0, 0), (x, self.sprite_sheet.get_height(), 32, 32))
        return svg
