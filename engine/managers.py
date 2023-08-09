from engine.classes import Entity

class CollisionManager:
    def __init__(self, masks, objects):
        self.masks = masks
        self.objects = objects
    
    def collidingWith(self, object: Entity, _object: Entity):
        return _object.getCollisionMask() in self.masks[object.getCollisionMask()] and object.element.colliderect(_object.element)
    
    def getCollisions(self, object):
        collisions = []
        for _object in self.objects:
            if _object != object and self.collidingWith(object, _object):
                collisions.append(_object)
        return collisions
    
    def update(self):
        for object in self.objects:
            if object.collision.mask in self.masks:
                object.collision.colliding = self.getCollisions(object)

class ObjectManager:
    def __init__(self, screen):
        self.objects = []
        self.screen = screen

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
                return True
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

    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        if self.i < len(self.objects):
            object = self.objects[self.i]
            self.i += 1
            return object
        else:
            raise StopIteration