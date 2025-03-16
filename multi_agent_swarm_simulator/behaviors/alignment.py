import pygame
def align(boid, boids, neighbor_radius):
    steering = pygame.Vector2(0, 0)
    total = 0
    for other in boids:
        if other != boid and boid.position.distance_to(other.position) < neighbor_radius:
            steering += other.velocity
            total += 1
    if total > 0:
        steering /= total
        steering.scale_to_length(boid.velocity.length())
        steering -= boid.velocity
    return steering
