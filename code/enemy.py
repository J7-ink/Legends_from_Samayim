import pygame
from settings import *
from entity import Entity
from support import *

class Enemy(Entity):
    def __init__(self, enemy_name, position, groups):

        # general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'

        # graphics setup
        self.import_graphics(enemy_name)
        self.image = self.animations[self.status][self.frame_index]
        # pygame.Surface((64, 64))
        self.rect = self.image.get_rect(topleft=position)

    def import_graphics(self, name):
        self.animations = {'idle': [], 'move': [], 'attack': []}
        self.status = 'idle'
        main_path = f'../image/enemy/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)
