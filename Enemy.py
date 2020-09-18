import pygame
import os
import time
import random
pygame.font.init()
import Ship

class Enemy(Ship):

    def __init__(self, x, y, rotation, image):
        

    ### Move towards player. Call shoot
    def move(self, player_x, player_y, lasers):


