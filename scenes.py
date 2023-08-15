from engine import Scene, WIDTH, HEIGHT, pygame
from scripts import *
from time import perf_counter
from random import randint
from pygame.locals import K_RETURN

class Main(Scene):
    def __init__(self, parent):
        super().__init__(parent)
        self.last = 0
        self.total = 0
        self.hud_sound = pygame.mixer.Sound("Assets/Hud/switch.wav")
        self.hud_sound.set_volume(0.6)
    
    def create(self):
        self.createObject("Player", Player, "Player", WIDTH / 2, HEIGHT / 1.05, 20)
        self.createHudObject("Infos", Infos, 10, 10, 2)
        self.paused = False
        self.asteroid_cooldown = 1.7

    def update(self):
        if not self.paused:
            self.drawAsteroids()

            player = self.parent.objects.objectExists("Player")
            if player.health <= 0:
                player.destroy()
                self.gameOver()
            
    def pause(self):
        self.paused = not self.paused
        self.hud_sound.play()
        if self.paused:
            self.createHudObject("Paused", PausedMenu, 0, 0, 1)
    
    def gameOver(self):
        self.paused = not self.paused
        self.parent.pauseScene(key=False)
        if self.paused:
            self.createHudObject("Paused", GameOverMenu, 0, 0, 1)

    def drawAsteroids(self):
        if perf_counter() - self.last >= self.asteroid_cooldown:
            self.createObject(f"Asteroid{self.total}", Asteroid, "Asteroid", randint(40, WIDTH-40), 0, randint(10, 20))
            self.last = perf_counter()
            self.total += 1
            self.asteroid_cooldown -= 0.01 if self.total % 2 == 0 else 0

class Start(Scene):
    def __init__(self, parent):
        super().__init__(parent)
        self.asteroid_cooldown = 1.0
        self.total = 0
        self.last = 0
        self.paused = False
        self.hud_sound = pygame.mixer.Sound("Assets/Hud/switch.wav")
        self.hud_sound.set_volume(0.6)
    
    def create(self):
        self.createHudObject("Menu", StartMenu, 0, 0, 1)
    
    def update(self):
        self.drawAsteroids()
        keys = pygame.key.get_pressed()
        if keys[K_RETURN]:
            self.hud_sound.play()
            self.parent.changeScene(Main)
    
    def drawAsteroids(self):
        if perf_counter() - self.last >= self.asteroid_cooldown:
            self.createObject(f"Asteroid{self.total}", Asteroid, "Asteroid", randint(40, WIDTH-40), 0, randint(10, 20))
            self.last = perf_counter()
            self.total += 1