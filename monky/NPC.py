import pygame
import random
import math

from Monkey import Monkey
from Projectile import VolleyBall

class MenuEntity:
    def __init__(self, imagefile, pos=(0,0)):
        self.shape = pygame.image.load(imagefile)
        self.raw_speed = (random.random()*1, random.random()*1)
        self.speed = [random.choice([-1, 1]) * self.raw_speed[0], random.choice([-1, 1]) * self.raw_speed[1]]
        self.update_coords(pos)

    def get_coords(self):
        return (self.left, self.top)

    def show(self, surface):
        surface.blit(self.shape, self.get_coords())

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

class Entity:
    def __init__(self, pos, dmg=.1, hp=150, spd=(.05,.05), r=40):
        '''
        Initializes an entity with position, damage, health points, speed, range, and imagefile

        Inputs:
        - pos: a tuple describing the location
        - damage: an integer representing damage output
        - health points: an integer of the total health points
        - speed: a tuple representing the speed
        - r: an integer represnting the range
        - ig: an image
        '''
        self.damage = dmg
        self.health = hp
        self.alive = True
        self.speed = spd
        self.rng = r
        self.img = pygame.image.load(random.choice(['tinyCollins.png', 'tinyOzenwozen.png']))
        self.update_coords(pos)

    def attack(self, other):
        '''
        Damages another entity

        Inputs:
        - other: the entity receiving damage
        '''
        if self.in_range(other):
            other.hurt(2 * random.random() * self.damage)
        else:
            self.move(other)

    def hurt(self, dmg):
        '''
        Entity receives damage and determines if the entity is still alive

        Inputs:
        - dmg: the receiving damage
        '''
        self.health -= dmg
        if self.health < 0:
            self.alive = False

    def is_alive(self):
        '''
        returns if the entity is alive
        '''
        return self.alive

    def get_coords(self):
        '''
        returns the location of the entity
        '''
        return self.position

    def distance(self, target):
        tar_coords = target.get_coords()
        curr_coords = self.get_coords()
        
        return math.sqrt(math.pow((tar_coords[0] - curr_coords[0]), 2) + math.pow((tar_coords[1] - curr_coords[1]), 2))
        
        return 0

    def in_range(self, target):
        '''
        Determines if self is in range of target

        Inputs:
        - target: an entity
        '''
        if self.distance(target) < self.rng:
            return True

        return False
        
    def update_coords(self, pos):
        '''
        Updates the location of the entity

        Inputs:
        - pos: the new location of the entity
        '''
        self.position = pos

    def show(self, surface):
        '''
        Displays the entity on the screen

        Inputs:
        - surface: the game screen
        '''
        if self.is_alive():
            surface.blit(self.img, self.get_coords())
    
    def move(self, target):
        '''
        Moves the entity towards a target location

        Inputs:
        - target: an entity
        '''
        tar_coords = target.get_coords()
        curr_coords = self.get_coords()
        movement = []
        
        if not self.in_range(target):
            if tar_coords[0] - curr_coords[0] < -5:
                movement.append(self.speed[0] * -1)
            elif tar_coords[0] - curr_coords[0] > 5:
                movement.append(self.speed[0])
            else:
                movement.append(0)

            if tar_coords[1] - curr_coords[1] < -5:
                movement.append(self.speed[1] * -1)
            elif tar_coords[1] - curr_coords[1] > 5:
                movement.append(self.speed[1])
            else:
                movement.append(0)

            self.update_coords((curr_coords[0] + movement[0], curr_coords[1] + movement[1]))

    def find_enemy(self, enemys):
        closest = 1000000
        close_enemy = None

        for enemy in enemys:
            dist = self.distance(enemy)
            #print(dist)

            if dist != 0 and dist < closest:
                close_enemy = enemy
                closest = dist

        return close_enemy

class Human:
    def __init__(self, pos, imagefile, hp=100, rng=40, speed=(0.05, 0)):
        self.image_RIGHT = imagefile[0]
        self.image_LEFT = imagefile[1]
        self.face = True
        self.attacks = 0
        self.range = rng
        self.max_health = hp
        self.health = hp
        self.alive = True
        #self.in_air = False
        #self.starttime = None
        #self.initialy = pos[1]
        self.speed = pygame.math.Vector2(speed)
        #self.jump_speed = pygame.math.Vector2((0, 250))
        self.update_coords(pos)
    
    def show(self, surface):
        if self.face:
            surface.blit(self.image_RIGHT, self.get_coords().xy)
        else:
            surface.blit(self.image_LEFT, self.get_coords().xy)
        self.draw_health_bar(surface, (self.get_coords()[0], self.get_coords()[1] + self.image_LEFT.get_height()), (50, 7), (0, 0, 0), (255, 0, 0), (0, 128, 0), self.health/self.max_health)  

    def draw_health_bar(self, surface, pos, size, borderC, backC, healthC, progress):
        pygame.draw.rect(surface, backC, (*pos, *size))
        pygame.draw.rect(surface, borderC, (*pos, *size), 1)
        innerPos  = (pos[0]+1, pos[1]+1)
        innerSize = ((size[0]-2) * progress, size[1]-2)
        rect = (round(innerPos[0]), round(innerPos[1]), round(innerSize[0]), round(innerSize[1]))
        pygame.draw.rect(surface, healthC, rect)


    def update_coords(self, pos):
        self.position = pos
    
    def get_coords(self):
        return self.position

    def move(self, monk:Monkey, dt):
        target = monk.get_coords()
        direction = target - self.get_coords()
        if direction.magnitude() > self.range:
            direction.y = 0
            direction.normalize_ip()
            direction *= self.speed.magnitude() * dt
            if direction.x < 0:
                self.face = False
            else:
                self.face = True

            self.update_coords(self.position + direction)
            
    def get_hitbox(self):
        return self.get_coords(), (self.get_coords() + pygame.math.Vector2((self.image_RIGHT.get_width(), self.image_LEFT.get_height())))

    def attack(self, monk:Monkey):
        target = monk.get_coords()
        distance = (target - self.get_coords()).magnitude()
        self.attacks += 1

        if distance < self.range and self.attacks % 500 == 0:
            print("ATTACK!")
            monk.hurt(self.damage)
    
    def hurt(self, damage):
        self.health -= damage
        if self.health < 0:
            self.alive = False
        
    def is_alive(self):
        return self.alive
        
class Owen(Human):
    def __init__(self, pos):
        super().__init__(pos, (pygame.image.load('./resources/owenattackRIGHT.png'), pygame.image.load('./resources/owenattackLEFT.png')), 50, 180)
    
    def attack(self, monk:Monkey, dt):
        direction = monk.get_coords() - self.get_coords()
        distance = direction.magnitude()
        direction.normalize_ip()
        self.attacks += dt

        if distance < self.range and 0 <= self.attacks % 1800 <= dt:
            return VolleyBall(self.get_coords(), direction)


# Melee enemy class
class Matteo(Human):
    def __init__(self, pos):
        super().__init__(pos, (pygame.image.load('matteoright.png'), pygame.image.load('matteoleft.png')), 100, 40, (0.2, 0))
    
    def attack(self, monk:Monkey, dt):
        direction = monk.get_coords() - self.get_coords()
        distance = direction.magnitude()
        direction.normalize_ip()
        self.attacks += dt

        if distance < self.range and 0 <= self.attacks % 900 <= dt:
            monk.hurt(400)

