import pygame
from pygame.sprite import Sprite

class Gun(Sprite): # create a child class of Sprite

    def __init__(self, screen):
        # initialize the gun and set its initial position
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Python/SpaceGame/image/laser_gun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        # draw a gun in the current position
        self.screen.blit(self.image, self.rect)

    def update_gun(self): 
        # update the position of the gun according to the flag
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        elif self.mleft and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center

    def create_gun(self):
        # create a gun in the center of the bottom side
        self.center = self.screen_rect.centerx


