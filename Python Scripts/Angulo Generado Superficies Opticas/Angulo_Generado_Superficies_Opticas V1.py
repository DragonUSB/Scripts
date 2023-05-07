from math import asin, pi

superficie = input("La supeficie es concava (1) o convexa (2): ")
r = float(input("Colocar el radio de curvatura de la superficie (mm): "))
d = float(input("Colocar el diametro medio de la fresa de diamante (mm): "))
e = float(input("Colocar el radio de curvatura del filo de la fresa (mm): "))

x1 = d / (2 * (r - e))
x2 = d / (2 * (r + e))

if x1 > 1 or x2 > 1:
    print("\nPor favor seleccione una fresa de diamante de menor diametro")
    d = float(input("Colocar el diametro medio de la fresa de diamante (mm): "))
e = float(input("Colocar el radio de curvatura del filo de la fresa (mm): "))

x1 = d / (2 * (r - e))
x2 = d / (2 * (r + e))

if superficie == '1':
    alpha = asin(x1)
else:
    alpha = asin(x2)

grados = alpha * (180 / pi)

print(f"\nEl angulo de inclinacion de la herramienta es de {alpha:.2f} rad o {grados:.2f}°")