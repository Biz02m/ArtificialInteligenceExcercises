import numpy as np


def gradient_descent(x, y, learning_rate, num_iterations):
    point = np.array([x, y], dtype=np.float64)

    for i in range(num_iterations):
        gradient = np.array([8 * point[0] - 4 * point[1], -4 * point[0] + 4 * point[1]], dtype=np.float64)
        point -= learning_rate**(i+1) * gradient
    return point


# Przykładowe użycie
x_start = 2.0
y_start = 3.0
learning_rate = 0.5
num_iterations = 100

result = gradient_descent(x_start, y_start, learning_rate, num_iterations)
print("Optymalny punkt (x, y):", result)
