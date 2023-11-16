import random

# 1. Allow the maze to be customized via command-line parameters
width = int(input("Enter width: ") or 10)
height = int(input("Enter height: ") or width)
seed = int(input("Enter seed: ") or random.randint(0, 0xFFFF_FFFF))
random.seed(seed)
grid = [[0] * width for _ in range(height)]

# 2. Set up constants to aid with describing the passage directions
S, E = 1, 2
HORIZONTAL, VERTICAL = 1, 2

# 3. Helper routines
def display_maze(grid):
    print(" " + "_" * (len(grid[0]) * 2 - 1))
    for y, row in enumerate(grid):
        print("|", end="")
        for x, cell in enumerate(row):
            bottom = y + 1 >= len(grid)
            south = (cell & S != 0 or bottom)
            south2 = (x + 1 < len(grid[y]) and grid[y][x + 1] & S != 0 or bottom)
            east = (cell & E != 0 or x + 1 >= len(grid[y]))
            print("_" if south else " ", end="")
            print("|" if east else "_" if south and south2 else " ", end="")
        print()

def choose_orientation(width, height):
    if width < height:
        return HORIZONTAL
    elif height < width:
        return VERTICAL
    else:
        return HORIZONTAL if random.randint(0, 1) == 0 else VERTICAL

# 4. The recursive-division algorithm itself
def divide(grid, x, y, width, height, orientation):
    if width < 2 or height < 2:
        return
    display_maze(grid)
    # sleep(0.02)
    horizontal = orientation == HORIZONTAL
    # where will the wall be drawn from?
    wx = x + (0 if horizontal else random.randint(0, width - 2))
    wy = y + (random.randint(0, height - 2) if horizontal else 0)
    # where will the passage through the wall exist?
    px = wx + (random.randint(0, width - 1) if horizontal else 0)
    py = wy + (0 if horizontal else random.randint(0, height - 1))
    # what direction will the wall be drawn?
    dx = 1 if horizontal else 0
    dy = 0 if horizontal else 1
    # how long will the wall be?
    length = width if horizontal else height
    # what direction is perpendicular to the wall?
    dir = S if horizontal else E
    for _ in range(length):
        if wx != px or wy != py:
            grid[wy][wx] |= dir
        wx += dx
        wy += dy
    nx, ny = x, y
    w, h = (width, wy - y + 1) if horizontal else (wx - x + 1, height)
    divide(grid, nx, ny, w, h, choose_orientation(w, h))
    nx, ny = (x, wy + 1) if horizontal else (wx + 1, y)
    w, h = (width, y + height - wy - 1) if horizontal else (x + width - wx - 1, height)
    divide(grid, nx, ny, w, h, choose_orientation(w, h))

print("\033[2J") # clear screen
divide(grid, 0, 0, width, height, choose_orientation(width, height))
display_maze(grid)

# 5. Show the parameters used to build this maze, for repeatability
print(f"{width} {height} {seed}")