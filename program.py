import numpy as np
import matplotlib.pyplot as plt

import minimize
import functions

# (b - a) * random() + a from interval [a, b)

fnc = functions.h
path = minimize.minimize_adaptive(fnc, dimension=4, initial_condition=(0.1 * np.random.rand(4)))

print("Position of the minimum:", path[-1])
print(f"Minimum value of function {fnc.__name__}:", fnc(path[-1]))

#Gets stuck at generating D=7 sphere    
#fnc = functions.Rosenbrock_function
#path = minimize.minimize_adaptive(fnc, dimension=7, initial_condition=(10 * np.random.rand(7) - 5))

print("Position of the minimum:", path[-1])
print(f"Minimum value of function {fnc.__name__}:", fnc(path[-1]))

# Several trajectories from random position into the minimum
for i in range(10):
    path = minimize.minimize_adaptive(fnc, dimension=4, initial_condition=(0.1 * np.random.rand(4)))
#    plt.plot(path[:,0], path[:,1])
#    
#plt.show()