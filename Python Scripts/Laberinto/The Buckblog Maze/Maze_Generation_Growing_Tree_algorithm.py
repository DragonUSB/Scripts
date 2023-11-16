import random

# 1. Allow the maze to be customized via command-line parameters
width = int(input("Enter width: "))
height = int(input("Enter height: "))
mode = input("Enter mode (random, newest, middle, oldest): ")
seed = random.randint(0, 0xFFFF_FFFF)
random.seed(seed)
grid = [[0] * width for _ in range(height)]

# 2. Set up constants to aid with describing the passage directions
N, S, E, W = 1, 2, 4, 8
DX = {E: 1, W: -1, N: 0, S: 0}
DY = {E: 0, W: 0, N: -1, S: 1}
OPPOSITE = {E: W, W: E, N: S, S: N}

# 3. Data structures to assist the algorithm
class Script:
    def __init__(self, arg):
        self.commands = [self.parse_command(cmd) for cmd in arg.split(";")]
        self.current = 0
    
    def parse_command(self, cmd):
        total_weight = 0
        parts = []
        for element in cmd.split(","):
            # name, weight = element.split(":")
            name = mode
            weight = 25
            weight = int(weight) if weight else 100
            if name not in ["random", "newest", "middle", "oldest"]:
                raise ValueError(f"commands must be random, newest, middle, or oldest (was {name})")
            total_weight += weight
            parts.append({"name": name, "weight": total_weight})
        return {"total": total_weight, "parts": parts}
    
    def next_index(self, ceil):
        command = self.commands[self.current]
        self.current = (self.current + 1) % len(self.commands)
        v = random.randint(0, command["total"] - 1)
        for part in command["parts"]:
            if v < part["weight"]:
                if part["name"] in ["random", "r"]:
                    return random.randint(0, ceil - 1)
                elif part["name"] in ["newest", "n"]:
                    return ceil - 1
                elif part["name"] in ["middle", "m"]:
                    return ceil // 2
                elif part["name"] in ["oldest", "o"]:
                    return 0
        raise ValueError(f"[bug] failed to find index ({v} of {command})")
    
    def __str__(self):
        return ";".join([",".join([f"{part['name']}:{part['weight'] - v}" for part in command["parts"]]) for command in self.commands])

cells = []
script = Script(mode)

# 4. A simple routine to emit the maze as ASCII
def display_maze(grid):
    print(" " + "_" * (len(grid[0]) * 2 - 1))
    for row in grid:
        print("|", end="")
        for cell in row:
            if cell == 0:
                print(" " if row.index(cell) + 1 < len(row) and row[row.index(cell) + 1] == 0 else "_", end="")
            else:
                print(" " if cell & S != 0 else "_", end="")
            if cell == 0:
                print(" " if row.index(cell) + 1 < len(row) and (row[row.index(cell) + 1] == 0 or grid[grid.index(row) + 1][row.index(cell)] == 0) else "_", end="")
            elif cell & E != 0:
                print(" " if (cell | row[row.index(cell) + 1]) & S != 0 else "_", end="")
            else:
                print("|", end="")
        print()

# 5. Growing Tree algorithm
print("\033[2J", end="") # clear the screen
display_maze(grid)
x, y = random.randint(0, width - 1), random.randint(0, height - 1)
cells.append([x, y])
while cells:
    index = script.next_index(len(cells))
    x, y = cells[index]
    for dir in random.sample([N, S, E, W], 4):
        nx, ny = x + DX[dir], y + DY[dir]
        if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == 0:
            grid[y][x] |= dir
            grid[ny][nx] |= OPPOSITE[dir]
            cells.append([nx, ny])
            index = None
            display_maze(grid)
            break
    if index is not None:
        cells.pop(index)
display_maze(grid)

# 5. Show the parameters used to build this maze, for repeatability
print(f"python growing-tree.py {width} {height} {script} {seed}")