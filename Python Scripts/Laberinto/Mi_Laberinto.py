import numpy as np
import matplotlib.pyplot as plt

dim = 16

maze = np.zeros((dim, dim), dtype = int)

x = np.arange(0, dim + 1, 1)
y = np.arange(0, dim + 1, 1)
xv, yv = np.meshgrid(x, y)

plt.plot(xv, yv, marker = '.', color = 'k', linestyle = 'none')
plt.xticks(range(dim + 1))
plt.yticks(range(dim + 1))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Maze')
plt.show()

# Pared Exterior del Laberinto
for i in range(dim + 1):
    for j in range(dim):
        if (i == 0 or i == dim):
            plt.plot(xv[i], yv[i], color = 'k')
        else:
            plt.plot([xv[0][0], xv[0][0]], [yv[j][0], yv[j + 1][0]], color = 'k')
            plt.plot([xv[0][dim], xv[0][dim]], [yv[j][dim], yv[j + 1][dim]], color = 'k')
plt.show()