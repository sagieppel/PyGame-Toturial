
import pygame
import random
#-----------------Create a circle at X,Y--------------------------------------------------------
def createcircle(x,y):
  circle={}
  circle["red"]=random.randint(0,255)
  circle["green"]=random.randint(0,255)
  circle["blue"]=random.randint(0,255)
  circle["x"]=x #random.randint(0,255)
  circle["y"]=y #random.randint(0,255)
  circle["size"]=random.randint(1,30)
  return circle
#------------------Draw a circle--------------------------------------------------------
def drawcircle(circle):
    pygame.draw.circle(screen, [circle["red"],circle["green"],circle["blue"]], [circle["x"],circle["y"]], circle["size"])
    
pygame.init()

screensize=500

screen=pygame.display.set_mode([screensize,screensize])

for i in range(1000000):
  pygame.event.get()
  x,y = pygame.mouse.get_pos() # Get position of the mouse
  circle=createcircle(x,y)
  drawcircle(circle)
  pygame.display.update()
