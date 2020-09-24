from Lasers import Lasers
from main import YELLOW_LASER, YELLOW_SPACE_SHIP
import pygame
import os
import time
import random
import Ship
import math
pygame.font.init()

## Animations for Player
class Player(Ship):
    cooldown_timer = 0

    ### Initialize the player image and any properties
    def __init__(self, x, y, rotation):
        super().__init__(x, y, rotation)
        self.ship_img = YELLOW_SPACE_SHIP

    ### Move player based on key strokes
    keys = pygame.key.get_pressed()

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

    #Am I doing this rotation correct?    
    def rotate_right(self):
            self.rotation += math.pi/4


    def rotate_left(self):
           self.rotation -= math.pi/4

    ### Creating a window
    def draw(self, window):    #I'm confuse here
        super().draw(window)
        

    ### Add health bar or any other player properties below
    def shoot(self, lasers):
        if (cooldown_timer > COOLDOWN):
            super().shoot(lasers)
        
