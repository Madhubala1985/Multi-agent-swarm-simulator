import pygame
import random

class Boid:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.uniform(-2, 2), random.uniform(-2, 2))
        self.acceleration = pygame.Vector2(0, 0)

    def update(self, max_speed, width, height):
        self.velocity += self.acceleration
        if self.velocity.length() > max_speed:
            self.velocity.scale_to_length(max_speed)
        self.position += self.velocity
        self.acceleration *= 0  # Reset acceleration

        # Wrap around edges
        if self.position.x > width: self.position.x = 0
        if self.position.x < 0: self.position.x = width
        if self.position.y > height: self.position.y = 0
        if self.position.y < 0: self.position.y = height

    def apply_force(self, force):
        self.acceleration += force

    @staticmethod
    def random(width, height):
        return Boid(random.randint(0, width), random.randint(0, height))
