from engine.classes import Hud
from engine import pygame, WIDTH, COLORS
from engine.fonts import ARIAL

class Infos(Hud):
    def __init__(self, x: float, y: float, z_index: int):
        super().__init__(x, y, z_index)
        self.score = 0
        self.health = 100
        self.energy = 100
    
    def update(self):
        self.score = round(max(0, self.score))

        self.drawHealth(80, 15, 5)
        self.drawEnergy(80, 15, 5)
        self.drawScore((WIDTH-40, 10))

    def drawHealth(self, w, h, p):
        percent = self.health / 100
        _w = w*percent

        background_size = (self.x, self.y, w, h)
        health_size = (self.x + (p/2), self.y + (p/2), _w-p, h-p)

        pygame.draw.rect(self.screen, COLORS["gray"], background_size)
        pygame.draw.rect(self.screen, COLORS["red"], health_size)
    
    def drawEnergy(self, w, h, p):
        percent = self.energy / 100
        _w = w*percent
        x, y = self.x + w + p*2, self.y
        background_size = (x, y, w, h)
        energy_size = (x + (p/2), y + (p/2), _w-p, h-p)

        pygame.draw.rect(self.screen, COLORS["gray"], background_size)
        pygame.draw.rect(self.screen, COLORS["light-blue"], energy_size)
    
    def drawScore(self, position):
        score_label = ARIAL.render(f"{self.score}", True, COLORS["white"])
        self.screen.blit(score_label, position)