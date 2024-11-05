import pygame as pg
from settings import *

class PhysicBody:
    def __init__(self, x, y, file, scale, angle):
        self.x = x
        self.y = y
        self.scale = scale
        self.angle = angle
        self.image = pg.image.load(file).convert_alpha()
        self.image = pg.transform.scale(self.image, (scale, scale))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.image = pg.transform.rotate(self.image, angle)
        self.resistance = 0
        self.gravity = 200
        self.mass = 5
        self.grounded = False
        self.ground = False

        self.bottom = pg.Rect((self.rect.x + 5, self.rect.y+self.scale, self.scale-10, 2))
        self.top = pg.Rect((self.rect.x + 5, self.rect.y-2, self.scale-10, 2))
        self.right = pg.Rect((self.rect.x+self.scale, self.rect.y+5, 2, self.scale - 10))
        self.left = pg.Rect((self.rect.x-2, self.rect.y+5, 2, self.scale - 10))

    def draw(self, sc, scroll_x, scroll_y):
        sc.blit(self.image, (self.rect.x-scroll_x, self.rect.y-scroll_y))

        self.bottom.x = self.rect.x + 5
        self.bottom.y = self.rect.y+self.scale

        self.top.x = self.rect.x + 5
        self.top.y = self.rect.y-2

        self.right.x = self.rect.x+self.scale
        self.right.y = self.rect.y-2

        self.left.x = self.rect.x-2
        self.left.y = self.rect.y+5

    def gravity_down(self, colliders):
        self.rect.y += self.gravity-self.resistance
        for i in colliders:
            if self.rect.colliderect(i):
                self.grounded = True
                self.ground = True
        if self.ground:
            self.grounded = True
            self.ground = False
        else:
            self.grounded = False
            self.ground = False

        if self.grounded:
            self.gravity = 0
        else:
            self.gravity = 10

        if self.resistance > 0:
            self.resistance -= 0.5
