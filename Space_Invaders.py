from os import path
import pygame
import time
import random
import sys
import pickle
from data.data import BACKGROUND
from drop import Drop
from enemy import Boss, Enemy
from laser import collide
from player import Player
from window import HEIGHT, WIDTH, WINDOW, Window
pygame.font.init()


def start_game() -> None:
    run = True
    FPS = 60
    window_rect = Window(0,0,BACKGROUND)

    high_score = 0
    if path.exists('data/high_score'):
        with open('data/high_score', 'rb') as fp:
            high_score = pickle.load(fp)
    level = 0
    lives = 10
    lost = False
    lost_messege_count = 0
    main_font = pygame.font.SysFont("comicsans", 40)
    lost_font = pygame.font.SysFont("comicsans", 60)

    enemies = []
    drops = []
    drops_timer = []

    wave_length = 0

    drop_speed = 4
    enemy_speed = 3
    laser_speed = 4
    n=0
    player = Player(300,640,5,10,10)

    clock = pygame.time.Clock()

    def redraw_window() -> None:
        WINDOW.blit(BACKGROUND, (0,0))

        # draw text
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        high_score_label = main_font.render(f"High Score: {high_score}",1, (255,255,255))
        enemies_label = main_font.render(f"Enemies: {len(enemies)}", 1, (255,255,255))

        WINDOW.blit(level_label, (WIDTH-level_label.get_width()-10,50))
        WINDOW.blit(lives_label, (10,10))
        WINDOW.blit(high_score_label, (WIDTH-level_label.get_width()-130,10))
        WINDOW.blit(enemies_label, (10,50))

        for enemy in enemies:
            enemy.draw(WINDOW)

        for drop in drops:
            drop.draw(WINDOW)

        player.draw(WINDOW)

        if lost:
            lost_label = lost_font.render("YOU LOST!", 1, (255,255,255))
            WINDOW.blit(lost_label, (WIDTH/2-lost_label.get_width()/2, 350))

        pygame.display.update()


    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_messege_count += 1

        if lost:
            with open('data/high_score', 'wb') as fp:
                pickle.dump(high_score, fp)
            if lost_messege_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            if level > high_score:
                high_score = level
            #if level % 5 == 0:
            #    if player.speed < 10:
            #        player.speed += 0.5
            #    if enemy_speed < 10:
            #        enemy_speed += 0.2
            #if player.RELOAD > 2:
            #    player.RELOAD -= 2
            if player.health != player.max_health:
                player.health += 1
            
            wave_length += 4

            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100),2, random.choice(["red", "blue", "green"]))
                enemies.append(enemy)
            if level % 5 == 0:
                boss = Boss(random.randrange(50, WIDTH-100), -1400,1, random.choice(["red", "blue", "green"]), health=5*level*2, laser_damage=2, number_of_lasers=3)
                enemies.append(boss)
                drop = Drop(random.randrange(50, WIDTH-100), random.randrange(-1200, -100), random.randint(0,5))
                drops.append(drop)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('data/high_score', 'wb') as fp:
                    pickle.dump(high_score, fp)
                sys.exit(0)

        keys = pygame.key.get_pressed()
        # Move left
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.x - player.speed > 0:
            player.x -= player.speed
        # Move right
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.x + player.speed + player.get_width() < WIDTH:
            player.x += player.speed
        # Move up
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and player.y - player.speed > 0:
            player.y -= player.speed
        # Move down
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.y + player.speed + player.get_height() + 15 < HEIGHT:
            player.y += player.speed
        # Shoot
        if keys[pygame.K_SPACE]:
            player.shoot()
        n += 1
        if n >= 10*FPS:
            if random.randrange(0, FPS):
                drop = Drop(random.randrange(50, WIDTH-100), random.randrange(-1200, -100), random.randint(0,5)) 
                drops.append(drop)
                n = 0

        for enemy in enemies[:]:
            enemy.move(enemy.speed)
            enemy.move_lasers(laser_speed, player)

            if type(enemy) == Enemy:
                if random.randrange(0, 6*FPS) == 1:
                    enemy.shoot()
            else:
                if random.randrange(0, 2*FPS) == 1:
                    enemy.shoot()
            
            if collide(enemy, player):
                if type(enemy) == Boss:
                    player.health -= 100
                player.health -= 1
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                if type(enemy) == Boss:
                    lives -= 100
                lives -= 1
                enemies.remove(enemy)
        
        for drop in drops[:]:
            drop.move(drop_speed)

            if collide(drop, player):
                if drop.drop_name == "explosion":
                    for enemy in enemies[:]:
                        if collide(enemy, window_rect):
                            enemy.health -= 10
                            if enemy.health <= 0:
                                enemies.remove(enemy)
                    drops.remove(drop)
                elif drop.drop_name == "hp":
                    player.drop_use(drop)
                    drops.remove(drop)
                elif drop.drop_name == "heart":
                    lives += 2
                    drops.remove(drop)
                else:
                    player.drop_use(drop)

                    drops_timer.append([drop, 0])
                    drops.remove(drop)

        for drop in drops_timer[:]:
            drop[1] += FPS
            #test = drop[0]
            #print(test.drop_name, drop[1])
        
            if drop[1] == 400*FPS:
                player.drop_expired(drop[0])
                drops_timer.remove(drop)
        
        #print(clock.tick(FPS))
        player.move_lasers(-laser_speed, enemies)

def main_menu():
    title_font = pygame.font.SysFont("comicsans", 60)
    run = True
    while run:
        WINDOW.blit(BACKGROUND, (0,0))
        title_label = title_font.render("Press the mouse to begin...", 1, (255,255,255))
        WINDOW.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_game()

main_menu()