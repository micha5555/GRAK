import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import time

import coordinates, edges
import verticies, transformations

def Cube(ver, edges):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(ver[vertex])
    glEnd()


def main():
    # print(len(verticies.get_verticies(1)))
    pygame.init()
    display = (800,600)
    viewport = (2400, 1800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 1000.0)

    glTranslatef(0.0,0.0, -5)

    i = 0.0
    flag = True
    ver = verticies.get_verticies()
    # i = 0.0
    while True:
        # gluPerspective(45+i, (display[0]/display[1]), 0.1, 50.0)
        # i += 0.001
        keys = pygame.key.get_pressed()
        transformation_matrix = transformations.transformate(keys)
        # zoom_matrix = transformations.zoom(keys)
        ver = verticies.transform_verticies(ver, transformation_matrix)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # viewport = transformations.count_zoom(keys)
        viewport_x = (display[0] - viewport[0]) // 2
        viewport_y = (display[1] - viewport[1]) // 2
        glViewport(viewport_x, viewport_y, viewport[0], viewport[1])
        # if (i > 5):
        #     flag = False
        # elif (i < 0):
        #     flag = True

        # if(flag):
        #     i += 0.01
        # else:
        #     i -= 0.01

        # glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube(ver, edges.edges)
        # Cube(coordinates.verticies, edges.edges)

        pygame.display.flip()
        pygame.time.wait(10)


main()