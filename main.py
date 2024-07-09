import pygame, sys
from pygame import *

from colors import *

pygame.init()


window = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Map maker")

#main loop
while True:
    window.fill(white)

    #handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    



