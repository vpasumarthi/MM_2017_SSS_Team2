#!/usr/bin/env python

"""
These are the Langevin integrators
"""

import numpy as np
import math as math
def vrorv(x,v,f):
    vt = 1 #initial velocity
    deltat = 4 #timestep
    #m = 1 #mass
    fofxt = f #np.array([1, 1, 1])  #force

    vtonefourth = vt + ((deltat / 2) * (1 / m) * fofxt); #first Langevin integrator

#    print ("Vt 1/4 is", vtonefourth)


    xt = x # np.array([1, 1, 1]) #initial position

    xthalf = xt + ((deltat / 2) * vtonefourth); #second Langevin integrator

#print ("Xt 1/2 is", xthalf)

    gamma = (-1) / (500 * deltat)
    gammat = (gamma * deltat)
#print ("gammat is", gammat)
    e = math.exp(gammat) #base e
    y = (2 * gammat)
#print ("y is", y)
    e2 = math.exp(y)
#print ("second e2 is", e2)
    z = (1) - (e2)
#print ("z is", z)
    xx = math.sqrt(z)
#kB = 1.38064852 ** (-23)
    zeta3_4 = np.random.randn()
#zeta = 3
    T = 0.9 
    vtthreefourths = (e * vtonefourth) + (z * (math.sqrt(T)) * zeta3_4) #third Langevin integrator

     print ("Vt 3/4 is", vtthreefourths)
     print ("first expression is", e)
     print ("second e2 is", e2)
     print ("z is", z)
     print ("final part is", math.sqrt(kB*T/m))


     x1 = xthalf + (deltat / 2) * (vtthreefourths) #fourth Langevin integrator

     print ("x1 is", x1)


    fofxt1 = np.array([2, 2, 2])

    v1 = vtthreefourths + ((deltat / 2) * (1 / m) * fofxt1) #fifth Langevin integrator

print ("v1 is", v1)
