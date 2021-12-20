import pygame

class Button:
    def __init__(self, imagefile1, imagefile2, pos=(0,0)):
        self.bttn1 = pygame.image.load(imagefile1)
        self.bttn2 = pygame.image.load(imagefile2)
        self.position = (pos[0] - self.bttn1.get_width() / 2, pos[1] - self.bttn1.get_height() / 2)

    def show(self, surface, muse):
        if self.hover(muse):
            surface.blit(self.bttn2, self.position)
        else:
            surface.blit(self.bttn1, self.position)

    def hover(self, muse):
        if self.position[0] > muse[0] or muse[0] > self.position[0] + self.bttn1.get_width():
            return False
        if self.position[1] > muse[1] or muse[1] > self.position[1] + self.bttn1.get_height():
            return False

        return True
