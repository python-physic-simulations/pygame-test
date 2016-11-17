# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 17:21:04 2016

@author: simone
"""

from threading import Thread
from sympy import *
from sympy.geometry import Point
from pygame.locals import *
from sympy.vector import CoordSysCartesian
N = CoordSysCartesian('N')


BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
draw_list = []


class time_counter():
    def __init__(self, one_second = 1):
        self.time = 0
        self.one_second = one_second
        self.old_time = self.time
    def get_seconds(self):
         """return the real time in seconds using the incremented time
         and one_second """
         return self.time * self.one_second   
    def get_seconds_diff(self):
        sec = (self.time - self.old_time) * self.one_second
        self.old_time = self.time
        return sec
    def increment(self):
        self.time += 1
        return self.get_seconds()

#class Point():
#    def __init__(self,x ,y):
#        self.x = S(x)
#        self.y = S(y)
#    def as_tuple(self):
#        return (self.x,self.y)
#    def as_int_tuple(self):
#        return (int(self.x),int(self.y))
class vector():
    def __init__(self , x = 0, y = 0):
        self.x = x
        self.y = y
    def __add__(self, oper):
        return vector(self.x + oper.x, self.y + oper.y)
    def __mul__(self, times):
        return vector(self.x * times, self.y * times)
        

class graphical_view(Thread):
    def __init__(self, screen_width = 1920,\
        screen_height = 1080):
        print("called screen init")    
        Thread.__init__(self)
        pygame.init()
        self.width = screen_width
        self.height = screen_height
        self.surface = pygame.display.set_mode((screen_width, screen_height))
        self.surface.fill(WHITE)
        self.one_meter = Integer(10)
        self.x = 0
        self.y = screen_height
        self.clock = pygame.time.Clock()
        self.myfont = pygame.font.SysFont("monospace", 25)
        self.myfont.set_bold(True)
    def to_pixel(self, meter):
        return meter * self.one_meter
    def run(self):
        print("called run")
        while True:
            self.surface.fill(WHITE)
#            print the currentime on the screen
            time_string = str(float(Time.get_seconds())) + " s"
            time_surface = self.myfont.render(time_string, 1, GREEN)
            time_height = self.myfont.size(time_string)[1]
            self.surface.blit(time_surface, (5, self.height - time_height))
            for point in draw_list:
                pixelCenter= Point(self.to_pixel(point.x), self.to_pixel(point.y))
                pygame.draw.circle( self.surface , RED, (int(N(pixelCenter.x)) - self.x ,\
                self.y - int(N(pixelCenter.y))), 7 )
            for event in pygame.event.get():
                if event.type == QUIT:
                     pygame.quit()
                     _thread.interrupt_main()
                     sys.exit()
            self.clock.tick(30)
            pygame.display.update()
class physic_object(): #inherit form Point ??? could not be a good option
    def __init__(self, settings={'center' : Point(0,0), 'speed': 0, 'mass' : 0}):
        self.center=settings['center']
        self.speed = settings['speed']
        self.mass = settings['mass']
    def __str__(self):
        return "x : {!s} y: {!s} speed : {!s}, {!s}.\n".format(\
        self.center.x, self.center.y, self.speed.express_coordinates(N)[0], \
        self.speed.express_coordinates(N)[1])