import random
import time

# 1. Allow the maze to be customized via command-line parameters
width = int(input("Enter the width of the maze: "))
height = int(input("Enter the height of the maze: "))
seed = int(input("Enter the seed for random number generation: "))
random.seed(seed)

# 2. Set up constants to aid with describing the passage directions
N, S, E, W = 1, 2, 4, 8
IN = 0x10
FRONTIER = 0x20
OPPOSITE = {E: W, W: E, N: S, S: N}

# 3. Data structures and methods to assist the algorithm
grid = [[0] * width for _ in range(height)]
frontier = []

def add_frontier(x, y, grid, frontier):
    if 0 <= x < width and 0 <= y < height and grid[y][x] == 0:
        grid[y][x] |= FRONTIER
        frontier.append((x, y))

def mark(x, y, grid, frontier):
    grid[y][x] |= IN
    add_frontier(x-1, y, grid, frontier)
    add_frontier(x+1, y, grid, frontier)
    add_frontier(x, y-1, grid, frontier)
    add_frontier(x, y+1, grid, frontier)

def neighbors(x, y, grid):
    n = []
    if x > 0 and grid[y][x-1] & IN != 0:
        n.append((x-1, y))
    if x+1 < width and grid[y][x+1] & IN != 0:
        n.append((x+1, y))
    if y > 0 and grid[y-1][x] & IN != 0:
        n.append((x, y-1))
    if y+1 < height and grid[y+1][x] & IN != 0:
        n.append((x, y+1))
    return n

def direction(fx, fy, tx, ty):
    if fx < tx:
        return E
    elif fx > tx:
        return W
    elif fy < ty:
        return S
    elif fy > ty:
        return N

# 4. Routines for displaying the maze
def empty(cell):
    return cell == 0 or cell == FRONTIER

def display_maze(grid):
    print(" " + "_" * (width * 2 - 1))
    for y, row in enumerate(grid):
        print("|", end="")
        for x, cell in enumerate(row):
            if cell == FRONTIER:
                print("\033[41m", end="")
            if empty(cell) and y+1 < height and empty(grid[y+1][x]):
                print(" ", end="")
            else:
                print(" " if cell & S != 0 else "_", end="")
            if cell == FRONTIER:
                print("\033[m", end="")
            if empty(cell) and x+1 < len(row) and empty(row[x+1]):
                print(" " if y+1 < height and (empty(grid[y+1][x]) or empty(grid[y+1][x+1])) else "_", end="")
            elif cell & E != 0:
                print(" " if (cell | row[x+1]) & S != 0 else "_", end="")
            else:
                print("|", end="")
        print()

# 5. Prim's algorithm
mark(random.randint(0, width-1), random.randint(0, height-1), grid, frontier)
while frontier:
    x, y = frontier.pop(random.randint(0, len(frontier)-1))
    n = neighbors(x, y, grid)
    nx, ny = n[random.randint(0, len(n)-1)]
    dir = direction(x, y, nx, ny)
    grid[y][x] |= dir
    grid[ny][nx] |= OPPOSITE[dir]
    mark(x, y, grid, frontier)
    display_maze(grid)
    time.sleep(0.01)

display_maze(grid)

# 6. Show the parameters used to build this maze, for repeatability
print(f"python {__file__} {width} {height} {seed}")