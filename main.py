import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame, clock, screen, dt variable for frame delta 
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    # Create groups for game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Set gameobject containers to defined groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    # Create player 
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        # Window close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update and draw objects
        for obj in updatable:
            obj.update(dt)

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # Limit framerate to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
