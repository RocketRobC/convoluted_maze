from heapq import heappop, heappush
from math import inf

class AstarPath(object):
    def __init__(self, maze, start, target, heuristic, neighbour_offsets):
        self.maze = maze
        self.start = start
        self.target = target
        self.swag_on_path = {}
        self.path = {}
        self.distances = self.initialise_dist(maze)
        self.heuristic = heuristic
        self.count = 0
        self.neighbour_offsets = neighbour_offsets

    def initialise_dist(self, maze):
        distances = {}
        for row_idx in range(len(maze)):
            for cell_idx in range(len(maze[row_idx])):
                if maze[row_idx][cell_idx] != 'wall':
                    distances[(row_idx, cell_idx)] = inf
                    self.path[(row_idx, cell_idx)] = [(0,0)]
                    self.swag_on_path[(row_idx, cell_idx)] = []
        return distances

    def find_paths(self):
        self.distances[self.start] = 0
        self.path[self.start] = [self.start]
        cells_to_explore = [(0, self.start)]
        while cells_to_explore and self.distances[self.target] == inf:
            current_dist, current_cell = heappop(cells_to_explore)
            for neighbour in self.neighbours_for(current_cell):
                new_dist = current_dist + 1 + self.heuristic(neighbour, self.target)
                if new_dist < self.distances[neighbour]:
                    self.distances[neighbour] = new_dist
                    self.path[neighbour] = self.path[current_cell] + [neighbour]
                    self.swag_on_path[neighbour] = self.swag_on_path[current_cell] + self.cell_with_swag(neighbour)
                    heappush(cells_to_explore, (new_dist, neighbour))
                    self.count += 1

    def neighbours_for(self, cell):
        neighbours = []
        for direction in self.neighbour_offsets:
            offset = self.neighbour_offsets.get(direction)
            adjacent_cell = (offset[0] + cell[0], offset[1] + cell[1]) 
            if self.cell_within_maze(adjacent_cell):
                if self.maze[adjacent_cell[0]][adjacent_cell[1]] != 'wall':
                    neighbours.append(adjacent_cell)
        return neighbours

    def cell_with_swag(self, cell):
        value = self.maze[cell[0]][cell[1]]
        if value != 'End' and value != 'empty':
            return [value]
        else:
            return ['none']

    def cell_within_maze(self, cell):
        if cell[0] >= 0 and \
           cell[1] >= 0 and \
           cell[0] < len(self.maze) and \
           cell[1] < len(self.maze[0]):
            return True
        else:
            return False

    def swag_list_for(self, cell):
        return [i for i in self.swag_on_path[cell] if i != 'none']
