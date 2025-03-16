import pygame

def render_simulation(boids, predators, obstacles):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for boid in boids:
            # Apply behaviors
            boid.update(4, 800, 600)
            pygame.draw.circle(screen, (255, 255, 255), (int(boid.position.x), int(boid.position.y)), 5)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
