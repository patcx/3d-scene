from numpy import *
from math import *
from enum import Enum

def normalize(vector):
    norm = linalg.norm(vector)
    return vector/norm

class CameraType(Enum):
    STATIC = 0
    FOLLOWING = 1
    MOVING_FOLLOWING = 2


class Camera:

    def __init__(self, a, fov):

        n = 1
        f = 100
        e  = (1 / tan(fov * pi / 180 / 2))
         
        self.projectionMatrix = matrix([
           [e, 0, 0, 0],
           [0, e/a, 0, 0],
           [0, 0, -(f+n)/(f-n), (-2*f*n)/(f-n)],
           [0, 0, -1, 0]
       ])
        self.lookAt([3.5, 0.5, 0.5], [0, 1, 0.5], [0, 0, 1])

        self.cameraType = CameraType.STATIC

    def lookAt(self, cameraPosition, cameraTarget, upVector):
        zAxis = normalize(array(cameraPosition) - array(cameraTarget))
        xAxis = normalize(cross(upVector, zAxis))
        yAxis = cross(zAxis, xAxis)

        self.viewMatrix = linalg.inv(matrix([
            [xAxis[0], yAxis[0], zAxis[0], cameraPosition[0]],
            [xAxis[1], yAxis[1], zAxis[1], cameraPosition[1]],
            [xAxis[2], yAxis[2], zAxis[2], cameraPosition[2]],
            [0, 0, 0, 1]
        ]))

    def setType(self, camType):
        self.cameraType = camType

    def update(self, obj):

        if self.cameraType == CameraType.STATIC:
            self.lookAt([20, -10, 5], [0, 0, 0], [0, 0, 1])
        elif self.cameraType == CameraType.MOVING_FOLLOWING:
            self.lookAt([obj.getX()+0.1, obj.getY(), 20], [obj.getX(), obj.getY(), 0], [0, 0, 1])
        elif self.cameraType == CameraType.FOLLOWING:
            self.lookAt([20, -10, 10], [obj.getX(), obj.getY(), 0], [0, 0, 1])
