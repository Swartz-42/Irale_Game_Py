from src.entities import Entity
import pygame

class Npc(Entity):

    def __init__(self, name, nb_points, nb_sprite, nb_face, dialog):
        super().__init__(name, nb_sprite, nb_face)
        self.nb_points = nb_points
        self.dialog = dialog
        self.points = []
        self.name = name
        self.speed = 1
        self.current_point = 0

    def move(self):
        current_point = self.current_point
        target_point = self.current_point + 1

        if target_point >= self.nb_points:
            target_point = 0

        current_rect = self.points[current_point]
        target_rect = self.points[target_point]

        self.direction(current_rect, target_rect)

        if self.down:
            self.move_down()
        elif self.up:
            self.move_up()
        elif self.right:
            self.move_right()
        elif self.left:
            self.move_left()
        elif self.up_right:
            self.move_up_right()
        elif self.up_left:
            self.move_up_left()
        elif self.down_right:
            self.move_down_right()
        elif self.down_left:
            self.move_down_left()

        if self.rect.colliderect(target_rect):
            self.current_point = target_point

    def direction(self, current_rect, target_rect):
        self.down = current_rect.y < target_rect.y and abs(current_rect.x - target_rect.x) < 3
        self.up = current_rect.y > target_rect.y and abs(current_rect.x - target_rect.x) < 3
        self.right = current_rect.x < target_rect.x and abs(current_rect.y - target_rect.y) < 3
        self.left = current_rect.x > target_rect.x and abs(current_rect.y - target_rect.y) < 3
        self.up_right = current_rect.y > target_rect.y and current_rect.x < target_rect.x
        self.up_left = current_rect.y > target_rect.y and current_rect.x > target_rect.x
        self.down_right = current_rect.y < target_rect.y and current_rect.x < target_rect.x
        self.down_left = current_rect.y < target_rect.y and current_rect.x > target_rect.x

    def teleport_spawn(self):
        location = self.points[self.current_point]
        self.position[0] = location.x
        self.position[1] = location.y
        self.save_location()

    def load_points(self, tmx_data):
        for num in range(1, self.nb_points+1):
            point = tmx_data.get_object_by_name(f"{self.name}_path{num}")
            rect = pygame.Rect(point.x, point.y, point.width, point.height)
            self.points.append(rect)
