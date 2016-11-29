# -*- coding: utf-8 -*-
from sympy.vector import CoordSysCartesian
N = CoordSysCartesian('N')
x0 = N.origin
v0 = 3*N.i

def update_pos(time):
    global x0
    x = N.origin.locate_new('p', x0.position_wrt(N) + v0 * time)
    print(x.position_wrt(N))
    x0 = x
 
 
class physic_obj() :
    def __init__(self, p = N.origin, vel = Vector.Zero):
        self.p = p
        self.vel = vel
    def update_pos(self, t):
        p = N.origin.locate_new('p', p.position_wrt(N) + vel * time)