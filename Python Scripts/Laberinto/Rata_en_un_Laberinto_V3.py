from colorama import Fore
import turtle

def get_starting_finishing_points():
    _start = [i for i in range(len(maze[0])) if maze[0][i] == 'c']
    _end = [i for i in range(len(maze[0])) if maze[len(maze)-1][i] == 'c']
    return [0, _start[0]], [len(maze) - 1, _end[0]]

def print_maze():
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == 'u':
                print(Fore.WHITE, f'{maze[i][j]}', end="")
            elif maze[i][j] == 'c':
                print(Fore.GREEN, f'{maze[i][j]}', end="")
            elif maze[i][j] == 'p':
                print(Fore.BLUE, f'{maze[i][j]}', end="")
            else:
                print(Fore.RED, f'{maze[i][j]}', end="")
        print('\n')

def escape():
    current_cell = rat_path[len(rat_path) - 1]

    if current_cell == finish:
        return

    if maze[current_cell[0] + 1][current_cell[1]] == 'c':
        maze[current_cell[0] + 1][current_cell[1]] = 'p'
        rat_path.append([current_cell[0] + 1, current_cell[1]])
        escape()

    if maze[current_cell[0]][current_cell[1] + 1] == 'c':
        maze[current_cell[0]][current_cell[1] + 1] = 'p'
        rat_path.append([current_cell[0], current_cell[1] + 1])
        escape()

    if maze[current_cell[0] - 1][current_cell[1]] == 'c':
        maze[current_cell[0] - 1][current_cell[1]] = 'p'
        rat_path.append([current_cell[0] - 1, current_cell[1]])
        escape()

    if maze[current_cell[0]][current_cell[1] - 1] == 'c':
        maze[current_cell[0]][current_cell[1] - 1] = 'p'
        rat_path.append([current_cell[0], current_cell[1] - 1])
        escape()

    # If we get here, this means that we made a wrong decision, so we need to
    # backtrack
    current_cell = rat_path[len(rat_path) - 1]
    if current_cell != finish:
        cell_to_remove = rat_path[len(rat_path) - 1]
        rat_path.remove(cell_to_remove)
        maze[cell_to_remove[0]][cell_to_remove[1]] = 'c'

if __name__ == '__main__':
    with open('Scripts/Python Scripts/Laberinto/maze.txt') as f:
        lines = [line.rstrip() for line in f]
        maze = []
        for i in range(len(lines)):
            a = [item for item in lines[i]]
            maze.append(a)

start, finish = get_starting_finishing_points()
maze[start[0]][start[1]] = 'p'

rat_path = [start]
escape()
print_maze()

PARTE_DEL_CAMINO = 'O'
INTENTADO = '.'
OBSTACULO = 'w'
CAJELLON_SIN_SALIDA = '-'

class Laberinto:
    def __init__(self,nombreArchivoLaberinto):
        filasEnLaberinto = 0
        columnasEnLaberinto = 0
        self.listaLaberinto = []
        archivoLaberinto = open(nombreArchivoLaberinto,'r')
        filasEnLaberinto = 0
        for linea in archivoLaberinto:
            listaFila = []
            columna = 0
            for caracter in linea[:-1]:
                listaFila.append(caracter)
                if caracter == 'c':
                    self.filaInicio = filasEnLaberinto
                    self.columnaInicio = columna
                columna = columna + 1
            filasEnLaberinto = filasEnLaberinto + 1
            self.listaLaberinto.append(listaFila)
            columnasEnLaberinto = len(listaFila)

        self.filasEnLaberinto = filasEnLaberinto
        self.columnasEnLaberinto = columnasEnLaberinto
        self.xTranslate = -columnasEnLaberinto/2
        self.yTranslate = filasEnLaberinto/2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-(columnasEnLaberinto-1)/2-.5,-(filasEnLaberinto-1)/2-.5,(columnasEnLaberinto-1)/2+.5,(filasEnLaberinto-1)/2+.5)

    def dibujarLaberinto(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.filasEnLaberinto):
            for x in range(self.columnasEnLaberinto):
                if self.listaLaberinto[y][x] == OBSTACULO:
                    self.dibujarCajaCentrada(x+self.xTranslate,-y+self.yTranslate,'orange')
        self.t.color('black')
        self.t.fillcolor('blue')
        self.wn.update()
        self.wn.tracer(1)

    def dibujarCajaCentrada(self,x,y,color):
        self.t.up()
        self.t.goto(x-.5,y-.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def moverTortuga(self,x,y):
        self.t.up()
        self.t.setheading(self.t.towards(x+self.xTranslate,-y+self.yTranslate))
        self.t.goto(x+self.xTranslate,-y+self.yTranslate)
        self.wn.exitonclick()

    def tirarMigaDePan(self,color):
        self.t.dot(10,color)

    def actualizarPosicion(self,fila,columna,val=None):
        if val:
            self.listaLaberinto[fila][columna] = val
        self.moverTortuga(columna,fila)

        if val == PARTE_DEL_CAMINO:
            color = 'green'
        elif val == OBSTACULO:
            color = 'red'
        elif val == INTENTADO:
            color = 'black'
        elif val == CAJELLON_SIN_SALIDA:
            color = 'red'
        else:
            color = None

        if color:
            self.tirarMigaDePan(color)

    def esSalida(self,fila,columna):
        return (fila == 0 or
                fila == self.filasEnLaberinto-1 or
                columna == 0 or
                columna == self.columnasEnLaberinto-1 )

    def __getitem__(self,indice):
        return self.listaLaberinto[indice]

def buscarDesde(laberinto, filaInicio, columnaInicio):
    laberinto.actualizarPosicion(filaInicio, columnaInicio)
    #  Verificar casos base:
    #  1. Hemos tropezado con un obstáculo, devolver False
    if laberinto[filaInicio][columnaInicio] == OBSTACULO :
        return False
    #  2. Hemos encontrado un cuadrado que ya ha sido explorado
    if laberinto[filaInicio][columnaInicio] == INTENTADO:
        return False
    # 3. Éxito, un borde exterior no ocupado por un obstáculo
    if laberinto.esSalida(filaInicio,columnaInicio):
        laberinto.actualizarPosicion(filaInicio, columnaInicio, PARTE_DEL_CAMINO)
        return True
    laberinto.actualizarPosicion(filaInicio, columnaInicio, INTENTADO)

    # De lo contrario, use cortocircuitos lógicos para probar cada
    # dirección a su vez (si fuera necesario)
    encontrado = buscarDesde(laberinto, filaInicio-1, columnaInicio) or \
            buscarDesde(laberinto, filaInicio+1, columnaInicio) or \
            buscarDesde(laberinto, filaInicio, columnaInicio-1) or \
            buscarDesde(laberinto, filaInicio, columnaInicio+1)
    if encontrado:
        laberinto.actualizarPosicion(filaInicio, columnaInicio, PARTE_DEL_CAMINO)
    else:
        laberinto.actualizarPosicion(filaInicio, columnaInicio, CAJELLON_SIN_SALIDA)
    return encontrado

miLaberinto = Laberinto('Scripts/Python Scripts/Laberinto/maze.txt')
miLaberinto.dibujarLaberinto()
miLaberinto.actualizarPosicion(miLaberinto.filaInicio,miLaberinto.columnaInicio)

buscarDesde(miLaberinto, miLaberinto.filaInicio, miLaberinto.columnaInicio)
miLaberinto.wn.exitonclick()