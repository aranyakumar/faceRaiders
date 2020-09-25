import pygame
import os
import time
import random
pygame.font.init()

## Controls both enemy and player
class Ship:

    ### Initialize self and projectiles of Player_1. Initialize self.mask from image. Initialize self.x, self.y, self.rotation
    def __init__(self, x, y, rotation, image):
        self.x = x
        self.y = y
        self.rotation = rotation
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.health = 100

    ### Draw this ship
    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    ### Returns a boolean if the ship can shoot or not
    def can_shoot(self):
        return True

    ### Shoot a laser. Enforce cooldown on shooting
    def shoot(self, lasers):
        lasers.spawn(self.x, self.y, self.rotation)

    ### Dimensions of player
    def get_width(self):
        pass

    ### Dimensions of player
    def get_height(self):
        pass

    ### Get location of player
    def get_location(self):
        pass
