from math import inf
from pprint import pformat
import numpy as np
import matplotlib.pyplot as plt
from pytest import fail
from sqlalchemy import true


#init conds
x0 = 2 * np.cos(2 * np.pi * np.random.rand())
y0 = 2 * np.sin(2 * np.pi * np.random.rand())
#init params 
a = 1
b = 1000
#2D cords
x = [y0]
y = [x0]
results = [inf]
#step
d = 0.1
#number of iter
N = 150

def Fmodel(x, y):
    return x**2 + y**2

def Gmodel(y, x, a, b):
    return (a - x)**2 + b * (y - x**2 )**2

for j in range(N):
    randomNumber = 2 * np.pi * np.random.rand()
    xj = x[j] + d * np.cos(randomNumber)
    yj = y[j] + d * np.sin(randomNumber)
    fi = Gmodel(xj, yj, a, b)

    fail = 0

    while(fi > results[j]):
        if (fail == 25):
            d = d / 5
        
        fail = fail + 1
        randomNumber = 2 * np.pi * np.random.rand()
        xj = x[j] + d * np.cos(randomNumber)
        yj = y[j] + d * np.sin(randomNumber)
        fi = Gmodel(xj, yj, a, b)

    results.append(fi)
    x.append(xj)
    y.append(yj)

print(len(x))

plt.figure()
plt.plot(x, y, label="walk")
plt.title("minimalization")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()