import pygame
from settings import *

class Upgrade:
    """
    This class makes a menu with a selection index that can allow you to influence your stats
    """
    def __init__(self, hero):

        # general setup
        self.display_serface = pygame.display.get_surface()
        self.hero = hero
        self.attribute_number = len(hero.stats)
        self.attribute_names = list(hero.stats.keys())
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # selection system
        self.selection_index = 0
        self.selection_time = None
        self.can_move = True

    def input(self):
        keys = pygame.key.get_pressed()

        if self.can_move:
            if keys[pygame.K_RIGHT] and self.selection_index < self.attribute_number -1:
                self.selection_index += 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            elif keys[pygame.K_LEFT] and self.selection_index >= 1:
                self.selection_index -= 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()

            if keys[pygame.K_SPACE]:
                # this will be my select button
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                print(self.selection_index)

    def selection_cooldown(self):
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 300:
                self.can_move = True

    def display(self):
        self.input()
        self.selection_cooldown()
