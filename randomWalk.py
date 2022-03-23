import numpy as np
import matplotlib.pyplot as plt

# import random
# random.randomint() <0,1)
#        .uniform(a ,b) <a,b)


#2D cords
x = [0]
y = [0]
#step
d = 1
#number of iter
N = 120
for j in range(N):
    randomNumber = 2 * np.pi * np.random.rand()
    xj = x[j] + d * np.cos(randomNumber)
    yj = y[j] + d * np.sin(randomNumber)
    
    x.append(xj)
    y.append(yj)

plt.figure()
plt.plot(x, y, label="částice 1.")
plt.title("Brownův pohyb")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()