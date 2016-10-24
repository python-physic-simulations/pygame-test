# -*- coding: utf-8 -*-
import sys, pygame

from pygame.locals import *

pygame.init()
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
screen_width = 800
screen_height = 600
screen_surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('ball')
screen_surface.fill(WHITE)
class Point():
    def __init__(self,x ,y):
        self.x = x
        self.y = y
    def as_tuple(self):
        return (self.x,self.y)
    def as_int_tuple(self):
        return (int(self.x),int(self.y))
class vector():
    def __init__(self , x , y):
        self.x = x
        self.y = y
    def __add__(self, oper):
        return vector(self.x + oper.x, self.y + oper.y)
    def __mul__(self, times):
        return vector(self.x * times, self.y * times)
class Ball():
    def __init__(self, x, y, radius= 10, color = RED, speed = vector(0.1,0.1),\
                    force= vector(0,1), mass = 10, acc = vector(0, 0.9)):
        self.baricenter=Point(x,y)
        self.color= color
        self.radius = radius
        self.speed = speed
        self.force = force
        self.mass = mass
        self.acc = acc
    def draw(self, surface):
        pygame.draw.circle( surface , self.color, self.baricenter.as_int_tuple(), self.radius )
    def update_pos(self,time_diff):
        """update pos using ball's speed giving time_diff in seconds"""
        self.update_speed(time_diff)
        self.baricenter.x = self.baricenter.x + self.speed.x * time_diff
        self.baricenter.y = self.baricenter.y + self.speed.y * time_diff
        if int(self.baricenter.y + self.radius) > screen_height-10 :
            self.speed.y = - self.speed.y 
        if int(self.baricenter.x + self.radius) > screen_width-10 :
            self.speed.x = - self.speed.x
        if int(self.baricenter.x - self.radius) < 0 :
            self.speed.x = - self.speed.x 
    def update_speed(self, time_diff):
        self.speed = self.speed + self.acc * time_diff
ball1 = Ball(50, screen_height-250 , speed = vector(0.5,-0.5), acc = vector(0,0.001))
ball1.draw(screen_surface)
clock= pygame.time.Clock()
while True:
    time_diff = clock.get_time()
    screen_surface.fill(WHITE)
    ball1.update_pos(time_diff)
#    print("x: ",ball1.baricenter.x," y: ", ball1.baricenter.y , "\n")
    ball1.draw(screen_surface)
#    if ball1.baricenter.y > screen_height:
#        break
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
     
    pygame.display.update()
    clock.tick(40)
while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()    
