import matplotlib.pyplot as plt
import numpy as np


from Maze import Maze
maze=np.zeros(shape=(16,16))
start_point=np.array([0,0])
maze_generator=Maze(maze, start_point)
plt.imshow(maze_generator.maze)
plt.show()