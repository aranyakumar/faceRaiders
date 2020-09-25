import pygame
import os
import time
import random
import math
pygame.font.init()

## Projectile of players
class Laser:
    def __init__(self, x, y, rotation, img, obj, speed = 10):
        self.x = x 
        self.y = y
        self.rotation = rotation #0 rad is vertically up, pi is directly down
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
        self.speed = speed
        self.obj = obj

    def draw(self, window):
        magic = pygame.transform.rotate(self.img, (180 / math.pi) * self.rotation)
        window.blit(magic, (self.x, self.y))

    ### Laser moves in a straight line. Optional: add logic for bouncing off of edge
    ### PASS THRU WINDOW MAX X PLS!!!
    def move(self):
        if (self.x > 750 or self.x < 0):
            self.rotation = -self.rotation
        self.x += self.speed*math.sin(self.rotation)
        self.y += self.speed*math.cos(self.rotation)
    ##?!?!?!?! wtf
    def off_screen(self):
        if self.y < 0 or self.y > 750:
            return True
        return False