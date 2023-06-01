import numpy as np


def random_search(initial_w, num_iterations):
    best_point = None
    best_value = float('-inf')
    w = initial_w.copy()

    for _ in range(num_iterations):
        # x = np.random.uniform(-10, 10)  # Losowy wybór x z przedziału [-10, 10]
        # y = np.random.uniform(-10, 10)  # Losowy wybór y z przedziału [-10, 10]

        value = f(w)  # Obliczenie wartości funkcji dla punktu (x, y)
        w_prime = w + np.random.randn(2)
        value_prime = f(w_prime)
        delta_value = value_prime - value

        if delta_value < 0:
            w = w_prime

    return w


def f(w):
    return 4*w[0]**2 - 4*w[0]*w[1] + 2*w[1]**2


# Przykładowe użycie
num_iterations = 1000
initial_w = np.array([2.0, 3.0])
best_point = random_search(initial_w, num_iterations)

print("Optymalny punkt (x, y):", best_point)
