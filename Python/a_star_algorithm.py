import numpy as np

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent  # parent of the current node
        self.position = position  # current position of the node in tuple
        self.g = 0  # cost from start to current node
        self.h = 0  # heuristic based estimated cost of current node to end node
        self.f = 0  # total cost of the present node i.e. f = g+h

    def __eq__(self, other):
        '''method for checking the equality of the node with another node.'''
        return self.position == other.position


def return_search_path(current_node, maze):
    '''function to return the path from the start node to the target node (end node).'''
    path = []
    no_of_rows, no_of_columns = np.shape(maze)

    # here, initialized result maze with -1 in every position
    result = [[-1 for i in range(no_of_columns)] for j in range(no_of_rows)]

    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent


    print(path)


if __name__ == '__main__':
    maze = [[0,1,0,0,0,0],
            [0,0,0,0,0,0],
            [0,1,0,1,0,0],
            [0,1,0,0,1,0],
            [0,0,0,0,1,0]]
    start = [0,0]
    end = [4,5]
    cost = 1

    return_search_path([1,0], maze)


