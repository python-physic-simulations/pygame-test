# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 12:16:10 2016

@author: ubuntu-gnome
"""
import sys, pygame

from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
class Point():
    def __init__(self,x ,y):
        self.x = x
        self.y = y
    def as_tuple(self):
        return (self.x,self.y)
    def as_int_tuple(self):
        return (int(self.x),int(self.y))
class Screen():
    """class for a screen"""
    def __init__(self,screen_width = 800,\
        screen_height = 600):
        pygame.init()
        self.width = screen_width
        self.height = screen_height
        self.surface = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('screen')
        self.surface.fill(WHITE)
        self.one_meter = 10
        self.x = 0
        self.y = screen_height
        pygame.display.update()
    def draw_circle(self, center=Point(200,200) , radius=10 , color=RED):
        print("called draw_circle")
#        self.surface.fill(WHITE)
        x= self.to_pixel(center.x)
        y = self.to_pixel(center.y)
        new_center= Point(self.to_pixel(center.x), self.to_pixel(center.y))
        print("called draw_circle")
        pygame.draw.circle( self.surface , color, (x - self.x , self.y - y), radius )
        pygame.display.update()
    def to_pixel(self, meter):
        return meter * self.one_meter
screen = Screen()
screen.draw_circle( Point(20,20) , 10 )
while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()    
