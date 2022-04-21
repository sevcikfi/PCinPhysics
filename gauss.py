import numpy as np
import matplotlib.pyplot as plt
import histogram


def gaussian_distribution(x):
    return 1 / np.sqrt(2 * np.pi) * np.exp(-x**2 / 2)

def generator_hit_and_miss(N=1):
    while True:
        x = 12 * np.random.random() - 6
        y = 0.5 * np.random.random()
        if y < gaussian_distribution(x):
            return x

def generator_clt():
    """central limit theorem"""
    return sum(np.random.random(12)) - 6
    

if __name__ == "__main__":
    N = 100000
    m = 12
    data = np.zeros(N)
    for _ in range(m):
        data += np.random.random(N)
    
    data_clt = [generator_clt() for _ in range(N)]
    data_rnd = [generator_hit_and_miss() for _ in range(N)]

    bins, vals = histogram.basicHistogram(data, normalize=True)
    plt.plot(bins-(m/2), vals)
    #plt.plot(bins-(m/2), vals)
    #Gaus
    #plt.plot()
    plt.ylim(0)
    plt.show()