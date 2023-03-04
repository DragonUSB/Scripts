# En primer lugar debemos de abrir el fichero que vamos a leer.
# Usa 'rb' en vez de 'r' si se trata de un fichero binario.
infile = open('Libro2.csv', 'r')
# Mostramos por pantalla lo que leemos desde el fichero
print('>>> Lectura del fichero línea a línea')
for line in infile:
    print(line)
# Cerramos el fichero.
infile.close()