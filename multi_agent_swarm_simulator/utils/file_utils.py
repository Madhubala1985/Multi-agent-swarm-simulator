import csv

def export_simulation_data(boids, file_name="simulation_data.csv"):
    """Exports the current simulation state to a CSV file."""
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Boid_ID", "X_Position", "Y_Position", "X_Velocity", "Y_Velocity"])
        for i, boid in enumerate(boids):
            writer.writerow([i, boid.position.x, boid.position.y, boid.velocity.x, boid.velocity.y])
