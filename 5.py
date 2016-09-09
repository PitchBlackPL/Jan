__author__ = 'Jan'
import numpy as np
import matplotlib.pyplot as plt
s = input()
x = np.arange(-10, 10.01, 0.01)
plt.plot(x, eval(s))
plt.show()