import time
from matplotlib import pyplot as plt
import numpy as np

from multiprocessing import Pool, Process, Value
from multiprocessing.dummy import Process
import MonterCarloIntegration as MCI

def integrate_1D_Pool(proc, n, f, a, b):
    """
    proc - number of processes
    n - number of elements
    f - function
    a - min end
    b - high end
    """
    #Old style
    #pool = Pool(processes=proc) 
    #with construction
    with Pool(processes=proc) as pool:
        args = ((f, a, b, n), ) * proc

        result = pool.starmap(MCI.integration, args)
    
    average = np.average(result)
    return average

def integrate_parallel(result, *args, **kwargs):
    result.value = MCI.integration(*args, **kwargs)

def integrate_1D_Process(p, n, f, a, b):
    processes = []
    results = []

    for _ in range(p):
        result = Value("d", 0)
        process = Process(target=integrate_parallel, args=(result, f, a, b, n))
        process.start()

        processes.append(process)
        results.append(result)

    for process in processes:
        process.join()

    results = [result.value for result in results]
    return np.average(results)

def plot_1D_duration(processes=range(1,20), n=100000000, f=MCI.func1, a=0, b=1):
    durations = []
    for p in (processes):
        start_time = time.time()
        result = integrate_1D_Process(p, n // p, f, a, b)
        #result = integrate_1D_Pool(p, n // p, f, a, b)
        duration = time.time() - start_time
        print(f"I({f.__name__}) = {result} Time in {p} threads: {duration}")
        durations.append(duration)

    plt.plot(processes, durations)
    plt.title("Total compute time")
    plt.xlabel(r"$p$")
    plt.ylabel(r"$T [s]$")
    plt.show()



if __name__ == "__main__":
    #t = integrate_1D_Pool(4, 100000, MCI.func1, 0, 2*np.pi)
    #print(t)
    #t = integrate_1D_Process(4, 10000000, MCI.func1, 0, 2*np.pi)
    #print(t)
    
    plot_1D_duration()