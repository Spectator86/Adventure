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

scroll_x = 0
scroll_y = 0
box_scale = 100

player = Player(WIDTH//2, 0, "images/HERO/anim_IDLE/anim1.png","images/HERO/eyes_anim/eyes1.png",  100, 0)
object = PhysicBody(100, HEIGHT//2, "images/hero.png", 100, 0)

while True:
    sc.fill(GREEN)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    if player.rect.y >= floor:
        count = 0

    object.draw(sc, scroll_x, scroll_y)
    object.gravity_down()

    player.draw(sc, scroll_x, scroll_y)
    player.move(10, 25)
    player.gravity_down()
    player.animator()
    player.eyes_draw(sc, scroll_x, scroll_y)
    if eyes_anim:
        player.eyes_animator()

    if player.rect.x+player.scale//2 > scroll_x+box_scale+WIDTH//2:
        scroll_x+=10
    elif player.rect.x < scroll_x-box_scale+WIDTH//2:
        scroll_x-=10

    if player.rect.y+player.scale//2 > scroll_y+box_scale+HEIGHT//2:
        scroll_y+=10
    elif player.rect.y < scroll_y-box_scale+HEIGHT//2:
        scroll_y-=10

    pg.display.update()
    clock.tick(FPS)
