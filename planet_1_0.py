#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#planet 1.0
"""
Created on Thu Nov 17 17:14:46 2016

@author: simone
 this module is a test for planets
"""
from base_classes import *
screen = graphical_view()
screen.start()
Time = time_counter(Rational(1,100))
planet1 = physic_object({
            'center' : Point(45,50),
            'speed' : 40 * N.y,
            'mass' : Integer(10),
            })
sun =  physic_object({
            'x' : 95,
            'y' : 50,
            'speed' : Integer(0),
            'mass' : 10,
            })          
while True:
    new_planet = {
        'center' : Point
        }