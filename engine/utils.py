from math import sin, cos, sqrt

def makeTriangle(x, y, r):
    '''p1 = (x + r, y)
    p2 = (x + r * (-0.5), y + r * (sqrt(3)/2))
    p3 = (x + r * (-0.5), y + r * (-sqrt(3)/2))'''
    p1 = (x - r, y)
    p2 = (x + r, y)
    p3 = (x, y - ((sqrt(3)/2) * r))

    return (p1, p2, p3)