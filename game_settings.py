import pygame


class Settings:

    def __init__(self):
        # Screen settings
        self.screen_width = 550 
        self.screen_height = 600
        self.screen_color = (0,0,0)
        
        self.fps = 80

        # Ship variables 
        self.num_lives = 5 
        self.ship_speed = 3     
        self.ship_width = 50 
        self.ship_height = 60 
        self.laser_speed = 5
        self.cooldown_time = 500

        # Alien settings
        self.num_enemies = 3
        self.x_alien_speed = 0.75
        self.y_alien_speed = 1.25
        self.alien_laser_speed = -2.5

        # Green enemy 
        self.green_width = 50 
        self.green_height = 60 

        self.laser_width = 40
        self.laser_height = 50

        self.power_up_speed = 1.5