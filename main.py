import pygame
from constants import *
from player import Player

def main():
    # Pygame init and variable instanciation
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    running = True
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Game loop
    while running:
        # Event Listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Screen black fill
        screen.fill((0,0,0))
        
        # Drawing player
        player.update(dt)
        player.draw(screen)
        
        # Updating display
        pygame.display.flip()
        
        # Limiting FPS to 60
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()