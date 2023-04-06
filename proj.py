import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import coordinates, edges
import moving_forward

def Cube(ver, edges):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(ver[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    i = 0.0
    flag = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        if (i > 5):
            flag = False
        elif (i < 0):
            flag = True

        if(flag):
            i += 0.01
        else:
            i -= 0.01

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube(moving_forward.get_verticies(i), edges.edges)
        # Cube(coordinates.verticies, edges.edges)

        pygame.display.flip()
        pygame.time.wait(10)


main()