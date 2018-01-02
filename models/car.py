from numpy import *
from models.model import *
from light import *

class Car(Model):

    def __init__(self):

        self.light = CarLightSource()
        self.light.setPosition([3, 0, 0, 1])
        self.light.setDirection([1, 0, -2, 1])

        self.beaconLight = CarBeaconLightSource()
        self.beaconLight.setPosition([0, 0, 1, 1])

        v0 = [-2, -1, -0.5]
        v1 = [-2, 1, -0.5]
        v2 = [3, 1, -0.5]
        v3 = [3, -1, -0.5]

        v4 = [-2, -1, 0.3]
        v5 = [-2, 1, 0.3]
        v6 = [3, 1, 0.3]
        v7 = [3, -1, 0.3]

        v8 = [-2, -1, 0.3]
        v9 = [-2, 1, 0.3]
        v10 = [1.4, 1, 0.3]
        v11 = [1.4, -1, 0.3]

        v12 = [-1.5, -0.8, 1]
        v13 = [-1.5, 0.8, 1]
        v14 = [0.5, 0.8, 1]
        v15 = [0.5, -0.8, 1]

        nBottom = [0, 0, -1]
        nTop = [0, 0, 1]
        nLeft = [0, -1, 0]
        nRight = [0, 1, 0]
        nFront = [1, 0, 0]
        nBack = [-1, 0, 0]

        self._addQuad(v0, v1, v2, v3, nBottom, [0.6, 0, 0])
        self._addQuad(v4, v5, v6, v7, nTop, [0.6, 0, 0])
        self._addQuad(v0, v3, v7, v4, nLeft, [0.6, 0, 0])
        self._addQuad(v1, v2, v6, v5, nRight, [0.6, 0, 0])
        self._addQuad(v0, v1, v5, v4, nBack, [0.6, 0, 0])
        self._addQuad(v3, v2, v6, v7, nFront, [0.6, 0, 0])

        self._addQuad(v12, v13, v14, v15, nTop, [0.6, 0, 0])
        self._addQuad(v8, v11, v15, v12, -self._getNormal(v8, v11, v15), [0.3, 0.3, 0.3])
        self._addQuad(v9, v10, v14, v13, self._getNormal(v9,v10, v14), [0.3, 0.3, 0.3])
        self._addQuad(v8, v9, v13, v12, self._getNormal(v8,v9, v13), [0.2, 0.2, 0.2])
        self._addQuad(v11, v10, v14, v15, -self._getNormal(v11, v10, v14), [0.3, 0.3, 0.3])

        wheelColor = [0.1, 0.1, 0.1]
        wheelR =  [0.4,  0.2, 0.4]
        self._addCube([2, 1, -0.4], wheelR, wheelColor)
        self._addCube([-1.2, 1, -0.4], wheelR, wheelColor)
        self._addCube([2, -1, -0.4], wheelR, wheelColor)
        self._addCube([-1.2, -1, -0.4], wheelR, wheelColor)

        lightsColor = [0.8, 0.8, 0.8]
        self._addCube([3, -0.7, 0], [0.02, 0.2, 0.1], lightsColor)
        self._addCube([3, 0.7, 0], [0.02, 0.2, 0.1], lightsColor)
        
        self._addCube([0, 0, 1], [0.2, 0.7, 0.2], lightsColor)
        

        self.angle = 0

    def _addCube(self, v, r, color):

        v0 = [v[0]-r[0], v[1]-r[1], v[2]-r[2]]
        v1 = [v[0]-r[0], v[1]+r[1], v[2]-r[2]]
        v2 = [v[0]+r[0], v[1]+r[1], v[2]-r[2]]
        v3 = [v[0]+r[0], v[1]-r[1], v[2]-r[2]]

        v4 = [v[0]-r[0], v[1]-r[1], v[2]+r[2]]
        v5 = [v[0]-r[0], v[1]+r[1], v[2]+r[2]]
        v6 = [v[0]+r[0], v[1]+r[1], v[2]+r[2]]
        v7 = [v[0]+r[0], v[1]-r[1], v[2]+r[2]]

        nBottom = [0, 0, -1]
        nTop = [0, 0, 1]
        nLeft = [0, -1, 0]
        nRight = [0, 1, 0]
        nFront = [1, 0, 0]
        nBack = [-1, 0, 0]

        self._addQuad(v0, v1, v2, v3, nBottom, color)
        self._addQuad(v4, v5, v6, v7, nTop, color)
        self._addQuad(v0, v3, v7, v4, nLeft, color)
        self._addQuad(v1, v2, v6, v5, nRight, color)
        self._addQuad(v0, v1, v5, v4, nBack, color)
        self._addQuad(v3, v2, v6, v7, nFront, color)

    def _getNormal(self, v0, v1, v2):
        normal = cross(array(v1)-array(v0), array(v2)-array(v0))
        normal = -normal/linalg.norm(normal)
        return normal

    def getLight(self):
        return self.light

    def getBeaconLight(self):
        return self.beaconLight


    def update(self):
        self.angle += 0.03
        self.angle %= 2*pi

        self._setRotation(pi/2 + self.angle)

        radius = 8
        self._setPosition(radius*cos(self.angle), radius*sin(self.angle), 0)

        self.light.update(self)
        self.beaconLight.update(self)
            
        


