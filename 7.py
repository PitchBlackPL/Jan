__author__ = 'Jan'

def Vey(k,y):
    s = 0
    for n in range(k):
        s += b**n*np.cos(a**n*np.pi*y)
    return s


import numpy as np
import matplotlib.pyplot as plt
a = 3
b = 0.4

x = np.arange(-10, 10.01, 0.01)
plt.plot(x/10,Vey(500,x/10))
plt.show()

