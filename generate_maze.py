from random import randint

def print_maze(grid):
  for row in grid:
    printable_row = ''
    for cell in row:
      if cell == 'wall':
        printable_row += '[#]'
      elif cell == 'empty':
        printable_row += '   '
      else:
        printable_row += " {0} ".format(cell[0])
    print(printable_row)
  
def mow(grid, i, j):
  directions = ['U', 'D', 'L', 'R']
  while (len(directions) > 0):
    direction_index = randint(0, len(directions) - 1)
    direction = directions.pop(direction_index) 
    if direction == 'U':
      if j - 2 < 0:
        continue
      elif grid[j - 2][i] == 'wall':
        grid[j - 1][i] = 'empty'
        grid[j - 2][i] = 'empty'
        mow(grid, i, j - 2)
    elif direction == 'D':
      if j + 2 >= len(grid):
        continue
      elif grid[j + 2][i] == 'wall':
        grid[j + 1][i] = 'empty'
        grid[j + 2][i] = 'empty'
        mow(grid, i, j + 2)
    elif direction == 'L':
      if i - 2 < 0:
        continue
      elif grid[j][i - 2] == 'wall':
        grid[j][i - 1] = 'empty'
        grid[j][i - 2] = 'empty'
        mow(grid, i - 2, j)
    else:
      if i + 2 >= len(grid[0]):
        continue
      elif grid[j][i + 2] == 'wall':
        grid[j][i + 1] = 'empty'
        grid[j][i + 2] = 'empty'
        mow(grid, i + 2, j)
        
def outside_grid(j, i, grid):
  if j < 0 or i < 0 or j >= len(grid) or i >= len(grid[0]):
    return True
  else:
    return False
  
def update_queue(j, i, grid, grid_copy):
    if grid_copy[j][i] != 'visited' and grid[j][i] != 'wall':
        return True
    else:
        return False

def explore_maze(grid, start_i, start_j, swag):
  grid_copy = [row[:] for row in grid]
  directions = ['U', 'D', 'L', 'R']
  queue = [[start_j, start_i]]
  while queue:
    j, i = queue.pop(0)
    if grid[j][i] != 'start' and randint(1, 10) == 5:
      grid[j][i] = swag[randint(0, len(swag) - 1)]
    grid_copy[j][i] = 'visited'
    for direction in directions:
      explore_j, explore_i = j, i
      if direction == 'U':
        explore_j = j - 1
      elif direction == 'D':
        explore_j = j + 1
      elif direction == 'L':
        explore_i = i - 1
      else:
        explore_i = i + 1

      if outside_grid(explore_j, explore_i, grid):
        continue
      elif update_queue(explore_j, explore_i, grid, grid_copy):
        queue.append([explore_j, explore_i])
   
  end = (j, i)
  grid[j][i] = 'End'
  return end
    
def build_maze(m, n, swag):
  grid = [['wall' for i in range(m)] for j in range(n)]
  start_i = randint(0, m - 1)
  start_j = randint(0, n - 1)
  grid[start_j][start_i] = 'start'
  mow(grid, start_i, start_j)
  end = explore_maze(grid, start_i, start_j, swag)
  return [grid, (start_j, start_i), end]
  

swag = ['giraffe', 'watch', 'cat', 'dog']
# maze = build_maze(25, 15, swag)
# print(maze[0])
# print_maze(maze[0])
