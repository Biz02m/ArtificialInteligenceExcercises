import numpy as np


def random_search(initial_w, num_iterations):
    w = initial_w.copy()

    for _ in range(num_iterations):
        value = f(w)
        w_prime = w + np.random.randn(2)
        value_prime = f(w_prime)
        delta_value = value_prime - value

        if delta_value < 0:
            w = w_prime
    return w


def f(w):
    return 4*w[0]**2 - 4*w[0]*w[1] + 2*w[1]**2


num_iterations = 1000
initial_w = np.array([2.0, 3.0])
best_point = random_search(initial_w, num_iterations)

print("Optymalny punkt (x, y):", best_point)
