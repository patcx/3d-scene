import pygame
from math import * 
from numpy import *

from OpenGL.arrays import vbo


from graphic import *
from models.car import *
from models.tree import *
from models.terrain import *
from models.lantern import *
from camera import *

   
def main():

    gfx = Graphic('3D Scene', (1200, 700))

    car = Car()
    tree1 = Tree(2, 0, 0)
    tree2 = Tree(3, 3, -3)
    tree3 = Tree(2.5, -3, -3)
    tree4 = Tree(2.5, -5, 10)
    lantern1 = Lantern(6, 3, 1, [-0.5, 0.5, -0.8])
    lantern2 = Lantern(6, -3, -10, [0.5, 0.5, -0.8])
    terrain = Terrain(30)

    gfx.lightSources.append(car.getLight())
    gfx.lightSources.append(lantern1.getLight())
    gfx.lightSources.append(lantern2.getLight())


    camera = Camera(gfx.screenHeight/gfx.screenWidth, 45)
    
    clock = pygame.time.Clock()

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

        terrain.update()

        camera.update(car)
        
        gfx.draw(camera, [car, tree1, tree2, tree3, tree4, terrain, lantern1, lantern2])

        pygame.display.flip()
        clock.tick(45)
        


main()