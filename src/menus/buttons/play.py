from src.menus.buttons import Button
import pygame

class PlayButton(Button):
    def __init__(
        self, 
        surface: pygame.Surface, 
        rect: tuple,
        func: any,
        text: str = "Play", 
        background_color: tuple = (0, 0, 0, 150), 
        text_color: tuple = (0, 255, 0),
        hovering_color: tuple = (255, 255, 255),
        text_size: int = 75):
        super().__init__(surface, rect, func, text, background_color, text_color, hovering_color, text_size)

    