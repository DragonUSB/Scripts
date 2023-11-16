import random

# 1. Allow the maze to be customized via command-line parameters
width = int(input("Enter width: "))
height = int(input("Enter height: "))
seed = int(input("Enter seed: "))
random.seed(seed)
grid = [[0] * width for _ in range(height)]

# 2. Set up constants to aid with describing the passage directions
N, S, E, W = 1, 2, 4, 8
IN = 0x10
DX = {E: 1, W: -1, N: 0, S: 0}
DY = {E: 0, W: 0, N: -1, S: 1}
OPPOSITE = {E: W, W: E, N: S, S: N}

# 3. A simple routine to emit the maze as ASCII
def display_maze(grid, cy=None):
    print(" " + "_" * (len(grid[0]) * 2 - 1))
    for y, row in enumerate(grid):
        print("|", end="")
        for x, cell in enumerate(row):
            if cy == y:
                print("\033[43m", end="")  # cursor is yellow
            if cell == 0 and y + 1 < len(grid) and grid[y + 1][x] == 0:
                print(" ", end="")
            else:
                print(" " if cell & S != 0 else "_", end="")
            if cy == y:
                print("\033[0m", end="")
            if cell == 0 and x + 1 < len(row) and row[x + 1] == 0:
                print(" " if y + 1 < len(grid) and (grid[y + 1][x] == 0 or grid[y + 1][x + 1] == 0) else "_", end="")
            elif cell & E != 0:
                print(" " if (cell | row[x + 1]) & S != 0 else "_", end="")
            else:
                print("|", end="")
        print()

# 4. Hunt and Kill algorithm
def walk(grid, x, y):
    directions = [N, S, E, W]
    random.shuffle(directions)
    for dir in directions:
        nx, ny = x + DX[dir], y + DY[dir]
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] == 0:
            grid[y][x] |= dir
            grid[ny][nx] |= OPPOSITE[dir]
            return nx, ny
    return None

def hunt(grid):
    for y, row in enumerate(grid):
        display_maze(grid, y)
        row = enumerate(row)
        for x, cell in row:
            if cell == 0:
                neighbors = []
                if y > 0 and grid[y - 1][x] != 0:
                    neighbors.append(N)
                if x > 0 and grid[y][x - 1] != 0:
                    neighbors.append(W)
                if x + 1 < len(grid[y]) and grid[y][x + 1] != 0:
                    neighbors.append(E)
                if y + 1 < len(grid) and grid[y + 1][x] != 0:
                    neighbors.append(S)
                if neighbors:
                    direction = random.choice(neighbors)
                    nx, ny = x + DX[direction], y + DY[direction]
                    grid[y][x] |= direction
                    grid[ny][nx] |= OPPOSITE[direction]
                    return x, y
    return None

print("\033[2J", end="")  # clear the screen
x, y = random.randint(0, width - 1), random.randint(0, height - 1)
while True:
    display_maze(grid)
    x, y = walk(grid, x, y)
    if not x:
        x, y = hunt(grid)
    if not x:
        break
display_maze(grid)

# 5. Show the parameters used to build this maze, for repeatability
print(f"{width} {height} {seed}")