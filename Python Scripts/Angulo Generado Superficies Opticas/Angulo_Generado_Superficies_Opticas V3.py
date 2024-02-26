from math import asin, pi, sin
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, Plot, Figure, Matrix, Alignat, Command
from pylatex.utils import italic, NoEscape
import os

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

if __name__ == '__main__':
    image_filename = os.path.join(os.path.dirname(__file__), 'Angulo_de_generado_superfices_opticas.png')
    
    geometry_options = {"tmargin": "2cm", "lmargin": "2cm", "rmargin": "2cm", "bmargin": "2cm"}
    doc = Document(geometry_options=geometry_options)
    
    doc.preamble.append(Command('title', 'Angulo de Generado'))
    doc.preamble.append(Command('author', 'Bernardo Conquet'))
    doc.append(NoEscape(r'\maketitle'))
    
    doc.append('En el fresado de superficies esfericas se emplea harramientas de diamante (Fig. 1). El diametro de la fresa y la inclinacion del eje con respecto al eje de la pieza a trabajar, deterniman la curvatura de la superficie obtenida, segun la relacion:')
    
    with doc.create(Alignat(numbering=False, escape=False)) as agn:
        agn.append(r'r &= \frac{d}{2 \sin(\alpha)} \\')
    
    doc.append('en la que:\n')
    doc.append(italic('r '))
    doc.append('= radio de curvatura de la superficie obtenida\n')
    doc.append(italic('d '))
    doc.append('= diametro de la fresa diamante\n')
    doc.append(italic(r'\alpha \\'))
    doc.append('= angulo de inclinacion de la herramienta con respecto al de la pieza a trabajar')
    
    with doc.create(Figure(position='h!')) as angulo_pic:
        angulo_pic.add_image(image_filename, width='150px')
        angulo_pic.add_caption('Representacion de la relacion entre el diametro del disco de diamante, el radio de la lente y el angulo de ataque')

pdf_file = os.path.join(os.path.dirname(__file__), 'Angulo_Generado')

doc.generate_pdf(pdf_file, clean_tex=False)