

def open_maze(filepath):
    """
    Open a maze from a given filepath, the maze should be a list of list
    :return list: maze
    """
    with open(filepath, 'r', encoding='utf-8') as maze_file:
        maze=[]
        for line in maze_file:
            line=[ n for n in line if n in "0123"  ]
            maze.append(line)
        return maze