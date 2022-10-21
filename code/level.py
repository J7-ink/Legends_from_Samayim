import pygame
from settings import *
from tile import Tile
from hero import Hero
# from piller1 import Piller
# from wall import Wall
from support import import_csv_layout, import_folder
from random import choice


class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        # sprite setup
        self.map_make()

    def map_make(self):
        layouts = {
            'boundary': import_csv_layout('../level_map/game_map1_border.csv'),
            'object': import_csv_layout('../level_map/game_map1_trees.csv'),
            'grass': import_csv_layout('../level_map/game_map1_grass.csv')
        }

        graphics = {
            'grass': import_folder('../level_map/grass'),
            'trees': import_folder('../z3/level_map/trees')
        }
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE

                        if style == 'grass':
                            # need to get grass in the game.
                            random_grass_image = choice(graphics['grass'])
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'grass', random_grass_image)

                    #    if style == 'object':
                    #        surf = graphics['trees'][int(col)]
                    #        Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)

                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')
        #         if col == 'x':
        #            Tile(pos=(x, y), groups=[self.visible_sprites, self.obstacle_sprites])

        #         if col == 'p1':
        #            Piller(pos=(x, y), groups=[self.visible_sprites, self.obstacle_sprites])

        #         if col == 'w':
        #             Wall(pos=(x, y), groups=[self.visible_sprites, self.obstacle_sprites])

        #         if col == 'p':
        #             self.player = Hero((x, y), [self.visible_sprites], self.obstacle_sprites)

        self.player = Hero((3970, 9950), [self.visible_sprites], self.obstacle_sprites)

    def run(self):
        # Update and draw the game.
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


class YSortCameraGroup(pygame.sprite.Group):
    """this spread group is going to function as a camera.
    it also sorts the sprites by there y coordinate in order ot give some overlap"""
    def __init__(self):
        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # Creating the floor
        self.floor_surf = pygame.image.load('../level_map/level1map.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, hero):

        # getting the offset
        self.offset.x = hero.rect.centerx - self.half_width
        self.offset.y = hero.rect.centery - self.half_height

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_position)
