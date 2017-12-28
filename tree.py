from numpy import *

class Tree:

    def __init__(self):
        r = 0.3
        v0 = [-3*r, -3*r, -1]
        v1 = [-3*r, 3*r, -1]
        v2 = [3*r, 3*r, -1]
        v3 = [3*r, -3*r, -1]

        v4 = [-r, -r, 4]
        v5 = [-r, r, 4]
        v6 = [r, r, 4]
        v7 = [r, -r, 4]

        nBottom = [0, 0, -1]
        nTop = [0, 0, 1]
        nLeft = [0, -1, 0]
        nRight = [0, 1, 0]
        nFront = [1, 0, 0]
        nBack = [-1, 0, 0]

        self.vertices = array([])
        self.normals = array([])
        self.indexes = array([])

        self._addWall(v0, v1, v2, v3, nBottom)
        self._addWall(v4, v5, v6, v7, nTop)
        self._addWall(v0, v3, v7, v4, nLeft)
        self._addWall(v1, v2, v6, v5, nRight)
        self._addWall(v0, v1, v5, v4, nBack)
        self._addWall(v3, v2, v6, v7, nFront)

        self.transformationMatrix = identity(4)
        self.rotationMatrix = identity(4)

        self.diffuse = [0, 1, 1]

    def _addWall(self, v0, v1, v2, v3, normal):
        start = self.vertices.size/3
        self.vertices = append(self.vertices, [v0, v1, v2, v3])
        self.normals = append(self.normals, [normal, normal, normal, normal])
        self.indexes = append(self.indexes, [start, start+1, start+2, start, start+2, start+3])

    def update(self):
        pass
        


