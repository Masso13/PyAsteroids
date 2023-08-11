import pygame
from pygame.locals import QUIT
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
        self.scene.create()
    
    def run(self):
        self.resetEngine()
        while True:
            self.clock.tick(FPS)
            self.screen.fill(COLORS["black"])

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
            
            self.objects.update()
            self.collisions.update()
            self.hud.update()
            self.scene.update()

            pygame.display.flip()