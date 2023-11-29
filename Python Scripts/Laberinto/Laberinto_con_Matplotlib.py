import matplotlib.pyplot as pyplot
from random import randint, seed

size_x = 16
size_y = 16

#seed(1)

scale = max(size_x, size_y) / 8

pyplot.figure(figsize=(size_x/scale, size_y/scale))
# pyplot.xticks([])
# pyplot.yticks([])
pyplot.style.use('dark_background')
pyplot.xlim(-1, size_x + 1)
pyplot.ylim(-1, size_y + 1)
# pyplot.axis('equal')
ax = pyplot.gca()
ax.set_aspect('equal', adjustable='box')

def line(x1, y1, x2, y2):
  pyplot.plot([x1, x2], [y1, y2], color='white')

def clearLine(x1, y1, x2, y2):
  pyplot.plot([x1, x2], [y1, y2], color='black')

# maze's border
def drawMazeBorder():
  line(0, 0, size_x, 0)
  line(0, 0, 0, size_y)
  line(size_x, 0, size_x, size_y)
  line(0, size_y, size_x, size_y)

# True or False if cell was visited, visited[x][y] = False
visitedMaze = [ [ False for y in range( size_y ) ] for x in range( size_x ) ]

# stack of visited cells; each item is [x, y]
visitedCells = []

# maze's start and goal
visitedMaze[0][0] = True
visitedCells.append([0, 0])
visitedMaze[7][7] = True
visitedCells.append([7, 7])
visitedMaze[7][8] = True
visitedCells.append([7, 8])
visitedMaze[8][7] = True
visitedCells.append([8, 7])
visitedMaze[8][8] = True
visitedCells.append([8, 8])

def visitCell(x, y):
  visitedMaze[x][y] = True
  visitedCells.append([x, y])

def getValidDirections(x, y):
  validDirections = []

  if (validCell(x, y + 1)):
    validDirections.append([x, y + 1])
  if (validCell(x + 1, y)):
    validDirections.append([x + 1, y])
  if (validCell(x, y - 1)):
    validDirections.append([x, y - 1])
  if (validCell(x - 1, y)):
    validDirections.append([x - 1, y])

  return validDirections

def getNextCell(x, y):
  validDirections = getValidDirections(x, y)
  
  if len(validDirections) == 0:
    return [-1, -1]

  dir = randint(0, len(validDirections) - 1)
  return validDirections[dir]


def validCell(x, y):
  if x < 0 or y < 0:
    return False
  if x >= size_x or y >= size_y:
    return False
  if visitedMaze[x][y]:
    return False
  return True

def drawClosedCell(x, y):
  line(x, y + 1, x + 1, y + 1)
  line(x, y, x + 1, y)
  line(x + 1, y, x + 1, y + 1)
  line(x, y, x, y + 1)

def drawOpening(old_x, old_y, new_x, new_y):  
  if old_x == new_x:
    # only Y changed
    if old_y < new_y:
      clearLine(old_x, old_y + 1, old_x + 1, old_y + 1)
    else:
      clearLine(old_x, old_y, old_x + 1, old_y)
  else:
    # only X changed
    if old_x < new_x:
      clearLine(old_x + 1, old_y, old_x + 1, old_y + 1)
    else:
      clearLine(old_x, old_y, old_x, old_y + 1)

def generateMaze():
  # starting cell
  x = randint(0, size_x - 1)
  y = randint(0, size_y - 1)

  # drawClosedCell(x, y)
  drawClosedCell(1, 1)

  while True:
    visitCell(x, y)
    #pyplot.savefig('maze\maze_{0:03}.png'.format(step))
    
    [new_x, new_y] = getNextCell(x, y)
    
    if new_x == -1:
      # no direction is possible, go back
      if len(visitedCells) <= 1:
        # no more options - maze is complete
        break
      removeCurrentCellAndIgnoreIt = visitedCells.pop()
      previousCell = visitedCells.pop()
      
      x = previousCell[0]
      y = previousCell[1]

    else:
      drawClosedCell(new_x, new_y)
      drawOpening(x, y, new_x, new_y)
      x = new_x
      y = new_y

drawMazeBorder()
generateMaze()
goal = randint(1,8)
# print(goal)
if goal == 1:
  clearLine(7, 7, 7, 8)
elif goal == 2:
  clearLine(7, 8, 7, 9)
elif goal == 3:
  clearLine(7, 9, 8, 9)
elif goal == 4:
  clearLine(8, 9, 9, 9)
elif goal == 5:
  clearLine(9, 9, 8, 9)
elif goal == 6:
  clearLine(8, 9, 7, 9)
elif goal == 7:
  clearLine(7, 9, 7, 8)
else:
  clearLine(7, 8, 7, 7)
clearLine(0, 1, 1, 1)
mng = pyplot.get_current_fig_manager()
mng.window.state('zoomed')
pyplot.show()