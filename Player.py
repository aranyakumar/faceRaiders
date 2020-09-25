import pygame
import os
import time
import random
from Ship import Ship
import math
pygame.font.init()

## Animations for Player
class Player(Ship):

    ### Initialize the player image and any properties
    def __init__(self, x, y, rotation):
        super().__init__(x, y, rotation, pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png")))

    ### Move player based on key strokes
    def move_right(self):
        if (self.x < 750):
            self.x += 1

    def move_left(self):
        if (self.x > 0):
            self.x -= 1

    def move_up(self):
        if (self.y > 500):
            self.y -= 1

    def move_down(self):
        if (self.y < 750):
            self.y += 1
   
    def rotate_right(self):
            self.rotation += math.pi/4

    def rotate_left(self):
           self.rotation -= math.pi/4

    ### Creating a window
    def draw(self, window):    
        super().draw(window)

    ### Add health bar or any other player properties below
    def shoot(self, lasers):
        if (super().can_shoot()):
            super().shoot(lasers)