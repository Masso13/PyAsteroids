import pygame
from pygame.locals import QUIT, KEYDOWN, K_p, K_r
from engine.constants import WIDTH, HEIGHT, FPS, COLORS
from engine.managers import CollisionManager, ObjectManager, HudManager
from engine.classes import Scene

class Engine:
    def __init__(self, masks, scene: Scene):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.hud = HudManager(self.screen)
        self.objects = ObjectManager(self.screen, self.hud)
        self.collisions = CollisionManager(masks, self.objects)
        self.scene = scene(self)
    
    def resetEngine(self):
        self.objects.deleteAllObjects()
        self.hud.deleteAllObjects()
        self.scene.create()
        self.objects.paused = self.scene.paused
    
    def changeScene(self, scene):
        self.scene = scene(self)
        self.resetEngine()
    
    def pauseScene(self, key=True):
        if key:
            self.scene.pause()
        self.objects.paused = self.scene.paused
        if not self.scene.paused:
            self.hud.deleteObject("Paused")
    
    def run(self):
        self.resetEngine()
        while True:
            self.clock.tick(FPS)
            self.screen.fill(COLORS["black"])

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_p:
                        self.pauseScene()
                    elif event.key == K_r and self.scene.paused:
                        self.resetEngine()
            
            self.objects.update()
            self.collisions.update()
            self.hud.update()
            self.scene.update()
            
            pygame.display.flip()