import time
import numpy as np
import matplotlib.pyplot as plt
from random import randint, shuffle, choice

dim = 16

maze = np.zeros((dim, dim), dtype = int)

x = np.arange(0, dim + 1, 1)
y = np.arange(0, dim + 1, 1)
xv, yv = np.meshgrid(x, y)

plt.plot(xv, yv, marker = '.', color = 'k', linestyle = 'none')
ax = plt.gca()

# Pared Exterior del Laberinto
plt.plot([xv[0][0], xv[0][dim]], [yv[0][0], yv[0][dim]], color = 'k')
plt.plot([xv[dim][0], xv[dim][dim]], [yv[dim][0], yv[dim][dim]], color = 'k')
plt.plot([xv[0][0], xv[dim][0]], [yv[0][0], yv[dim][0]], color = 'k')
plt.plot([xv[0][dim], xv[dim][dim]], [yv[0][dim], yv[dim][dim]], color = 'k')

# Comienzo del Laberinto
maze[0][0] = 1
plt.plot([xv[0][1], xv[1][1]], [yv[0][1], yv[1][1]], color = 'k')

# Meta del Laberinto
c1 = int((dim / 2) - 1)
c2 = int(dim / 2)
c3 = int((dim / 2) + 1)
m = randint(1, 8)
maze[c1][c1] = maze[c1][c2] = maze[c2][c1] = maze[c2][c2] = 1
if m == 1:
    plt.plot([xv[c1][c1], xv[c3][c1]], [yv[c1][c1], yv[c3][c1]], color = 'k')
    plt.plot([xv[c1][c1], xv[c1][c3]], [yv[c1][c1], yv[c1][c3]], color = 'k')
    plt.plot([xv[c1][c3], xv[c3][c3]], [yv[c1][c3], yv[c3][c3]], color = 'k')
    plt.plot([xv[c3][c2], xv[c3][c3]], [yv[c3][c2], yv[c3][c3]], color = 'k')
elif m == 2:
    plt.plot([xv[c1][c1], xv[c3][c1]], [yv[c1][c1], yv[c3][c1]], color = 'k')
    plt.plot([xv[c1][c1], xv[c1][c3]], [yv[c1][c1], yv[c1][c3]], color = 'k')
    plt.plot([xv[c1][c3], xv[c3][c3]], [yv[c1][c3], yv[c3][c3]], color = 'k')
    plt.plot([xv[c3][c1], xv[c3][c2]], [yv[c3][c1], yv[c3][c2]], color = 'k')
elif m == 3:
    plt.plot([xv[c1][c1], xv[c3][c1]], [yv[c1][c1], yv[c3][c1]], color = 'k')
    plt.plot([xv[c1][c1], xv[c1][c3]], [yv[c1][c1], yv[c1][c3]], color = 'k')
    plt.plot([xv[c1][c3], xv[c2][c3]], [yv[c1][c3], yv[c2][c3]], color = 'k')
    plt.plot([xv[c3][c1], xv[c3][c3]], [yv[c3][c1], yv[c3][c3]], color = 'k')
elif m == 4:
    plt.plot([xv[c1][c1], xv[c3][c1]], [yv[c1][c1], yv[c3][c1]], color = 'k')
    plt.plot([xv[c1][c1], xv[c1][c3]], [yv[c1][c1], yv[c1][c3]], color = 'k')
    plt.plot([xv[c2][c3], xv[c3][c3]], [yv[c2][c3], yv[c3][c3]], color = 'k')
    plt.plot([xv[c3][c1], xv[c3][c3]], [yv[c3][c1], yv[c3][c3]], color = 'k')
elif m == 5:
    plt.plot([xv[c1][c1], xv[c3][c1]], [yv[c1][c1], yv[c3][c1]], color = 'k')
    plt.plot([xv[c1][c1], xv[c1][c2]], [yv[c1][c1], yv[c1][c2]], color = 'k')
    plt.plot([xv[c1][c3], xv[c3][c3]], [yv[c1][c3], yv[c3][c3]], color = 'k')
    plt.plot([xv[c3][c1], xv[c3][c3]], [yv[c3][c1], yv[c3][c3]], color = 'k')
elif m == 6:
    plt.plot([xv[c1][c1], xv[c3][c1]], [yv[c1][c1], yv[c3][c1]], color = 'k')
    plt.plot([xv[c1][c2], xv[c1][c3]], [yv[c1][c2], yv[c1][c3]], color = 'k')
    plt.plot([xv[c1][c3], xv[c3][c3]], [yv[c1][c3], yv[c3][c3]], color = 'k')
    plt.plot([xv[c3][c1], xv[c3][c3]], [yv[c3][c1], yv[c3][c3]], color = 'k')
elif m == c1:
    plt.plot([xv[c2][c1], xv[c3][c1]], [yv[c2][c1], yv[c3][c1]], color = 'k')
    plt.plot([xv[c1][c1], xv[c1][c3]], [yv[c1][c1], yv[c1][c3]], color = 'k')
    plt.plot([xv[c1][c3], xv[c3][c3]], [yv[c1][c3], yv[c3][c3]], color = 'k')
    plt.plot([xv[c3][c1], xv[c3][c3]], [yv[c3][c1], yv[c3][c3]], color = 'k')
else:
    plt.plot([xv[c1][c1], xv[c2][c1]], [yv[c1][c1], yv[c2][c1]], color = 'k')
    plt.plot([xv[c1][c1], xv[c1][c3]], [yv[c1][c1], yv[c1][c3]], color = 'k')
    plt.plot([xv[c1][c3], xv[c3][c3]], [yv[c1][c3], yv[c3][c3]], color = 'k')
    plt.plot([xv[c3][c1], xv[c3][c3]], [yv[c3][c1], yv[c3][c3]], color = 'k')

dirs = ['N', 'E']
i = 1
for y in range(dim):
    for x in range(dim):
        ax.text(x + .5, y + .5, (x,y), fontsize = 6, horizontalalignment = 'center', verticalalignment = 'center')
        i += 1
        if maze[x][y] == 0:
            dir = choice(dirs)
            if dir == 'N':
                plt.plot([xv[x][y], xv[x + 1][y + 1]], [yv[x + 1][y], yv[x + 1][y]], color = 'k')
            if dir == 'E':
                    plt.plot([xv[x][y + 1], xv[x + 1][y + 1]], [yv[x][y + 1], yv[x + 1][y + 1]], color = 'k')

plt.xticks(range(dim + 1))
plt.yticks(range(dim + 1))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Maze')
ax.set_aspect('equal', adjustable='box')
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
plt.show()