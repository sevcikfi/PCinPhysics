import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt

#rndGen = rnd.Generator

def basicHistogram(data: np.ndarray, min_value=None, max_value=None, num_bins=100, normalize=False):

    if min_value is None:
        min_value = min(data)
    if max_value is None:
        max_value = max(data)

    bin_width = (max_value - min_value ) / num_bins
    histogram = np.zeros(num_bins)

    for d in data:
        if min_value <= d < max_value:
            index = int((d - min_value) / bin_width)
            histogram[index] += 1

    bins = np.linspace(min_value, max_value, num_bins, endpoint=False)
    mid_points = bins + 0.5 * bin_width

    if normalize:
        histogram /= bin_width * len(data)
    
    return mid_points, histogram




if __name__ == "__main__":
    #data = np.random.uniform(1, 6, 1000)
    #data1 = np.random.uniform(1, 6, 1000)
    N = 100000
    m = 12
    data = np.zeros(N)
    for _ in range(m):
        data += np.random.random(N)
    
    bins, vals = basicHistogram(data)
    plt.plot(bins, vals)
    plt.plot(bins-(m/2), vals)
    #Gaus
    #plt.plot()
    plt.ylim(0)
    plt.show()