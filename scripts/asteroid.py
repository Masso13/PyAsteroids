from engine.classes import Entity
from engine import pygame, HEIGHT, COLORS
from random import randint

class Asteroid(Entity):
    def __init__(self, mask: str, x: float, y: float, r: int):
        super().__init__(mask, x, y, r)
        self.asteroid_velocity = HEIGHT * ((r*0.02)/100)
        self.explosion_sound = pygame.mixer.Sound(f"Assets/Asteroid/asteroid_explosion{randint(1, 2)//1}.wav")
    
    def update(self):
        if not self.paused():
            self.y += self.asteroid_velocity

        infos = self.parent.hud.objectExists("Infos")
        if self.y > HEIGHT:
            if infos:
                infos.score -= self.r//2
            self.destroy()
        
        collide = self.collision["Player"]
        if collide:
            collide.updateHealth(self.r)
            if infos:
                infos.score -= self.r

            self.hitDestroy()
        
        self.element = pygame.draw.circle(self.screen, COLORS["yellow"], (self.x, self.y), self.r)
    
    def hitDestroy(self):
        self.explosion_sound.play(maxtime=800)
        self.destroy()