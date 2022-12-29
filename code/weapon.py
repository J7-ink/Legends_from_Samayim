import pygame


class Weapon(pygame.sprite.Sprite):
    def __init__(self, hero, groups):
        super().__init__(groups)
        self.sprite_type = 'weapon'
        direction = hero.status.split('_')[0]
        # print(direction)

        # graphic
        full_path = f'../image/weapon/{hero.weapon}/{direction}.PNG'
        self.image = pygame.image.load(full_path).convert_alpha()

        # placement
        if direction == 'right':
            self.rect = self.image.get_rect(midleft=hero.rect.midright - pygame.math.Vector2(0, 3))
        elif direction == 'left':
            self.rect = self.image.get_rect(midright=hero.rect.midleft - pygame.math.Vector2(0, 3))
        elif direction == 'down':
            self.rect = self.image.get_rect(midtop=hero.rect.midbottom + pygame.math.Vector2(12, 0))
        else:
            self.rect = self.image.get_rect(midbottom=hero.rect.midtop - pygame.math.Vector2(11, 0))
