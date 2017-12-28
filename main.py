import pygame
from math import * 
from numpy import *

from OpenGL.arrays import vbo


from graphic import *
from car import *
from tree import *
from terrain import *
from camera import *

   
def main():

    gfx = Graphic('3D Scene', (800, 600))
   
    car = Car()
    tree = Tree()
    terrain = Terrain()

    camera = Camera(gfx.screenHeight/gfx.screenWidth, 45)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    camera.setType(CameraType.STATIC)
                if event.key == pygame.K_F2:
                    camera.setType(CameraType.FOLLOWING)
                if event.key == pygame.K_F3:
                    camera.setType(CameraType.MOVING_FOLLOWING)

        car.update()
        tree.update()
        terrain.update()

        camera.update(car)

        gfx.draw(camera, [car, tree, terrain])

        pygame.display.flip()
        pygame.time.wait(10)


main()