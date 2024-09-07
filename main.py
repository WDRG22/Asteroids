import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    shots = pygame.sprite.Group()

    # Set gameobject containers to defined groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
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

        # Check for collisions
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()

        # Limit framerate to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
