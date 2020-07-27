import pygame
import random

pygame.init()

win = pygame.display.set_mode((750,750))

pygame.display.set_capacity('Space Invaders')


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50,25])
        self.image.fill(green)

def redraw():
    win.fill(black)
    pygame.display.update()

white = (255, 255, 255)
green = (0, 255, 255)
black = (255, 0, 0)

run = True

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    redraw()