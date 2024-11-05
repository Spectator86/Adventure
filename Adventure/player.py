from settings import *
from physics import *
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
    def __init__(self, x, y, file, eyes, scale, angle, speed):
        super().__init__(x, y, file,  scale, angle)
        self.speed = speed
        self.eyes_image = pg.image.load(eyes).convert_alpha()
        self.eyes_image = pg.transform.scale(self.eyes_image, (scale, scale))
        self.eyes_image = pg.transform.rotate(self.eyes_image, angle)
        self.count = 0
        self.direction = " "
        self.cooldown = 60
        self.timer = self.cooldown
        self.dash_len = 500
        self.dash = True
        self.double_jump = True
        self.dashedR = False
        self.dashedL = False
        self.new_dash = 0
        self.mef = 0
        self.idle = False

        self.rightAllow = True
        self.leftAllow = True

    def eyes_draw(self, sc, scroll_x, scroll_y):
        sc.blit(self.eyes_image, (self.rect.x-scroll_x+self.mef, self.rect.y+10-scroll_y))

    def draw(self, sc, scroll_x, scroll_y):
        sc.blit(self.image, (self.rect.x-scroll_x, self.rect.y-scroll_y))

        self.bottom.x = self.rect.x + 5
        self.bottom.y = self.rect.y + self.scale

        self.top.x = self.rect.x + 5
        self.top.y = self.rect.y - 2

        self.right.x = self.rect.x + self.scale
        self.right.y = self.rect.y - 2

        self.left.x = self.rect.x - 2
        self.left.y = self.rect.y + 5

        if self.timer < self.cooldown:
            pg.draw.rect(sc, WHITE, (self.rect.x+self.scale//2-scroll_x, self.rect.y - 20-scroll_y, self.timer, 10))
            pg.draw.rect(sc, WHITE, ((self.rect.x+self.scale//2)-self.timer-scroll_x, self.rect.y - 20-scroll_y, self.timer, 10))

    def move(self, jump, colliders) -> None:
        for i in colliders:
            if self.right.colliderect(i):
                self.rightAllow = False
            else:
                self.rightAllow = True
            if self.left.colliderect(i):
                self.leftAllow = False
            else:
                self.leftAllow = True

        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            self.rect.x += self.speed
            self.direction = "right"
            self.idle = False

        elif keys[pg.K_a]:
            self.rect.x -= self.speed
            self.direction = "left"
            self.idle = False

        else:
            self.idle = True

        if keys[pg.K_e] and self.dash:
            if self.timer >= self.cooldown:
                if self.direction == "right":
                    self.dashedR = True
                    self.new_dash = self.rect.x + self.dash_len
                    self.timer = 0

                elif self.direction == "left":
                    self.dashedL = True
                    self.new_dash = self.rect.x - self.dash_len
                    self.timer = 0

        if self.timer < self.cooldown:
            self.timer += 1

        if self.idle:
            self.mef = 0
            self.angle = 0
        elif self.direction == "right":
            self.mef = 5
            self.angle = -10
        elif self.direction == "left":
            self.mef = -5
            self.angle = 10

        if self.dashedR and self.rect.x < self.new_dash:
            self.rect.x += 30
        else:
            self.dashedR = False
        if self.dashedL and self.rect.x > self.new_dash:
            self.rect.x -= 30
        else:
            self.dashedL = False
        if keys[pg.K_SPACE] and self.grounded:
            self.resistance = jump

    def animator(self):
        self.image = anim.update_anim()
        self.image = pg.transform.scale(self.image, (self.scale, self.scale))
        self.image = pg.transform.rotate(self.image, self.angle)

    def eyes_animator(self):
        self.eyes_image = anim1.update_anim()
        self.eyes_image = pg.transform.scale(self.eyes_image, (self.scale, self.scale))
        self.eyes_image = pg.transform.rotate(self.eyes_image, self.angle)
