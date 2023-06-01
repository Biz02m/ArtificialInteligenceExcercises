import random
def f(x):
    return x ** 2

def swarm(num_iterations, own_weight, population_size, global_weight):
    population = []
    velocity = []
    best_position = []
    best_value = float('inf')

    for _ in range(population_size):
        position = random.uniform(-10, 10)
        population.append(position)
        velocity.append(0)

        value = f(position)
        if value < best_value:
            best_position = position
            best_value = value

    for iteration in range(num_iterations):
        for i in range(population_size):
            velocity[i] = (own_weight * velocity[i] +
                           global_weight * random.uniform(0, 1) * (best_position - population[i]))
            population[i] += velocity[i]

            value = f(population[i])
            if value < best_value:
                best_position = population[i]
                best_value = value

    return best_position, best_value


num_iterations = 50
own_weight = 0.5
population_size = 100
global_weight = 0.5

best_position, best_value = swarm(num_iterations, own_weight, population_size, global_weight)

# Wyświetlenie najlepszego rozwiązania
print("Optymalizacja rojem cząsteczek (PSO):")
print("Najlepsza pozycja:", best_position)
print("Najlepsza wartość:", best_value)