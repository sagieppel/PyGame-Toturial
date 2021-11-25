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
  circle["speedx"]=3
  circle["speedy"]=-5
  circle["gravity"]=0.1
  return circle
#------------------Draw a circle--------------------------------------------------------
def updatecircle(circle):
    circle["x"] += circle ["speedx"]
    circle["y"] += circle ["speedy"]
    circle["speedy"]+= circle["gravity"]
    pygame.draw.circle(screen, [circle["red"],circle["green"],circle["blue"]], [int(circle["x"]),int(circle["y"])], int(circle["size"]))

#----------------initiate pygame---------------------------------------------------------    
pygame.init()
screensize=700
screen=pygame.display.set_mode([screensize,screensize]) # Set screen

circle=createcircle(300,300)

#----------------------------Main loop--------------------------------------------------------------------
for i in range(10000000):
  #pygame.event.get() # Get user input
  #x,y = pygame.mouse.get_pos() # Get position of the mouse
  pygame.Surface.fill(screen,(0,0,0)) # Fill screen
  updatecircle(circle)
  pygame.time.delay(10) # Wait 10 milli second
  pygame.display.update()
