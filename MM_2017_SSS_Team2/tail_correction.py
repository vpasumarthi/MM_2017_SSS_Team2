"""
This is correction function to the potential energy. The correction function
is used to compensate the switch off the LJ potential after rcutoff
"""
"""
The function is U*corr = (8*pi*num_particles^2)/(3*volume)*[(1/3)*(1/cutoff)^9-(1/cutoff)^3]
"""
#defined the box length for a cubic box, cutoff = 3*sigma,
#where sigma is the distance where the LJ potential is zero

import numpy as np

#box_length = -10.0
#cutoff = 3.0
#num_particles = 800

def tail_correction(box_length, cutoff, num_particles):
   try:
       isinstance(box_length, float) and isinstance(cutoff, float)
   except:
       raise ValueError('Box length and cutoff must be float')

   if box_length < 0.0 or cutoff < 0.0:
       raise ValueError('Box length and cutoff must be positive')

   volume = box_length**3
   sig_by_cutoff3 = (1 / cutoff)**3
   sig_by_cutoff9 = sig_by_cutoff3**3
   e_correction = sig_by_cutoff9 - 3.0 * sig_by_cutoff3
   e_correction *= 8.0 / 9.0 * np.pi * num_particles**2 / volume
   return e_correction



