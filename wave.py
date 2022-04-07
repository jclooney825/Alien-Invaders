import random
import pygame
from alien import Alien
from laser import Laser
from game_settings import Settings


'''
Wave class

'''
settings = Settings()

class Wave:

    def __init__(self, num_enemies):
        self.num_enemies = num_enemies
        colors = ['green', 'blue', 'purple']
        
        self.enemies = []
        for i in range(self.num_enemies):
            x = random.randint(41, settings.screen_width - 60)
            y = -random.randint(0, settings.screen_height)
            self.enemies.append(Alien(x,y, random.choice(colors)))

    def move(self, screen):
        for enemy in self.enemies:
            enemy.blit_me(screen)
            enemy.move()
    
    def shoot(self):
        for enemy in self.enemies:
            enemy.shoot()

    def move_lasers(self, screen):
        for enemy in self.enemies:
            enemy.move_lasers(screen)

    def check_events(self, player):
        player_lasers = player.get_lasers()
        for enemy in self.enemies[:]:
            if enemy.hit(player_lasers): 
                self.enemies.remove(enemy)
                player.score += 5
                destroyed = pygame.mixer.Sound('sounds/invaderkilled.wav')
                pygame.mixer.Sound.play(destroyed)

            elif enemy.y > settings.screen_height:
                self.enemies.remove(enemy)
                if player.lives > 0:
                    player.remove_life()

    def get_enemies(self):
       return self.enemies