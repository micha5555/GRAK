def get_verticies(offset):
    verticies = (
    # RIGHT BOTTOM FRONT
        (1, -1, 1+offset),
        (1, -0.25, 1+offset),
        (0.25, -0.25, 1+offset),
        (0.25, -1, 1+offset),
        (1, -1, 0.25+offset),
        (1, -0.25, 0.25+offset),
        (0.25, -0.25, 0.25+offset),
        (0.25, -1, 0.25+offset),
        
        # RIGHT TOP FRONT
        (1, 1, 1+offset),
        (1, 0.25, 1+offset),
        (0.25, 0.25, 1+offset),
        (0.25, 1, 1+offset),
        (1, 1, 0.25+offset),
        (1, 0.25, 0.25+offset),
        (0.25, 0.25, 0.25+offset),
        (0.25, 1, 0.25+offset),

        # LEFT TOP FRONT
        (-1, 1, 1+offset),
        (-1, 0.25, 1+offset),
        (-0.25, 0.25, 1+offset),
        (-0.25, 1, 1+offset),
        (-1, 1, 0.25+offset),
        (-1, 0.25, 0.25+offset),
        (-0.25, 0.25, 0.25+offset),
        (-0.25, 1, 0.25+offset),

        # LEFT BOTTOM FRONT
        (-1, -1, 1+offset),
        (-1, -0.25, 1+offset),
        (-0.25, -0.25, 1+offset),
        (-0.25, -1, 1+offset),
        (-1, -1, 0.25+offset),
        (-1, -0.25, 0.25+offset),
        (-0.25, -0.25, 0.25+offset),
        (-0.25, -1, 0.25+offset),

        # RIGHT BOTTOM BACK
        (1, -1, -1+offset),
        (1, -0.25, -1+offset),
        (0.25, -0.25, -1+offset),
        (0.25, -1, -1+offset),
        (1, -1, -0.25+offset),
        (1, -0.25, -0.25+offset),
        (0.25, -0.25, -0.25+offset),
        (0.25, -1, -0.25+offset),
        
        # # RIGHT TOP BACK
        (1, 1, -0.25+offset),
        (1, 0.25, -0.25+offset),
        (0.25, 0.25, -0.25+offset),
        (0.25, 1, -0.25+offset),
        (1, 1, -1+offset),
        (1, 0.25, -1+offset),
        (0.25, 0.25, -1+offset),
        (0.25, 1, -1+offset),

        # # LEFT TOP BACK
        (-1, 1, -0.25+offset),
        (-1, 0.25, -0.25+offset),
        (-0.25, 0.25, -0.25+offset),
        (-0.25, 1, -0.25+offset),
        (-1, 1, -1+offset),
        (-1, 0.25, -1+offset),
        (-0.25, 0.25, -1+offset),
        (-0.25, 1, -1+offset),

        # # LEFT BOTTOM BACK
        (-1, -1, -0.25+offset),
        (-1, -0.25, -0.25+offset),
        (-0.25, -0.25, -0.25+offset),
        (-0.25, -1, -0.25+offset),
        (-1, -1, -1+offset),
        (-1, -0.25, -1+offset),
        (-0.25, -0.25, -1+offset),
        (-0.25, -1, -1+offset)
    )
    # for point in verticies:
    #     point[2] = (point[2]+offset)
    return verticies