from math import asin, pi

superficie = input("La supeficie es concava o convexa: ")
r = float(input("Colocar el radio de curvatura de la superficie (mm): "))
d = float(input("Colocar el diametro medio de la fresa de diamante (mm): "))
e = float(input("Colocar el radio de curvatura del filo de la fresa (mm): "))

if superficie == 'concava':
    alpha = asin(d / (2 * (r - e)))
else:
    alpha = asin(d / (2 * (r + e)))

grados = alpha * (180 / pi)

print(f"El angulo de inclinacion de la herramienta es de {alpha:.2f} rad o {grados:.2f}°")