import pygame 
import random

#-------------------------------------------------------------------------
def drawcircle():
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)
    x=200
    y=200
    size=10
    pygame.draw.circle(screen, [red,green,blue], [x,y], size)
#--------------------------------------------------------------------------
pygame.init()

screensize=500

screen=pygame.display.set_mode([screensize,screensize])


drawcircle()
pygame.display.update()

pygame.time.delay(1000000)
