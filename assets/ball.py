# Ball is also a sprite

import pygame

from . import globals

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([globals.WIDTH_UNIT, globals.WIDTH_UNIT])
        self.image.fill(globals.WHITE)
        self.rect = self.image.get_rect()
        # Initialize to some number
        self.velocity = [1,2]
    
    # How ball will update itself based on the interactions in the game
    def update(self):
        # Every frame you add the velocity 
        # Uses first component of the velocity vector to represent the x position
        self.rect.x += self.velocity[0]

        self.rect.y += self.velocity[1]

        # 0 is top
        # FIELD_HEIGHT is bottom edge
    
        if self.rect.y < 0 or self.rect.y > globals.FIELD_HEIGHT - globals.WIDTH_UNIT:
            # Reverse the direction
            self.velocity[1] = -self.velocity[1]