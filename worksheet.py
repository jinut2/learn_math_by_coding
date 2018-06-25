import math
import numpy as np
from CodingTheMatrix.image import *


def rotate(L, angle=0):
    return {(math.cos(angle*math.pi) - 1j*math.sin(angle*math.pi))*z for z in L}
    # return {math.e**(angle*1j)*z for z in L}


def circle(r, point_dist_radial_pi=0.1):
    R = r + 0j
    angles = np.arange(0.0,2.0,point_dist_radial_pi)
    C = {(math.cos(angle*math.pi) - 1j*math.sin(angle*math.pi))*R for angle in angles}
    return C


def img2Cmplx(file_path):
    I = color2gray(file2image(file_path))
    r = len(I)
    c = len(I[0])
    M = [x + y*1j for x in range(c) for y in range(r) if I[r-y-1][x] < 120]
    return {'M': M, 'l': max(r, c)}
