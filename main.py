from engine import Engine
from scenes import Start

masks = {
    "Player": ["Asteroid", "Item"],
    "Asteroid": ["Player", "Projectile"],
    "Item": ["Player"],
    "Projectile": ["Asteroid"]
}

_engine = Engine(masks, Start)
_engine.run()