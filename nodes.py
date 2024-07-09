import pygame
from pygame import *

from colors import *

class Node:
    def __init__(self, x: int, y: int, name: str = "Unnamed", width: int = 60, height: int = 60):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name
    
    def draw(self, window: pygame.Surface):
        pygame.draw.rect(window, blue, (self.x, self.y, self.width, self.height))
    
