class Collision:
    def __init__(self, mask):
        self.mask = mask
        self.colliding = []

    def __getitem__(self, __value):
        for object in self.colliding:
            if object.collision.mask == __value:
                return object
        return False

class Entity:
    def __init__(self, mask: str, x: float, y: float, r: int):
        self.x, self.y, self.r = x, y, r
        self.collision = Collision(mask)
    
    def getCollisionMask(self):
        return self.collision.mask
    
    def destroy(self):
        self.parent.deleteObject(self.id)
    
class Scene:
    def __init__(self, parent):
        self.parent = parent

    def createObject(self, id: str, object: Entity, mask: str, x: float, y: float, r: int = 0):
        self.parent.objects.createObject(id, object, mask, x, y, r)