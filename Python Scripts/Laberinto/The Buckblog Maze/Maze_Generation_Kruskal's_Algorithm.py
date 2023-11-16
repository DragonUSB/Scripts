# --------------------------------------------------------------------
# An implementation of Kruskal's algorithm for generating mazes.
# Fairly expensive, memory-wise, as it requires memory proportional
# to the size of the entire maze, and it's not the fastest of the
# algorithms (what with all the set and edge management is has to
# do). Also, the mazes it generates tend to have a lot of very short
# dead-ends, giving the maze a kind of "spiky" look.
# --------------------------------------------------------------------
# NOTE: the display routine used in this script requires a terminal
# that supports ANSI escape sequences. Windows users, sorry. :(
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# 1. Allow the maze to be customized via command-line parameters
# --------------------------------------------------------------------
import sys
import random
import time

width = int(sys.argv[1]) if len(sys.argv) > 1 else 10
height = int(sys.argv[2]) if len(sys.argv) > 2 else width
seed = int(sys.argv[3]) if len(sys.argv) > 3 else random.randint(0, 0xFFFF_FFFF)
delay = float(sys.argv[4]) if len(sys.argv) > 4 else 0.01
random.seed(seed)
# --------------------------------------------------------------------
# 2. Set up constants to aid with describing the passage directions
# --------------------------------------------------------------------
N, S, E, W = 1, 2, 4, 8
DX = {E: 1, W: -1, N: 0, S: 0}
DY = {E: 0, W: 0, N: -1, S: 1}
OPPOSITE = {E: W, W: E, N: S, S: N}
# --------------------------------------------------------------------
# 3. Data structures and methods to assist the algorithm
# --------------------------------------------------------------------
def display_maze(grid):
    print("\033[H")  # move to upper-left
    print(" " + "_" * (len(grid[0]) * 2 - 1))
    for y, row in enumerate(grid):
        print("|", end="")
        for x, cell in enumerate(row):
            if cell == 0:
                print("\033[47m", end="")
            print(" " if cell & S != 0 else "_", end="")
            if cell & E != 0:
                print(" " if (cell | row[x + 1]) & S != 0 else "_", end="")
            else:
                print("|", end="")
            if cell == 0:
                print("\033[m", end="")
        print()
grid = [[0] * width for _ in range(height)]
sets = [[Tree() for _ in range(width)] for _ in range(height)]
# build the list of edges
edges = []
for y in range(height):
    for x in range(width):
        if y > 0:
            edges.append([x, y, N])
        if x > 0:
            edges.append([x, y, W])
edges.sort(key=lambda x: random.random())
# --------------------------------------------------------------------
# 4. Kruskal's algorithm
# --------------------------------------------------------------------
print("\033[2J")  # clear the screen
while edges:
    x, y, direction = edges.pop()
    nx, ny = x + DX[direction], y + DY[direction]
    set1, set2 = sets[y][x], sets[ny][nx]
    if not set1.connected(set2):
        display_maze(grid)
        time.sleep(delay)
        set1.connect(set2)
        grid[y][x] |= direction
        grid[ny][nx] |= OPPOSITE[direction]
display_maze(grid)
# --------------------------------------------------------------------
# 5. Show the parameters used to build this maze, for repeatability
# --------------------------------------------------------------------
print(f"{sys.argv[0]} {width} {height} {seed}")