#!/usr/bin/env python

"""
These are the Langevin integrators
"""

import numpy as np
import math as math
vt = 1 #initial velocity
deltat = 4 #timestep
m = 2 #mass
fofxt = np.array([1, 1, 1]) #force

vtonefourth = vt + ((deltat / 2) * (1 / m) * fofxt); #first Langevin integrator

print ("Vt 1/4 is", vtonefourth)


xt = 1 #initial position

xthalf = xt + ((deltat / 2) * vtonefourth); #second Langevin integrator

print ("Xt 1/2 is", xthalf)


gammat = (gamma * deltat)
gamma = -1 / (500 * deltat)
e = math.log(gamma[base]) #base e
e2 = math.log((-2*gamma)[base])
x = math.sqrt((1-e2))
kB = 1.38064852 ** (-23)
zeta = np.random.randn()

vtthreefourths = (e * vtonefourth) + (e2 * (math.sqrt(kB*T/m)) * zeta) #third Langevin integrator



