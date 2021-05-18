""" 
Maze implementation with list of list
"""

def blank_maze(xy):
    """
    Creates a new maze of xy size.
    :return list: empty maze
    """

    maze=[]
    for y in range(xy[1]):
        row=[]
        for x in range(xy[0]):
            if y in [0, xy[1]-1] or x in [0, xy[0]-1]:
                row.append(1)
            else:
                row.append(0)
        maze.append(row)
    return maze

if __name__ == "__main__":
    xy=(5,5)
    print(blank_maze(xy))