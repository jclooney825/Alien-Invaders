import pygame 
from game_settings import Settings

settings = Settings()

class Laser():

    def __init__(self, x, y, laser_image):
         
        self.x = x
        self.y = y 
        self.laser_image = pygame.image.load(laser_image).convert_alpha()
        self.laser_image = pygame.transform.scale(self.laser_image, (40,50))
        
        self.laser_rect = self.laser_image.get_rect()
        self.laser_rect.centerx =  self.x
        self.laser_rect.centery =  self.y 

    def blit_me(self, screen):
        screen.blit(self.laser_image, (self.x,self.y)) 

    def move(self, laser_speed):
        self.y -= laser_speed
        self.laser_rect.centery = self.y
    
    def get_width(self):
        return settings.laser_width
    
    def get_height(self):
        return settings.laser_height

