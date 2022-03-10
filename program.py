import math
import ODE
import numpy as np
import matplotlib.pyplot as plt

y0 = 0
v0 = 1
dt = 0.1
maxt = 100

def model(y, t):
    x, v = y
    return np.array([v, -x])


y1, t = ODE.ode_solve(model, [y0, v0],ODE.euler_2, dt, maxt)
y2, t  = ODE.ode_solve(model, [y0, v0], dt=dt, maxt=maxt)
y = np.sin(t)

plt.plot(t, y2[:, 0], label = f"sinus Euler1 with step = {dt}")
plt.plot(t, y1[:, 0], label = f"sinus Euler2 with step = {dt}") 
plt.plot(t, y, label = f"Vanila sinus") 

plt.xlabel("time t")
plt.ylabel("distance y")
plt.legend()
plt.show()