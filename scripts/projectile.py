from engine.classes import Entity
from engine import pygame, HEIGHT, COLORS

class Projectile(Entity):
    def __init__(self, mask: str, x: float, y: float, r: int):
        super().__init__(mask, x, y, r)
        self.projectile_velocity = HEIGHT * 0.02
        self.explosion_sound = pygame.mixer.Sound(f"Assets/Ship/ship_explosion.wav")
        self.explosion_sound.set_volume(0.3)
    
    def update(self):
        self.y -= self.projectile_velocity

        if self.y < 0:
            self.destroy()
        
        collide = self.collision["Asteroid"]
        if collide:
            self.explosion_sound.play(maxtime=800)
            if collide.r <= self.r:
                collide.hitDestroy()
                infos = self.parent.hud.objectExists("Infos")
                infos.score += self.r
            else:
                collide.r /= 2

            self.destroy()

        self.element = pygame.draw.circle(self.screen, COLORS["light-blue"], (self.x, self.y), self.r)