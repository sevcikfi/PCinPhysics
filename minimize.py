import random
import numpy as np

def random_direction_2d():
    """ Generates a random direction in the 2D plane """
    phi = random.uniform(0, 2 * np.pi)
    return np.array([np.cos(phi), np.sin(phi)])

def minimize(function, step_size=0.01, initial_condition=(0, 0), max_failed_steps=100):
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
        new_position = position + step_size * random_direction_2d()
        newf = function(new_position)

        if newf < f:
            position = new_position
            f = newf

            path.append(position)

            failed_steps = 0

        else:
            failed_steps += 1        # Rejected step

        num_steps += 1

    print(f"Minimum = {position}, function value = {f}, steps = {num_steps}")

    return np.array(path)

