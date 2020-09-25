import pygame
import os
import time
import random
pygame.font.init()

from Ship import Ship
from Player import Player
from Lasers import Lasers
from Laser import Laser
from Enemy import Enemy

### Can be changed based on if you want full-screen or not
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Face Raiders")

# Load images
    ####
    #### Attach someone else's face from OpenCV saved image
    ####
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_my_player_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_my_player_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_my_player_blue_small.png"))

# Player my_player
    ####
    #### Attach own face from OpenCV saved image
    ####
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_my_player_yellow.png"))


# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
    ####
    #### Attach any background you like
    ####
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    enemies = []
    wave_length = 5
    enemy_vel = 1

    player_vel = 5
    laser_vel = 5

    player = Player(300, 630)
    
    lasers = Lasers()


    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        WIN.blit(BG, (0,0))
        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)
        
        lasers.draw(WIN)

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                
        ### Periodically spawn enemies here
        x = 0
        if x < 0:
            color = random.randint(3,1)
            side = WIDTH*random.rand()
            if (color == 0):
                enemies.append(Enemy(side, 0,0, BLUE_SPACE_SHIP))
            elif color == 1:
                enemies.append(Enemy(side, 0,0, RED_SPACE_SHIP))
            else:
                enemies.append(Enemy(side, 0,0, YELLOW_SPACE_SHIP))
                x = random.randint(10)
        else:
            x = x - 1


        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0: # left
            player.move_left()
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: # right
            player.move_right()
        if keys[pygame.K_w] and player.y - player_vel > 0: # up
            player.move_up()
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down
            player.move_down()
        if keys[pygame.K_q]: #  rotate left
            player.rotate_left()
        if keys[pygame.K_e]: # rotate right
            player.rotate_right()
        if keys[pygame.K_SPACE]:
            player.shoot()
            ### spawn a laser from the player
            lasers.spawn(Laser(player.x, player.y, player.rotation,RED_LASER))

        for enemy in enemies[:]:
            ### Fill in logic for moving enemies. Remove a life and enemy if it reaches the bottom
            enemy.move(player.x, player.y)
            if enemy.y == 750:
                enemies.remove(enemy)
                lives -= 1

        lasers.update()

        ### Check for laser collisions with player or enemies. Remove a life or the enemies if necessary.
        if lasers.collide_player():
            lives -= 1
        for enemy in lasers.collide_enemy(enemies):
            enemies.remove(enemy)

def main_menu():
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        WIN.blit(BG, (0,0))
        title_label = title_font.render("Press the mouse to begin...", 1, (255,255,255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


main_menu()