# This is a sprite in pygame - something that will move 
import pygame

from . import globals

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x_pos = 0, y_pos = 0):
        super().__init__() # Will initialize all the things from the super class

        
        self.image = pygame.Surface([globals.WIDTH_UNIT, globals.PADDLE_HEIGHT])
        self.image.fill(globals.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

# 8 sprites
class QuantumPaddles:
    def __init__(self, x_pos=0):
        # Stores all of the quantum paddles
        self.paddles = []
        # Loop through for each of the number of basis states 2^number of qubits
        for i in range(2**globals.NUM_QUBITS):
            # adds each new paddle to the list
            self.paddles.append(Paddle(x_pos, i*globals.PADDLE_HEIGHT))