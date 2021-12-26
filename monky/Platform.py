import pygame
from pygame.math import Vector2
from pygame.surface import Surface

class Platform:
    def __init__(self, pos:Vector2, clr:tuple, sz:Vector2) -> None:
        self.position = pos
        self.size = sz
        self.color = clr
    
    def show(self, surface:Surface) -> None:
        pygame.draw.rect(surface, self.color, self.get_dimensions())

    def get_dimensions(self) -> None:
        '''
        Returns the dimensions of Platform as a tuple with positions, left, top, right, bottom
        '''
        return self.position.xy, self.size.xy