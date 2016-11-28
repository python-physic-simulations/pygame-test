# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 09:09:57 2016

@author: ubuntu-gnome
"""

#vector 1.0
from sympy.geometry import Point
#%% 
class Vector():
    def __init__(self, start = Point(0,0), end = Point(0,0) ):
        self.start = start
        self.end = end
    @property
    def x(self):
        return   self.end.x - self.start.x
    @x.setter
    def x(self, value):
        x = self.start.x + value
        self.end = Point(x, self.end.y)
    def __str__(self):
        return 'start: ' + str(self.start) + ' end: '+ str(self.end) + 'x :'+\
        str(self.x)
    def __mul__(self, Op):
        pass
#    @classmethod
#    def from_comp(cls, start = Point(0,0), x= 0 , y = 0):
#        return cls(start, Point(start.x + x, start.y +y))
#%% 