import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption('QPong')
clock = pygame.time.Clock()

def main():

    exit = False
    while not exit:
        # When you click the x on the pygame window the while loop will end
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        # Set the framerate - 60 frame per second game.
        clock.tick(60)

if __name__ == '__main__':
    main()