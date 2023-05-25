from raytracing import *

def exempleCode(comments = None):
    path = ImagingPath()
    path.append(Space(d = 100))
    path.append(ThickLens(R1 = 121, R2 = 1e10, n = 1.55, thickness = 3.14, diameter = 50, label = 'Lens'))
    path.append(Space(d = 252.98))
    path.append(ThickLens(R1 = 1e10, R2 = 21.21, n = 1.55, thickness = 3.6, diameter = 16.5, label = 'Lens'))
    path.append(Space(d = 25))
    path.displayWithObject(diameter = 20, comments = comments)

exempleCode()