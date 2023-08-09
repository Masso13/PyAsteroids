from engine.classes import Entity
from engine import pygame, WIDTH, HEIGHT, COLORS
from pygame.locals import K_a, K_d, K_SPACE
from engine.utils import makeTriangle
from scripts.projectile import Projectile
from time import perf_counter

class Player(Entity):
    def __init__(self, mask: str, x: float, y: float, r: int):
        super().__init__(mask, x, y, r)
        self.player_velocity = WIDTH * 0.01
        self.shoot_cooldown = 0.3
        self.total = 0
        self.last = 0
    
    def shoot(self):
        self.parent.createObject(f"Projectile{self.total}", Projectile, "Projectile", self.x, self.y, 5)
        self.total += 1
    
    def update(self):
        dir_x = 0
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            dir_x = -1
        if keys[K_d]:
            dir_x = 1
        if keys[K_SPACE] and perf_counter() - self.last >= self.shoot_cooldown:
            self.shoot()
            self.last = perf_counter()

        self.x += self.player_velocity * dir_x
        self.x = max(self.r, min(self.x, WIDTH - self.r))

        self.trian = pygame.draw.polygon(self.screen, COLORS["blue"], makeTriangle(self.x, self.y, self.r))