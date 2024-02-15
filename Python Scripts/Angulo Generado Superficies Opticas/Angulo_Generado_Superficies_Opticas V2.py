from math import asin, pi

superficie = input("La supeficie es concava (1) o convexa (2): ")
r = float(input("Colocar el radio de curvatura de la superficie (mm): "))
d1 = float(input("Colocar el diametro exterior de la fresa de diamante (mm): "))
d2 = float(input("Colocar el diametro interior de la fresa de diamante (mm): "))

x1 = d1 / (2 * r)
x2 = d2 / (2 * r)

if x1 > 1 and superficie == '1':
    print("\nPor favor seleccione una fresa de diamante de menor diametro")
    d1 = float(input("Colocar el diametro exterior de la fresa de diamante (mm): "))
    d2 = float(input("Colocar el diametro interior de la fresa de diamante (mm): "))
    
if x2 > 1 and superficie == '2':
    print("\nPor favor seleccione una fresa de diamante de menor diametro")
    d1 = float(input("Colocar el diametro exterior de la fresa de diamante (mm): "))
    d2 = float(input("Colocar el diametro interior de la fresa de diamante (mm): "))

x1 = d1 / (2 * r)
x2 = d2 / (2 * r)

if superficie == '1':
    alpha = asin(x1)
else:
    alpha = asin(x2)

grados = alpha * (180 / pi)

print(f"\nEl angulo de inclinacion de la herramienta es de {alpha:.2f} rad o {grados:.2f}°")