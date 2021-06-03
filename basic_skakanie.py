import pygame
from pygame.locals import *
import sys

class gracz:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.jumping = False
        self.jump_offset = 0

def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
def keys(gracz):
    keys = pygame.key.get_pressed()
    if keys[K_SPACE] and gracz.jumping == False and gracz.jump_offset == 0:
        gracz.jumping = True

def skakanie(gracz):
    global jump_height

    if gracz.jumping:
        gracz.jump_offset += 1
        if gracz.jump_offset >= jump_height:
            gracz.jumping = False
    elif gracz.jump_offset > 0 and gracz.jumping == False:
        gracz.jump_offset -=1



W, H = 1280, 720
HW, HH, = W //2, H//2
AREA = W * H

bialy = (255,255,255)
czarny = (0,0,0)
czerwony = (255, 0, 0)
SOLID_FILL = 0

g = gracz(HW, HH, 30)
jump_height = 50

pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
FPS = 30

while True:
    events()
    keys(g)
    skakanie(g)
    pygame.draw.circle(DS, bialy,(g.x, g.y - g.jump_offset), g.size, SOLID_FILL)

    platform_color = czerwony
    if g.jump_offset == 0:
        platform_color = bialy
    pygame.draw.rect(DS, platform_color, (HW - 100, HH + g.size, 200, 10), SOLID_FILL)

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(czarny)
