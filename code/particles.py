import pygame
from support import import_folder
from random import choice


class AnimationPlayer:
    def __init__(self):
        self.frames = {
            # magic/skills
            # unneeded 'flame': import_folder('../particles/flame/frames'),
            'aura': import_folder('../particles/aura'),
            'heal': import_folder('../particles/heal/frames'),
            'arc': import_folder('../particles/arc/up_arc'),
            'down_arc': import_folder('../particles/arc/down_arc'),
            'right_arc': import_folder('../particles/arc/right_arc'),
            'left_arc': import_folder('../particles/arc/left_arc'),
            'dual_arc': import_folder('../image/skill/dual_arc'),
            'minor_heal': import_folder('../image/skill/heal/frames'),


            # attacks
            'claw': import_folder('../particles/claw'),
            'slash': import_folder('../particles/slash'),
            'sparkle': import_folder('../particles/sparkle'),
            'leaf_attack': import_folder('../particles/leaf_attack'),
            'thunder': import_folder('../particles/thunder'),
            'smack': import_folder('../particles/thunder'),

            # monster deaths
            'slime': import_folder('../particles/smoke_orange'),
            'squid': import_folder('../particles/smoke_orange'),
            'raccoon': import_folder('../particles/raccoon'),
            'spirit': import_folder('../particles/nova)'),
            'bamboo': import_folder('../particles/bamboo'),

            # leafs
            'leaf': (
                import_folder('../particles/leaf1'),
                import_folder('../particles/leaf2'),
                import_folder('../particles/leaf3'),
                import_folder('../particles/leaf4'),
                import_folder('../particles/leaf5'),
                import_folder('../particles/leaf6'),
                self.reflect_images(import_folder('../particles/leaf1')),
                self.reflect_images(import_folder('../particles/leaf2')),
                self.reflect_images(import_folder('../particles/leaf3')),
                self.reflect_images(import_folder('../particles/leaf4')),
                self.reflect_images(import_folder('../particles/leaf5')),
                self.reflect_images(import_folder('../particles/leaf6'))
            )
        }

    def reflect_images(self, frames):
        # this reflects images to make more veritably
        new_frames = []

        for frame in frames:
            flipped_frame = pygame.transform.flip(frame, True, False)
            new_frames.append(flipped_frame)
        return new_frames

    def create_grass_particles(self, pos, groups):
        """
        This creates the grass particles
        """
        animation_frames = choice(self.frames['leaf'])
        ParticleEffect(pos, animation_frames, groups)

    def create_particles(self, animation_type, pos, groups):
        """
        this function creates the attack animation frames.
        """
        animation_frames = self.frames[animation_type]
        ParticleEffect(pos, animation_frames, groups)


class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'skill'
        self.frame_index = 0
        self.animation_speed = 0.23
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        # this increases the frame index and if it is still inside the list it picks one image from the list.
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
            # if it goes beyond the list the sprite is destroyed. so this animation only needs to be run once.
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        # this calls the particle affect.
        self.animate()
