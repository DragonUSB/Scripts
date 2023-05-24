from raytracing import *

def exempleCode(comments = None):
    path = ImagingPath()
    path.append(Space(d = 50))
    path.append(ThickLens(R1 = 121, R2 = 1e10, n = 1.55, thickness = 3.14, diameter = 50, label = 'Lens'))
    path.append(Space(d = 250))
    path.displayWithObject(diameter = 20, comments = comments)

exempleCode()