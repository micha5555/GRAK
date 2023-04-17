import pygame
from pygame.locals import *

import numpy, math

import const

def transformate(keys):
    transformation_matrixes = ()
    if keys[K_w]:
        transformation_matrixes += (create_translation_matrix(0, 0, const.TRANSLATION_PICK),)
    if keys[K_a]:
        transformation_matrixes += (create_translation_matrix(const.TRANSLATION_PICK, 0, 0),)
    if keys[K_s]:
        transformation_matrixes += (create_translation_matrix(0, 0, -const.TRANSLATION_PICK),)
    if keys[K_d]:
        transformation_matrixes += (create_translation_matrix(-const.TRANSLATION_PICK, 0, 0),)
    if keys[K_q]:
        transformation_matrixes += (create_translation_matrix(0, const.TRANSLATION_PICK, 0),)
    if keys[K_e]:
        transformation_matrixes += (create_translation_matrix(0, -const.TRANSLATION_PICK, 0),)
    if keys[K_i]:
        transformation_matrixes += (create_OX_rotation_matrix(const.ROTATION_ANGLE_PICK),)
    if keys[K_j]:
        transformation_matrixes += (create_OZ_rotation_matrix(-const.ROTATION_ANGLE_PICK),)
    if keys[K_k]:
        transformation_matrixes += (create_OX_rotation_matrix(-const.ROTATION_ANGLE_PICK),)
    if keys[K_l]:
        transformation_matrixes += (create_OZ_rotation_matrix(const.ROTATION_ANGLE_PICK),)
    if keys[K_v]:
        transformation_matrixes += (create_OY_rotation_matrix(-const.ROTATION_ANGLE_PICK),)
    if keys[K_b]:
        transformation_matrixes += (create_OY_rotation_matrix(const.ROTATION_ANGLE_PICK),)

    if len(transformation_matrixes) == 0:
        return numpy.matrix('1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1')

    output_matrix = transformation_matrixes[0]
    for i in range(1, len(transformation_matrixes)):
        output_matrix = numpy.matmul(output_matrix, transformation_matrixes[i])
    return output_matrix

def change_viewport_based_on_zoom(viewport, keys):
    if keys[K_u] and viewport[0] <= const.MAX_VIEWPORT_SIZE_X:
        viewport = (viewport[0]+const.ZOOM_PICK_X, viewport[1]+const.ZOOM_PICK_Y)
    if keys[K_o] and viewport[0] >= 800:
        viewport = (viewport[0]-const.ZOOM_PICK_X, viewport[1]-const.ZOOM_PICK_Y)
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