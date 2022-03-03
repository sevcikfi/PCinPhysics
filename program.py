import ODE
import numpy as np
import matplotlib.pyplot as plt

y0 = 0
v0 = 1
dt = 0.1
maxt = 10

def model(y, t):
    x, v = y
    return np.array([v, -x])

y, t = ODE.ode_solve(model, [y0, v0], dt, maxt)

plt.plot(t, y[:, 0])
plt.show()