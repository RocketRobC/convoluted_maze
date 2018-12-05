from math import sqrt

def manhattan(start, target):
  x_distance = abs(start[0] - target[0])
  y_distance = abs(start[1] - target[1])
  return x_distance + y_distance

def euclidean(start, target):
  x_distance = abs(start[0] - target[0])
  y_distance = abs(start[1] - target[1])
  # print(start, target)
  # print(sqrt(x_distance**2 + y_distance**2))
  return sqrt(x_distance**2 + y_distance**2)
