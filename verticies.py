import numpy

verticies = (
    # RIGHT BOTTOM FRONT
    (1, -1, 1),
    (1, -0.25, 1),
    (0.25, -0.25, 1),
    (0.25, -1, 1),
    (1, -1, 0.25),
    (1, -0.25, 0.25),
    (0.25, -0.25, 0.25),
    (0.25, -1, 0.25),
    
    # RIGHT TOP FRONT
    (1, 1, 1),
    (1, 0.25, 1),
    (0.25, 0.25, 1),
    (0.25, 1, 1),
    (1, 1, 0.25),
    (1, 0.25, 0.25),
    (0.25, 0.25, 0.25),
    (0.25, 1, 0.25),

    # LEFT TOP FRONT
    (-1, 1, 1),
    (-1, 0.25, 1),
    (-0.25, 0.25, 1),
    (-0.25, 1, 1),
    (-1, 1, 0.25),
    (-1, 0.25, 0.25),
    (-0.25, 0.25, 0.25),
    (-0.25, 1, 0.25),

    # LEFT BOTTOM FRONT
    (-1, -1, 1),
    (-1, -0.25, 1),
    (-0.25, -0.25, 1),
    (-0.25, -1, 1),
    (-1, -1, 0.25),
    (-1, -0.25, 0.25),
    (-0.25, -0.25, 0.25),
    (-0.25, -1, 0.25),

    # RIGHT BOTTOM BACK
    (1, -1, -1),
    (1, -0.25, -1),
    (0.25, -0.25, -1),
    (0.25, -1, -1),
    (1, -1, -0.25),
    (1, -0.25, -0.25),
    (0.25, -0.25, -0.25),
    (0.25, -1, -0.25),
    
    # # RIGHT TOP BACK
    (1, 1, -0.25),
    (1, 0.25, -0.25),
    (0.25, 0.25, -0.25),
    (0.25, 1, -0.25),
    (1, 1, -1),
    (1, 0.25, -1),
    (0.25, 0.25, -1),
    (0.25, 1, -1),

    # # LEFT TOP BACK
    (-1, 1, -0.25),
    (-1, 0.25, -0.25),
    (-0.25, 0.25, -0.25),
    (-0.25, 1, -0.25),
    (-1, 1, -1),
    (-1, 0.25, -1),
    (-0.25, 0.25, -1),
    (-0.25, 1, -1),

    # # LEFT BOTTOM BACK
    (-1, -1, -0.25),
    (-1, -0.25, -0.25),
    (-0.25, -0.25, -0.25),
    (-0.25, -1, -0.25),
    (-1, -1, -1),
    (-1, -0.25, -1),
    (-0.25, -0.25, -1),
    (-0.25, -1, -1)
)

def transform_verticies(ver, transformation_matrix):
    new_verticies = ()
    for i in range(len(ver)):
        point = ver[i]
        point_vector = numpy.matrix(str(point[0]) + '; ' + str(point[1]) + '; ' + str(point[2]) + '; 1')
        transformed_point = numpy.matmul(transformation_matrix, point_vector)
        new_verticies += ((transformed_point[0], transformed_point[1], transformed_point[2]),)
    return new_verticies

def get_verticies():
    
    # for point in verticies:
    #     point[2] = (point[2]+offset)
    return verticies