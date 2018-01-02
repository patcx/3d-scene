import pygame
from numpy import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL import shaders



class Graphic:
    lightSources = list()

    def __init__(self, caption, resolution):
        pygame.init()
        self.screen =  pygame.display.set_mode(resolution, pygame.DOUBLEBUF|pygame.OPENGL)
        pygame.display.set_caption(caption)
        self.screenWidth = resolution[0]
        self.screenHeight = resolution[1]

        fragmentShaderSource = open("shaders/shader.frag", "r")
        vertexShaderSource = open("shaders/shader.vert", "r")

        VERTEX_SHADER = shaders.compileShader(vertexShaderSource.read(), GL_VERTEX_SHADER)
        FRAGMENT_SHADER = shaders.compileShader(fragmentShaderSource.read(), GL_FRAGMENT_SHADER)
        self.shader = shaders.compileProgram(VERTEX_SHADER,FRAGMENT_SHADER)


        self.positionAttrib = glGetAttribLocation(self.shader, "position")
        glEnableVertexAttribArray(self.positionAttrib)
    
        self.normalAttrib = glGetAttribLocation(self.shader, "normal")
        glEnableVertexAttribArray(self.normalAttrib)

        self.diffuseAttrib = glGetAttribLocation(self.shader, "diffuse")
        glEnableVertexAttribArray(self.diffuseAttrib)

        glEnable(GL_DEPTH_TEST)

        self.normalMatrixUniform = glGetUniformLocation(self.shader, "uNormalMatrix")
        self.modelMatrixUniform = glGetUniformLocation(self.shader, "uModelMatrix")
        self.viewMatrixUniform = glGetUniformLocation(self.shader, "uViewMatrix")
        self.projectionMatrixUniform = glGetUniformLocation(self.shader, "uProjectionMatrix")

    def draw(self, camera, objects):

        shaders.glUseProgram(self.shader)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        i = 0
        for light in self.lightSources:
            glUniform4fv(glGetUniformLocation(self.shader, "uLights[{0}].position".format(i)), 1, light.position)
            glUniform4fv(glGetUniformLocation(self.shader, "uLights[{0}].spotDirection".format(i)), 1, light.direction)
            glUniform1f(glGetUniformLocation(self.shader, "uLights[{0}].spotCutOff".format(i)), light.spotCutOff)
            glUniform1f(glGetUniformLocation(self.shader, "uLights[{0}].intensity".format(i)), light.intensity)
            i += 1

        for obj in objects:
            glVertexAttribPointer(self.positionAttrib, 3, GL_FLOAT, False, 0, obj.vertices)
            glVertexAttribPointer(self.normalAttrib, 3, GL_FLOAT, False, 0, obj.normals)
            glVertexAttribPointer(self.diffuseAttrib, 3, GL_FLOAT, False, 0, obj.diffuse)
            

            rotationMatrix = obj.rotationMatrix
            transformationMatrix = obj.transformationMatrix
            viewMatrix = camera.viewMatrix
            projectionMatrix = array(camera.projectionMatrix)

            glUniformMatrix3fv(self.normalMatrixUniform, 1, GL_TRUE, array(transpose(linalg.inv(rotationMatrix[0:3,0:3]))))
            glUniformMatrix4fv(self.modelMatrixUniform, 1, GL_TRUE, array(transformationMatrix * rotationMatrix))
            glUniformMatrix4fv(self.viewMatrixUniform, 1, GL_TRUE, array(viewMatrix))
            glUniformMatrix4fv(self.projectionMatrixUniform, 1, GL_TRUE, projectionMatrix)

            glDrawElements(GL_TRIANGLES, obj.indexes.size, GL_UNSIGNED_SHORT, obj.indexes)

        shaders.glUseProgram(0)


        