import pygame
import os
import time
import random
from Ship import Ship
pygame.font.init()

## Animations for Player
class Player(Ship):

    ### Initialize the player image and any properties
    def __init__(self, x, y, rotation):
        super().__init__(x, y, rotation, pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png")))

    ### Move player based on key strokes
    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1

    def rotate_right(self):
        pass

    def rotate_left(self):
        pass

    ### Add health bar or any other player properties below