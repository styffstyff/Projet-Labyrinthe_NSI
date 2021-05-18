

def open_maze(filename):
    with open(filename, 'r', encoding='utf-8') as maze_file:
        maze=[]
        for line in maze_file:
            line=[ n for n in line if n in "0123"  ]
            maze.append(line)
        return maze