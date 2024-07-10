import pygame, sys
from pygame import *

from colors import *
from nodes import Node
from edges import Edge

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
        self.name_input = False

        #edges
        self.edges = []
        self.create_new_edge = False
        self.node1 = None
        self.node2 = None

    def search_for_clicked_node(self):
        for i in range(len(self.nodes)):
            node = self.nodes[i]
            if node.x < self.mouse_x and node.y < self.mouse_y and node.x+node.width > self.mouse_x and node.y+node.height > self.mouse_y:
                return i
        return None
    
    def remove_node(self, node: Node):
        to_remove = []
        for edge in self.edges:
            if edge.contains_node(node):
                to_remove.append(edge)
        for edge in to_remove:
            self.edges.remove(edge)
        self.nodes.remove(node)


    def draw_all(self):
        self.window.fill(white)
        for edge in self.edges:
            edge.draw(self.window)
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
                    if self.name_input:
                        #enter
                        if event.key == pygame.K_RETURN:    
                            self.name_input = False
                        elif event.key == pygame.K_BACKSPACE:
                            self.nodes[self.clicked_idx].name = self.nodes[self.clicked_idx].name[:-1:]
                        else:
                            self.nodes[self.clicked_idx].name += pygame.key.name(event.key)
                        continue
                    if event.key == pygame.K_n:
                        self.nodes.append(Node(self.mouse_x, self.mouse_y))
                    elif event.key == pygame.K_m:
                        self.create_new_edge = True
                    elif event.key == pygame.K_x:
                        self.clicked_idx = self.search_for_clicked_node()
                        if self.clicked_idx is not None:
                            self.remove_node(self.nodes[self.clicked_idx])
                    
                #mouse down
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicked_idx = self.search_for_clicked_node()
                    #left
                    if event.button == 1:
                        self.mouse_click = True
                        if self.clicked_idx is not None:
                            #create new edge
                            if self.create_new_edge:
                                if self.node1 is None:
                                    self.node1 = self.nodes[self.clicked_idx]
                                else:
                                    self.node2 = self.nodes[self.clicked_idx]
                                    if self.node1 is not self.node2:
                                        self.edges.append(Edge(self.node1, self.node2))
                                    self.create_new_edge = False
                                    self.node1 = None
                                    self.node2 = None
                        else:
                            self.create_new_edge = False
                    #right
                    elif event.button == 3:
                        if self.clicked_idx is not None and not self.name_input:
                            self.nodes[self.clicked_idx].name = ""
                            self.name_input = True

                #mouse up
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_click = False
                    if not self.name_input:
                        self.clicked_idx = None



            #display refresh
            pygame.display.update()
            self.clock.tick(self.FPS)

