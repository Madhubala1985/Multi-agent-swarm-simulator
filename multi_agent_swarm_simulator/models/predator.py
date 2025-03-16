import pygame
import random

class Predator:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.uniform(-2, 2), random.uniform(-2, 2))

    def update(self, width, height):
        self.position += self.velocity

        # Wrap around edges
        if self.position.x > width: self.position.x = 0
        if self.position.x < 0: self.position.x = width
        if self.position.y > height: self.position.y = 0
        if self.position.y < 0: self.position.y = height

    @staticmethod
    def random(width, height):
        return Predator(random.randint(0, width), random.randint(0, height))
