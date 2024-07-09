import pygame, sys
from pygame import *

from colors import *

pygame.init()


window = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Map maker")

FPS = 60
clock = pygame.time.Clock()

#main loop
while True:
    #update view
    window.fill(white)

    #handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    #display refresh
    pygame.display.update()
    clock.tick(FPS)
    



