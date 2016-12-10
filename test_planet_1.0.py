# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 08:09:26 2016

@author: ubuntu
"""

# -*- coding: utf-8 -*-
import time
from sympy.vector import CoordSysCartesian, Vector
import matplotlib.pyplot as plt
import numpy as np
from sympy import Rational
N = CoordSysCartesian('N')

        
class physic_obj() :
    def __init__(self, p = N.origin, vel = Vector.zero, 
                 mass = Rational(1,1),
                 ref_frame = N ):
        self.p = p
        self.vel = vel
        self.mass = mass
        self.ref = ref_frame
        self.forces = []
    def update_pos(self, t):
        tot_force = Vector.zero
        for f in self.forces:
            tot_force += f
        acc = tot_force / self.mass
        new_p = self.ref.origin.locate_new('p', self.p.position_wrt(self.ref) +\
        self.vel * t + Rational(1,2) * acc * t ** 2)
        self.vel += acc * t
        self.forces = []# not sure that is good idea..
        self.p  = new_p
        print('pos :',self.p.express_coordinates(N),'\n vel:',self.vel)
ball = physic_obj(N.origin.locate_new('p',10*N.i), 10*N.j, Rational(1,1))  
sun = physic_obj(mass = Rational(2,1))
plt.plot(*sun.p.express_coordinates(N)[0:2], 'ro')
for i in range(10):
    ball.forces.append(sun.mass * ball.mass / (sun.p.position_wrt(N) - ball.p.position_wrt(N))**2 )
    ball.update_pos(1)
    plt.plot(*ball.p.express_coordinates(N)[0:2], 'ro')
plt.show()
#    for testinf pouprose sleep for one second
 