# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:49:30 2019

@author: salam
"""

import numpy as np
import matplotlib.pyplot as plt

Afname = input(str('Name of airfoil:')) 
    
Airfoil = np.loadtxt(Afname+'.dat', skiprows = 1)

xarray = []
yarray = []
xlist = np.append(xarray, Airfoil[:,0])
ylist = np.append(yarray, Airfoil[:,1])

## NORMALIZED THE AIRFOIL=======================================

if xlist[0] != 1.0:
    xlist [0]= 1.0
else:
    None

if xlist [int((len(xlist))/2)] != 0.0:
    xlist [int((len(xlist))/2)] = 0.0
else:
    None

if xlist[-1] != 1.0:
    xlist [-1] = 1.0
else:
    None

a = xlist [0]
b = xlist [int((len(xlist))/2)]
c = xlist [-1]

Airfoil[0,0] = a
Airfoil [int((len(xlist))/2),0] = b
Airfoil [-1,0]= c

print(Airfoil)
np.savetxt(Afname+'.dat',Airfoil)
plt.show()
plt.close()