import numpy as np


def EmpRisc(w, d, x1, x2):
    yi = 0
    sumo = 0
    for i in range(len(d)):
        yi = w[0]*x1[i] + w[1]*x2[i] + w[2]*x1[i]*x2[i] + w[3]*(x1[i]/x2[i]) + w[4]*x1[i]**2 + w[5]*x2[i]**2
        sumo = sumo + (yi - d[i])**2
    return sumo/len(d)


x1 = np.array([0.2, -0.3, -0.5, -0.1, -1.0, -0.3, 0.1])
x2 = np.array([0.3, 0.4, 3.3, 4.8, 3.2, 7.2, 3.4])
d = np.array([0.8, 0.2, -0.3, 1.2, 1.6, 0.5, -0.2])
A = np.zeros((7, 6))
for i in range(7):
    A[i, :] = [x1[i], x2[i], x1[i]*x2[i], x1[i]/x2[i], x1[i]**2, x2[i]**2]
Atransposed = A.transpose()
w = np.linalg.inv(np.matmul(Atransposed, A))
w = np.matmul(w, Atransposed)
w = np.matmul(w, d)
print(w)

print(EmpRisc(w, d, x1, x2))
