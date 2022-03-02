from dataclasses import dataclass
import pygame, pytmx, pyscroll

from src.map import Portal
from src.entities import Npc


@dataclass
class World:
    name: str
    walls: list[pygame.Rect]
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap
    portals: list[Portal]
    npcs: list[Npc]