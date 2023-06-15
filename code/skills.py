import pygame
from settings import *
from support import import_folder


class SkillPlayer:

    def __init__(self, animation_player):
        self.animation_player = animation_player

    def minimal_heal(self, hero, strength, cost, groups):
        if hero.energy >= cost:
            hero.health += strength
            hero.energy -= cost
            if hero.health >= hero.stats['health']:
                hero.health = hero.stats['health']
            self.animation_player.create_particles('aura', hero.rect.center, groups)
            self.animation_player.create_particles('heal', hero.rect.center, groups)

    def single_arc(self, hero, cost, groups):
        if hero.energy >= cost:
            hero.energy -= cost
            # gets direction for the ability to go
            if hero.status.split('_')[0] == 'right':
                direction = pygame.math.Vector2(1, 0)

            elif hero.status.split('_')[0] == 'left':
                direction = pygame.math.Vector2(-1, 0)

            elif hero.status.split('_')[0] == 'up':
                direction = pygame.math.Vector2(0, -1)

            else:
                direction = pygame.math.Vector2(0, 1)

            for i in range(1, ):
                if direction.x: # horizontal
                    offset_x = (direction.x * 1) * TILESIZE
                    x = hero.rect.centerx + offset_x
                    y = hero.rect.centery

                    if hero.status.split('_')[0] == 'right':
                        self.animation_player.create_particles('right_arc', (x, y), groups)
                    else:
                        self.animation_player.create_particles('left_arc', (x, y), groups)

                else: # vertical
                    offset_y = (direction.y * 1) * TILESIZE
                    x = hero.rect.centerx
                    y = hero.rect.centery + offset_y

                    if hero.status.split('_')[0] == 'up':
                        self.animation_player.create_particles('arc', (x, y), groups)
                    else:
                        self.animation_player.create_particles('down_arc', (x, y), groups)
                    # self.animation_player.create_particles('arc', (x, y), groups)

    def dual_arc(self, hero, cost, groups):
        if hero.energy >= cost:
            hero.energy -= cost
            # gets direction for the ability to go
            if hero.status.split('_')[0] == 'right':
                direction = pygame.math.Vector2(1, 0)

            elif hero.status.split('_')[0] == 'left':
                direction = pygame.math.Vector2(-1, 0)
            elif hero.status.split('_')[0] == 'up':
                direction = pygame.math.Vector2(0, -1)
            else:
                direction = pygame.math.Vector2(0, 1)
            for i in range(1, ):

                if direction.x: # horizontal
                    offset_x = (direction.x * 1) * TILESIZE
                    x = hero.rect.centerx + offset_x
                    y = hero.rect.centery
                    if hero.status.split('_')[0] == 'left':
                        self.animation_player.create_particles('right_arc', (x+64, y), groups)
                        self.animation_player.create_particles('left_arc', (x, y), groups)
                    elif hero.status.split('_')[0] == 'right':
                        self.animation_player.create_particles('right_arc', (x-20, y), groups)
                        self.animation_player.create_particles('left_arc', (x-92, y), groups)

                else:  # vertical
                    offset_y = (direction.y * 1) * TILESIZE
                    x = hero.rect.centerx
                    y = hero.rect.centery + offset_y

                    if hero.status.split('_')[0] == 'up':
                        self.animation_player.create_particles('arc', (x, y+20), groups)
                        self.animation_player.create_particles('down_arc', (x, y+84), groups)
                    elif hero.status.split('_')[0] == 'down':
                        self.animation_player.create_particles('arc', (x, y-84), groups)
                        self.animation_player.create_particles('down_arc', (x, y-20), groups)
