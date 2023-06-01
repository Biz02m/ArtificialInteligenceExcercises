import numpy as np

def simulated_annealing(initial_w, Tmax, cooling_rate, max_iterations):
    w = initial_w.copy()
    T = Tmax
    k = 1

    def energy_function(w):
        x, y = w
        return 4*x**2 - 4*x*y + 2*y**2

    while k <= max_iterations:
        w_prime = w + np.random.randn(2) * T
        E = energy_function(w)
        E_prime = energy_function(w_prime)
        delta_E = E_prime - E

        if delta_E < 0 or np.random.rand() < np.exp(-delta_E / T):
            w = w_prime

        T *= cooling_rate
        k += 1

    return w

initial_w = np.array([2.0, 3.0])
Tmax = 100.0
cooling_rate = 0.95
max_iterations = 100

result = simulated_annealing(initial_w, Tmax, cooling_rate, max_iterations)
print("Optymalny punkt (x, y):", result)
