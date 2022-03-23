import random
import numpy as np
import matplotlib.pyplot as plt

import minimize

def f(X):
    """ Quadratic test function """ 
    x, y = X
    return x*x + y*y


def g(X, parameters=(1, 100)):
    """ Rosenbrock test function """
    x, y = X
    a, b = parameters
    return (a - x)**2 + b * (y - x * x)**2

fnc = g
path = minimize.minimize(fnc, initial_condition=(2 * random.random() - 1, 2 * random.random() - 1))

print("Position of the minimum:", path[-1])
print(f"Minimum value of function {fnc.__name__}:", fnc(path[-1]))

# Several trajectories from random position into the minimum
for i in range(10):
    path = minimize.minimize(fnc, initial_condition=(2 * random.random() - 1, 2 * random.random() - 1))
    plt.plot(path[:,0], path[:,1])

plt.show()