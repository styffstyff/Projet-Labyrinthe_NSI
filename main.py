"""
Main module
"""

def open_maze(filepath):
    """
    Open a maze from a given filepath, the maze should be a list of list.
    :return list: maze
    """
    with open(filepath, 'r', encoding='utf-8') as maze_file:
        maze=[]
        for line in maze_file:
            row=[ int(n) for n in line if n in "0123" ]
            if len(row)>0:
                maze.append(row)
        return maze

if __name__ == "__main__":
    maze_example=open_maze('./maze.txt')
    for e in maze_example:
        print(e)
