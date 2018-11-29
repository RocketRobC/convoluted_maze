import generate_maze
from printer import Printer
from dijkstras_path import DijkstrasPath

swag = ['phone', 'tablet', 'ninja']
maze_and_start = generate_maze.build_maze(25, 15, swag)
d = DijkstrasPath(maze_and_start[0], maze_and_start[1])
paths = d.find_paths()
Printer(maze_and_start[0]).print()
print()
print('--------------------------------------------------')
print()
Printer(maze_and_start[0]).overlay_path(d.path.get(maze_and_start[2])).print()
print()
print("The shortest path from Start to End takes {0} moves".format(d.distances[(maze_and_start[2])]))
print('You collected the following items: {0}'.format(d.swag_list_for(maze_and_start[2])))
