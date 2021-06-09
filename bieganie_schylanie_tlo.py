import pygame as pg

pg.init()

width = 900
height = 600
screen = pg.display.set_mode((width, height))

icon = pg.image.load("assets\grad_cap_icon.jpg")
pg.display.set_icon(icon)

pg.display.set_caption("Student")

running = [pg.image.load("assets\postac_początek.png"), pg.image.load("assets\postac_bieg1.png"), pg.image.load("assets\postac_bieg2.png")]
bending = [pg.image.load("assets\postac_schylenie1.png"), pg.image.load("assets\postac_schylenie2.png")]

background = pg.image.load("assets\podłoga.png")

class Student():
    pos_x = 70
    pos_y = 320
    pos_y_bend = 405

    def __init__(self):
        self.run_img = running
        self.bend_img = bending

        self.student_run = True
        self.student_bend = False

        self.step_index = 0
        self.image = self.run_img[0]
        self.student_rect = self.image.get_rect()
        self.student_rect.x = self.pos_x
        self.student_rect.y = self.pos_y

    def update(self, userInput):
        if self.student_run:
            self.run()
        if self.student_bend:
            self.bend()

        if userInput[pg.K_DOWN]:
            self.student_bend = True
            self.student_run = False
        if userInput[pg.K_RIGHT]:
            self.student_run = True
            self.student_bend = False

        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.student_run = True
        self.student_bend = False
        self.image = self.run_img[self.step_index // 5]
        self.student_rect = self.image.get_rect()
        self.student_rect.x = self.pos_x
        self.student_rect.y = self.pos_y
        self.step_index += 1

    def bend(self):
        self.student_run = False
        self.student_bend = True
        self.image = self.bend_img[self.step_index // 5]
        self.student_rect = self.image.get_rect()
        self.student_rect.x = self.pos_x
        self.student_rect.y = self.pos_y_bend
        self.step_index += 1

    def draw(self, screen):
        screen.blit(self.image, (self.student_rect.x, self.student_rect.y))


run = True
clock = pg.time.Clock()
player = Student()

game_speed = 20

pos_x_bg = 0
pos_y_bg = 0

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False


    screen.fill((122, 125, 128))
    screen.blit(background, (pos_x_bg, pos_y_bg))
    screen.blit(background, (width+pos_x_bg, pos_y_bg))
    if pos_x_bg <= -width:
        screen.blit(background, (width+pos_x_bg, pos_y_bg))
        pos_x_bg = 0
    pos_x_bg -= game_speed

    userInput = pg.key.get_pressed()

    player.draw(screen)
    player.update(userInput)
    clock.tick(30)
    pg.display.update()
