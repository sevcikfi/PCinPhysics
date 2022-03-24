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

def h(X):
    """ h function"""
    s, t, u, v = X
    sum2 = s**2 + t**2 + u**2 + v**2
    if sum2 > 2:
        return float("inf")

    k2 = (s**2 + t**2) * (2 - sum2) + (s * u - t * v)**2
    k3 = np.sqrt(2 - sum2)
    return (sum2 / 2) - (k2 / 4) + (k3 * s / 4)

def Rosenbrock_function(X: np.ndarray, params=(1, 100)):
    """Rosenbrock function"""
    D = len(X) - 1  #works only if 1d array
    a, b = params
    sum = 0
    for i in range(D - 1):
        sum += (a - X[i]**2 + b*(X[i+1] - X[i]**2 )**2 )

    return sum

def metropolisF(X):
    x, y = X
    return x**4 + - x**2 + x + y**2

def sinus(X):
    x, y = X
    return np.sin(x / 10) * np.sin(y / 10)

if __name__ == "__main__":
    fnc = g
    path = minimize.minimize(fnc, initial_condition=(2 * random.random() - 1, 2 * random.random() - 1))
    
    print("Position of the minimum:", path[-1])
    print(f"Minimum value of function {fnc.__name__}:", fnc(path[-1]))
    
    # Several trajectories from random position into the minimum
    for i in range(10):
        path = minimize.minimize(fnc, initial_condition=(2 * random.random() - 1, 2 * random.random() - 1))
        plt.plot(path[:,0], path[:,1])
    
    plt.show()
