from engine import Engine, Scene, WIDTH, HEIGHT
from scripts import *
from time import perf_counter
from random import randint

masks = {
    "Player": ["Asteroid", "Item"],
    "Asteroid": ["Player", "Projectile"],
    "Item": ["Player"],
    "Projectile": ["Asteroid"]
}

class Principal(Scene):
    def __init__(self, parent):
        super().__init__(parent)
        self.last = 0
        self.asteroid_cooldown = 1.5
        self.total = 0
    
    def create(self):
        self.createObject("Player", Player, "Player", WIDTH / 2, HEIGHT / 1.05, 20)
        self.createHudObject("Infos", Infos, 10, 10, 2)

    def update(self):
        if perf_counter() - self.last >= self.asteroid_cooldown:
            self.createObject(f"Asteroid{self.total}", Asteroid, "Asteroid", randint(40, WIDTH-40), 0, randint(10, 20))
            self.last = perf_counter()
            self.total += 1

_engine = Engine(masks, Principal)
_engine.run()