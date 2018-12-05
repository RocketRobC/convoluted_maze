import generate_maze
import generate_landscape
from printer import Printer
from dijkstras_path import DijkstrasPath
from astar_path import AstarPath
from heuristics import *

swag = ['beyblade', 'robot', 'ninja', 'book']
maze_and_start = generate_landscape.build_maze(25, 15, swag)
d = DijkstrasPath(maze_and_start[0], maze_and_start[1])
a = AstarPath(maze_and_start[0], maze_and_start[1], maze_and_start[2], euclidean)

printed_maze = Printer([row[:] for row in maze_and_start[0]])
d_print = Printer([row[:] for row in maze_and_start[0]])
a_print = Printer([row[:] for row in maze_and_start[0]])

d.find_paths()
a.find_paths()

printed_maze.print()
print()
print('--------------------------------------------------')
print()
print("Dijkstra's")
print()
d_print.overlay_path(d.path.get(maze_and_start[2])).print()
print()
print('You collected the following items: {0}'.format(d.swag_list_for(maze_and_start[2])))
print()
print('AStar')
print()
a_print.overlay_path(a.path.get(maze_and_start[2])).print()
print()
# print(d.distances)
# print(maze_and_start[2])
# print("The shortest path from Start to End takes {0} moves".format(a.count))
print('You collected the following items: {0}'.format(a.swag_list_for(maze_and_start[2])))
