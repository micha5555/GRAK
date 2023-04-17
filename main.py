import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import time

import points, edges, transformations, const

def Cube(points, edges):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(points[vertex])
    glEnd()


def main():
    pygame.init()
    display = (const.DISPLAY_DEFAULT_SIZE_X, const.DISPLAY_DEFAULT_SIZE_Y)
    default_viewport = (const.MIN_VIEWPORT_SIZE_X, const.MIN_VIEWPORT_SIZE_Y)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 1000.0)

    glTranslatef(0.0,0.0, -5)

    all_points = points.points_array
    viewport = default_viewport
    while True:
        keys = pygame.key.get_pressed()
        transformation_matrix = transformations.transformate(keys)
        all_points = points.transform_points(all_points, transformation_matrix)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        viewport = transformations.change_viewport_based_on_zoom(viewport, keys)
        viewport_x = (display[0] - viewport[0]) // 2
        viewport_y = (display[1] - viewport[1]) // 2
        if keys[K_z]:
            viewport = default_viewport
            all_points = points.points_array
        glViewport(viewport_x, viewport_y, viewport[0], viewport[1])
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube(all_points, edges.edges)

        pygame.display.flip()
        pygame.time.wait(10)


main()