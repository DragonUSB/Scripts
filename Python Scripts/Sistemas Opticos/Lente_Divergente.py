from raytracing import *

def exempleCode(comments = None):
    path = ImagingPath()
    path.append(Space(d = 35))
    path.append(ThickLens(R1 = 1e10, R2 = 21.21, n = 1.55, thickness = 3.6, diameter = 16.5, label = 'Lens'))
    path.append(Space(d = 250))
    path.displayWithObject(diameter = 10, comments = comments)

exempleCode()