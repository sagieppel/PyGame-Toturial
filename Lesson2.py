import pygame 
import random

#-------------------------------------------------------------------------
def drawcircle(x,y):
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)
   # x=random.randint(0,500)
  #  y=random.randint(0,500)
    size=random.randint(1,30)
    pygame.draw.circle(screen, [red,green,blue], [x,y], size)
#--------------------------------------------------------------------------
pygame.init()

screensize=500

screen=pygame.display.set_mode([screensize,screensize])


for i in range(100000):
   pygame.event.get()
   x,y = pygame.mouse.get_pos()
   drawcircle(x,y)
   pygame.display.update()
