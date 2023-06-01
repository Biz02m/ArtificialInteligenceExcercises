import random

swarm_size = 50
max_iterations = 100
max_velocity = 1.0
c1 = 2.0
c2 = 2.0


def init():
    swarm = []
    for _ in range(swarm_size):
        position = [random.uniform(-10, 10), random.uniform(-10, 10)]
        velocity = [random.uniform(-max_velocity, max_velocity),
                    random.uniform(-max_velocity, max_velocity)]
        swarm.append(
            {"position": position, "velocity": velocity, "best_position": position, "best_fitness": float('inf')})
    return swarm


def update_velocity_and_position(particle, global_best_position):
    new_velocity = [particle["velocity"][0] + c1 * random.random() * (
            particle["best_position"][0] - particle["position"][0]) + c2 * random.random() * (
                            global_best_position[0] - particle["position"][0]),
                    particle["velocity"][1] + c1 * random.random() * (
                            particle["best_position"][1] - particle["position"][1]) + c2 * random.random() * (
                            global_best_position[1] - particle["position"][1])]
    new_velocity = [max(-max_velocity, min(max_velocity, new_velocity[0])),
                    max(-max_velocity, min(max_velocity, new_velocity[1]))]  # Ograniczenie prędkości
    new_position = [particle["position"][0] + new_velocity[0], particle["position"][1] + new_velocity[1]]
    particle["velocity"] = new_velocity
    particle["position"] = new_position


# Roj
def swarm_a():
    swarm = init()

    global_best_fitness = float('inf')
    global_best_position = [0, 0]

    for _ in range(max_iterations):
        for particle in swarm:
            update_velocity_and_position(particle, global_best_position)

            particle_fitness = f(particle["position"][0], particle["position"][1])
            if particle_fitness < particle["best_fitness"]:
                particle["best_fitness"] = particle_fitness
                particle["best_position"] = particle["position"]

            if particle_fitness < global_best_fitness:
                global_best_fitness = particle_fitness
                global_best_position = particle["position"]

    return global_best_position


def f(x, y):
    return 4*x**2 - 4*x*y + 2*y**2


best_solution = swarm_a()
minimum_value = f(best_solution[0], best_solution[1])

print("Best Solution: (", best_solution[0], ", ", best_solution[1], ")")
print("Min:", minimum_value)