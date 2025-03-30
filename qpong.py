import pygame

from assets.circuit_grid import CircuitGrid
from assets import globals

pygame.init()
screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption('QPong')
clock = pygame.time.Clock()

def main():
    #initialize the game
    circuit_grid = CircuitGrid(5, globals.FIELD_HEIGHT)


    exit = False
    while not exit:
        # When you click the x on the pygame window the while loop will end
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        # update game section - happens every frame can be handling some inputs or character moving

        # draw game section 
        circuit_grid.draw(screen)
        pygame.display.flip()

        # Set the framerate - 60 frame per second game.
        clock.tick(60)

if __name__ == '__main__':
    main()