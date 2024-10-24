import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Pygame init 
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Objects instanciation and groups set-up
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    dt = 0
    running = True
    
    # Game loop
    while running:
        # Event Listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Updating objects
        for obj in updatable:
            obj.update(dt)
            
        for asteroid in asteroids:
            if asteroid.iscolliding(player):
                print("Game Over!")
                sys.exit()
            
        # Screen black fill
        screen.fill((0,0,0))
        
        # Drawing objects
        for obj in drawable:
            obj.draw(screen)
        
        # Updating display
        pygame.display.flip()
        
        # Limiting FPS to 60
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()