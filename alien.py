import pygame 
from ship import Ship
from laser import Laser
from game_settings import Settings
import random 

settings = Settings()

class Alien(Ship):
    
    def __init__(self, x, y, color):
        super().__init__(x, y, health = 100)

        self.ship_types = {
                            "green":  ['images/green_enemy.png', 'images/pixel_laser_green.png'],
                            "blue": ['images/blue_enemy.png', 'images/pixel_laser_blue.png'],
                            "purple": ['images/purple_enemy.png', 'images/pixel_laser_purple.png']
                        }
        
        self.ship_image, self.laser_image = self.ship_types[color]
        self.ship_image = pygame.image.load(self.ship_image).convert_alpha()
        self.ship_image = pygame.transform.scale(self.ship_image, (40, 30))
       
        self.rect = self.ship_image.get_rect()
        self.rect.centerx =  self.x
        self.rect.centery =  self.y 

        self.x_speed = random.randrange(-1,1, 2) * settings.x_alien_speed
        self.y_speed = settings.y_alien_speed

    def blit_me(self, screen):
        screen.blit(self.ship_image, (self.x,self.y)) 

    def move(self):
        if self.x > settings.screen_width - 40:
            self.x_speed *= -1 
            self.x += self.x_speed 
            self.rect.centerx = self.x
        elif self.x < 40:
            self.x_speed *= -1
            self.x += self.x_speed
            self.rect.centerx = self.x  
        else:
            self.x += self.x_speed 
            self.rect.centerx = self.x
        self.y += self.y_speed 
        self.rect.centery = self.y

    def hit(self, player_lasers):
        for laser in player_lasers[:]: 
            if laser.laser_rect.colliderect(self.rect):
                player_lasers.remove(laser)
                return True
            else:
                return False

    def shoot(self):
        if self.y > 0:
            if random.randint(0, 2*settings.fps) == 1:
                self.lasers.append(Laser(self.x, self.y, self.laser_image))
    
    def move_lasers(self, screen):
        for laser in self.lasers[:]:
            laser.blit_me(screen)
            laser.move(settings.alien_laser_speed)
            if laser.y > settings.screen_height:
                self.lasers.remove(laser)
        