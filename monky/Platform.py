import pygame

class Platform:
    def __init__(self, pos, clr, sz):
        self.position = pos
        self.size = sz
        self.color = clr
    
    def show(self, surface):
        pygame.draw.rect(surface, self.color, self.get_dimensions())

    def get_dimensions(self):
        return self.position.xy, self.size.xy