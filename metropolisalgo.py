from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt

from functions import metropolF


def random_direction_2d():
    """ Generates a random direction in the 2D plane """
    phi = np.random.uniform(0, 2 * np.pi)
    return np.array([np.cos(phi), np.sin(phi)])

def gainDecide(f, newf, T):
    C = np.exp(- (newf - f)/ T)
    k = np.random.rand()
    return k < C

def metropolis(function, step_size=0.01, initial_condition=(0, 0), max_failed_steps=10, max_step=25000, temperature=0.01):
    """ Simple minimization method using random walk.

    Arguments:
    function -- function to minimize
    max_failed_steps -- number of steps to stop the calculation
    """

    position = np.array(initial_condition)
    f = function(position)

    path = [position]

    failed_steps = 0                    # Number of consecutive steps in which we haven't moved (criterion to stop the minimization) 
    num_steps = 0                       # Total number of steps

    while failed_steps < max_failed_steps:
        if max_step < num_steps:
            break
        new_position = position + step_size * random_direction_2d()
        newf = function(new_position)

        if newf < f:
            position = new_position
            f = newf
            path.append(position)
            failed_steps = 0

        else:
            if gainDecide(f, newf, temperature):
                position = new_position
                f = newf
                path.append(position)
                failed_steps = 0
            else:
                failed_steps += 1        # Rejected step

        num_steps += 1

    print(f"Minimum = {position}, function value = {f}, steps = {num_steps}")

    return np.array(path)

def minimaize_and_plot(fnc, box_size=1.5, num_contours=100, **kwargs):
    path = metropolis(fnc, initial_condition=(1,1), **kwargs)
    print("Position of the minimum:", path[-1])
    print(f"Minimum value of function {fnc.__name__}: {fnc(path[-1])}")
    #print(f"Minimum value of function {fnc.__name__}: {fnc(path[-1])} with {steps} steps")


    x = y = np.linspace(-box_size, box_size, 100)
    X, Y = np.meshgrid(x,y)
    Z = fnc([X, Y])

    plt.contourf(X, Y, Z, num_contours, cmap=cm.hot)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.colorbar(label=f"{fnc.__name__} (x,y)")
    plt.plot(path[:,0], path[:,1])
    plt.show()



if __name__ == "__main__":
    fnc = metropolF
    minimaize_and_plot(fnc)
    #for i in range(1):
    #    path = metropolis(fnc, initial_condition=(2 * np.random.random() - 1, 2 * np.random.random() - 1))
    #    plt.plot(path[:,0], path[:,1])
    #plt.show()
