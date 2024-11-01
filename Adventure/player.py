from colors import WHITE
from physics import *
from settings import *
from anim import *
import pygame as pg

path = "images/HERO/anim_IDLE/"
path1 = "images/HERO/eyes_anim/"

anim_list = list()

for i in range(6):
    anim_list.append(f"{path}anim{i+1}.png")

anim = Anim(anim_list, 15)

eyes_anim_list = list()

for i in range(4):
    eyes_anim_list.append(f"{path1}eyes{i+1}.png")

eyes_anim_list.append(f"{path1}eyes4.png")
eyes_anim_list.append(f"{path1}eyes3.png")
eyes_anim_list.append(f"{path1}eyes2.png")
eyes_anim_list.append(f"{path1}eyes1.png")

for i in range(20):
    eyes_anim_list.append(f"{path1}eyes1.png")

anim1 = Anim(eyes_anim_list, 15)

timer = 0

class Player(PhysicBody):
    def __init__(self, x, y, file, eyes, scale, angle):
        super().__init__(x, y, file,  scale, angle)
        self.eyes_image = pg.image.load(eyes).convert_alpha()
        self.eyes_image = pg.transform.scale(self.eyes_image, (scale, scale))
        self.count = 0
        self.direction = " "
        self.cooldown = 60
        self.timer = self.cooldown
        self.dash_len = 200
        self.dash = True
        self.double_jump = True

    def eyes_draw(self, sc, scroll_x, scroll_y):
        sc.blit(self.eyes_image, (self.rect.x-scroll_x, self.rect.y+10-scroll_y))

    def draw(self, sc, scroll_x, scroll_y):
        sc.blit(self.image, (self.rect.x-scroll_x, self.rect.y-scroll_y))
        if self.timer < self.cooldown:
            pg.draw.rect(sc, WHITE, (self.rect.x+self.scale//2-scroll_x, self.rect.y - 20-scroll_y, self.timer, 10))
            pg.draw.rect(sc, WHITE, ((self.rect.x+self.scale//2)-self.timer-scroll_x, self.rect.y - 20-scroll_y, self.timer, 10))

    def move(self, speed, jump) -> None:
        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            self.rect.x += speed
            self.direction = "right"

        if keys[pg.K_a]:
            self.rect.x -= speed
            self.direction = "left"

        if keys[pg.K_e] and self.dash:
            if self.timer >= self.cooldown:
                if self.direction == "right":
                    self.rect.x += self.dash_len
                    self.timer = 0

                if self.direction == "left":
                    self.rect.x -= self.dash_len
                    self.timer = 0
        if self.timer < self.cooldown:
            self.timer += 1

        if keys[pg.K_SPACE] and self.rect.y >= floor:
            self.resistance = jump

    def animator(self) -> None:
        self.image = anim.update_anim()
        self.image = pg.transform.scale(self.image, (self.scale, self.scale))

    def eyes_animator(self):
        self.eyes_image = anim1.update_anim()
        self.eyes_ima
