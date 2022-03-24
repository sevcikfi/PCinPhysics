import numpy as np
import matplotlib.pyplot as plt

import minimize
import functions

# (b - a) * random() + a from interval [a, b)

fnc = functions.h
path, steps = minimize.minimize_adaptive(fnc, dimension=4, initial_condition=(0.1 * np.random.rand(4)))

print("Position of the minimum:", path[-1])
print(f"Minimum value of function {fnc.__name__}: {fnc(path[-1])} with {steps} steps")
#
##Gets stuck at generating D=7 sphere    
#fnc = functions.Rosenbrock_function
#path = minimize.minimize_adaptive(fnc, dimension=7, initial_condition=(10 * np.random.rand(7) - 5))

#print("Position of the minimum:", path[-1])
#print(f"Minimum value of function {fnc.__name__}:", fnc(path[-1]))

#fnc = functions.g
## Several trajectories from random position into the minimum
#for i in range(20):
#    initConds = (10 * np.cos(2 * np.pi * np.random.rand()), 10 * np.cos(2 * np.pi * np.random.rand()))
#    path, num_steps = minimize.minimize_adaptive(fnc, dimension=2, initial_condition=initConds)
#    plt.plot(path[:,0], path[:,1], label=num_steps)
#
#plt.legend()    
#plt.show()