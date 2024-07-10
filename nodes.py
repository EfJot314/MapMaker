import pygame
from pygame import *

from colors import *

class Node:
    def __init__(self, x: int, y: int, name: str = "Unnamed", width: int = 100, height: int = 100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name
        self.color = gray

    def get_position(self):
        return self.x, self.y
    
    def draw(self, window: pygame.Surface):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
    
