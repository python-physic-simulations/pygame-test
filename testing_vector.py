# -*- coding: utf-8 -*-
from sympy.vector import CoordSysCartesian, Vector
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
        self.p = self.ref.origin.locate_new('p', self.p.position_wrt(self.ref) +\
        self.vel * t + Rational(1,2) * acc * t ** 2)
#        self.forces = []# not sure that is good idea..
ball = physic_obj(N.origin, N.i + N.j, Rational(2,1))  
ball.forces.append(N.i + N.j)
        