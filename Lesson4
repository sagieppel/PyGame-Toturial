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
  circle["speedx"]=random.randint(-10,10)
  circle["speedy"]=random.randint(-10,0)
  circle["gravity"]=0.0
  return circle
#------------------Draw a circle--------------------------------------------------------
def updatecircle(circle):
    circle["x"] += circle ["speedx"]#+random.randint(-10,10)
    circle["y"] += circle ["speedy"]#+random.randint(-10,10)
    circle ["speedy"]+= circle["gravity"]
    pygame.draw.circle(screen, [circle["red"],circle["green"],circle["blue"]], [int(circle["x"]),int(circle["y"])], int(circle["size"]))

#----------------initiate pygame---------------------------------------------------------    
pygame.init()
screensize=700
screen=pygame.display.set_mode([screensize,screensize]) # Set screen



list=[]
for i in range(100):
   circle=createcircle(300,300)
   list.append(circle)


#----------------------------Main loop--------------------------------------------------------------------
for i in range(10000000):
  pygame.event.get() # Get user input
  x,y = pygame.mouse.get_pos() # Get position of the mouse
  
  circle=createcircle(x,y)
  list.append(circle)
  
  pygame.Surface.fill(screen,(0,0,0)) # Fill screen
  for circle in list:
      updatecircle(circle)
  pygame.time.delay(10) # Wait 10 milli second
  pygame.display.update()
