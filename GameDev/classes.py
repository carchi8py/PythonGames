import pygame

class BaseClass(pygame.sprite.Sprite):
    #List of all Sprites in the game
    allsprites = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string):
        pygame.sprite.Sprite.__init__(self)
        BaseClass.allsprites.add(self)

        #The image of the sprite
        self.image = pygame.image.load(image_string)
        #Is the rectangle of our image
        self.rect = self.image.get_rect()
        #The Starting location of our image
        self.rect.x = x
        self.rect.y = y
        #the size of our image
        self.width = width
        self.height = height

class Bug(BaseClass):
    List = pygame.sprite.Group()
    def __init__(self, x, y, width, height, image_string):
        BaseClass.__init__(self, x, y, width, height, image_string)
        Bug.List.add(self)

        self.velx = 3

    def motion(self):
        self.rect.x += self.velx