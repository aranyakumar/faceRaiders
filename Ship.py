import pygame
import os
import time
import random
pygame.font.init()

## Controls both enemy and player
class Ship:
    COOLDOWN = 30

    ### Initialize self and projectiles of Player_1. Initialize self.mask from image. Initialize self.x, self.y, self.rotation
    def __init__(self, x, y, rotation, image):
        self.x = x
        self.y = y
        self.image = image
        self.rotation = rotation
        self.cool_down_counter = 0
        self.mask = pygame.mask.from_surface(self.image)

    ### Draw this ship
    def draw(self, window):
        magic = pygame.transform.rotate(self.image, self.rotation)
        window.blit(magic,(self.x,self.y))
        self.cool_down_counter = self.cool_down_counter + 1

    ### Returns a boolean if the ship can shoot or not
    def can_shoot(self):
        if (self.COOLDOWN < self.cool_down_counter):
            return True
        else:
            return False

    ### Shoot a laser. Enforce cooldown on shooting
    def shoot(self, lasers):
        '''call lasers.spawn from the lasers class'''
        lasers.spawn(self.x,self.y,self.rotation, self)
        self.cool_down_counter = 0

    ### Dimensions of player
    def get_width(self):
        return self.image.get_width()

    ### Dimensions of player
    def get_height(self):
        return self.image.get_height()

    ### Get location of player
    def get_location(self):
        return (self.x,self.y)

    ### This is a test comment from Rucha
