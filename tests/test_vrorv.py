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
print ("gammat is", gammat)
e = math.exp(gammat) #base e
y = (2 * gammat)
print ("y is", y)
e2 = math.exp(y)
print ("second e2 is", e2)
z = (1) - (e2)
print ("z is", z)
x = math.sqrt(z)
kB = 1.38064852 ** (-23)
#zeta = np.random.randn()
zeta = 3
T = 300 
vtthreefourths = (e * vtonefourth) + (z * (math.sqrt(kB*T/m)) * zeta) #third Langevin integrator

print ("Vt 3/4 is", vtthreefourths)
print ("first expression is", e)
print ("second e2 is", e2)
print ("z is", z)
print ("final part is", math.sqrt(kB*T/m))


x1 = xthalf + (deltat / 2) * (vtthreefourths) #fourth Langevin integrator

print ("x1 is", x1)


fofxt1 = 2

v1 = vtthreefourths + ((deltat / 2) * (1 / m) * fofxt1) #fifth Langevin integrator

print ("v1 is", v1)
