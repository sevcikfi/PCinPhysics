from mimetypes import init
from pickle import NONE
import random
import numpy as np


def random_direction_2d():
    """ Generates a random direction in the 2D plane """
    phi = random.uniform(0, 2 * np.pi)
    return np.array([np.cos(phi), np.sin(phi)])

def random_direction(dimension=2):    

    if dimension == 2:
        return random_direction_2d()
    
    #! if the bigger dimension, the longer this takes!
    while True:                                 
        #rand_vector 
        rnd_vector = 2 * np.random.rand(dimension) - 1
        norm = np.linalg.norm(rnd_vector)    #norm
        if norm <= 1:                        #see if it fits in an unit cube
            return rnd_vector / norm


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


def minimize_adaptive(function, dimension=2, init_step=0.1, final_step=1E-6, initial_condition=None, max_failed_steps=100):
    """ Simple minimization method using random walk.

    Arguments:
    function -- function to minimize
    dimension -- number of free variables going into function
    init_condition -- starting point
    max_failed_steps -- number of steps to stop the calculation
    """
    if initial_condition is None:
        initial_condition = np.zeros(dimension)

    position = np.array(initial_condition)
    f = function(position)

    path = [position]

    failed_steps = 0                    # Number of consecutive steps in which we haven't moved (criterion to stop the minimization) 
    num_steps = 0                       # Total number of steps
    step_size = init_step             

    while final_step < step_size:
        new_position = position + step_size * random_direction(dimension)
        newf = function(new_position)

        if newf < f:
            position = new_position
            f = newf

            path.append(position)

            failed_steps = 0

        else:
            failed_steps += 1        # Rejected step

            if failed_steps > max_failed_steps:
                failed_steps = 0
                step_size /= 2.718 #np.e   #divides current step by e, read somewhere it does some nice properties but idk

        num_steps += 1

    print(f"Minimum adaptive step = {position}, function value = {f}, steps = {num_steps}")

    return np.array(path), num_steps
