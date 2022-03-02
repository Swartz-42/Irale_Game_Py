import pygame

# definir classe animation
class AnimateSprite(pygame.sprite.Sprite):

    # init création entité
    def __init__(self, name, nb_sprite, nb_face):
        super().__init__()
        self.sprite = pygame.image.load(f'assets/character/{name}.svg').convert_alpha()
        self.nb_sprite = nb_sprite
        self.nb_face = nb_face
        self.width_sprite = (self.sprite.get_width() / self.nb_sprite)
        self.height_sprite = (self.sprite.get_height() / self.nb_face)
        self.animation_index = 0
        self.clock = 0
        self.speed = 2
        self.animation = False

        self.images = {
            'down': self.get_line_svgs(0),
            'right': self.get_line_svgs(1),
            'left': self.get_line_svgs(2),
            'up': self.get_line_svgs(3)
        }

    def start_animation(self):
        self.animation = True

    def change_animation(self, name):
        self.image = self.images[name][self.animation_index]
        self.image.set_colorkey(0, 0)
        self.clock += self.speed * 8

        if self.clock >= 100:

            self.animation_index += 1
            if self.animation_index >= len(self.images[name]):
                self.animation_index = 0
            self.clock = 0

    # boucle sur toute les image d'une ligne
    def get_line_svgs(self, line):
        images = []

        for i in range(0, self.nb_sprite):
            x = self.width_sprite * i
            images.append(self.get_svg(x, line))
        return images

    # recup une image
    def get_svg(self, x, line):
        # création du calque
        image = pygame.Surface([self.width_sprite, self.height_sprite])
        # copie svg / colle sur le calque: (position en x, position en y du cadre, taille en x, taille en y du cadre)
        image.blit(self.sprite, (5, 5), (x, (self.height_sprite * line), self.width_sprite, self.height_sprite))
        # resize image en 30*30
        image = pygame.transform.scale(image, (30, 30))
        # renvoie l'image d'un sprite
        return image
