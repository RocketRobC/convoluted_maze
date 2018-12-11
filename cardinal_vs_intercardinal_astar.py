from lib.generate_maze import build_maze
from lib.printer import Printer
from lib.astar_path import AstarPath
from lib.heuristics import *
from lib.sorting import QuickSort
from lib.neighbour_offsets import complete, half
from lib.swag_formatter import SwagFormatter

swag = ['lamp', 'robot', 'ninja', 'book', 'sword']
maze_and_start = build_maze(25, 15, swag)
e = AstarPath(maze_and_start[0], maze_and_start[1], maze_and_start[2], euclidean, half)
m = AstarPath(maze_and_start[0], maze_and_start[1], maze_and_start[2], euclidean, complete)

printed_maze = Printer([row[:] for row in maze_and_start[0]])
e_print = Printer([row[:] for row in maze_and_start[0]])
m_print = Printer([row[:] for row in maze_and_start[0]])

e.find_paths()
m.find_paths()

printed_maze.print()
print()
print('--------------------------------------------------')
print()
print("Cardinal Directions")
print()
e_print.overlay_path(e.path.get(maze_and_start[2])).print()
print()
e_swag = e.swag_list_for(maze_and_start[2])
e_sorted_swag = SwagFormatter().format(QuickSort(e_swag, 0, len(e_swag) - 1).sort())
print('You collected the following items: {0}'.format(e_sorted_swag))
print("It took {0} cycles to find the shortest path".format(e.count))
print("The length of the path is {0} cells.".format(len(e.path.get(maze_and_start[2]))))
print()
print('Intercardinal Directions')
print()
m_print.overlay_path(m.path.get(maze_and_start[2])).print()
print()
m_swag = m.swag_list_for(maze_and_start[2])
m_sorted_swag = SwagFormatter().format(QuickSort(m_swag, 0, len(m_swag) - 1).sort())
print('You collected the following items: {0}'.format(m_sorted_swag))
print("It took {0} cycles to find the shortest path".format(m.count))
print("The length of the path is {0} cells.".format(len(m.path.get(maze_and_start[2]))))
