__author__ = 'Jan'
import math
import pylab
from matplotlib import mlab

tmin = -20.0
tmax = 20.0

dt = 0.01
tlist = mlab.frange (tmin, tmax, dt)

pylab.ion()

for n in range (250):
    xlist = [math.sin(t + n/24.0) for t in tlist]
    ylist = [math.cos (t*2.0) for t in tlist]
    pylab.clf()
    pylab.plot (xlist, ylist)
    pylab.draw()
    pylab.pause(0.001)


pylab.close()