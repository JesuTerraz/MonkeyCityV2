import pygame
from pygame.math import Vector2

class Projectile:
    def __init__(self, pos, direction, dmg, imagefile):
        self.speed = direction / 5
        self.image = imagefile
        self.damage = dmg
        self.update_coords(pos)

    def show(self, surface):
        surface.blit(self.image, self.get_coords().xy)
    
    def get_coords(self):
        return self.position
    
    def update_coords(self, pos:Vector2):
        self.position = pos
    
    def move(self, dt):
        self.update_coords(self.position + (self.speed * dt))

    def on_screen(self, surface:pygame.Surface):
        if self.get_coords().x < 0 or self.get_coords().x > surface.get_width():
            return False
        if self.get_coords().y < 0 or self.get_coords().y > surface.get_height():
            return False
        
        return True

    def hit(self, hbox):
        point = self.get_coords() + pygame.math.Vector2(self.image.get_width() / 2, self.image.get_height() / 2)
        if point.x > hbox[0].x and point.x < hbox[1].x:
            if point.y > hbox[0].y and point.y < hbox[1].y:
                return True
        
        return False
    
    def get_damage(self):
        return self.damage

class Banana(Projectile):
    def __init__(self, pos, direction):
        super().__init__(pos, direction, 10, pygame.image.load('banan.png'))

class VolleyBall(Projectile):
    def __init__(self, pos, direction):
        super().__init__(pos, direction, 100, pygame.image.load('owenweapon.png'))
