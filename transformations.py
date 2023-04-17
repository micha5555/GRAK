import pygame
from pygame.locals import *

import numpy, math

import verticies

TRANSLATION_PICK = 0.05
ROTATION_ANGLE_PICK = 0.04
ZOOM_IN_RATIO = 1.01
ZOOM_OUT_RATIO = 0.99

def transformate(keys):
    transformation_matrixes = ()
    if keys[K_w]:
        transformation_matrixes += (create_translation_matrix(0, 0, TRANSLATION_PICK),)
    if keys[K_a]:
        transformation_matrixes += (create_translation_matrix(TRANSLATION_PICK, 0, 0),)
    if keys[K_s]:
        transformation_matrixes += (create_translation_matrix(0, 0, -TRANSLATION_PICK),)
    if keys[K_d]:
        transformation_matrixes += (create_translation_matrix(-TRANSLATION_PICK, 0, 0),)
    if keys[K_q]:
        transformation_matrixes += (create_translation_matrix(0, TRANSLATION_PICK, 0),)
    if keys[K_e]:
        transformation_matrixes += (create_translation_matrix(0, -TRANSLATION_PICK, 0),)
    if keys[K_i]:
        transformation_matrixes += (create_OX_rotation_matrix(ROTATION_ANGLE_PICK),)
    if keys[K_j]:
        transformation_matrixes += (create_OZ_rotation_matrix(-ROTATION_ANGLE_PICK),)
    if keys[K_k]:
        transformation_matrixes += (create_OX_rotation_matrix(-ROTATION_ANGLE_PICK),)
    if keys[K_l]:
        transformation_matrixes += (create_OZ_rotation_matrix(ROTATION_ANGLE_PICK),)
    if keys[K_v]:
        transformation_matrixes += (create_OY_rotation_matrix(-ROTATION_ANGLE_PICK),)
    if keys[K_b]:
        transformation_matrixes += (create_OY_rotation_matrix(ROTATION_ANGLE_PICK),)
    # if keys[K_u]:
    #     transformation_matrixes += (create_zoom_marix(ZOOM_IN_RATIO),)
    # if keys[K_o]:
    #     transformation_matrixes += (create_zoom_marix(ZOOM_OUT_RATIO),)

    if len(transformation_matrixes) == 0:
        return numpy.matrix('1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1')

    output_matrix = transformation_matrixes[0]
    for i in range(1, len(transformation_matrixes)):
        output_matrix = numpy.matmul(output_matrix, transformation_matrixes[i])

    return output_matrix

# def zoom(keys):
#     zoom_matrixes = ()
#     if keys[K_u]:
#         zoom_matrixes += (create_zoom_marix(ZOOM_IN_RATIO),)
#     if keys[K_o]:
#         zoom_matrixes += (create_zoom_marix(ZOOM_OUT_RATIO),)
#     if len(zoom_matrixes) == 0:
#         return numpy.matrix('1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1')

#     output_matrix = zoom_matrixes[0]
#     for i in range(1, len(zoom_matrixes)):
#         output_matrix = numpy.matmul(output_matrix, zoom_matrixes[i])

#     return output_matrix

def count_zoom(viewport, keys):
    if keys[K_u] and viewport[0] <= 2400:
        viewport = (viewport[0]+16, viewport[1]+12)
        print(viewport[0])
        # transformation_matrixes += (create_zoom_marix(ZOOM_IN_RATIO),)
    if keys[K_o] and viewport[0] >= 800:
        viewport = (viewport[0]-16, viewport[1]-12)
        print(viewport[0])
    return viewport

def create_translation_matrix(p_x, p_y, p_z):
    first_row = '1 0 0 ' + str(p_x) + '; '
    second_row = '0 1 0 ' + str(p_y) + '; '
    third_row = '0 0 1 ' + str(p_z) + '; '
    fourth_row ='0 0 0 1'
    translation_matrix = numpy.matrix(first_row + second_row + third_row + fourth_row)
    return translation_matrix

def create_OX_rotation_matrix(angle):
    first_row = '1 0 0 0; '
    second_row = '0 ' + str(math.cos(angle)) + ' ' + str(-math.sin(angle)) + ' 0; '
    third_row = '0 ' + str(math.sin(angle)) + ' ' + str(math.cos(angle)) + ' 0; '
    fourth_row ='0 0 0 1'
    rotation_matrix = numpy.matrix(first_row + second_row + third_row + fourth_row)
    return rotation_matrix

def create_OY_rotation_matrix(angle):
    first_row = str(math.cos(angle)) + ' 0 ' + str(math.sin(angle)) + ' 0; '
    second_row = '0 1 0 0; '
    third_row = str(-math.sin(angle)) + ' 0 ' + str(math.cos(angle)) + ' 0; '
    fourth_row ='0 0 0 1'
    rotation_matrix = numpy.matrix(first_row + second_row + third_row + fourth_row)
    return rotation_matrix

def create_OZ_rotation_matrix(angle):
    first_row = str(math.cos(angle)) + ' ' + str(-math.sin(angle)) + ' 0 0; '
    second_row = str(math.sin(angle)) + ' ' + str(math.cos(angle)) + ' 0 0; '
    third_row = '0 0 1 0; '
    fourth_row ='0 0 0 1'
    rotation_matrix = numpy.matrix(first_row + second_row + third_row + fourth_row)
    return rotation_matrix

def create_zoom_marix(ratio):
    first_row = str(ratio) + ' 0 0 0; '
    second_row = '0 ' + str(ratio) + ' 0 0; '
    third_row = '0 0 ' + str(ratio) + ' 0; '
    fourth_row = '0 0 0 1'
    zoom_matrix = numpy.matrix(first_row + second_row + third_row + fourth_row)
    return zoom_matrix