from engine import Engine, Scene, WIDTH, HEIGHT
from scripts import *

masks = {
    "Player": ["Asteroid", "Item"],
    "Asteroid": ["Player", "Projectile"],
    "Item": ["Player"],
    "Projectile": ["Asteroid"]
}

class Principal(Scene):
    def __init__(self, parent):
        super().__init__(parent)
    
    def create(self):
        self.createObject("Player", Player, "Player", WIDTH / 2, HEIGHT / 1.05, 20)

_engine = Engine(masks, Principal)
_engine.run()