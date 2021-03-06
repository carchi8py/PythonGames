import pygame
import sys

def process(bug):
    #Processes
    for event in pygame.event.get():
        #Allows us to quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()

    #Horizontal movement
    if keys[pygame.K_d]:
        bug.image = pygame.image.load("images/bug.png")
        bug.velx = 5
    elif keys[pygame.K_a]:
        bug.image = pygame.image.load("images/bugflipped.png")
        bug.velx = -5
    else:
        bug.velx = 0

    #Vertical Movement
    if keys[pygame.K_w]:
        bug.jumping = True