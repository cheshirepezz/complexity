import numpy as np
import math

class Integrator:
    '''Class of Integrator which numerically integrates the function f(x)
    '''
    def __init__(self, xMin, xMax, N):
        '''init method or constructor -> used to initializing the object’s state
        '''
        # instance variable
        self.xmin = xMin
        self.xmax = xMax
        self.n = N
        
    def func(self, x):
        '''One variable function
        '''
        return x**2 * np.exp(-x) * np.sin(x)

    def integrate(self):
        deltax = (self.xmax - self.xmin)/self.n

        sum = 0. 
        for i in range(self.n):
            #xi = self.xmin + i * deltax
            #print(xi)
            #sum += self.func(xi) * deltax
            #print(sum)
            sum += deltax
            print(i)
            return sum

    def show(self):
        '''Method of show print on the screen the result of integration
        '''
        print('Intergation with given param.: ' + str(self.integrate()))


examp = Integrator(1, 3, 200)
examp.integrate()
examp.show()
