import pygame
def move_toward_goal(boid, goal):
    desired = goal - boid.position
    if desired.length() > 0:
        desired.scale_to_length(boid.velocity.length())
    steering = desired - boid.velocity
    return steering
