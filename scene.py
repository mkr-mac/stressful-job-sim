import pygame, os
from pygame.locals import *
from image import StressImage as Image
from button import StressButton as Button
from gauge import StressGauge as Gauge
from text import Text

class Scene():
    def __init__(self, object_list):
        self.objects = object_list

    def update(self):
        for obj in self.objects:
            obj.update()

    def checkclick(self, mousex, mousey, camera_offset_x=0):
        for obj in self.objects:
            obj.checkclick(mousex, mousey, camera_offset_x)
    
    def draw(self, DS, camera_offset_x=0):
        for obj in self.objects:
            obj.draw(DS, camera_offset_x)

def test():
    print("YOUI PHSHUED THE BUT TON")

def desk():
    return [
        Image('desk.png', 0, 0),
        Button('buttonup.png', 200, 500, True, test),
        Button('buttonup.png', 300, 500, True, test),
        Button('buttonup.png', 400, 500, True, test),
        Button('buttonup.png', 500, 500, True, test),
        Button('buttonup.png', 600, 500, True, test),
        Gauge(400, 400),
        Text('10000', 662, 411, os.path.join("fonts",'ARIALBD.TTF'), 60, (255,184,0)),
    ]