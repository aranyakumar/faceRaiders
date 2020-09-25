import pygame
import os
import time
import random
pygame.font.init()

## Projectile of players
class Laser:
    def __init__(self, x, y, rotation, img):
        self.x = x
        self.y = y
        self.rotation = rotation
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
        

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    ### Laser moves in a straight line. Optional: add logic for bouncing off of edge
    def move(self):
        self.y -= 5

    def off_screen(self):
        return self.x < 0 or self.y < 0 or self.x > 750 or self.y > 750