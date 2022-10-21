import pygame
from settings import *


class Piller(pygame.sprite.Sprite):
    def __init__(self, pos, groups, ):
        super().__init__(groups)
        self.image = pygame.image.load('../image/piller.PNG').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, 10)
