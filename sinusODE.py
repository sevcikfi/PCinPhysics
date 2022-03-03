#import numpy as np
import matplotlib.pyplot as plt

# init values
y0 = 0 
v0 = 1
t0 = 0
#time change and max time
deltaT = 0.1
maxT = 100
#def. array
y = [y0]
v = [v0]
t = [t0]


#number of iter
N = int(maxT / deltaT)
print(N)
#main loop
for j in range(N):
    y1 = deltaT * v[j] + y[j]
    v1 = -deltaT * y[j] + v[j]
    t1 = t[j] + deltaT

    y.append(y1)
    v.append(v1)
    t.append(t1)

print(y)
