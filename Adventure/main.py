import pygame as pg
from physics import PhysicBody
from settings import *
from player import Player

DARK_BLUE = (0, 0, 20)

pg.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))

clock = pg.time.Clock()
count = 0

eyes_anim = True

player = Player(WIDTH//2, -100, "images/HERO/anim_IDLE/anim1.png","images/HERO/eyes_anim/eyes1.png", 100, 0, 10)
object = PhysicBody(WIDTH//2, -800, "images/hero.png", 100, 0)

scroll_x = 0
scroll_y = player.rect.y
box_scale_x = 30
box_scale_y = 50

colliders = list()

bricks = list()
for i in range(20):
    bricks.append(PhysicBody(i*100, 800, "images/brick.png", 100, 0))
for i in range(20):
    bricks.append(PhysicBody((i+20)*100, 900, "images/brick.png", 100, 0))

for i in bricks:
    colliders.append(i.rect)

while True:
    sc.fill(DARK_BLUE)
    keys = pg.key.get_pressed()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    for i in range(len(bricks)):
        bricks[i].draw(sc, scroll_x, scroll_y)

    object.draw(sc, scroll_x, scroll_y)
    object.gravity_down(colliders)

    player.draw(sc, scroll_x, scroll_y)
    player.eyes_draw(sc, scroll_x, scroll_y)
    player.move(25, colliders)
    player.gravity_down(colliders)
    player.animator()

    print(object.grounded)

    if eyes_anim:
        player.eyes_animator()

    if player.rect.x+player.scale//2 > scroll_x+box_scale_x+WIDTH//2:
        scroll_x=player.rect.x+player.scale//2-WIDTH//2-box_scale_x
    elif player.rect.x+player.scale//2 < scroll_x-box_scale_x+WIDTH//2:
        scroll_x=player.rect.x+player.scale//2-WIDTH//2+box_scale_x

    if player.rect.y+player.scale//2 > scroll_y+box_scale_y+HEIGHT//2:
        scroll_y=player.rect.y+player.scale//2-HEIGHT//2-box_scale_y
    elif player.rect.y+player.scale//2 < scroll_y-box_scale_y+HEIGHT//2:
        scroll_y=player.rect.y+player.scale//2-HEIGHT//2+box_scale_y

    pg.display.update()
    clock.tick(FPS)
