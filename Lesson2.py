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
    #circle["size"]=circle["size"]+0.1
    circle["x"] = circle["x"]+0.1
    pygame.draw.circle(screen, [circle["red"],circle["green"],circle["blue"]], [int(circle["x"]),int(circle["y"])], int(circle["size"]))
#----------------initiate pygame---------------------------------------------------------    
pygame.init()
screensize=500
screen=pygame.display.set_mode([screensize,screensize])
circle=createcircle(100,100)
#----------------------------Main loop--------------------------------------------------------------------
for i in range(1000000):
  pygame.event.get()
  x,y = pygame.mouse.get_pos() # Get position of the mouse
  pygame.Surface.fill(screen,(0,255,0))
  drawcircle(circle)
  pygame.display.update()

