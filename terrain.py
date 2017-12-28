from numpy import *

class Terrain:

    def __init__(self):
        a = 30
        v0 = [-a, -a, -1]
        v1 = [-a, a, -1]
        v2 = [a, a, -1]
        v3 = [a, -a, -1]

        normal = [0, 0, 1]

        self.vertices = array([v0, v1, v2, v3])
        self.normals = array([normal, normal, normal, normal])
        self.indexes = array([0, 1, 2, 0, 2, 3])

        self.transformationMatrix = identity(4)
        self.rotationMatrix = identity(4)

        self.diffuse = [0, 0.5, 0]

    def update(self):
        pass
        


