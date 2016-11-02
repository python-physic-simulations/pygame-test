#screen 1.0 test
import sys, pygame, time, random
from threading import Thread
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
                pygame.draw.circle( self.surface , RED, (pixelCenter.x - self.x ,\
                self.y - pixelCenter.y), 7 )
            for event in pygame.event.get():
                if event.type == QUIT:
                     pygame.quit()
                     sys.exit()
            self.clock.tick(30)
            pygame.display.update()
draw_list.append(Point(0,0))
print("main")
Time = time_counter()
print("current time: ",Time.get_seconds())
screen = graphical_view()
screen.start()

while True:
    draw_list.append(Point(random.randint(0, 80),random.randint(0, 60)))
#    increment the time
    Time.increment()
#    for testinf pouprose sleep for one second
    time.sleep(1)
    

