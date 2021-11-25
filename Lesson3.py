import pygame
import random
#-----------------Create a circle at X,Y--------------------------------------------------------
def createcircle(x,y):
  circle={}
  circle["red"]=random.randint(0,255)
  circle["green"]=random.randint(0,255)
  circle["blue"]=random.randint(0,255)
  circle["x"]=x
  circle["y"]=y 
  circle["size"]=random.randint(1,30)
  return circle
#------------------Draw a circle--------------------------------------------------------
def drawcircle(circle):
    pygame.draw.circle(screen, [circle["red"],circle["green"],circle["blue"]], [int(circle["x"]),int(circle["y"])], int(circle["size"]))
#----------------initiate pygame---------------------------------------------------------    

pygame.init()
screensize=500
screen=pygame.display.set_mode([screensize,screensize]) # Set screen

circle=createcircle(100,100)

#----------------------------Main loop--------------------------------------------------------------------
for i in range(10000000):
  #pygame.event.get() # Get user input
  #x,y = pygame.mouse.get_pos() # Get position of the mouse
  pygame.Surface.fill(screen,(0,0,0)) # Fill screen
  drawcircle(circle)
  pygame.time.delay(10) # Wait 10 milli second
  pygame.display.update()
