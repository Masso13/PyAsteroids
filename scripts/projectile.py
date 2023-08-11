from engine.classes import Entity
from engine import pygame, WIDTH, HEIGHT, COLORS

class Projectile(Entity):
    def __init__(self, mask: str, x: float, y: float, r: int):
        super().__init__(mask, x, y, r)
        self.projectile_velocity = HEIGHT * 0.02
    
    def update(self):
        self.y -= self.projectile_velocity

        if self.y < 0:
            self.destroy()
        
        collide = self.collision["Asteroid"]
        if collide:
            if collide.r <= self.r:
                collide.destroy()
            else:
                collide.r /= 2

            self.destroy()

        self.element = pygame.draw.circle(self.screen, COLORS["light-blue"], (self.x, self.y), self.r)