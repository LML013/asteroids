import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    fps = 60

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    

    #Primary Game Loop
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        pygame.Surface.fill(screen, (0,0,0))

        updatable.update(dt)

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        

        #at the end
        dt = clock.tick(fps)/1000


if __name__ == "__main__":
    main()