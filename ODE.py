import numpy as np
import matplotlib.pyplot as plt


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

def runge_kutta_4(model, y, t, dt):
    """ Fourth-order Runge-Kutta algoritm"""
    k1 = model(y, t)
    k2 = model(y + 0.5 * k1 * dt, t + 0.5 * dt)
    k3 = model(y + 0.5 * k2 * dt, t + 0.5 * dt)
    k4 = model(y + k3 * dt, t + dt)
    
    y1 = y + (k1 + 2 * k2 + 2 * k3 + k4) * dt / 6
    t1 = t + dt
    
    return y1, t1

def ode_solve(model, initial_conditions, integrator=runge_kutta_4, dt=0.1, maxt=10):
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
    ti = 0.0

    y = [yi]
    t = [ti]

    while ti < maxt:
        yi1, ti1 = integrator(model, yi, ti, dt)

        y.append(yi1)
        t.append(ti1)

        yi = yi1
        ti = ti1

    return np.array(y), np.array(t)

if __name__ == "__main__":  
    y0 = 0
    v0 = 1
    dt = 0.1
    maxt = 100

    def model(y, t):
        x, v = y
        return np.array([v, -x])


    y1, t = ode_solve(model, [y0, v0],euler_2, dt, maxt)
    y2, t  = ode_solve(model, [y0, v0], dt=dt, maxt=maxt)
    y = np.sin(t)

    plt.plot(t, y2[:, 0], label = f"sinus Euler1 with step = {dt}")
    plt.plot(t, y1[:, 0], label = f"sinus Euler2 with step = {dt}") 
    plt.plot(t, y, label = f"Vanila sinus") 

    plt.xlabel("time t")
    plt.ylabel("distance y")
    plt.legend()
    plt.show()