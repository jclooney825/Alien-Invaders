import pygame 
from ship import Ship
from laser import Laser
from game_settings import Settings

settings = Settings()

class Player(Ship):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.ship_image = pygame.image.load('images/player.png').convert_alpha()
        self.ship_image = pygame.transform.scale(self.ship_image, (settings.ship_width, settings.ship_height))
        
        self.laser_image = pygame.image.load('images/pixel_laser_red.png')

        self.rect = self.ship_image.get_rect()
        self.rect.centerx =  self.x
        self.rect.centery =  self.y 

        self.player_mask = pygame.mask.from_surface(self.ship_image)

        self.speed = settings.ship_speed 
        self.laser_image = 'images/pixel_laser_red.png'
        self.laser_speed = 7

        self.lives = settings.num_lives 
        self.score = 0 
    # Move the player
    def move(self, keys):
        if self.lives > 0:
            if keys[pygame.K_a] and self.x > 0:
                self.x -= self.speed
            if keys[pygame.K_d] and self.x < (settings.screen_width - settings.ship_width):
                self.x += self.speed
            if keys[pygame.K_w] and self.y > 0:
                self.y -= self.speed
            if keys[pygame.K_s] and self.y < (settings.screen_height - settings.ship_height):
                self.y += self.speed
        
            self.rect.centerx = self.x
            self.rect.centery = self.y

    # Add laser to the laser list 
    def shoot(self):
        if self.lives > 0:
            laser = Laser(self.x + 5, self.y, self.laser_image)
            self.lasers.append(laser)
            shoot_sound = pygame.mixer.Sound('sounds/shoot.wav')
            pygame.mixer.Sound.play(shoot_sound)

    def damaged(self, wave):
        aliens = wave.get_enemies()
        for alien in aliens[:]:
            lasers = alien.get_lasers()
            for laser in lasers:
                laser_rect = laser.laser_rect
                if laser_rect.colliderect(self.rect):
                    lasers.remove(laser)
                    if self.lives == 0:
                        break
                    else:
                        self.lives -= 1 
                    explosion = pygame.mixer.Sound('sounds/explosion.wav')
                    pygame.mixer.Sound.play(explosion)

    def remove_life(self):
        self.lives -= 1 
    
    def get_lives(self):
        return self.lives
