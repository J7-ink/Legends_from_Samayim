import pygame
from settings import *

class SkillPlayer:
    def __init__(self, animation_player):
        self.animation_player = animation_player

    def minimal_heal(self, hero, strength, cost, groups):
        if hero.energy >= cost:
            hero.health += strength
            hero.energy -= cost
            if hero.health >= hero.stats['health']:
                hero.health = hero.stats['health']

    def single_arc(self):
        pass

    def dual_arc(self):
        pass