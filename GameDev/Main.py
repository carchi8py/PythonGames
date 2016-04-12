import pygame
import sys

from classes import *
from process import process

pygame.init()
maxX = 640
maxY = 360
screen = pygame.display.set_mode((maxX, maxY), 0, 32)

clock = pygame.time.Clock()
FPS = 24

background = pygame.image.load("images/forest.jpg")
bug = Bug(0, maxY - 40, 40, 40, "images/bug.png")
fly = Fly(40, 100, 40, 35, "images/fly.png")

while True:
    process(bug)
    #Logic
    bug.motion(maxX, maxY)

    #Draw
    screen.blit(background, (0,0))
    BaseClass.allsprites.draw(screen)
    pygame.display.flip()

    #Other
    clock.tick(FPS)