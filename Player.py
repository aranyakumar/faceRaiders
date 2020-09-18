import pygame
import os
import time
import random
pygame.font.init()

## Animations for Player
class Player(Player_1):

    ### Initialize the player image and any properties
    def __init__(self, x, y):
        super().__init__(x, y)

    ### Animation for projectiles
    def move_lasers(self):

    ### Move player based on key strokes
    def move_right(self):

    def move_left(self):

    def move_up(self):

    def move_down(self):

    def rotate_right(self):

    def rotate_left(self):

    ### Creating a window
    def draw(self, window):
        super().draw(window)

    ### Add health bar or any other player properties below