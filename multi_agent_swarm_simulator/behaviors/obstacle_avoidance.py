import pygame
def avoid_obstacles(boid, obstacles):
    steering = pygame.Vector2(0, 0)
    for obstacle in obstacles:
        distance = boid.position.distance_to(obstacle.position)
        if distance < obstacle.radius + 20:  # Avoid radius
            diff = boid.position - obstacle.position
            diff /= distance  # Normalize and scale
            steering += diff
    return steering
