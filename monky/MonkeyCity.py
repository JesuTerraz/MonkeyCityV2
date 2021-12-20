import pygame
import sys
import os
from pygame.locals import *
from Objects import *
import time
import random
from Button import *

pygame.init()
clock = pygame.time.Clock()

#Menu
bg = pygame.image.load('jungle.jpg')
surfacedims = (bg.get_width(), bg.get_height())
center = (surfacedims[0] / 2, surfacedims[1] / 2)
screen = pygame.display.set_mode((surfacedims[0], surfacedims[1]))
pygame.mouse.set_visible(True)
pygame.display.set_caption('Monkey City')

#Title and Start Button
titlecolor = (255, 255, 255)
font = pygame.font.Font('freesansbold.ttf', 32)
title = font.render('Welcome to Monkey City V2!', True, titlecolor)
titleRect = title.get_rect()
titleRect.center = (center[0], center[1] - 64)
start_button = Button("startbutton1.png", "startbutton2.png", (center[0], center[1]))
start = True

#Character Showcase
characters = ["tinyRhett.png", "tinyOzenwozen.png", "tinyCollins.png", "tinyJbcDemon.png"]
objects = []
for _ in range(50):
    objects.append(MenuEntity(random.choice(characters), center))

while start:
    screen.blit(bg, (0, 0))
    muse = pygame.mouse.get_pos()
    time.sleep(.001) 

    for obj in objects:
        obj.move(surfacedims)
        obj.show(screen)   
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and start_button.hover(muse):
            start = False
            
                    
            
    screen.blit(title, titleRect)
    start_button.show(screen, muse)

    pygame.display.update()

#Level Select
level_select = True
level1 = False
level2 = False
level3 = False
level4 = False
level5 = False
level6 = False
level7 = False
level8 = False
levels = []
for _ in range(4):
    levels.append(Button("sad.monkey.jpg", "cool.monkey.jpg", (_ * surfacedims[0] / 4 + surfacedims[0] / 8, surfacedims[1] / 4)))
    levels.append(Button("sad.monkey.jpg", "cool.monkey.jpg", (_ * surfacedims[0] / 4 + surfacedims[0] / 8, 3 * surfacedims[1] / 4)))

while level_select:
    screen.blit(bg, (0,0))
    muse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if levels[0].hover(muse):
                level1 = True
                #Create new background for level 1
                bg = pygame.image.load('playingField.png')
                
                while level1:
                    screen.blit(bg, (0,0))

                    
                    #if play:
                        #Allow Characters to move
                        #if any characters remain
                        #   play = False
                        #   level_complete = True
                    #else:
                        #Allow player to select characters

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        #if start_level1 == True:
                        #   play == True
                        #if level_complete == True:
                        #   Show completion screen
                        #   level1 = False

                    pygame.display.update()

            if levels[1].hover(muse):
                level2 = True

                while level2:
                    screen.blit(bg, (0,0))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        #if event.type == pygame.MOUSEBUTTONDOWN:
                        #    level1 = False

                    pygame.display.update()

            if levels[2].hover(muse):
                level3 = True

                while level3:
                    screen.blit(bg, (0,0))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        #if event.type == pygame.MOUSEBUTTONDOWN:
                        #    level1 = False

                    pygame.display.update()

            if levels[3].hover(muse):
                level4 = True

                while level4:
                    screen.blit(bg, (0,0))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        #if event.type == pygame.MOUSEBUTTONDOWN:
                        #    level1 = False

                    pygame.display.update()

            if levels[4].hover(muse):
                level5 = True

                while level5:
                    screen.blit(bg, (0,0))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        #if event.type == pygame.MOUSEBUTTONDOWN:
                        #    level1 = False

                    pygame.display.update()
                    
            if levels[5].hover(muse):
                level6 = True

                while level6:
                    screen.blit(bg, (0,0))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        #if event.type == pygame.MOUSEBUTTONDOWN:
                        #    level1 = False

                    pygame.display.update()
                    
            if levels[6].hover(muse):
                level7 = True

                while level7:
                    screen.blit(bg, (0,0))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        #if event.type == pygame.MOUSEBUTTONDOWN:
                        #    level1 = False

                    pygame.display.update()
                    
            if levels[7].hover(muse):
                level8 = True

                while level8:
                    screen.blit(bg, (0,0))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        #if event.type == pygame.MOUSEBUTTONDOWN:
                        #    level1 = False

                    pygame.display.update()
                    

    for lvl in levels:
        lvl.show(screen, muse)

    pygame.display.update()

