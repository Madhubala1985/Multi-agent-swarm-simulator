import matplotlib.pyplot as plt

def plot_metrics(avg_speeds, distances_to_goal, time_steps):
    """Plots average speed and distance to goal over time."""
    plt.figure(figsize=(12, 6))

    # Average speed
    plt.subplot(1, 2, 1)
    plt.plot(time_steps, avg_speeds, label="Average Speed", color="blue")
    plt.xlabel("Time Steps")
    plt.ylabel("Speed")
    plt.title("Average Speed Over Time")
    plt.legend()

    # Average distance to goal
    plt.subplot(1, 2, 2)
    plt.plot(time_steps, distances_to_goal, label="Distance to Goal", color="orange")
    plt.xlabel("Time Steps")
    plt.ylabel("Distance")
    plt.title("Average Distance to Goal Over Time")
    plt.legend()

    plt.tight_layout()
    plt.show()

def plot_clustering_and_avoidance(time_steps, clustering_metrics, avoidance_metrics):
    """Plots clustering and obstacle avoidance efficiency over time."""
    plt.figure(figsize=(12, 6))

    # Clustering metrics
    plt.subplot(1, 2, 1)
    plt.plot(time_steps, clustering_metrics, label="Average Clustering", color="green")
    plt.xlabel("Time Steps")
    plt.ylabel("Clustering (Avg Distance)")
    plt.title("Clustering Over Time")
    plt.legend()

    # Obstacle avoidance efficiency
    plt.subplot(1, 2, 2)
    plt.plot(time_steps, avoidance_metrics, label="Avoidance Efficiency", color="red")
    plt.xlabel("Time Steps")
    plt.ylabel("Efficiency")
    plt.title("Obstacle Avoidance Efficiency Over Time")
    plt.legend()

    plt.tight_layout()
    plt.show()
