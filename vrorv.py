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

gamma = (-1) / (500 * deltat)
gammat = (gamma * deltat)
e = math.exp(gammat) #base e
y = (2 * gammat)
e2 = math.exp(y)
z = (1) - (e2)
x = math.sqrt(z)
kB = 1.38064852 ** (-23)
#zeta = np.random.randn()
zeta = 3
T = 300 
vtthreefourths = (e * vtonefourth) + (z * (math.sqrt(kB*T/m)) * zeta) #third Langevin integrator

print ("Vt 3.4 is", vtthreefourths)
