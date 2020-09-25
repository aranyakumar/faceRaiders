import pygame
import os
import time
import random
pygame.font.init()
from Player import Player
from Enemy import Enemy
from Laser import Laser

## Controls all lasers in game
class Lasers:

    def __init__(self):
        self.lasers = []
        self.image = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))

    ### Spawn a new laser at position to direction
    def spawn(self, x, y, direction):
        self.lasers.append(Laser(x, y, direction, self.image))
   
   ### Move all lasers, remove lasers offscreen
    def update(self):
        for l in self.lasers:
            l.move()
            if l.off_screen():
                self.lasers.remove(l)

    ### Draw lasers
    def draw(self, window):
        for l in self.lasers:
            l.draw(window)

    ### Return boolean if any laser hits a player. Removes that laser
    def collide_player(self, player):
        for l in self.lasers:
            if collide(l, player):
                self.lasers.remove(l)
                return True
        return False

    ### Returns a list of enemies that collided with a laser. Removes those lasers
    def collide_enemy(self, enemies):
        ret = []
        for e in enemies:
            for l in self.lasers:
                if collide(l, e):
                    ret.append(e)
                    self.lasers.remove(l)
        return ret

def collide(obj1, obj2):
    offset_x = int(obj2.x - obj1.x)
    offset_y = int(obj2.y - obj1.y)
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None