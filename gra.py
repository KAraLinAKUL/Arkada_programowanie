import pygame

pygame.init()

screen = pygame.display.set_mode((900, 600))

icon = pygame.image.load("grad_cap_icon.jpg")
pygame.display.set_icon(icon)

pygame.display.set_caption("Student (?)")




# def main():
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
