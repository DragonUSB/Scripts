import random
import time

# An implementation of the "Binary Tree" algorithm for generating mazes
def binary_tree_maze(width=10, height=None, seed=None):
    """
    Generate a maze using the Binary Tree algorithm.

    Args:
    - width (int): Width of the maze
    - height (int): Height of the maze (default is same as width)
    - seed (int): Seed for random number generation

    Returns:
    - grid (list): 2D list representing the maze
    """

    # Set default height if not provided
    if height is None:
        height = width

    # Set seed for random number generation
    if seed is not None:
        random.seed(seed)

    # Set up constants to aid with describing the passage directions
    N, S, E, W = 1, 2, 4, 8
    DX = {E: 1, W: -1, N: 0, S: 0}
    DY = {E: 0, W: 0, N: -1, S: 1}
    OPPOSITE = {E: W, W: E, N: S, S: N}

    # Data structures to assist the algorithm
    grid = [[0 for _ in range(width)] for _ in range(height)]

    # A simple routine to emit the maze as ASCII
    def display_maze(grid):
        print(" " + "_" * (len(grid[0]) * 2 - 1))
        for y, row in enumerate(grid):
            line = "|"
            for x, cell in enumerate(row):
                if cell == 0 and y + 1 < len(grid) and grid[y + 1][x] == 0:
                    line += " "
                else:
                    line += " " if cell & S != 0 else "_"

                if cell == 0 and x + 1 < len(row) and row[x + 1] == 0:
                    line += " " if y + 1 < len(grid) and (grid[y + 1][x] == 0 or grid[y + 1][x + 1] == 0) else "_"
                elif cell & E != 0:
                    line += " " if (cell | row[x + 1]) & S != 0 else "_"
                else:
                    line += "|"
            print(line)

    # Binary Tree algorithm
    print("\033[2J")  # clear the screen
    for y in range(height):
        for x in range(width):
            display_maze(grid)
            time.sleep(0.02)

            dirs = []

            if y > 0:
                dirs.append(N)
            if x > 0:
                dirs.append(W)

            if dirs:
                dir = random.choice(dirs)
                nx, ny = x + DX[dir], y + DY[dir]
                grid[y][x] |= dir
                grid[ny][nx] |= OPPOSITE[dir]

    display_maze(grid)

    # Show the parameters used to build this maze, for repeatability
    print(f"{__file__} {width} {height} {seed}")

    return grid

# Example usage
maze = binary_tree_maze(25, 25, 123)