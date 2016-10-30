#screen 1.0 test
import sys, pygame, time
from threading import Thread
from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
draw_list = []
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
        pygame.display.set_caption('screen test')
        self.surface.fill(WHITE)
        self.one_meter = 10
        self.x = 0
        self.y = screen_height
        self.clock = pygame.time.Clock()
    def to_pixel(self, meter):
        return meter * self.one_meter
    def run(self):
        print("called screen run")
        while True:
            self.surface.fill(WHITE)
            for point in draw_list:
                pixelCenter= Point(self.to_pixel(point.x), self.to_pixel(point.y))
                pygame.draw.circle( self.surface , RED, (pixelCenter.x - self.x ,\
                self.y - pixelCenter.y), 7 )
                pygame.display.update()
                self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                     pygame.quit()
                     sys.exit()
draw_list.append(Point(10,10))
screen = graphical_view()
print("returned to main")
screen.start()
for i in range(50):
    draw_list.append(randint(0, 80),randint(0, 60))

