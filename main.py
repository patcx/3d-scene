import pygame
from math import * 
from numpy import *

from OpenGL.arrays import vbo


from graphic import *
from models.car import *
from models.tree import *
from models.terrain import *
from models.lantern import *
from models.rock import *
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
    rock1 = Rock(0.5, 0, 12)
    rock2 = Rock(0.2, 0, 10)
    rock3 = Rock(1, 0, -2)

    gfx.lightSources.append(car.getLight())
    gfx.lightSources.append(car.getBeaconLight())
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
                if event.key == pygame.K_SPACE:
                    car.getBeaconLight().disabled = not car.getBeaconLight().disabled  
                if event.key == pygame.K_1:
                    gfx.useBlinn = False
                if event.key == pygame.K_2:
                    gfx.useBlinn = True  
                if event.key == pygame.K_p:
                        gfx.loadShader("phong")
                if event.key == pygame.K_g:
                        gfx.loadShader("gouraud")     
                  
                        

        car.update()
        terrain.update()
        camera.update(car)
        gfx.draw(camera, [car, tree1, tree2, tree3, tree4, terrain, lantern1, lantern2, rock1, rock2, rock3])
        pygame.display.flip()
        clock.tick(45)
        


main()