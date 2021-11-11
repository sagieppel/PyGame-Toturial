import pygame 

pygame.init()

screen=pygame.display.set_mode([500,500])

pygame.draw.circle(screen, [255,0,0], [100,100], 50)

pygame.display.update()

pygame.time.delay(10000)

pygame.quit()
