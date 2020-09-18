import pygame
import os
import time
import random
pygame.font.init()

## Projectile of players
class Laser:
    def __init__(self, x, y, rotation, img):
        

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    ### Laser moves in a straight line. Optional: add logic for bouncing off of edge
    def move(self):

    def off_screen(self):