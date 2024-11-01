import pygame as pg
from settings import *

class Anim:
    def __init__(self, anim_list, speed, loop=True):
        self.anim_list = anim_list
        self.speed = speed
        self.loop = loop
        self.count = 0
        self.timer = 0

    def update_anim(self):
        if self.timer >= FPS/self.speed:
            if self.count < len(self.anim_list)-1:
                self.count += 1
            elif self.loop:
                self.count = 0

            self.timer = 0
        else:
            self.timer+= 1
        return pg.image.load(self.anim_list[self.count - 1]).convert_alpha()

    def anim_one(self):
        for i in range(len(self.anim_list)):
            return pg.image.load(self.anim_list[i]).convert_alpha()

    def anim_reset(self):
        self.count = 0