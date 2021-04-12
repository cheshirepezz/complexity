'''
Author: L. Pezzini 
Copyright: MIT license

Simple calculator to compute the state evolution of the system: ds/dt = - 10 * s(t)
with analytical solution s(t) = s0 * exp(-10 * t)
*------------ IMPLICIT METHOD ------------------ EXPLICIT METHOD -------------*
|            sj+1 = sj −10 * dt * sj+1    |     sj+1 = sj * (1 − 10 * dt)     |
|            sj+1 = sj / (1 + 10 * dt)    |                                   | 
*-----------------------------------------------------------------------------*
'''
import numpy as np

def Explicit(ic, dt, iter):
    s = ic
    for i in range(0, iter):
        s *= (1. - 10. * dt)
        #print(s)
    return s

def Implicit(ic, dt, iter):
    s = ic
    for i in range(0, iter):
        s /= (1. + 10. * dt)
        #print(s)print(
    return s

CFL = 2/10. # when the solution start to oscillate

print(Explicit(1, 0.05, 4))
print(Implicit(1, 0.05, 4))
print(Explicit(1, 0.1, 4))
print(Implicit(1, 0.1, 4))
print(Explicit(1, 0.2, 4))
print(Implicit(1, 0.2, 4))
print(Explicit(1, 0.25, 4))
print(Implicit(1, 0.25, 4))
print(CFL)