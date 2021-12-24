import pygame
from pygame.event import Event
from Projectile import *

class Monkey:
    def __init__(self, pos):
            self.image_RIGHT = pygame.image.load("monkeymonk.png")
            self.image_LEFT = pygame.image.load("monkeymonkeleft.png")
            self.face = True
            self.in_air = False
            self.starttime = None
            self.initialy = pos[1]
            self.speed = pygame.math.Vector2((.25, 0))
            self.jump_speed = 225
            self.health = 1000
            self.attacks = 0
            self.jump_time = 0
            self.update_coords(pos)
        
    def get_hitbox(self):
        return self.get_coords(), (self.get_coords() + pygame.math.Vector2((self.image_RIGHT.get_width(), self.image_LEFT.get_height())))

    def get_coords(self) -> Vector2:
        return self.position

    def update_coords(self, pos):
        self.position = pos

    def show(self, surface):
        if self.face:
            surface.blit(self.image_RIGHT, self.get_coords().xy)
        else:
            surface.blit(self.image_LEFT, self.get_coords().xy)
    
    def jump(self, input, dt):
        groundposition = pygame.math.Vector2((self.get_coords()[0], self.initialy))

        if input[pygame.K_w] and not self.in_air:
            self.in_air = True
            self.jump_time = 1
            self.update_coords(groundposition - self.jump_height())
        elif self.in_air:
            self.jump_time += dt
            self.update_coords(groundposition - self.jump_height())

    def jump_height(self):
        height = (self.jump_speed * (self.jump_time / 1000) - (1/2) * 265 * (self.jump_time / 1000) ** 2)
        if height < 0:
            height = 0
            self.in_air = False
            self.jump_time = 0

        height_vector = pygame.math.Vector2((0, height))

        return height_vector

    def move(self, input, screendims, dt):
        if input[pygame.K_a] and not self.get_coords().x < 0:
            self.update_coords(self.get_coords() - (self.speed * dt))
            self.face = False
        if input[pygame.K_d] and not self.get_coords().x > screendims[0] - self.image_RIGHT.get_width():
            self.update_coords(self.get_coords() + (self.speed * dt))
            self.face = True
    
    def throw(self, mouse:Vector2, dt):
        self.attacks += dt
        if 0 <= self.attacks % 500 <= dt:
            direction =  mouse - self.get_coords()
            direction.normalize_ip()
            return Banana(self.get_coords(), direction)

    def hurt(self, damage):
        self.health -= damage
        if self.health < 0:
            print("DIE DIE DIE")
