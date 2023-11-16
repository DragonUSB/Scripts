import random

# 1. Allow the maze to be customized via command-line parameters
import sys
width = int(sys.argv[1]) if len(sys.argv) > 1 else 25
height = int(sys.argv[2]) if len(sys.argv) > 2 else width
seed = int(sys.argv[3]) if len(sys.argv) > 3 else random.randint(0, 0xFFFF_FFFF)
random.seed(seed)
grid = [[0] * width for _ in range(height)]

# 2. Set up constants to aid with describing the passage directions
N, S, E, W = 1, 2, 4, 8
DX = {E: 1, W: -1, N: 0, S: 0}
DY = {E: 0, W: 0, N: -1, S: 1}
OPPOSITE = {E: W, W: E, N: S, S: N}

# 3. The recursive-backtracking algorithm itself
def carve_passages_from(cx, cy, grid):
    directions = [N, S, E, W]
    # random.shuffle(directions)
    for direction in directions:
        nx, ny = cx + DX[direction], cy + DY[direction]
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]) and grid[ny][nx] == 0:
            grid[cy][cx] |= direction
            grid[ny][nx] |= OPPOSITE[direction]
            carve_passages_from(nx, ny, grid)

carve_passages_from(0, 0, grid)

# 4. A simple routine to emit the maze as ASCII
print(" " + "_" * (width * 2 - 1))
for y in range(height):
    row = "|"
    for x in range(width):
        row += " " if grid[y][x] & S != 0 else "_"
        if grid[y][x] & E != 0:
            row += " " if (grid[y][x] | grid[y][x+1]) & S != 0 else "_"
        else:
            row += "|"
    print(row)

# 5. Show the parameters used to build this maze, for repeatability
print(f"{sys.argv[0]} {width} {height} {seed}")