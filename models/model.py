from numpy import *

class Model:

    vertices = array([])
    normals = array([])
    indexes = array([])
    diffuse = array([])

    transformationMatrix = identity(4)
    rotationMatrix = identity(4)

    def _setPosition(self, x, y, z):

        self.transformationMatrix = matrix([
            [1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1],
            ])

    def _setRotation(self, angle):
        
        angleCos = cos(angle)
        angleSin = sin(angle)

        self.rotationMatrix = matrix([
            [angleCos, -angleSin, 0, 0],
            [angleSin, angleCos, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            ])

    def _addQuad(self, v0, v1, v2, v3, normal, diffuse):
        start = self.vertices.size/3
        self.vertices = append(self.vertices, [v0, v1, v2, v3])
        self.normals = append(self.normals, [normal, normal, normal, normal])
        self.diffuse = append(self.diffuse, [diffuse, diffuse, diffuse, diffuse])
        self.indexes = append(self.indexes, [start, start+1, start+2, start, start+2, start+3])
    
    def _addTriangle(self, v0, v1, v2, normal, diffuse):
        start = self.vertices.size/3

        self.vertices = append(self.vertices, [v0, v1, v2])
        self.normals = append(self.normals, [normal, normal, normal])
        self.diffuse = append(self.diffuse, [diffuse, diffuse, diffuse])
        self.indexes = append(self.indexes, [start, start+1, start+2])

    def getX(self):
        return self.transformationMatrix[0, 3]

    def getY(self):
        return self.transformationMatrix[1, 3]

    def getZ(self):
        return self.transformationMatrix[2, 3]

    def update(self):
        pass