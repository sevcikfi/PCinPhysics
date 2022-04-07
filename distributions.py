import numpy as np
import matplotlib.pyplot as plt

from histogram import histogram

import gauss

def plot_histogram(data, title="", distribution_function=None, **kwargs):
    """ Plots data and compares them with theoretic distributionFunction, if specified """
    x, h = histogram(data, **kwargs)

    plt.plot(x, h, label="Histogram")
    plt.title(title)
    plt.xlabel(r"$x$")
    plt.ylabel(r"$\rho$")
    plt.ylim(0)

    if distribution_function is not None:
        plt.plot(x, distribution_function(x), label="Hustota pravděpodobnosti")
        plt.legend()

    plt.show()

def uniform(num_values=100000, num_bins=100):
    """ Histogram of the uniform distribution """
    data = np.random.random(num_values)

    plot_histogram(data, r"Rovnoměrné rozdělení na $\langle0,1\rangle$", num_bins=num_bins, min_value=0, max_value=1, normalize=False)

def sum_m_uniform(m=2, num_values=100000, num_bins=100):
    """ Histogram of the sum of n uniform distributions, compared with the Gaussian distribution """
    data = np.zeros(num_values)

    for _ in range(m):
        data += np.random.random(num_values)

    plot_histogram(data, f"Součet {m} rovnoměrně rozdělených čísel", num_bins=num_bins, min_value=0, max_value=m, normalize=False)