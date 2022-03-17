import numpy as np
import matplotlib.pyplot as plt
import ODE

from scipy.integrate import odeint

sigma = 10
rho = 28
beta = 8/3

def lorenz(w, t):
    """ Lorenz model of atmospheric convection """
    x, y, z = w

    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z

    return np.array([dx, dy, dz])

#own ODE solver
w, t = ODE.ode_solve(lorenz, (1,1,1),integrator=ODE.runge_kutta_4, dt=0.01, maxt=100)
to = np.arange(0, 100, 0.01)
wo = odeint(lorenz, [1,1,1], t)

plt.figure()
plt.plot(w[:,0], w[:,2], label="Runge-Kutta")
plt.plot(wo[:,0], wo[:,2], label="odeint from Scipy")
plt.xlabel("x")
plt.ylabel("z")
plt.title("Lorenz attractor")
plt.legend()
plt.show()