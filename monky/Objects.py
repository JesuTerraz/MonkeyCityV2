import pygame
import random

class MenuEntity:
    def __init__(self, imagefile, pos=(0,0)):
        self.shape = pygame.image.load(imagefile)
        self.raw_speed = (random.random()*1, random.random()*1)
        self.speed = [random.choice([-1, 1]) * self.raw_speed[0], random.choice([-1, 1]) * self.raw_speed[1]]
        self.update_coords(pos)

    def get_coords(self):
        return (self.left, self.top)

    def show(self, surface):
        surface.blit(self.shape, (self.left, self.top))

    def update_coords(self, pos):
        self.left = pos[0] #- self.shape.get_width() / 2
        self.top = pos[1] #- self.shape.get_height() / 2

    def move(self, surfacedims):
        if self.get_coords()[0] < 0 :
            self.speed[0] = self.raw_speed[0]
        elif self.get_coords()[0] > surfacedims[0] - self.shape.get_width():
            self.speed[0] = -self.raw_speed[0]
        if self.get_coords()[1] < 0:
            self.speed[1] = self.raw_speed[1]
        elif self.get_coords()[1] > surfacedims[1] - self.shape.get_height():
            self.speed[1] = -self.raw_speed[1]
        
        self.update_coords((self.left + self.speed[0], self.top + self.speed[1]))


#    def find_enemy(self, pos):
#        print('Found!')
#    
#    def attack(self):
#       print('AAAHAHHHHH')
'''
class Monkey(Sprite):
    def __init__(self, pos):
        super().__init__(pos)


    def __init__(self, pos):
        super().__init__(pos)

class MGrunt(Monkey):
    def __init__(self, pos):
        super().__init__(pos)
        print('HSOjskdlfj')

class MSoldier(Monkey):
    def __init__(self, pos):
        super().__init__(pos)
        print("oohohhhoh")

class MTank(Monkey):
    def __init__(sefl, pos):
        super().__init__(pos)
        print("OH OH OH")
'''
