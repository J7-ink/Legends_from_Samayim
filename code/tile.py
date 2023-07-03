import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        # self.image = pygame.image.load('../image/tree3.png').convert_alpha()
        if sprite_type == 'object':
            # do an offset for objects larger than 64*64.
            self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - TILESIZE))
        else:
            # no offset required
            self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
        # the inflate method takes a rectangle and changes the size.

