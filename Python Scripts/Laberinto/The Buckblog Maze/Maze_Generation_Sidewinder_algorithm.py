import random
import time

# An implementation of the Sidewinder algorithm for maze generation.
# This algorithm is kind of a cross between the trivial Binary Tree
# algorithm, and Eller's algorithm. Like the Binary Tree algorithm,
# the result is biased (but not as heavily).
#
# Because the Sidewinder algorithm only needs to consider the current
# row, it can be used (like the Binary Tree and Eller's algorithms)
# to generate infinitely large mazes.

# Allow the maze to be customized via command-line parameters
width = int(input("Enter width of the maze: ") or 10)
height = int(input("Enter height of the maze: ") or width)
weight = int(input("Enter weight: ") or 2)
seed = int(input("Enter seed: ") or random.randint(0, 0xFFFF_FFFF))

random.seed(seed)

# Set up constants to aid with describing the passage directions
N, S, E, W = 1, 2, 4, 8

# Data structures to assist the algorithm
grid = [[0 for _ in range(width)] for _ in range(height)]

# A simple routine to emit the maze as ASCII
def display_maze(grid):
    print(" " + "_" * (len(grid[0]) * 2 - 1))
    for y, row in enumerate(grid):
        print("|", end="")
        for x, cell in enumerate(row):
            if cell == 0 and y+1 < len(grid) and grid[y+1][x] == 0:
                print(" ", end="")
            else:
                print(" " if cell & S != 0 else "_", end="")

            if cell == 0 and x+1 < len(row) and row[x+1] == 0:
                print(" " if y+1 < len(grid) and (grid[y+1][x] == 0 or grid[y+1][x+1] == 0) else "_", end="")
            elif cell & E != 0:
                print(" " if (cell | row[x+1]) & S != 0 else "_", end="")
            else:
                print("|", end="")
        print()

# Sidewinder algorithm
print("\033[2J")  # clear the screen

for y in range(height):
    run_start = 0
    for x in range(width):
        display_maze(grid)
        time.sleep(0.02)

        if y > 0 and (x+1 == width or random.randint(0, weight) == 0):
            cell = run_start + random.randint(0, x - run_start)
            grid[y][cell] |= N
            grid[y-1][cell] |= S
            run_start = x+1
        elif x+1 < width:
            grid[y][x] |= E
            grid[y][x+1] |= W

display_maze(grid)

# Show the parameters used to build this maze, for repeatability
print(f"Parameters used: width={width}, height={height}, seed={seed}")