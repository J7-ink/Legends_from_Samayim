import pygame
from settings import *
from tile import Tile
from hero import Hero
from support import import_csv_layout, import_folder
from random import choice
from debug import *
from weapon import Weapon
from ui import UI
from enemy import Enemy
from particles import AnimationPlayer
from random import randint
from skills import SkillPlayer
from upgrade import Upgrade


class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        self.game_paused = False

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # attack sprites
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        # sprite setup
        self.map_make()

        # user interface
        self.ui = UI()
        self.upgrade = Upgrade(self.player)

        # particles
        self.animation_player = AnimationPlayer()
        self.skill_player = SkillPlayer(self.animation_player)

    def map_make(self):
        layouts = {
            'boundary': import_csv_layout('../level_map/game_map1_border.csv'),
            'object': import_csv_layout('../level_map/game_map1_trees.csv'),
            'grass': import_csv_layout('../level_map/game_map1_grass.csv'),
            'entities': import_csv_layout('../level_map/game_map1_enemy.csv')
        }

        graphics = {
            'grass': import_folder('../level_map/grass'),
            'object': import_folder('../level_map/trees')
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
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites, self.attackable_sprites],
                                 'grass', random_grass_image)

                        # if style == 'object':
                        #    surf = graphics['object'][int(col)]
                        #    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)

                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')

                        if style == 'entities':
                            if col == '394':
                                self.player = Hero(
                                    (x, y),
                                    [self.visible_sprites],
                                    self.obstacle_sprites,
                                    self.create_attack,
                                    self.destroy_attack,
                                    self.create_magic)
                            else:
                                if col == '5':
                                    enemy_name = 'slime'
                                elif col == '6':
                                    enemy_name = 'knight'
                                elif col == '9':
                                    enemy_name = 'mino'
                                elif col == '8':
                                    enemy_name = 'kex'
                                else:
                                    enemy_name = 'slime'

                                Enemy(
                                    enemy_name,
                                    (x, y),
                                    [self.visible_sprites, self.attackable_sprites],
                                    self.obstacle_sprites,
                                    self.damage_hero,
                                    self.trigger_death_particles,
                                    self.add_exp)

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites, self.attack_sprites])
        # hero = , groups =

    def create_magic(self, style, strength, cost):
        if style == 'minimal_heal':
            self.skill_player.minimal_heal(self.player, strength, cost, [self.visible_sprites])

        if style == 'single_arc':
            self.skill_player.single_arc(self.player, cost, [self.visible_sprites, self.attack_sprites])
        if style == 'dual_arc':
            self.skill_player.dual_arc(self.player, cost, [self.visible_sprites, self.attack_sprites])

        # print(style)
        # print(strength)
        # print(cost)

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def hero_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(sprite=attack_sprite,
                                                                group=self.attackable_sprites, dokill=False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type == 'grass':
                            # the next two lines will get the position the struck grass.
                            pos = target_sprite.rect.center
                            offset_pos = pygame.math.Vector2(0, 70)
                            # this line will make multiple leaves appear, when grass is cut.
                            for leaf in range(randint(3, 6)):
                                # this line will make the particles for grass.
                                self.animation_player.create_grass_particles(pos - offset_pos, [self.visible_sprites])
                            target_sprite.kill()
                        else:
                            target_sprite.get_damage(self.player, attack_sprite.sprite_type)

    def damage_hero(self, amount, attack_type):
        if self.player.vunerable_to_attack:
            self.player.health -= amount
            self.player.vunerable_to_attack = False
            self.player.hurt_time = pygame.time.get_ticks()
            # spawn particles
            self.animation_player.create_particles(attack_type, self.player.rect.center, [self.visible_sprites])

    def trigger_death_particles(self, pos, particle_type):
        """makes a particle effect for when you defeat an enemy, or when you yourself are defeated"""
        self.animation_player.create_particles(particle_type, pos, self.visible_sprites)

    def add_exp(self, amount):
        self.player.exp += amount

    def toggle_menu(self):
        self.game_paused = not self.game_paused

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.ui.display(self.player)

        if self.game_paused:
            # display the upgrade, and settings menu
            self.upgrade.display()

        else:
            # play game
            self.visible_sprites.update()
            self.visible_sprites.enemy_update(self.player)
            self.hero_attack_logic()
            # Update and draw the game.





        # debug(self.player.status)


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

    def enemy_update(self, hero):
        """
        This function allows the enemies to move without making the previous functions to complicated and unusable.
        """
        enemy_sprites = [sprite for sprite in self.sprites() if
                         hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(hero)
        enemy_movement_direction = []
