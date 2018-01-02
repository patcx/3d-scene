from numpy import *
from models.model import *

class Tree(Model):

    def __init__(self, h, x, y):
        
        self._setPosition(x, y, 0)

        r = 0.3
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

        
        brown = [0.33, 0.1, 0.1]
        self._addQuad(v0, v1, v2, v3, nBottom, brown)
        self._addQuad(v4, v5, v6, v7, nTop, brown)
        self._addQuad(v0, v3, v7, v4, nLeft, brown)
        self._addQuad(v1, v2, v6, v5, nRight, brown)
        self._addQuad(v0, v1, v5, v4, nBack, brown)
        self._addQuad(v3, v2, v6, v7, nFront, brown)

        f = 4
        green = [0.24, 0.53, 0.24]

        v8 = [-r*f, -r*f, h]
        v9 = [-r*f, r*f, h]
        v10 = [r*f, r*f, h]
        v11 = [r*f, -r*f, h]

        v12 = [0, 0, 3*h]

        self._addQuad(v8, v9, v10, v11, nBottom, green)
        self._addTriangle(v8, v9, v12, _getNormal(v8, v9, v12), green)
        self._addTriangle(v9, v10, v12, _getNormal(v9, v10, v12), green)
        self._addTriangle(v10, v11, v12, _getNormal(v10, v11, v12), green)
        self._addTriangle(v11, v8, v12, _getNormal(v11, v8, v12), green)

def _getNormal(v0, v1, v2):
    normal = cross(array(v1)-array(v0), array(v2)-array(v0))
    normal = -normal/linalg.norm(normal)
    return normal
