import pygame
from pygame import *

from colors import *
from nodes import Node

class Edge:
    def __init__(self, node1: Node, node2: Node):
        self.node1 = node1
        self.node2 = node2
        self.color = black
    
    def contains_node(self, node: Node):
        return self.node1 == node or self.node2 == node
    
    def draw(self, window: pygame.Surface):
        pygame.draw.line(window, self.color, self.node1.get_center_position(), self.node2.get_center_position(), 3)
    
