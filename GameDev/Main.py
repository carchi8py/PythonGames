import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 360), 0, 32)

clock = pygame.time.Clock()
FPS = 60
totalFrames = 0

while True:
    #Processes
    for event in pygame.event.get():
        #Allows us to quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Logic
    totalFrames += 1
    
    #Draw
    pygame.display.flip()

    #Other
    clock.tick(FPS)