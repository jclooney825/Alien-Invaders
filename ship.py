import pygame 

class Ship:
    
    def __init__(self, x, y, health = 100):
     
        self.x = x 
        self.y = y 
        self.health = health
        self.ship_image = None
        self.laser_image = None
        self.lasers = [] 
        self.cooldown = 0


    def blit_me(self, screen):
        screen.blit(self.ship_image, (self.x,self.y)) 

    def move_lasers(self, screen):
        lasers = self.get_lasers()
        for laser in lasers[:]:
            laser.blit_me(screen)
            laser.move(self.laser_speed)
            if laser.y < -laser.get_height():
                lasers.remove(laser)
            
    def get_position(self):
        return (self.x, self.y)
    
    def get_lasers(self):
        return self.lasers

    def get_health(self):
        return self.health 
    
