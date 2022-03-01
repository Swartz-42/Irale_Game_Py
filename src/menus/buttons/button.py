from cgitb import text
import pygame

import src.utils as utils


class Button:
    def __init__(self, surface: pygame.Surface, rect: tuple, func: any, text: str, background_color: tuple,
                 text_color: tuple, hovering_color: tuple, text_size: int = 75):
        self.surface = surface
        self.pos = rect[:2]
        if len(rect) != 2:
            self.width = rect[2]
            self.height = rect[3]
        else:
            self.width = -1
            self.height = -1
        self.text = text
        self.background_color = background_color
        self.text_color = text_color
        self.hovering_color = hovering_color
        self.func = func

        self.update_text(self.text, text_size)

        self.old_mouse_state = False
        self.old_hover_state = False

    def update(self):
        self.background = utils.draw_rect_alpha(self.surface, self.background_color, (
            self.pos[0],
            self.pos[1],
            self.width,
            self.height))
        self.surface.blit(self.text_render, (
            self.background.x + ((self.width / 2) - self.text_boundaries.width / 2),
            self.background.y + ((self.height / 2) - self.text_boundaries.height / 2),
            self.text_boundaries.width,
            self.text_boundaries.height))

    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.background.collidepoint(event.pos) and pygame.mouse.get_pressed()[0]:
                self.background_color = utils.increase_alpha_on_color(self.background_color, 50)
                return True
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.old_mouse_state == pygame.MOUSEBUTTONDOWN and event.button == utils.MOUSELEFT and self.background.collidepoint(
                    event.pos):
                self.background_color = utils.reduce_alpha_on_color(self.background_color, 50)
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
            self.old_mouse_state = event.type
        return False

    def hover(self, event):
        if event.type != pygame.MOUSEMOTION:
            return False

        if self.background.collidepoint(event.pos):
            if not self.old_hover_state:
                self.text_render = self.font.render(self.text, True, self.hovering_color)
                self.old_hover_state = True
                return True
        elif self.old_hover_state:
            self.text_render = self.font.render(self.text, True, self.text_color)
            self.old_hover_state = False
        return False

    def update_text(self, text: str, text_size: int = 75):
        self.font = utils.get_font(text_size)
        self.text = text
        self.text_size = text_size
        self.text_render = self.font.render(self.text, True, self.text_color)
        self.text_boundaries = self.text_render.get_rect()
        if self.width == -1:
            self.width = self.text_boundaries.width
        if self.height == -1:
            self.height = self.text_boundaries.height

    def scale(self, value: int):
        self.update_text(self.text, self.text_size + value)
        self.width = self.text_boundaries.width
        self.height = self.text_boundaries.height
