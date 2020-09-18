import pygame
import os
import time
import random
pygame.font.init()
import Player
import Enemy

## Controls all lasers in game
class Lasers:

    def __init__(self):

    ### Spawn a new laser at position to direction
    def spawn(self, x, y, direction):
   
   ### Move all lasers, remove lasers offscreen
    def update(self):

    ### Draw lasers
    def draw(self, window):

    ### Return boolean if any laser hits a player. Removes that laser
    def collide_player(self, x, y):

    ### Returns a list of enemies that collided with a laser. Removes those lasers
    def collide_enemy(self, enemies):

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None