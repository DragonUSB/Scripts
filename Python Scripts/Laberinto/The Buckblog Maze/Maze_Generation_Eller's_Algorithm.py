import random

# 1. Allow the maze to be customized via command-line parameters
width = int(input("Enter the width of the maze: "))
height = int(input("Enter the height of the maze: "))
seed = int(input("Enter the seed for random number generation: "))
random.seed(seed)

# 2. Set up constants to aid with describing the passage directions
S, E = 1, 2

# 3. Data structures to assist the algorithm
class State:
    def __init__(self, width, next_set=-1):
        self.width = width
        self.next_set = next_set
        self.sets = {}
        self.cells = {}

    def next(self):
        return State(self.width, self.next_set)

    def populate(self):
        for cell in range(self.width):
            if cell not in self.cells:
                set_id = self.next_set + 1
                self.sets[set_id] = [cell]
                self.cells[cell] = set_id
        return self

    def merge(self, sink_cell, target_cell):
        sink = self.cells[sink_cell]
        target = self.cells[target_cell]
        self.sets[sink].extend(self.sets[target])
        for cell in self.sets[target]:
            self.cells[cell] = sink
        del self.sets[target]

    def same(self, cell1, cell2):
        return self.cells[cell1] == self.cells[cell2]

    def add(self, cell, set_id):
        self.cells[cell] = set_id
        self.sets[set_id].append(cell)
        return self

    def each_set(self):
        for set_id, set_cells in self.sets.items():
            yield set_id, set_cells

def row2str(row, last=False):
    s = "\r|"
    for index, cell in enumerate(row):
        south = bool(cell & S)
        next_south = bool(row[index+1] & S) if index+1 < len(row) else False
        east = bool(cell & E)
        s += " " if south else "_"
        if east:
            s += " " if south or next_south else "_"
        else:
            s += "|"
    return s

state = State(width).populate()
print(state)
row_count = 0

# 4. Eller's algorithm
def step(state, finish=False):
    connected_sets = []
    connected_set = [0]

    # create the set of horizontally connected corridors in this row
    for c in range(state.width-1):
        if state.same(c, c+1) or (not finish and random.randint(0, 1)):
            connected_sets.append(connected_set)
            connected_set = [c+1]
        else:
            state.merge(c, c+1)
            connected_set.append(c+1)
    connected_sets.append(connected_set)

    # create the set of vertically connected corridors from this row, but only if this is not the last row
    verticals = []
    next_state = state.next()
    if not finish:
        for set_id, set_cells in state.each_set():
            cells_to_connect = random.sample(set_cells, 1 + random.randint(0, len(set_cells)-1))
            verticals.extend(cells_to_connect)
            for cell in cells_to_connect:
                next_state.add(cell, set_id)

    # translate the connected sets and verticals into a bitmap that can be returned and displayed
    row = []
    for connected_set in connected_sets:
        for index, cell in enumerate(connected_set):
            last = (index+1 == len(connected_set))
            map = 0 if last else E
            map |= S if cell in verticals else 0
            row.append(map)

    return next_state.populate(), row

# allow ctrl-c to stop the program gracefully, letting the final row be generated and displayed before aborting.
spinning = True
def stop_spinning(signal, frame):
    global spinning
    spinning = False
import signal
signal.signal(signal.SIGINT, stop_spinning)

print(" " + "_" * (width * 2 - 1))
while spinning:
    state, row = step(state)
    row_count += 1
    print(row2str(row))
    spinning = row_count+1 < height if height else False

state, row = step(state, True)
row_count += 1
print(row2str(row))

# 5. Show the parameters used to build this maze, for repeatability
print(f"{__file__} {width} {row_count} {seed}")