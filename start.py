import pygame
import random

pygame.init()

win = pygame.display.set_mode((750,750))

pygame.display.set_caption('Space Invaders')

white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0,0,0)

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50,25])
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.live = 5

    def draw(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

ship = Ship()
ship.rect.x = 375
ship.rect.y = 650

def redraw():
    win.fill(black)
    ship.draw()
    pygame.display.update()

run = True

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        ship.rect.x += -10

    if key[pygame.K_RIGHT]:
        ship.rect.x += 10

    redraw()

pygame.quit()