import pygame
from pygame import *

from colors import *
from nodes import Node

class Edge:
    def __init__(self, node1: Node, node2: Node):
        self.node1 = node1
        self.node2 = node2
        self.color = black
    
    def draw(self, window: pygame.Surface):
        pygame.draw.line(window, self.color, self.node1.get_position(), self.node2.get_position())
    
