import pygame as pg

from physics import PhysicBody
from settings import *
from player import Player
from colors import *

pg.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))

clock = pg.time.Clock()
count = 0

eyes_anim = True

player = Player(WIDTH//2, 0, "images/HERO/anim_IDLE/anim1.png","images/HERO/eyes_anim/eyes1.png",  100, 0)
object = PhysicBody(100, HEIGHT//2, "images/hero.png", 100, 0)

while True:
    sc.fill(GREEN)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    if player.rect.y >= floor:
        count = 0

    object.draw(sc)
    object.gravity_down()

    player.draws(sc)
    player.move(10, 25)
    player.gravity_down()
    player.animator()
    player.eyes_draw(sc)
    if eyes_anim:
        player.eyes_animator()

    pg.display.update()
    clock.tick(FPS)