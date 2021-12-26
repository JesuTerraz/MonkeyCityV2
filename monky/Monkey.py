import pygame
from pygame.event import Event
from Projectile import *
import os

class Monkey:
    def __init__(self, surfacedims:tuple, pos:Vector2) -> None:
        #Monkey Visuals
        self.image_RIGHT = pygame.image.load("./resources/monkeymonk.png")
        self.image_LEFT = pygame.image.load("./resources/monkeymonkeleft.png")
        self.face = True

        #Vertical Movement
        self.in_air = False
        self.starttime = None
        self.initial_y = pos.y
        self.jump_speed = 225
        self.jump_time = 0
        self.falling = False
        self.jumping = False

        #Lateral Movement
        self.speed = pygame.math.Vector2((.25, 0))
        self.health = 1000
        self.attacks = 0
        
        #Screen Interactions
        self.surfacedims = surfacedims
        self.update_coords(pos)
        
    def get_hitbox(self):
        '''
        returns the hitbox as a tuple containing two position vectors of the top left and bottom right points of Monkey 
        '''
        return self.get_coords(), (self.get_coords() + pygame.math.Vector2((self.image_RIGHT.get_width(), self.image_LEFT.get_height())))

    def get_coords(self) -> Vector2:
        '''
        returns the top left position of Monkey as a vector
        '''
        return self.position

    def update_coords(self, pos:Vector2) -> None:
        '''
        Updates the position of Monkey to pos
        '''
        self.position = pos

    def show(self, surface:pygame.Surface) -> None:
        '''
        Displays Monkey on surface
        '''
        if self.face:
            surface.blit(self.image_RIGHT, self.get_coords().xy)
        else:
            surface.blit(self.image_LEFT, self.get_coords().xy)
    
    def jump(self, keys:list, platforms:list, dt:int) -> None:
        '''
        Updates the coordinates of Monkey in jumping motion if player jumps, does nothing
        otherwise

        Inputs:
        - keys, a list of booleans representing player key input
        - platforms, a list of containing all Platform objects
        - dt, an integer representing time in milliseconds since last frame
        '''
        #Maintains horizontal position
        x_position = pygame.math.Vector2((self.get_coords()[0], 0))

        #If player jumps and Monkey not already in air, jumping motion is initiated
        if keys[pygame.K_w] and not self.in_air:
            self.in_air = True
            self.jumping = True
            self.jump_time = 1
            self.update_coords(x_position + self.jump_height(platforms, dt))
        #If Monkey is in the air and in jumping action, motion is continued
        elif self.jumping and self.in_air:
            self.jump_time += dt
            self.update_coords(x_position + self.jump_height(platforms, dt))

    def jump_height(self, platforms:list, dt:int) -> Vector2:
        '''
        **Needs rework**

        Determines the y position of Monkey while in jumping motion
        
        Inputs:
        - platforms, a list containing all Platform objects
        - dt, an integer representing time in milliseconds since last frame
        '''
        #Determines the y position based on kinematics
        y_position = self.initial_y + (-1 * self.jump_speed * (self.jump_time / 1000) + (1/2) * 265 * (self.jump_time / 1000) ** 2)
        max_height_time = 1000 * self.jump_speed / 265
        
        #If Monkey reaches max height, a landing platform is found
        if max_height_time - self.jump_time <= dt:
            self.falling = True
        if self.falling:
            ground = self.platform_below(platforms)

            #If Monkey falls below platform, the y position is set to platform height
            #and falling motion is ended
            if y_position > ground:
                y_position = ground
                self.in_air = False
                self.jump_time = 0
                self.falling = False
                self.jumping = False

        y_position = pygame.math.Vector2((0, y_position))

        return y_position

    def move(self, keys:list, platforms:list, dt:int) -> None:
        '''
        **Needs rework: falling motion**

        Updates the coordinates of Monkey if player moves horizontally. If Monkey falls off 
        a platform, the coordinates of Monkey are updated

        Inputs:
        - keys, a list of booleans representing player key input
        - platforms, a list of containing all Platform objects
        - dt, an integer representing time in milliseconds since last frame 
        '''

        #If player moves left or right and Monkey is not off screen, moves Monkey
        #and updates facing direction
        if keys[pygame.K_a] and not self.get_coords().x < 0:
            self.update_coords(self.get_coords() - (self.speed * dt))
            self.face = False
        if keys[pygame.K_d] and not self.get_coords().x > self.surfacedims[0] - self.image_RIGHT.get_width():
            self.update_coords(self.get_coords() + (self.speed * dt))
            self.face = True

        #If monkey is not on platform, y position is changed in falling motion
        self.on_platform(platforms)
        self.update_ground_position()
        if self.falling and not self.jumping:
            self.jump_time += dt
            self.in_air = True

            #Determines y position based on kinematics
            y_position = self.initial_y + ((1/2) * 265 * (self.jump_time / 1000) ** 2)
            ground = self.platform_below(platforms)

            #If Monkey falls below a platform, y position is set to platform height
            #and falling motion is ended
            if y_position > ground:
                y_position = ground
                self.in_air = False
                self.jump_time = 0
                self.falling = False
            self.update_coords(pygame.math.Vector2(self.get_coords().x, y_position))
    
    def update_ground_position(self) -> None:
        '''
        Updates initial ground position if Monkey is not in air
        '''
        if not self.in_air:
            self.initial_y = self.get_coords().y
        
    def throw(self, mouse:Vector2, dt:int) -> Banana:
        '''
        Monkey throws a Banana object if player clicks

        Inputs:
        - mouse, the position of the mouse
        - dt, and integer representing time in milliseconds since last frame
        '''
        #Manages time between attacks
        self.attacks += dt
        if 0 <= self.attacks % 500 <= dt:
            #Creates a Banana with tragectory towards mouse
            direction =  mouse - self.get_coords()
            direction.normalize_ip()
            return Banana(self.get_coords(), direction)

    def hurt(self, damage:int) -> None:
        '''
        Damages Monkey damage amount
        '''
        self.health -= damage
        if self.health < 0:
            print("DIE DIE DIE")

    def platform_below(self, platforms:list) -> int:
        '''
        Locates the nearest Platform object under Monkey

        Inputs:
        - platforms, a list of containing all Platform objects

        returns the height of Monkey standing on the highest Platform object
        '''
        #Height of ground
        ground = self.surfacedims[1] - self.image_LEFT.get_height()

        #Searches for highest platform below monkey
        for platform in platforms:
            plat_pos, plat_size = platform.get_dimensions()

            #If Monkey is within platform's bounds
            if plat_pos[0] < self.get_coords().x < plat_pos[0] + plat_size[0]:
                platform_ground = plat_pos[1]
                if ground > platform_ground >= self.get_hitbox()[1].y:
                    #Sets ground to height of Monkey standing on highest platform
                    ground = platform_ground - self.image_LEFT.get_height()
        
        return ground

    def on_platform(self, platforms:list) -> None:
        '''
        Determines if Monkey is standing on a Platform Object, sets falling to 
        true if not

        Inputs:
        - platforms, a list of containing all Platform objects
        '''
        if not self.falling:
            ground = self.platform_below(platforms)
            if self.get_coords().y < ground:
                self.falling = True
            else:
                self.falling = False
