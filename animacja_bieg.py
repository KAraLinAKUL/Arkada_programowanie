import pygame as pg
import sys

class Player(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites= []
        self.is_running = False
        self.sprites.append(pg.image.load("assets\postac_początek.png"))
        self.sprites.append(pg.image.load("assets\postac_bieg1.png"))
        self.sprites.append(pg.image.load("assets\postac_bieg2.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def run(self):
        self.is_running = True

    def update(self, speed):
        if self.is_running == True:
            self.current_sprite += speed

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[int(self.current_sprite)]




pg.init()
clock = pg.time.Clock()

screen = pg.display.set_mode((900, 600))
pg.display.set_caption("Student")

moving_sprites = pg.sprite.Group()
player = Player(70, 320)
moving_sprites.add(player)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                player.run()

    screen.fill((122, 125, 128))
    moving_sprites.draw(screen)
    moving_sprites.update(0.25)
    pg.display.flip()
    clock.tick(30)
