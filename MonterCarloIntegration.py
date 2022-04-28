import numpy as np



def func1(x): #0 to 2pi
    return np.exp(-x) * np.sin(x)

def func2(x): #0 to sqrt(10pi)
    return np.sin(x**2) / np.sqrt(1 + x**4)

def funcH(x, y, v, w): 
    return np.sin( np.sqrt(np.log(x + y + v + w + 2)))

def hyper_square_for_funcH():    
    x, y , v , w = np.random.rand(4)
    if (x - 0.5)**2 + (y - 0.5)**2 + (v - 0.5)**2 + (w - 0.5)**2 <= 0.25:
        return x, y, v, w
    return None

def integration_Nd(function=None, min_value=None, max_value=None, num_values=10000, dist_space_func=None):
    hits = 0
    sum = 0

    for _ in range(num_values):
        x, y , v , w = np.random.rand(4)
        if (x - 0.5)**2 + (y - 0.5)**2 + (v - 0.5)**2 + (w - 0.5)**2 <= 0.25:
            hits += 1
            sum += np.sin(np.sqrt(np.log(x + y + v + w + 2)))
        #if dist_space_func():
        #    hits += 1
        #    sum = funcH
            
    volume = hits / num_values
    intergral = sum / hits * volume

    return intergral



def integration(function=None, min_value=None, max_value=None, num_values=10000):

    if function is None:
        print("specify function!")
        return
    
    data = np.random.uniform(min_value, max_value, num_values)
    integral = (max_value - min_value) * np.average(function(data))
    return integral

if __name__ == "__main__":
    i = integration(func1, min_value=0, max_value=2*np.pi, num_values=1000000)
    print(i)

    i = integration(func2, min_value=0, max_value=np.sqrt(10*np.pi), num_values=1000000)
    print(i)
