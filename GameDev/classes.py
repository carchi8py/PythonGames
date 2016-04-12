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
        self.vely = 5

        self.jumping = False
        self.go_down = False

    def motion(self, screenwidth, screenheight):
        #if the next frame is going to be over the image screen stop it.
        predicted_location = self.rect.x + self.velx
        if predicted_location < 0:
            self.velx = 0
        elif predicted_location + self.width > screenwidth:
            self.velx = 0
        self.rect.x += self.velx

        self.__jump(screenheight)

    def __jump(self, screenheight):

        max_jump = 200

        if self.jumping:
            if self.rect.y < max_jump:
                self.go_down = True
            if  self.go_down:
                self.rect.y += self.vely
                predicted_location = self.rect.y + self.vely
                if predicted_location + self.height > screenheight:
                    self.jumping = False
                    self.go_down = False
            else:
                self.rect.y -= self.vely

class Fly(BaseClass):
    List = pygame.sprite.Group()
    def __init__(self, x, y, width, height, image_string):
        BaseClass.__init__(self, x, y, width, height, image_string)
        Fly.List.add(self)

