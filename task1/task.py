import json

with open('json.json', 'r') as file:
    tree = json.load(file)

def Check_depth(data, depth, parent=None):
  for key, value in data.items():
    if (int(key) > depth): depth = int(key)
    depth = Check_depth(value, depth, key)
  return depth

def create_matrix_of_zeroes(depth):
  matrix = []
  for i in list(range(depth)):
    matrix.append([0] * depth)
  return matrix

def write_adjacency(data, matrix, parent=None):
  for key, value in data.items():
    for i in value:
      matrix[int(key)-1][int(i)-1] = 1
      matrix[int(i)-1][int(key)-1] = 1
    matrix = write_adjacency(value, matrix, key)
  return matrix

if __name__ == "__main__":
    write_adjacency(tree, create_matrix_of_zeroes(Check_depth(tree, 0, None)), None)