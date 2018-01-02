from numpy import *
from models.model import *

class Terrain(Model):

    def __init__(self, a):
        v0 = [-a, -a, -1]
        v1 = [-a, a, -1]
        v2 = [a, a, -1]
        v3 = [a, -a, -1]

        normal = [0, 0, 1]

        self._addQuad(v0, v1, v2, v3, normal, [0.3, 0.3, 0.3])
        


