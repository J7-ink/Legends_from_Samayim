import pygame
from settings import *
from entity import Entity
from support import *


class Enemy(Entity):
    def __init__(self, enemy_name, position, groups, obstacle_sprites):

        # general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'

        # graphics setup
        self.import_graphics(enemy_name)
        self.image = self.animations[self.status][self.frame_index]
        # pygame.Surface((64, 64))

        # movement
        self.rect = self.image.get_rect(topleft=position)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites

        # Stats
        self.enemy_name = enemy_name
        enemy_info = enemy_data[self.enemy_name]
        self.health = enemy_info['health']
        self.exp = enemy_info['exp']
        self.speed = enemy_info['speed']
        self.attack_damage = enemy_info['damage']
        self.resistance = enemy_info['resistance']
        self.attack_radius = enemy_info['attack_radius']
        self.notice_radius = enemy_info['notice_radius']
        self.attack_type = enemy_info['attack_type']

        # player interaction
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 450 # this will change when we add it to individual attributes in the enemy dictionary

    def import_graphics(self, name):
        self.animations = {'idle': [], 'move': [], 'attack': []}
        self.status = 'idle'
        main_path = f'../image/enemy/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)

    def get_hero_distance_direction(self, hero):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(hero.rect.center)
        distance = (player_vec - enemy_vec).magnitude()
        # the .magnitude converts a vector into a distance.
        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
            # normally the distance would be by far greater than needed, so we'll have to use '.normalize' on it.
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)

    def get_status(self, hero):
        distance = self.get_hero_distance_direction(hero)[0]

        if distance <= self.attack_radius and self.can_attack:
            if self.status != 'attack':
                self.frame_index = 0
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    def actions(self, hero):
        if self.status == 'attack':
            self.attack_time = pygame.time.get_ticks()
            print("attack")
        elif self.status == 'move':
            self.direction = self.get_hero_distance_direction(hero)[1]
        else:
            self.direction = pygame.Vector2()

    def animate(self):
        """
        We want this to be the same kind of animate as the player. Though there are some minimal changes.
        """
        animation = self.animations[self.status]
        # the above line makes the code more readable
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            if self.status == 'attack':
                self.can_attack = False
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def cooldown(self):
        if not self.can_attack:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

    def get_damage(self, hero, attack_type):
        if attack_type == 'weapon':
            self.health -= hero.get_full_weapon_damage()
        else:
            pass # magic/skill damage

    def check_death(self):
        if self.health <= 0:
            self.kill()

    def update(self):
        self.move(self.speed)
        self.animate()
        self.cooldown()
        self.check_death()

    def enemy_update(self, hero):
        self.get_status(hero)
        self.actions(hero)
