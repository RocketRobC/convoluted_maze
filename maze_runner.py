from lib.generate_maze import build_maze
from lib.printer import Printer
from lib.dijkstras_path import DijkstrasPath
from lib.astar_path import AstarPath
from lib.heuristics import *
from lib.sorting import QuickSort
from lib.neighbour_offsets import complete, half
from lib.swag_formatter import SwagFormatter

swag = ['lamp', 'robot', 'ninja', 'book', 'sword']
maze_and_start = build_maze(25, 15, swag)
d = DijkstrasPath(maze_and_start[0], maze_and_start[1], half)
a = AstarPath(maze_and_start[0], maze_and_start[1], maze_and_start[2], euclidean, half)

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
d_swag = d.swag_list_for(maze_and_start[2])
d_sorted_swag = SwagFormatter().format(QuickSort(d_swag, 0, len(d_swag) - 1).sort())
print('You collected the following items: {0}'.format(d_sorted_swag))
print("It took {0} cycles to find the shortest path".format(d.count))
print()
print('AStar')
print()
a_print.overlay_path(a.path.get(maze_and_start[2])).print()
print()
a_swag = a.swag_list_for(maze_and_start[2])
a_sorted_swag = SwagFormatter().format(QuickSort(a_swag, 0, len(a_swag) - 1).sort())
print('You collected the following items: {0}'.format(a_sorted_swag))
print("It took {0} cycles to find the shortest path".format(a.count))
