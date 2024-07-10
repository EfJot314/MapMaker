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
        self.font = pygame.font.Font(pygame.font.get_default_font(), 15)

    def get_center_position(self):
        return self.x+self.width/2, self.y+self.height/2
    
    def draw(self, window: pygame.Surface, chosen: bool = False):
        col = self.color
        if chosen:
            col += (20, 20, 20)
        pygame.draw.rect(window, col, (self.x, self.y, self.width, self.height))
        label = self.font.render(self.name, 1, black)
        label_rect = label.get_rect()
        label_rect.centerx, label_rect.centery = self.get_center_position()
        window.blit(label, label_rect)
    
