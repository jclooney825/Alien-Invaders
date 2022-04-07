#!/usr/bin/env python3

import pygame 
from game_settings import Settings
from player import Player
from wave import Wave
import random 


def run_game():
    pygame.init()
    clock = pygame.time.Clock()

    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    background = pygame.image.load('images/background-black.png').convert()
    background = pygame.transform.scale(background, (settings.screen_width, settings.screen_height))

    font = pygame.font.Font('ARCADECLASSIC.TTF', 35)

    player = Player(settings.screen_width/2 - settings.ship_width/2, settings.screen_height - 100)

    speed = settings.ship_speed 
    last_shot = pygame.time.get_ticks()
    last_enemies = pygame.time.get_ticks()
    last_power_up = pygame.time.get_ticks()
    i = 0 

    num_enemies = settings.num_enemies

    waves = []
    waves.append(Wave(num_enemies))
    lives = player.get_lives()
    lost = False
    lost_count = 0

    pygame.mixer.music.load('sounds/music.mp3')
    pygame.mixer.music.play(-1)
    running = True
    while running:  
    
        clock.tick(settings.fps)
        screen.fill((0,0,0))
        screen.blit(background,(0, -i))
        screen.blit(background,(0,-settings.screen_height - i))

        if (i == -settings.screen_height):
            screen.blit(background,(0,settings.screen_height + i))
            i=0
        i -= 1
    
        enemy_timer = pygame.time.get_ticks() - last_enemies 
        cooldowntime = pygame.time.get_ticks() - last_shot  
    
        if enemy_timer > 5000:
            if random.randint(0,10) == 1:
                num_enemies += 1 
                waves.append(Wave(num_enemies))
            else:
                waves.append(Wave(num_enemies))
                last_enemies = pygame.time.get_ticks()
     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)

        if keys[pygame.K_SPACE] and cooldowntime >  settings.cooldown_time:
            player.shoot()
            last_shot = pygame.time.get_ticks()

        player.move_lasers(screen)
        lasers = player.get_lasers()
    

        for wave in waves:
            wave.move(screen)
            wave.shoot()
            wave.move_lasers(screen)
            wave.check_events(player)
            player.damaged(wave)


        life_label = font.render(f'Lives  {player.get_lives()}', 1, (255,255,255))
        score_label = font.render(f'Score   {player.score}', 1, (255,255,255))

        player.blit_me(screen)

        game_over = font.render(f'Game Over', 1, (255,255,255))
        if player.get_lives() < 1:
            player.lives = 0 
            lost = True
            screen.blit(game_over, (settings.screen_width/2 - 75, 250))
            lost_count += 1 

        if lost:
            pygame.mixer.music.stop()
            if lost_count > settings.fps * 4:
                run_game()


        screen.blit(life_label, (25, settings.screen_height - 50))
        screen.blit(score_label, (settings.screen_width/2 - score_label.get_width()/2, 10))

        pygame.display.flip()
    pygame.quit()
 

if __name__ == '__main__':
    run_game()