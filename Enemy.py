import pygame
import os
import time
import random
pygame.font.init()
import Ship
import math

class Enemy(Ship):

    def __init__(self, x, y, rotation, image):
        super().__init__(x, y, rotation, image)
        

    ### Move towards player. Call shoot
    def move(self, player_x, player_y, lasers):
        self.y = self.y+1

        if player_x < self.x:
            self.rotation = math.arctan((player_y-self.y)/(player_x - self.x)) + math.pi
        elif player_x = self.x:
            self.rotation = math.pi    
        else: 
             self.rotation = math.arctan((player_y-self.y)/(player_x - self.x)) + math.pi/2


        if super().can_shoot():
            super().shoot(lasers)
        



