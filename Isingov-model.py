"""
Implementation of Monte Carlo simulation of Ishingov model
for spin, magnetization and the temperature of the matrix
"""
global J
J=1
global kBoltz
KBoltz=1

import numpy as np
import matplotlib.pyplot as plt

def Initialize_sample(size_N=10):
    """Init array
    """
    return np.random.choice([-1,1], (size_N, size_N))

def Median_magnetization(spin_array:np.ndarray):
    """average magnet"""
    if spin_array is None:
        print("Need array")
        return
  
    return spin_array.sum() / spin_array.size

def Total_energy(spin_array:np.ndarray):
    if spin_array is None:
        print("Need array")
        return
    cumulative = 0
    for m in range(spin_array.shape[1]):
        for n in range(spin_array.shape[0]-1, -1, -1):
            cumulative += spin_array[m,n]*spin_array[m,n-1]
            cumulative += spin_array[m,n]*spin_array[m-1,n]
    return -J * cumulative

def One_step(spin_array:np.ndarray, temp=1):
    energy_before = Total_energy(spin_array)
    energy_after = 0
    for m in range(spin_array.shape[1]):
        for n in range(spin_array.shape[0]):
            #change spin
            spin_array[m,n] = -1 * spin_array[m,n]
            #calc energy
            energy_after = Total_energy(spin_array)
            #check if smaler
            diff = energy_after - energy_before
            if diff < 0:
                energy_before = energy_after
                continue
            ## NEED TO PUT BOLTZMAN STUFF HERE
            rands = np.random.rand()
            if propability(diff, temp) > rands:
                energy_before = energy_after
                continue
            spin_array[m,n] = -1 * spin_array[m,n]

    return spin_array

def propability(diff, temp):
    return np.exp(- diff / (KBoltz*temp))

def Metropolis_algo():
    spin_array = Initialize_sample()
    magnet = Median_magnetization(spin_array)
    print(spin_array.sum())
    print(magnet)
    print(spin_array)
    energy = Total_energy(spin_array)
    print(energy)

    print(Total_energy(One_step(spin_array)))

def Temp_computation(r=50, m=50, temp=1):
    #array gen
    spin_array = Initialize_sample()
    #relaxation
    for i in range(r):
        spin_array = One_step(spin_array, temp)
    #compute energy and magnetization
    Energy = [Total_energy(spin_array)]
    Magnetization = [Median_magnetization(spin_array)]
    for i in range(m):
        spin_array = One_step(spin_array, temp)
        Energy.append(Total_energy(spin_array))
        Magnetization.append(Median_magnetization(spin_array))
    #returns both averages
    return np.average(Energy), np.average(Magnetization)

def Temp_graph(min_temp, max_temp):
    temp_arr = np.linspace(min_temp,max_temp, 100)
    energy = []
    magnet = []
    for temp in temp_arr:
        en, mag = Temp_computation(temp = temp)
        energy.append(en)
        magnet.append(mag)
    
    plt.plot(temp_arr, energy, label = f"Energy")
    plt.scatter(temp_arr, magnet, label = f"Magnetization")
    plt.xlabel("Temperature")
    plt.legend()
    plt.show()

if __name__ == "__main__":
        print("Isingov")
        
        #Metropolis_algo()

        #en, mag = Temp_computation()
        #print(en, mag)
        Temp_graph(0.0001, 5)