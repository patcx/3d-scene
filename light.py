from numpy import *

class LightSource:
    position = array([0, 0, 0, 1])
    direction = array([1, 0, -1, 1])
    spotCutOff = 0.4
    intensity = 1

    def setPosition(self, v):
        self.position = v

    def setDirection(self, v):
        self.direction = v

class CarLightSource(LightSource):

    def __init__(self):
        self._basePosition = self.position
        self._baseDirection = self.direction

    def setPosition(self, v):
        self._basePosition = v

    def setDirection(self, v):
        self._baseDirection = v

    def update(self, car):
        self.position = array(car.transformationMatrix *  car.rotationMatrix * matrix(self._basePosition).reshape(4,1))
        self.direction = array(car.rotationMatrix * matrix(self._baseDirection).reshape(4,1))

class CarLightSource(LightSource):

    def __init__(self):
        self._basePosition = self.position
        self._baseDirection = self.direction

    def setPosition(self, v):
        self._basePosition = v

    def setDirection(self, v):
        self._baseDirection = v

    def update(self, car):
        self.position = array(car.transformationMatrix *  car.rotationMatrix * matrix(self._basePosition).reshape(4,1))
        self.direction = array(car.rotationMatrix * matrix(self._baseDirection).reshape(4,1))
        
class CarBeaconLightSource(LightSource):

    def __init__(self):
        self._basePosition = self.position
        self._baseDirection = self.direction
        self._angle = 0
        self.intensity = 1

    def setPosition(self, v):
        self._basePosition = v

    def setDirection(self, v):
        self._baseDirection = v

    def update(self, car):
        self._angle += 0.1
        self._angle %= 2*pi
        self._setRotation(self._angle)
        self.position = array(car.transformationMatrix *  car.rotationMatrix * matrix(self._basePosition).reshape(4,1))
        self.direction = array(self.rotationMatrix * matrix(self._baseDirection).reshape(4,1))

    def _setRotation(self, angle):
        angleCos = cos(angle)
        angleSin = sin(angle)

        self.rotationMatrix = matrix([
            [angleCos, -angleSin, 0, 0],
            [angleSin, angleCos, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            ])
        
