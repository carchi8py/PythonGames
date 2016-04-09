import pygame
import sys

from classes import *
from process import process

pygame.init()
maxX = 1920
maxY = 1080
screen = pygame.display.set_mode((maxX, maxY), 0, 32)

clock = pygame.time.Clock()
FPS = 60

bug = Bug(0, maxY - 40, 40, 40, "images/bug.png")

while True:
    process(bug)
    #Logic
    bug.motion(maxX)

    #Draw
    screen.fill((0,0,0))
    BaseClass.allsprites.draw(screen)
    pygame.display.flip()

    #Other
    clock.tick(FPS)