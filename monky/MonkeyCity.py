import pygame
import sys
import os
from pygame.locals import *
from NPC import *
import time
import random
from Button import *
from Monkey import *
from PlayGame import *
from Platform import *

pygame.init()
clock = pygame.time.Clock()

#Menu
bg = pygame.image.load('./resources/jungle.jpg')
surfacedims = (bg.get_width(), bg.get_height())
center = (surfacedims[0] // 2, surfacedims[1] // 2)
screen = pygame.display.set_mode((surfacedims[0], surfacedims[1]))
pygame.mouse.set_visible(True)
pygame.display.set_caption('Monkey City')

#Title and Start Button
titlecolor = (255, 255, 255)
font = pygame.font.Font('freesansbold.ttf', 32)
title = font.render('Welcome to Monkey City V2!', True, titlecolor)
titleRect = title.get_rect()
titleRect.center = (center[0], center[1] - 64)
start_button = Button("./resources/startbutton1.png", "./resources/startbutton2.png", (center[0], center[1]))
start = True

#Character Showcase
characters = ["./resources/tinyRhett.png", "./resources/tinyOzenwozen.png", "./resources/owenattackLEFT.png", "./resources/tinyJbcDemon.png"]
objects = []
for _ in range(50):
    objects.append(MenuEntity(random.choice(characters), center))

#Menu Screen
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

#Level Select Screen
level_select = True
levels = []
for _ in range(4):
    levels.append(Button("./resources/sad.monkey.jpg", "./resources/cool.monkey.jpg", (_ * surfacedims[0] / 4 + surfacedims[0] / 8, surfacedims[1] / 4)))
    levels.append(Button("./resources/sad.monkey.jpg", "./resources/cool.monkey.jpg", (_ * surfacedims[0] / 4 + surfacedims[0] / 8, 3 * surfacedims[1] / 4)))

while level_select:
    screen.blit(bg, (0,0))
    muse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Level 1
            if levels[0].hover(muse):
                level1 = True
                #Create new background for level 1
                #bg = pygame.image.load('playingField.png')
                monk = Monkey(surfacedims, pygame.math.Vector2(center[0], surfacedims[1] - 60))

                platforms = [Platform(pygame.math.Vector2((100, 280)), (255, 0, 0), pygame.math.Vector2(100, 10))]
                platforms.append(Platform(pygame.math.Vector2((0, surfacedims[1])), (0, 0, 0), pygame.math.Vector2(surfacedims[0], 0)))
                projectiles = []
                humans = []
                for _ in range(2):
                    humans.append(Owen(random.choice([pygame.math.Vector2(0, surfacedims[1] - 40), pygame.math.Vector2(surfacedims[0] - 40, surfacedims[1] - 44)])))
                frame = 0
                starttime = pygame.time.get_ticks()

                while level1:
                    screen.blit(bg, (0,0))
                    dt = clock.tick(100)
                    #print(dt)
                    muse = pygame.math.Vector2(pygame.mouse.get_pos())
                    #frame += 1
                    #print(frame / ((pygame.time.get_ticks() + 1 - starttime) / 1000))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                    
                    if pygame.mouse.get_pressed()[0]:
                        ban = monk.throw(muse, dt)
                        if ban != None:
                            projectiles.append(ban)

                    monk.move(pygame.key.get_pressed(), dt)
                    monk.jump(pygame.key.get_pressed(), platforms, dt)
                    monk.show(screen)

                    for platform in platforms:
                        platform.show(screen)

                    play_humans(humans, monk, projectiles, screen, dt)
                    play_projectiles(humans, monk, projectiles, screen, dt)

                    pygame.display.update()


            #Level 2
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
            
            #Level 3
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

            #Level 4
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

            #Level 5
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

            #Level 6
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

            #Level 7
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

            #Level 8
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

