from config import CONFIG
from models.agent import Boid
from models.predator import Predator
from models.obstacle import Obstacle
from behaviors.alignment import align
from behaviors.cohesion import cohesion
from behaviors.separation import separation
from behaviors.goal_seeking import move_toward_goal
from behaviors.obstacle_avoidance import avoid_obstacles
from behaviors.flee import flee
from utils.file_utils import export_simulation_data
from visualizations.metrics_plot import plot_metrics, plot_clustering_and_avoidance
import pygame
import matplotlib.pyplot as plt

def calculate_clustering(boids):
    """Calculate the average distance between boids."""
    total_distance = 0
    total_pairs = 0
    for i, boid in enumerate(boids):
        for other in boids[i + 1:]:
            total_distance += boid.position.distance_to(other.position)
            total_pairs += 1
    if total_pairs > 0:
        return total_distance / total_pairs
    return 0

def calculate_avoidance_efficiency(boids, obstacles, avoid_radius):
    """Calculate the efficiency of obstacle avoidance."""
    collisions = 0
    for boid in boids:
        for obstacle in obstacles:
            if boid.position.distance_to(obstacle.position) < (obstacle.radius + avoid_radius):
                collisions += 1
    return 1 - (collisions / (len(boids) * len(obstacles)))

def main():
    # Initialize Pygame
    pygame.init()

    # Initialize boids, predators, and obstacles
    boids = [Boid.random(CONFIG['width'], CONFIG['height']) for _ in range(CONFIG['num_boids'])]
    predators = [Predator.random(CONFIG['width'], CONFIG['height']) for _ in range(CONFIG['num_predators'])]
    obstacles = [Obstacle.random(CONFIG['width'], CONFIG['height']) for _ in range(CONFIG['num_obstacles'])]

    # Initialize metrics
    avg_speeds = []
    distances_to_goal = []
    clustering_metrics = []
    avoidance_metrics = []
    time_steps = []

    # Simulation goal
    goal = pygame.Vector2(CONFIG['width'] - 100, CONFIG['height'] - 100)

    # Pygame rendering setup
    screen = pygame.display.set_mode((CONFIG['width'], CONFIG['height']))
    pygame.display.set_caption("Multi-Agent Swarm Intelligence Simulator")
    clock = pygame.time.Clock()
    running = True
    step = 0

    while running:
        screen.fill((0, 0, 0))  # Clear screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update and draw obstacles
        for obstacle in obstacles:
            obstacle.update(CONFIG['width'], CONFIG['height'])
            pygame.draw.circle(screen, (255, 0, 0), (int(obstacle.position.x), int(obstacle.position.y)), obstacle.radius)

        # Update and draw predators
        for predator in predators:
            predator.update(CONFIG['width'], CONFIG['height'])
            pygame.draw.circle(screen, (0, 255, 0), (int(predator.position.x), int(predator.position.y)), 10)

        # Apply behaviors to boids and update their states
        for boid in boids:
            alignment = align(boid, boids, CONFIG['neighbor_radius'])
            cohesion_force = cohesion(boid, boids, CONFIG['neighbor_radius'])
            separation_force = separation(boid, boids, CONFIG['avoid_radius'])
            goal_force = move_toward_goal(boid, goal)
            obstacle_avoidance = avoid_obstacles(boid, obstacles)
            predator_flee = flee(boid, predators)

            # Combine forces and apply to the boid
            boid.apply_force(alignment * 1.0)
            boid.apply_force(cohesion_force * 1.0)
            boid.apply_force(separation_force * 1.5)
            boid.apply_force(goal_force * 1.0)
            boid.apply_force(obstacle_avoidance * 2.0)
            boid.apply_force(predator_flee * 2.0)

            boid.update(CONFIG['max_speed'], CONFIG['width'], CONFIG['height'])

            # Draw the boid
            pygame.draw.circle(screen, (255, 255, 255), (int(boid.position.x), int(boid.position.y)), 5)

        # Draw the goal
        pygame.draw.circle(screen, (0, 0, 255), (int(goal.x), int(goal.y)), 8)

        # Metrics collection
        avg_speed = sum(boid.velocity.length() for boid in boids) / len(boids)
        avg_distance_to_goal = sum(boid.position.distance_to(goal) for boid in boids) / len(boids)
        avg_clustering = calculate_clustering(boids)
        avoidance_efficiency = calculate_avoidance_efficiency(boids, obstacles, CONFIG['avoid_radius'])

        avg_speeds.append(avg_speed)
        distances_to_goal.append(avg_distance_to_goal)
        clustering_metrics.append(avg_clustering)
        avoidance_metrics.append(avoidance_efficiency)
        time_steps.append(step)

        # Update the simulation step
        step += 1

        # Display the simulation
        pygame.display.flip()
        clock.tick(60)

        # Stop simulation after 500 steps
        if step >= 500:
            running = False

    # Export data and display metrics
    export_simulation_data(boids)
    plot_metrics(avg_speeds, distances_to_goal, time_steps)
    plot_clustering_and_avoidance(time_steps, clustering_metrics, avoidance_metrics)

    pygame.quit()

if __name__ == "__main__":
    main()
