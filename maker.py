import pygame, sys
from pygame import *

from colors import *
from nodes import Node

class Maker:
    def __init__(self, width: int, height: int):
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

        #mouse variables
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.mouse_click = False

        #nodes
        self.nodes = []
        self.clicked_idx = None

    def search_for_clicked_node(self):
        for i in range(len(self.nodes)):
            node = self.nodes[i]
            if node.x < self.mouse_x and node.y < self.mouse_y and node.x+node.width > self.mouse_x and node.y+node.height > self.mouse_y:
                return i
        return None

    def draw_all(self):
        self.window.fill(white)
        
        for node in self.nodes:
            node.draw(self.window)

    def run(self):
        while True:
            #update size variables values
            self.width, self.height = self.window.get_size()

            #mouse position
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

            #moving nodes
            if self.mouse_click and self.clicked_idx is not None:
                node = self.nodes[self.clicked_idx]
                node.x = self.mouse_x - node.width/2
                node.y = self.mouse_y - node.height/2

            #update view
            self.draw_all()

            #handle events
            for event in pygame.event.get():
                #quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                #keys
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        self.nodes.append(Node(self.mouse_x, self.mouse_y))
                #mouse down
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_click = True
                    self.clicked_idx = self.search_for_clicked_node()
                #mouse up
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_click = False
                    self.clicked_idx = None



            #display refresh
            pygame.display.update()
            self.clock.tick(self.FPS)

