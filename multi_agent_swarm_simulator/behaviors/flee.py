import pygame
def flee(boid, predators):
    steering = pygame.Vector2(0, 0)
    for predator in predators:
        distance = boid.position.distance_to(predator.position)
        if distance < 50:  # Flee radius
            diff = boid.position - predator.position
            diff /= distance
            steering += diff
    return steering
