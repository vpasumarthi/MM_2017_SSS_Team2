#!/usr/bin/env python

"""
These are the Langevin integrators
"""

import numpy as np

vt = 1 #initial velocity
deltat = 4 #timestep
m = 2 #mass
fofxt = np.array([1, 1, 1]) #force

vtonefourth = vt + ((deltat / 2) * (1 / m) * fofxt);

print ("Vt 1/4 is", vtonefourth)
