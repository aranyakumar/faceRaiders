import pygame
import os
import time
import random
pygame.font.init()

## Controls both enemy and player
class Ship:

    ### Initialize self and projectiles of Player_1. Initialize self.mask from image. Initialize self.x, self.y, self.rotation
    def __init__(self, x, y, rotation, image):

    ### Draw this ship
    def draw(self, window):

    ### Returns a boolean if the ship can shoot or not
    def can_shoot(self):

    ### Shoot a laser. Enforce cooldown on shooting
    def shoot(self, lasers):

    ### Dimensions of player
    def get_width(self):

    ### Dimensions of player
    def get_height(self):

    ### Get location of player
    def get_location(self):
