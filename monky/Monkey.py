import pygame
from pygame.event import Event
from Projectile import *
import os

class Monkey:
    def __init__(self, surfacedims, pos):
            print(os.getcwd())
            self.image_RIGHT = pygame.image.load("./resources/monkeymonk.png")
            self.image_LEFT = pygame.image.load("./resources/monkeymonkeleft.png")
            self.face = True
            self.in_air = False
            self.starttime = None
            self.initial_y = pos[1]
            self.speed = pygame.math.Vector2((.25, 0))
            self.jump_speed = 225
            self.health = 1000
            self.attacks = 0
            self.jump_time = 0
            self.falling = False
            self.surfacedims = surfacedims
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
    
    def jump(self, input, platforms, dt):
        x_position = pygame.math.Vector2((self.get_coords()[0], 0))

        if input[pygame.K_w] and not self.in_air:
            self.in_air = True
            self.jump_time = 1
            self.initial_y = self.get_coords().y
            print("Intial_y", self.initial_y)
            self.update_coords(x_position + self.jump_height(platforms, dt))
        elif self.in_air:
            self.jump_time += dt
            self.update_coords(x_position + self.jump_height(platforms, dt))

    def jump_height(self, platforms, dt):
        y_position = self.initial_y + (-1 * self.jump_speed * (self.jump_time / 1000) + (1/2) * 265 * (self.jump_time / 1000) ** 2)
        #print(y_position)
        max_height_time = 1000 * self.jump_speed / 265
        
        if max_height_time - self.jump_time <= dt:
            self.falling = True
        if self.falling:
            ground = self.platform_below(platforms)
            if y_position > ground:
                print('Landed ', ground)
                y_position = ground
                self.in_air = False
                self.jump_time = 0
                self.falling = False

        y_position = pygame.math.Vector2((0, y_position))

        return y_position

    def move(self, input, dt):
        if input[pygame.K_a] and not self.get_coords().x < 0:
            self.update_coords(self.get_coords() - (self.speed * dt))
            self.face = False
        if input[pygame.K_d] and not self.get_coords().x > self.surfacedims[0] - self.image_RIGHT.get_width():
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

    def platform_below(self, platforms):
        ground = 100000000
        for platform in platforms:
            plat_pos, plat_size = platform.get_dimensions()
            print(plat_pos[1])
            if plat_pos[0] < self.get_coords().x < plat_pos[0] + plat_size[0]:
                platform_ground = plat_pos[1]
                print('platform', platform_ground)
                if ground > platform_ground:
                    ground = platform_ground - self.image_LEFT.get_height()
                    print('Ground', ground)
        
        return ground
