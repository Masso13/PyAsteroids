from engine.classes import Entity, Hud

class CollisionManager:
    def __init__(self, masks, objectManager):
        self.masks = masks
        self.objectManager = objectManager
    
    def collidingWith(self, object: Entity, _object: Entity):
        try:
            return _object.getCollisionMask() in self.masks[object.getCollisionMask()] and object.element.colliderect(_object.element)
        except AttributeError:
            return False

    def getCollisions(self, object):
        collisions = []
        for _object in self.objectManager.objects:
            if _object != object and self.collidingWith(object, _object):
                collisions.append(_object)
        return collisions
    
    def update(self):
        for object in self.objectManager.objects:
            if object.collision.mask in self.masks:
                object.collision.colliding = self.getCollisions(object)

class ObjectManager:
    def __init__(self, screen, hud):
        self.objects = []
        self.screen = screen
        self.hud = hud
        self.paused = False

    def createObject(self, id: str, object: Entity, mask: str, x: float, y: float, r: int = 0):
        if not self.objectExists(id):
            _object = object(mask, x, y, r)
            _object.id = id
            _object.screen = self.screen
            _object.parent = self
            self.objects.append(_object)
        else:
            raise "This object has already been instantiated"

    def objectExists(self, id):
        for object in self.objects:
            if object.id == id:
                return object
        return False
    
    def update(self):
        for object in self.objects:
            object.update()
    
    def deleteAllObjects(self):
        del self.objects
        self.objects = []
    
    def deleteObject(self, id):
        if self.objectExists(id):
            for i, object in enumerate(self.objects):
                if object.id == id:
                    self.objects.pop(i)
                    return True
        else:
            raise "This object has not been instantiated"
    
    def getTotalObjectsByMask(self, mask):
        total = 0
        for object in self.objects:
            if object.collision.mask == mask:
                total += 1
        return total

    def getTotalObjects(self):
        return len(self.objects)

class HudManager:
    def __init__(self, screen):
        self.objects = []
        self.screen = screen
    
    def update(self):
        for object in self.objects:
            object.update()

    def sort(self):
        _objects = self.objects.copy()
        self.objects = []
        while len(_objects) > 0:
            object = max(_objects, key=lambda o: o.z_index)
            self.objects.append(object)
            _objects.pop(_objects.index(object))
    
    def createObject(self, id: str, object: Hud, x: float, y: float, z_index: int):
        if not self.objectExists(id):
            _object = object(x, y, z_index)
            _object.id = id
            _object.screen = self.screen
            _object.parent = self
            self.objects.append(_object)
            self.sort()
        else:
            raise "This object has already been instantiated"

    def objectExists(self, id):
        for object in self.objects:
            if object.id == id:
                return object
        return False
    
    def deleteAllObjects(self):
        del self.objects
        self.objects = []
    
    def deleteObject(self, id):
        if self.objectExists(id):
            for i, object in enumerate(self.objects):
                if object.id == id:
                    self.objects.pop(i)
                    return True
        else:
            raise "This object has not been instantiated"