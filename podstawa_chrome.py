# to działa identycznie jak to w chromie, czyli jak wpadnie na przeszkodę to umiera. Postaram się to zrobić, żeby to się odejmowało od paska. Ale przyjmniej jest bieganie, skakanie i coś się dzieje jak mija się przeszkody. Wpisałam obrazki niektóre dość randomowo, ale git
import pygame
import os
import random
pygame.init()

# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join(f'/home/justyna/Pulpit/gra/postac_bieg1.png')),
           pygame.image.load(os.path.join(f'/home/justyna/Pulpit/gra/postac_bieg2.png'))]
JUMPING = pygame.image.load(os.path.join(f'/home/justyna/Pulpit/gra/postac_skok.png'))
DUCKING = [pygame.image.load(os.path.join(f'/home/justyna/Pulpit/gra/postac_schylenie1.png')),
           pygame.image.load(os.path.join(f'/home/justyna/Pulpit/gra/postac_schylenie2.png'))]

SMALL_CACTUS = [pygame.image.load(os.path.join(f'/home/justyna/Pulpit/gra/przeszkoda_atom.png')),
                pygame.image.load(os.path.join(f'/home/justyna/Pulpit/gra/przeszkoda_atom.png')),
                pygame.image.load(os.path.join(f'/home/justyna/Pulpit/gra/przeszkoda_atom.png'))]
LARGE_CACTUS = [pygame.image.load(os.path.join(f'/home/justyna/Pulpit/gra/przeszkoda_atom.png')),
                pygame.image.load(os.path.join(f'/home/justyna/Pulpit/gra/przeszkoda_atom.png')),
                pygame.image.load(os.path.join(f'/home/justyna/Pulpit/gra/przeszkoda_atom.png'))]

BIRD = [pygame.image.load(os.path.join(f'/home/justyna/Pulpit/gra/przeszkoda_mail.png')),
        pygame.image.load(os.path.join(f'/home/justyna/Pulpit/gra/przeszkoda_mail.png'))]

CLOUD = pygame.image.load(os.path.join(f'/home/justyna/Pulpit/gra/grad_cap_icon.jpg'))

BG = pygame.image.load(os.path.join(f'/home/justyna/Pulpit/gra/podłoga.png'))


class Student:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.st_duck = False
        self.st_run = True
        self.st_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.st_rect = self.image.get_rect()
        self.st_rect.x = self.X_POS
        self.st_rect.y = self.Y_POS

    def update(self, userInput):
        if self.st_duck:
            self.duck()
        if self.st_run:
            self.run()
        if self.st_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.st_jump:
            self.st_duck = False
            self.st_run = False
            self.st_jump = True
        elif userInput[pygame.K_DOWN] and not self.st_jump:
            self.st_duck = True
            self.st_run = False
            self.st_jump = False
        elif not (self.st_jump or userInput[pygame.K_DOWN]):
            self.st_duck = False
            self.st_run = True
            self.st_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.st_rect = self.image.get_rect()
        self.st_rect.x = self.X_POS
        self.st_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.st_rect = self.image.get_rect()
        self.st_rect.x = self.X_POS
        self.st_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.st_jump:
            self.st_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.st_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.st_rect.x, self.st_rect.y))


class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Student()
    cloud = Cloud()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.st_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)

        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(30)
        pygame.display.update()


def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()


menu(death_count=0)
