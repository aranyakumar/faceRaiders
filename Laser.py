import pygame
import os
import time
import random
import math
pygame.font.init()

## Projectile of players
class Laser:
    def __init__(self, x, y, rotation, img, speed = 10):
        self.x = x 
        self.y = y
        self.rotation = rotation #0 rad is vertically up, pi is directly down
        self.img = img
        self.speed = speed

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    ### Laser moves in a straight line. Optional: add logic for bouncing off of edge
    ### PASS THRU WINDOW MAX X PLS!!!
    def move(self, max_x):
        if (self.x > max_x):
            self.rotation = -self.rotation
        self.x += self.speed*math.sin(self.rotation)
        self.y += self.speed*math.cos(self.rotation)
    ##?!?!?!?! wtf
    def off_screen(self, max_y):
        if self.y > max_y:
            return True
        return False