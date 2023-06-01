import numpy as np
import sklearn.neural_network as nn


def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


def isInside(x, y):
    A = area(2, 2, 4, 3, 4, 1)
    A1 = area(x, y, 4, 3, 4, 1)
    A2 = area(2, 2, x, y, 4, 1)
    A3 = area(2, 2, 4, 3, x, y)
    if (A == A1 + A2 + A3):
        return True
    else:
        return False


def generate_data():
    x_tab = []
    y_tab = []
    while len(x_tab) < 50000 and y_tab.count(-1) < 25000 and y_tab.count(1) < 25000:
        x1 = np.random.randint(0, 6)
        x2 = np.random.randint(0, 6)
        x_tab.append([x1, x2])
        if isInside(x1, x2):
            y_tab.append(1)
        else:
            y_tab.append(-1)
    return x_tab, y_tab


model = nn.MLPClassifier(hidden_layer_sizes=(3,), activation='tanh', solver='adam', max_iter=1000000)
x_train, y_train = generate_data()
model.fit(x_train, y_train)

X_test = [[0.5, 0.5], [3, 3], [2, 1], [6, 6], [4, 1], [4, 3], [2, 2]]
y_test = model.predict(X_test)
print(y_test)

weights = model.coefs_
for i, layer_weights in enumerate(weights):
    print(f"Weights of Layer {i + 1}:")
    print(layer_weights)
    print()

biases = model.intercepts_
for i, layer_biases in enumerate(biases):
    print(f"Biases of Layer {i + 1}:")
    print(layer_biases)
    print()