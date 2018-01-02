from numpy import *
from models.model import *
from light import *
from math import *

class Lantern(Model):

    def __init__(self, h, x, y, dir):
        
        self._setPosition(x, y, 0)
        angle = atan2(dir[1], dir[0])
        self._setRotation(angle)

        r = 0.1
        nBottom = [0, 0, -1]
        nTop = [0, 0, 1]
        nLeft = [0, -1, 0]
        nRight = [0, 1, 0]
        nFront = [1, 0, 0]
        nBack = [-1, 0, 0]


        v0 = [-r, -r, -1]
        v1 = [-r, r, -1]
        v2 = [r, r, -1]
        v3 = [r, -r, -1]

        v4 = [-r, -r, h]
        v5 = [-r, r, h]
        v6 = [r, r, h]
        v7 = [r, -r, h]

        v8 = [-r+1, -r, h+0.4]
        v9 = [-r+1, r, h+0.4]
        v10 = [r+1, r, h+0.4]
        v11 = [r+1, -r, h+0.4]


        
        color = [0.7, 0.7, 0.7]
        self._addQuad(v0, v1, v2, v3, nBottom, color)
        self._addQuad(v4, v5, v6, v7, nTop, color)
        self._addQuad(v0, v3, v7, v4, nLeft, color)
        self._addQuad(v1, v2, v6, v5, nRight, color)
        self._addQuad(v0, v1, v5, v4, nBack, color)
        self._addQuad(v3, v2, v6, v7, nFront, color)

        self._addQuad(v4, v5, v6, v7, nBottom, color)
        self._addQuad(v8, v9, v10, v11, nTop, color)
        self._addQuad(v4, v7, v11, v8, nLeft, color)
        self._addQuad(v5, v6, v10, v9, nRight, color)
        self._addQuad(v4, v5, v9, v8, nBack, color)
        self._addQuad(v7, v6, v10, v11, nFront, color)


        self.light = LightSource()
        self.light.setPosition([x, y, h])
        self.light.setDirection(dir)
        self.light.spotCutOff = 0.8
        self.light.intensity = 0.7


    def getLight(self):
        return self.light

