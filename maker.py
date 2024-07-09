import pygame, sys
from pygame import *

from colors import *

class Maker:
    def __init__(self, width, height):
        #window size
        self.width = width
        self.height = height

        #fps and clock
        self.FPS = 60
        self.clock = pygame.time.Clock()
        
        #pygame initialization
        pygame.init()

        #create window
        self.window = pygame.display.set_mode((800, 700))
        pygame.display.set_caption("Map maker")

    def draw_all(self):
        self.window.fill(white)

    def run(self):
        while True:
            #update size variables values
            self.width, self.height = self.window.get_size()

            #update view
            self.draw_all()

            #handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

            #display refresh
            pygame.display.update()
            self.clock.tick(self.FPS)

