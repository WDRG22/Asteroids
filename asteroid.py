import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = 100

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    # If asteroid big enough, split into two when shot
    def split(self):
        self.kill()

        # Small asteroid -> just kill
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Create two new smaller asteroids moving in different directions
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_velocity_1 = self.velocity.rotate(random_angle)
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = new_velocity_1 * 1.2

        new_velocity_2 = self.velocity.rotate(-random_angle)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = new_velocity_2 * 1.2
