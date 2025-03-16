import pygame
def separation(boid, boids, avoid_radius):
    steering = pygame.Vector2(0, 0)
    total = 0
    for other in boids:
        distance = boid.position.distance_to(other.position)
        if other != boid and distance < avoid_radius:
            diff = boid.position - other.position
            diff /= distance  # Normalize and scale
            steering += diff
            total += 1
    if total > 0:
        steering /= total
    return steering
