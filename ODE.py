import numpy as np
import matplotlib.pyplot as plt


def model():
    return

def euler_1(model, y, t, dt):
    """
    ODE solver with Euler method 1.
    """
    y1 = y + model(y, t) * dt
    t1 = t + dt
    return y1, t1

def euler_2(model, y, t, dt):
    """
    ODE solver with Euler method 2.
    """
    k1 = model(y, t)
    k2 = model(y + k1 * dt, t +dt)
    y1 = y + 0.5 * (k1 + k2) * dt
    t1 = t + dt
    return y1, t1

def ode_solve(model, initial_conditions, integrator=euler_1, dt=0.1, maxt=10):
    """
    Numeric solution of a differential equation system
        
    ##params: 
        model: right side of the equation
        ini_conds: initial conditions
        dt: size of one step
        maxt: end time
    returns: array of solution and array of time
    """
    #init
    yi = np.array(initial_conditions)
    ti = 0

    y = [yi]
    t = [ti]

    while ti < maxt:
        yi1, ti1 = integrator(model, yi, ti, dt)

        y.append(yi1)
        t.append(ti1)

        yi = yi1
        ti = ti1

    return np.array(y), np.array(t)