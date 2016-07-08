#!/usr/bin/python3
# Backup Fall Height Calculator
# O. Ross, J. Postler, 2016

import numpy as np
from scipy.optimize import fsolve

# define variables
lgap = np.float32(50) # L_gap
height = np.float32(40) # h
backuplooplength = np.float32(2) # d_t
backuploopsag = np.float32(0.5) # s_t
sag = np.float32(4) # S
leash = np.float32(1) # L_l

# calculate number of backup loops spread across the entire line. 
nloops = np.floor(lgap/backuplooplength)

# np.cosh(backuplooplength/(2*a))=(backuploopsag+a)/a
# this equation is fulfilled for a=radius in the center of the catenary.
# needed to determine the length of the catenary
def catenary(a):
    return np.cosh(backuplooplength/(2*a))-(backuploopsag+a)/a

# solve the catenary function from above to determine radius of backup loops.
# use backuploopsag as a starting point for the radius (has to be in the same region)
radius = fsolve(catenary, backuploopsag)

# total backup length is amount of loops times the length of each loop.
backuplength = nloops*2*radius*np.sinh(backuplooplength/(2*radius))

# calculate falling height (h1) and whether we hit the ground (h1 < h?).
fallheight = np.sqrt(backuplength**2-lgap**2)/2 + leash
print('The slackliner falls %f m below the anchor points.' % fallheight)
print('This is %f m above the ground' % (height - fallheight))


