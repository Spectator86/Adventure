import pygame as pg

from settings import floor


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

    def draw(self, sc, scroll_x, scroll_y):
        sc.blit(self.image, (self.rect.x-scroll_x, self.rect.y-scroll_y))

    def gravity_down(self):
        self.rect.y += self.gravity-self.resistance

        if self.rect.y >= floor:
            self.gravity = 0
        else:
            self.gravity = 10

        if self.resistance > 0:
            self.resistance -= 0.5
