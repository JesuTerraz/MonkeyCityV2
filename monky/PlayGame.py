import pygame
from Projectile import *
from NPC import *
from Monkey import *

def play_humans(humans, monk, projectiles, screen, dt):
    human_die = []
    for human in humans:
        if human.is_alive():
            human.show(screen)
            human.move(monk, dt)
            if type(human) == Owen:
                volley = human.attack(monk, dt)
                if volley != None:
                    projectiles.append(volley)
            elif type(human) == Sebby:
                bullets = human.attack(monk, dt)
                if bullets != None:
                    projectiles += bullets
            else:
                human.attack(monk, dt)
        else:
            human_die.append(human)
    
    for human in human_die:
        humans.remove(human)

def play_projectiles(humans, monk, projectiles, screen, dt):
    to_remove = []
    for proj in projectiles:
        if proj.on_screen(screen):
            proj.move(dt)
            proj.show(screen)
            if type(proj) == VolleyBall and proj.hit(monk.get_hitbox()):
                monk.hurt(proj.get_damage())
                to_remove.append(proj)
            if type(proj) == Chest and proj.hit(monk.get_hitbox()):
                monk.hurt(proj.get_damage())
                to_remove.append(proj)
            if type(proj) == Banana:
                for human in humans:
                    if proj.hit(human.get_hitbox()):
                        human.hurt(proj.get_damage())
                        to_remove.append(proj)
                        break
        else:
            to_remove.append(proj)
    
    for proj in to_remove:
        projectiles.remove(proj)