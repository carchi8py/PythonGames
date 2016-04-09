import pygame
import sys

from classes import *

pygame.init()
maxX = 1920
maxY = 1080
screen = pygame.display.set_mode((maxX, maxY), 0, 32)

clock = pygame.time.Clock()
FPS = 60

bug = Bug(0, 100, 40, 40, "images/bug.png")
bug2 = Bug(0, 300, 40, 40, "images/bug.png")
bug3 = Bug(0, 500, 40, 40, "images/bug.png")

while True:
    #Processes
    for event in pygame.event.get():
        #Allows us to quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Logic
    bug.motion()

    #Draw
    screen.fill((0,0,0))
    BaseClass.allsprites.draw(screen)
    pygame.display.flip()

    #Other
    clock.tick(FPS)