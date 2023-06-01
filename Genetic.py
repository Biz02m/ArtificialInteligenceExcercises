import random
import numpy as np

# Parametry algorytmu genetycznego
population_size = 90
chromosome_length = 4
selection_size = 3
mutation_rate = 0.3
max_generations = 100


# Inicjalizacja populacji początkowej
def init_population():
    population = np.random.uniform(-10, 10, size=(population_size, chromosome_length))
    return population


# Selekcja
def selection(population, fitness_values):
    tournament_indices = np.random.choice(len(population), size=selection_size, replace=False)
    tournament_fitness = fitness_values[tournament_indices]
    selected_parents_indices = tournament_indices[np.argsort(tournament_fitness)[:2]]
    selected_parents = population[selected_parents_indices]
    return selected_parents


# Ocena przystosowania dla populacji
def evaluate_population(population):
    fitness_values = np.sum(population ** 2, axis=1)
    return fitness_values


# Mutacja
def mutate(chromosome):
    for i in range(chromosome_length):
        if random.random() < mutation_rate:
            chromosome[i] += random.uniform(-1, 1)
            chromosome[i] = np.clip(chromosome[i], -10, 10)  # Ograniczenie wartości do przedziału [-10, 10]
    return chromosome


# Krzyżowanie dwupunktowe
def crossover(parent1, parent2):
    chromosome_len = len(parent1)

    # Wybierz dwa różne punkty podziału
    point1 = random.randint(1, chromosome_len - 1)
    point2 = random.randint(1, chromosome_len - 1)

    if point1 > point2:
        point1, point2 = point2, point1

    child1 = np.concatenate((parent1[:point1], parent2[point1:point2], parent1[point2:]))
    child2 = np.concatenate((parent2[:point1], parent1[point1:point2], parent2[point2:]))

    return child1, child2

# Algorytm genetyczny
def Genetic():
    population = init_population()

    for generation in range(max_generations):
        fitness_values = evaluate_population(population)

        # Wybór dwóch rodziców
        parent1, parent2 = selection(population, fitness_values)

        # Krzyżowanie i mutacja
        offspring1, offspring2 = crossover(parent1, parent2)
        offspring1 = mutate(offspring1)
        offspring2 = mutate(offspring2)

        # Zastąpienie dwóch najgorszych osobników potomkami
        worst_indices = np.argsort(fitness_values)[-2:]
        population[worst_indices[0]] = offspring1
        population[worst_indices[1]] = offspring2

    best_index = np.argmin(fitness_values)
    best_solution = population[best_index]
    minimum_value = fitness_values[best_index]

    return best_solution, minimum_value


# Wywołanie algorytmu genetycznego
best_solution, minimum_value = Genetic()

print("Najlepsze rozwiązanie: x =", best_solution[0], "y =", best_solution[1])
print("Wartość minimalna:", minimum_value)