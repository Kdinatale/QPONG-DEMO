import pygame

from assets.circuit_grid import CircuitGrid
from assets import globals, ui, paddle

pygame.init()
screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption('QPong')
clock = pygame.time.Clock()

def main():
    #initialize the game
    circuit_grid = CircuitGrid(5, globals.FIELD_HEIGHT)
    classical_paddle = paddle.Paddle()
    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(classical_paddle)

    exit = False
    while not exit:
        # update game 


        # When you click the x on the pygame window the while loop will end
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN: # pygame.KEYDOWN is triggered anytime a key is pressed down
                circuit_grid.handle_input(event.key) # passes key to the circuit grid

            

        # update game section - happens every frame can be handling some inputs or character moving

        # draw game section 
        circuit_grid.draw(screen)
        ui.draw_statevector_grid(screen)
        moving_sprites.draw(screen)
        pygame.display.flip()

        # Set the framerate - 60 frame per second game.
        clock.tick(60)

if __name__ == '__main__':
    main()