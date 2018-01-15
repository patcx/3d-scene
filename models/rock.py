from numpy import *
from math import * 
from models.model import *

class Rock(Model):

    def __init__(self, s, x, y):
        
        self.transformationMatrix = matrix([
            [s, 0, 0, x],
            [0, s, 0, y],
            [0, 0, s, 0],
            [0, 0, 0, 1],
            ])

        t = (1.0 + sqrt(5.0)) / 2.0

        v0 = [-1,  t,  0]
        v1 = [ 1,  t,  0]
        v2 = [-1, -t,  0]
        v3 = [ 1, -t,  0]

        v4 = [ 0, -1,  t]
        v5 = [ 0,  1,  t]
        v6 = [ 0, -1, -t]
        v7 = [ 0,  1, -t]

        v8 = [ t,  0, -1]
        v9 = [ t,  0,  1]
        v10 = [-t,  0, -1]
        v11 = [-t,  0,  1]
        
        color = [0.5, 0.5, 0.5]

        self.addTriangleWithNormal(v0, v5, v11, color)       
        self.addTriangleWithNormal(v0, v1, v5, color)       
        self.addTriangleWithNormal(v5, v4, v11, color)       
        self.addTriangleWithNormal(v4, v5, v9, color)       
        self.addTriangleWithNormal(v2, v11, v4, color)       
        self.addTriangleWithNormal(v10, v11, v2, color)       
        self.addTriangleWithNormal(v10, v0, v11, color)       
        self.addTriangleWithNormal(v7, v0, v10, color)       
        self.addTriangleWithNormal(v7, v1, v0, color)       
        self.addTriangleWithNormal(v10, v6, v2, color)
        self.addTriangleWithNormal(v2, v3, v6, color)       
        self.addTriangleWithNormal(v2, v4, v3, color)       
        self.addTriangleWithNormal(v3, v9, v8, color)       
        self.addTriangleWithNormal(v3, v4, v9, color)       
        self.addTriangleWithNormal(v8, v6, v3, color)       
        self.addTriangleWithNormal(v6, v8, v7, color)       
        self.addTriangleWithNormal(v8, v9, v1, color)       
        self.addTriangleWithNormal(v1, v8, v7, color)            
        self.addTriangleWithNormal(v7, v10, v6, color)       
        self.addTriangleWithNormal(v5, v1, v9, color)       

    def addTriangleWithNormal(self, v0, v1, v2, color):
        self._addTriangle(v0, v1, v2, _getNormal(v0,v1,v2), color)

def _getNormal(v0, v1, v2):
    normal = cross(array(v1)-array(v0), array(v2)-array(v0))
    normal = -normal/linalg.norm(normal)
    return normal
