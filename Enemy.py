import pygame
import os
import time
import random
pygame.font.init()

class Enemy(Player):

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.my_player_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.my_player_img)

    ### Move towards player_1
    def move(self, vel):

    ### 
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None