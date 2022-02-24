import pygame, pytmx, pyscroll

from src.map import Portal, World
from src.entities import Npc

class MapManager:
    def __init__(self, screen, player):
        self.maps = dict()  # "house" -> Map("house", walls, group)
        self.current_map = "world"
        self.screen = screen
        self.player = player

        self.register_map("world", portals=[
            Portal(from_world="world", origin_point="enter_house", to_world="house", tp_point="spawn_house"),
            Portal(from_world="world", origin_point="enter_dungeon", to_world="dungeon", tp_point="spawn_dungeon")
        ], npcs=[
            Npc("paul", nb_points=4, dialog=["Hey jeune aventurier !", "Tu connais Brohr Rolnarson Drakung ?", "C'est ma PUTE !!!"])
        ])
        self.register_map("house", portals=[
            Portal(from_world="house", origin_point="exit_house", to_world="world", tp_point="spawn_exit_house")
        ])
        self.register_map("dungeon", portals=[
            Portal(from_world="dungeon", origin_point="exit_dungeon", to_world="world", tp_point="spawn_exit_player")
        ])

        self.tp_player("player")
        self.tp_npcs()

    def check_collision(self):

        # portals
        for portal in self.get_map().portals:
            if portal.from_world == self.current_map:
                point = self.get_object(portal.origin_point)
                rect = pygame.Rect(point.x, point.y, point.width, point.height)

                if self.player.feet.colliderect(rect):
                    copy_portal = portal
                    self.current_map = portal.to_world
                    self.tp_player(copy_portal.tp_point)

        #collision mur
        for sprite in self.get_group().sprites():

            if type(sprite) is Npc:
                if sprite.feet.colliderect(self.player.rect):
                    sprite.speed = 0
                else:
                    sprite.speed = 1

            if sprite.feet.collidelist(self.get_walls()) > -1:
                sprite.move_back()

    def register_map(self, name, portals=[], npcs=[]):

        # charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame(f'map/{name}.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # definir les collisions
        walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de calques
        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        group.add(self.player)

        # recup npc sur la map
        for npc in npcs:
            group.add(npc)

        self.maps[name] = World(name, walls, group, tmx_data, portals, npcs)

    def tp_player(self, name):
        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()

    def get_map(self): return self.maps[self.current_map]

    def get_group(self): return self.get_map().group

    def get_walls(self): return self.get_map().walls

    def get_object(self, name): return self.get_map().tmx_data.get_object_by_name(name)

    def tp_npcs(self):
        for map in self.maps:
            map_data = self.maps[map]
            npcs = map_data.npcs
            for npc in npcs:
                npc.load_points(map_data.tmx_data)
                npc.teleport_spawn()

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def update(self):
        self.get_group().update()
        self.check_collision()

        for npc in self.get_map().npcs:
            npc.move()

    def check_npc_collisions(self, dialog_box):
        for sprite in self.get_group().sprites():
            if sprite.feet.colliderect(self.player.rect) and type(sprite) is Npc:
                dialog_box.execute(sprite.dialog)