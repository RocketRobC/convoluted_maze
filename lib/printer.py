from math import inf

class Printer(object):
    def __init__(self, maze):
        self.maze = maze

    def overlay_path(self, path):
        for location in path:
            if self.maze[location[0]][location[1]] == 'start':
                self.maze[location[0]][location[1]] = 'S'
            elif self.maze[location[0]][location[1]] == 'End':
                self.maze[location[0]][location[1]] = 'E'
            else:
                self.maze[location[0]][location[1]] = '*'
        return self

    def print(self):
        for row in self.maze:
            printable_row = ''
            for cell in row:
                if cell == 'wall':
                    printable_row += '[#]'
                elif cell == 'empty':
                    printable_row += '   '
                else:
                    if isinstance(cell, str):
                        cell = cell[0]
                    printable_row += " {0} ".format(cell)
            print(printable_row)
