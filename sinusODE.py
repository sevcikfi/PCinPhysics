import matplotlib.pyplot as plt
import numpy as np

# init values
y0 = 0 
v0 = 1
t0 = 0
#time change and max time
deltaT = 0.1
maxT = 10
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

#print(y)
#plt.scatter(t , y)
plt.plot(t,y, label="sinus")
plt.plot(t, np.sin(t), label="numpy")
plt.show()
plt.xlabel("time t")
plt.ylabel("distance y")