#import numpy as np

# init values
y0 = 0 
v0 = 1

#def. array
y = []
y[0] = y0
v = []
v[0] = v0
t = []
t[0] = 0
deltaT = 0.1

#number of iter
N = 100
#main loop
for j in range(100):
    y1 = deltaT * v[j] + y[j]
    v1 = -deltaT * y[j] + v[j]
    t1 = t[j] + deltaT

    y.append(y1)
    v.append(v1)
    t.append(t1)
