import pygame, os
from pygame.locals import *
from stressobject import StressObject

class StressImage(StressObject):
    def __init__(self, image, x, y, clickable = False, action = None):
        self.x = x
        self.y = y
        self.ox = x
        self.oy = y
        self.coords = (x,y)
        self.url = os.path.join("img", image)
        self.original_image = pygame.image.load(os.path.join("img", image))
        self.image = pygame.image.load(os.path.join("img", image))
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.clickable = clickable
        self.action = action
    
    def draw(self, DS, camera_offset_x=0):
        DS.blit(self.image, (self.x-camera_offset_x,self.y))

    def update(self):
        pass
    
    def checkclick(self, mousex, mousey, camera_offset_x=0):
        return (self.y+self.height > mousey > self.y and 
        self.x+self.width-camera_offset_x > mousex > self.x-camera_offset_x)
        
    def change_pic(self, image):
        self.image = pygame.image.load(os.path.join("img", image))
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def change_pic_from_string(self, image):
        self.image = pygame.image.frombuffer(original_image, (32, 32), 'RGB')
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def rotate(self, deg):
        self.image = pygame.transform.rotate(self.original_image, deg)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.x = self.rect.topleft[0] + self.ox
        self.y = self.rect.topleft[1] + self.oy
