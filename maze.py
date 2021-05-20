""" 
Maze implementation with list of list
"""

from random import randint

go_N = lambda pos: (pos[0]-1, pos[1])
go_S = lambda pos: (pos[0]+1, pos[1])
go_E = lambda pos: (pos[0], pos[1]+1)
go_W = lambda pos: (pos[0], pos[1]-1)

wall = lambda maze: [ (x,y) for x, rows in enumerate(maze) for y, value in enumerate(rows) if x==0 or y==0 or x==len(maze[0])-1 or y==len(maze)-1 ]

distance = lambda AB: (AB[1][0]-AB[0][0])**2+(AB[1][1]-AB[0][1])**2

def mark_start(pos, maze):
    maze[pos[0]][pos[1]]=2
    return maze

def mark_exit(pos, maze):
    """
    Mark the number 3 on the maze which symbolize the 'exit'
    :return list: maze with an exit
    """
    
    y_len=len(maze)
    x_len=len(maze[0])
    
    #We select 3 exits point at each 4 corner of the maze
    exit_points=[(0, 1), (0, x_len-2), (y_len-1, 1), (y_len-1, x_len-2)]
    #We choose the furthest
    exit_points.sort( key=lambda coord: distance((pos, coord )), reverse=True)

    #Check if the position of the exit point is near a path
    pos_move=moves1(exit_points[0], maze)

    #We assume that their must be a path within 2 blocks of distance
    #We check at one block distance
    if len(pos_move)>0:
        maze[exit_points[0][0]][exit_points[0][1]]=3
        return maze
    #We check at two block distance
    else:
        pos_move=moves(exit_points[0], maze)
        maze[pos_move[0][0][0]][pos_move[0][0][1]]=0
        maze[exit_points[0][0]][exit_points[0][1]]=3
        return maze

def mark_wall(pos, maze):
    maze[pos[0]][pos[1]]=1
    return maze

def mark_visited(pos, maze):
    maze[pos[0]][pos[1]]=9
    return maze

def add_wall(pos, maze):
    """
    Add walls around pos 
    :return tuple: maze, wall in the maze

    """
    y_len=len(maze)
    x_len=len(maze[0])
    neighbors=[go_N(pos), go_S(pos), go_E(pos), go_W(pos)]
    
    for pos in neighbors:
        if y_len>pos[0]>=0 and x_len>pos[1]>=0:
            if maze[pos[0]][pos[1]]==0:
                maze[pos[0]][pos[1]]=1
    
    return maze

def blank_maze(xy):
    """
    Creates a new maze of xy size.
    :return list: empty maze
    """

    assert xy[0]>=5, "The maze must be larger."
    assert xy[1]>=5, "The maze must be larger."

    maze=[[0 for x in range(xy[1])]for y in range(xy[0])]

    return maze

def is_maze(maze):
    """
    :return bool: true if the argument is a blank maze 
    """

    x_len=len(maze[0])
    if x_len<5 or len(maze) <5:
        return False
    for rows in maze:
        if len(rows)<x_len:
            return False
    
    return True

def moves1(pos, maze):
    """
    Search the unvisited neighbors 2 blocks around of pos
    :return list: list of unvisited points
    """
    y_len=len(maze)
    x_len=len(maze[0])

    #list of coordinates for 4 directional move
    pos_move=[go_N(pos), 
              go_S(pos),
              go_E(pos),
              go_W(pos)]

    move=[]
    
    for index, pos in enumerate(pos_move):
        if y_len>pos[0]>=0 and x_len>pos[1]>=0:
            if maze[pos[0]][pos[1]]==0:
                move.append(pos_move[index]) 
    
    return move

def moves(pos, maze):
    """
    Search the unvisited neighbors 2 blocks around of pos
    :return list: list of unvisited points
    """

    y_len=len(maze)
    x_len=len(maze[0])

    #list of couple of position for 4 direction move
    pos_move=[(go_N(pos), go_N(go_N(pos)) ), 
              (go_S(pos), go_S(go_S(pos)) ),
              (go_E(pos), go_E(go_E(pos)) ),
              (go_W(pos), go_W(go_W(pos)) )]

    move=[]
    
    for index, pos in enumerate(pos_move):
        if y_len>pos[1][0]>=0 and x_len>pos[1][1]>=0:
            if maze[pos[1][0]][pos[1][1]]==0:
                move.append(pos_move[index])
            if maze[pos[1][0]][pos[1][1]]==9:
                move.append(0)   
    
    return move


def make_walls(maze):
    """
    Creates walls for a maze
    :return list: maze
    """

    walls=[walls for walls in wall(maze)]

    stack=[]

    assert is_maze(maze), "The argument is not a maze"

    #We always start the maze from a random point
    start=walls[randint(0, len(walls)-1)]
    maze = mark_start(start, maze)
    stack.append(start)
    
    maze=rec_dfsa(start, maze, stack, walls)

    for y,row in enumerate(maze):
        for x,value in enumerate(row):
            if value==0:
                maze[y][x]=1
            if value==9:
                maze[y][x]=0

    maze=mark_exit(start, maze)

    return maze


def rec_dfsa(pos, maze, stack, walls):
    """
    Recursive implementation of the depth-first search algorithm to create walls
    :return list: the maze full of walls 
    """

    #If the stack is empty every accessible point have been reached
    if len(stack)==0:
        return maze
    
    pos_move=moves(pos, maze)
    
    #If every neighbor is already visited we move backward 
    if pos_move.count(0) == len(pos_move):
        pos=stack.pop()
        rec_dfsa(pos, maze, stack, walls)

    else:
        pos_move=[position for position in pos_move if position!=0]
        move=pos_move[randint(0,len(pos_move)-1)]
        for m in move:
            maze=mark_visited(m, maze)
            stack.append(m)
                
        maze=add_wall(pos, maze)

        maze=add_wall(stack[-2], maze)


        rec_dfsa(move[1], maze, stack, walls)
    
    return maze

def new_maze(filename, xy):
    """
    Creates a txt file with a xy size maze implemented in python list of list in the same directory
    :return None: 
    """

    maze = blank_maze(xy)
    maze = make_walls(maze)

    with open(filename, 'w', encoding='utf-8') as maze_file:
        maze_file.write(str(maze))


if __name__ == "__main__":
    xy=(22,22)
    maze=blank_maze(xy)
    maze=make_walls(maze)
    for rows in maze:
        print(rows)
    
    

    