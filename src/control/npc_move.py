def move(self):
    current_point = self.current_point
    target_point = self.current_point + 1

    if target_point >= self.nb_points:
        target_point = 0

    current_rect = self.points[current_point]
    target_rect = self.points[target_point]

    if current_rect.y < target_rect.y and abs(current_rect.x - target_rect.x) < 3:
        self.move_down()
    elif current_rect.y > target_rect.y and abs(current_rect.x - target_rect.x) < 3:
        self.move_up()
    elif current_rect.x < target_rect.x and abs(current_rect.y - target_rect.y) < 3:
        self.move_right()
    elif current_rect.x > target_rect.x and abs(current_rect.y - target_rect.y) < 3:
        self.move_left()

    if self.rect.colliderect(target_rect):
        self.current_point = target_point