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
#w, t = ODE.ode_solve(lorenz, (1,1,1), dt=0.01, maxt=100)
t = np.arange(0,100,0.01)
w = odeint(lorenz, [1,1,1], t)

plt.figure()
plt.plot(w[:,0], w[:,2])
plt.xlabel("x")
plt.ylabel("z")
plt.title("Lorenz attractor")
plt.show()

# Thanks Samuel J. for this part of the code (plots a 3D interactive graph)
try:                                                                                            
    import plotly.express as px                                                                 
    
    fig = px.line_3d(x=w[:,0], y=w[:,1], z=w[:,2])
    fig.show()
except:
    print("Missing Plotly module.")  