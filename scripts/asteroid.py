from engine.classes import Entity
from engine import pygame, WIDTH, HEIGHT, COLORS
from random import randint

class Asteroid(Entity):
    def __init__(self, mask: str, x: float, y: float, r: int):
        super().__init__(mask, x, y, r)
        self.asteroid_velocity = HEIGHT * ((r*0.02)/100)
    
    def update(self):
        self.y += self.asteroid_velocity

        if self.y > HEIGHT:
            self.destroy()
        
        collide = self.collision["Player"]
        if collide:
            collide.updateHealth(self.r)
            self.destroy()
        
        self.element = pygame.draw.circle(self.screen, COLORS["yellow"], (self.x, self.y), self.r)