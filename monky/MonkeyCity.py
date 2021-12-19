import pygame
import sys
import os
from pygame.locals import *
from Objects import *
import time
import random

#Initialize the game
pygame.init()
clock = pygame.time.Clock()
bg = pygame.image.load('jungle.jpg')
surfacedims = (bg.get_width(), bg.get_height())
print(surfacedims)
screen = pygame.display.set_mode((surfacedims[0], surfacedims[1]))
pygame.mouse.set_visible(True)
pygame.display.set_caption('Monkey City')

framerate = 60

#Initialize entity
obj = MenuEntity(surfacedims, "tinyRhett.png", (surfacedims[0] / 2, surfacedims[1] / 2))


while True:
    #time = clock.tick(framerate) / 1000.0
    screen.blit(bg, (0, 0))
    #x, y = pygame.mouse.get_pos()
    obj.move(surfacedims)

    time.sleep(.001)    
    obj.show(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
    