import pygame
import random

class Obstacle:
    def __init__(self, x, y, radius):
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

    def update(self, width, height):
        self.position += self.velocity

        # Bounce off edges
        if self.position.x < 0 or self.position.x > width:
            self.velocity.x *= -1
        if self.position.y < 0 or self.position.y > height:
            self.velocity.y *= -1

    @staticmethod
    def random(width, height):
        return Obstacle(random.randint(0, width), random.randint(0, height), random.randint(20, 50))
