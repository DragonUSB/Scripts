import random

# 1. Allow the maze to be customized via command-line parameters
width = int(input("Enter the width of the maze: "))
height = int(input("Enter the height of the maze: "))
seed = int(input("Enter the seed for random number generation: "))
random.seed(seed)
grid = [[0] * width for _ in range(height)]

# 2. Set up constants to aid with describing the passage directions
N, S, E, W = 1, 2, 4, 8
DX = {E: 1, W: -1, N: 0, S: 0}
DY = {E: 0, W: 0, N: -1, S: 1}
OPPOSITE = {E: W, W: E, N: S, S: N}

# 3. A simple routine to emit the maze as ASCII
def display_maze(grid, cx=None, cy=None):
    print(" " + "_" * (len(grid[0]) * 2 - 1))
    for y, row in enumerate(grid):
        print("|", end="")
        for x, cell in enumerate(row):
            if cx == x and cy == y:
                print("\033[43m", end="")  # cursor is yellow
            elif cell == 0:
                print("\033[47m", end="")  # unvisited is white
            print(" " if cell & S != 0 else "_", end="")
            print("\033[0m", end="")
            if cell & E != 0:
                print(" " if (cell | row[x+1]) & S != 0 else "_", end="")
            else:
                print("|", end="")
        print()

# 4. The Aldous-Broder algorithm
print("\033[2J")  # clear screen
x, y = random.randint(0, width-1), random.randint(0, height-1)
remaining = width * height - 1
while remaining > 0:
    display_maze(grid, x, y)
    # sleep 0.02
    directions = [N, S, E, W]
    random.shuffle(directions)
    for dir in directions:
        nx, ny = x + DX[dir], y + DY[dir]
        if 0 <= nx < width and 0 <= ny < height:
            if grid[ny][nx] == 0:
                grid[y][x] |= dir
                grid[ny][nx] |= OPPOSITE[dir]
                remaining -= 1
            x, y = nx, ny
            break

display_maze(grid)

# 5. Show the parameters used to build this maze, for repeatability
print(f"{width} {height} {seed}")