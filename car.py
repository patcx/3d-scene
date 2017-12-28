from numpy import *

class Car:

    def __init__(self):
        v0 = [-1, -1, -1]
        v1 = [-1, 1, -1]
        v2 = [1, 1, -1]
        v3 = [1, -1, -1]

        v4 = [-1, -1, 1]
        v5 = [-1, 1, 1]
        v6 = [1, 1, 1]
        v7 = [1, -1, 1]

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

        self.angle = 0
        self.diffuse = [1, 0, 0]

    def _addWall(self, v0, v1, v2, v3, normal):
        start = self.vertices.size/3
        self.vertices = append(self.vertices, [v0, v1, v2, v3])
        self.normals = append(self.normals, [normal, normal, normal, normal])
        self.indexes = append(self.indexes, [start, start+1, start+2, start, start+2, start+3])

    def update(self):
        self.angle += 0.01
        self.angle %= 2*pi
        angleCos = cos(self.angle)
        angleSin = sin(self.angle)

        self.rotationMatrix = matrix([
            [angleCos, -angleSin, 0, 0],
            [angleSin, angleCos, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            ])

        radius = 8
        self.transformationMatrix = matrix([
            [1, 0, 0, radius*angleCos],
            [0, 1, 0, radius*angleSin],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            ])
            
    def getX(self):
        return self.transformationMatrix[0, 3]

    def getY(self):
        return self.transformationMatrix[1, 3]
        


