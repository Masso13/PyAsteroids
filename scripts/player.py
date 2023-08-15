from engine.classes import Entity
from engine import pygame, WIDTH, COLORS
from pygame.locals import K_a, K_d, K_SPACE
from engine.utils import makeTriangle
from scripts.projectile import Projectile
from time import perf_counter
from random import randint

class Player(Entity):
    def __init__(self, mask: str, x: float, y: float, r: int):
        super().__init__(mask, x, y, r)
        self.player_velocity = WIDTH * 0.01
        self.shoot_cooldown = 0.2
        self.reload_cooldown = 0.2
        self.health = 100
        self.total = 0
        self.last_shoot = 0
        self.last_reload = 0
        self.energy = 100
        self.shoot_sound = pygame.mixer.Sound("Assets/Ship/shoot.wav")
        self.shoot_sound.set_volume(0.8)
    
    def shoot(self):
        r = randint(5, 10)
        if self.energy >= r:
            self.energy -= r
            self.shoot_sound.play(maxtime=835)
            self.parent.createObject(f"Projectile{self.total}", Projectile, "Projectile", self.x, self.y, r)
            self.total += 1
    
    def update(self):
        dir_x = 0
        if not self.paused():
            keys = pygame.key.get_pressed()
            if keys[K_a]:
                dir_x = -1
            if keys[K_d]:
                dir_x = 1
            if keys[K_SPACE] and perf_counter() - self.last_shoot >= self.shoot_cooldown:
                self.shoot()
                self.last_shoot = perf_counter()

        self.x += self.player_velocity * dir_x
        self.x = max(self.r, min(self.x, WIDTH - self.r))

        if self.energy < 100 and perf_counter() - self.last_reload >= self.reload_cooldown and not self.paused():
            self.energy += 5
            self.last_reload = perf_counter()
            infos = self.parent.hud.objectExists("Infos")
            infos.energy = self.energy
        
        self.energy = max(0, min(self.energy, 100))

        self.element = pygame.draw.polygon(self.screen, COLORS["blue"], makeTriangle(self.x, self.y, self.r))
    
    def updateHealth(self, damage):
        self.health -= damage
        self.health = max(0, self.health)

        infos = self.parent.hud.objectExists("Infos")
        infos.health = self.health