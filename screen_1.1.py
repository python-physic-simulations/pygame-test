#! /usr/bin/env python3
#screen 1.1 test
import sys, pygame, time, random, _thread
from threading import Thread
from sympy.solvers import solve
from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
draw_list = []


class time_counter():
    def __init__(self, one_second = 1):
        self.time = 0
        self.one_second = one_second
    def get_seconds(self):
         """return the real time in seconds using the incremented time
         and one_second """
         return self.time * self.one_second   
    def increment(self):
        self.time += 1
        return self.get_seconds()


class Point():
    def __init__(self,x ,y):
        self.x = x
        self.y = y
    def as_tuple(self):
        return (self.x,self.y)
    def as_int_tuple(self):
        return (int(self.x),int(self.y))
class vector():
    def __init__(self , x = 0, y = 0):
        self.x = x
        self.y = y
    def __add__(self, oper):
        return vector(self.x + oper.x, self.y + oper.y)
    def __mul__(self, times):
        return vector(self.x * times, self.y * times)
        

class graphical_view(Thread):
    def __init__(self, screen_width = 800,\
        screen_height = 600):
        print("called screen init")    
        Thread.__init__(self)
        pygame.init()
        self.width = screen_width
        self.height = screen_height
        self.surface = pygame.display.set_mode((screen_width, screen_height))
        self.surface.fill(WHITE)
        self.one_meter = 10
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
            time_string = str(Time.get_seconds()) + " s"
            time_surface = self.myfont.render(time_string, 1, GREEN)
            time_height = self.myfont.size(time_string)[1]
            self.surface.blit(time_surface, (5, self.height - time_height))
            for point in draw_list:
                pixelCenter= Point(self.to_pixel(point.x), self.to_pixel(point.y))
                pygame.draw.circle( self.surface , RED, (int(pixelCenter.x) - self.x ,\
                self.y - int(pixelCenter.y)), 7 )
            for event in pygame.event.get():
                if event.type == QUIT:
                     pygame.quit()
                     _thread.interrupt_main()
                     sys.exit()
            self.clock.tick(30)
            pygame.display.update()


class command(Thread):
    """class for command line interface"""
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        while True:
            command = input("insert command>> ")
    
class physic_object(Point): #inherit form Point ??? could not be a good option
    def __init__(self, settings={'x':0, 'y':0, 'speed': vector()}):
        super().__init__(settings['x'], settings['y'])
        self.speed = settings['speed']
        
class gravity_field():
    def __init__(self, g = 9.81):
        self.g = 9.81
    def update_pos(self, ob):
        ob_set = {
            'x' : ob.x + ob.speed.x * t,
            'y' : ob.y + ob.speed.y * t + 0.5 * self.g * t * t,
            'speed' : vector(ob.x, ob.y  + self.g * t),
            }
        return physic_object(ob_set)
    def time_at_x_pos(self, x):
        t = Symbol("t", positive=True)
        solve(ob.y - x + ob.speed.y * t + 0.5 * self.g * t * t, t)








ob = physic_object({ 'speed':vector(5, 15), 'acc':vector(0, -100), 'x' : 0, 'y':0 })
draw_list.append(ob)
print("main")
Time = time_counter(0.01)
print("current time: ",Time.get_seconds())
screen = graphical_view()
screen.start()
command = command()
command.start()
debug_file=open("punti parabola.debug.csv",'w')
while True:
    
    t = Time.get_seconds()
    ob.y = ob.y + ob.speed.y*t + ob.acc.y*t*t*0.5
    ob.x = ob.x + ob.speed.x*t
    print("X: ", ob.x ,"   y: ",ob.y, "\n" )
    debug_file.write(str(ob.x)+','+str(ob.y)+'\n')
#    draw_list.append(Point(random.randint(0, 80),random.randint(0, 60)))
#    increment the time
    Time.increment()
#    for testinf pouprose sleep for one second
    time.sleep(0.1)
    

