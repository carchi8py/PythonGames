import pygame
import sys

pygame.init()
maxX = 1920
maxY = 1080
screen = pygame.display.set_mode((maxX, maxY), 0, 32)

clock = pygame.time.Clock()
FPS = 60
totalFrames = 0

clr1 = (22, 122, 211)
clr2 = (255, 44, 166)
clr3 = (34, 55, 245)

i = 0
while True:
    #Processes
    for event in pygame.event.get():
        #Allows us to quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Logic
    totalFrames += 1
    i += 1
    if i > 255:
        i %= 255

    #Draw
    screen.fill((90,i,180))
    pygame.draw.line(screen, clr1, (0, 0), (maxX, maxY), 5)
    pygame.draw.rect(screen, clr2, (40,40,400,200))
    pygame.draw.circle(screen, clr3, (1500, 700), 100, 5)

    pygame.display.flip()

    #Other
    clock.tick(FPS)