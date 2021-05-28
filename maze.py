"""
Maze implementation with list of list
"""

from random import randint

def go_n(pos):
    return (pos[0]-1, pos[1])

def go_s(pos):
    return (pos[0]+1, pos[1])

def go_e(pos):
    return (pos[0], pos[1]+1)

def go_w(pos):
    return (pos[0], pos[1]-1)

def distance(points):
    return (points[1][0]-points[0][0])**2+(points[1][1]-points[0][1])**2

def wall(maze):
    """
    Get all the coordinates on the side of the wall
    :return list: list of coordinate
    """
    walls=[]

    for y_pos, rows in enumerate(maze):
        for x_pos, value in enumerate(rows):
            if x_pos==0 or y_pos==0 or x_pos==len(maze[0])-1 or y_pos==len(maze)-1:
                walls.append((y_pos, x_pos))
    return walls

def mark_start(pos, maze):
    maze[pos[0]][pos[1]]=2
    return maze

def mark_exit(pos, maze, walls):
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
    pos_move=moves1(exit_points[0], maze, walls)

    #We assume that their must be a path within 2 blocks of distance
    #We check at one block distance
    if len(pos_move)>0:
        maze[exit_points[0][0]][exit_points[0][1]]=3
    #We check at two block distance
    else:
        pos_move=moves(exit_points[0], maze, walls)
        maze[pos_move[0][0][0]][pos_move[0][0][1]]=0
        maze[exit_points[0][0]][exit_points[0][1]]=3
    return maze

def mark_wall(pos, maze):
    maze[pos[0]][pos[1]]=1
    return maze

def mark_visited(pos, maze):
    maze[pos[0]][pos[1]]=9
    return maze

#####################################

def add_wall(pos, maze, walls):
    """
    Add walls around pos
    :return tuple: maze, wall in the maze
    """
    y_len=len(maze)
    x_len=len(maze[0])
    neighbors=[go_n(pos), go_s(pos), go_e(pos), go_w(pos)]
    for coord in neighbors:
        if y_len>coord[0]>=0 and x_len>coord[1]>=0:
            if coord not in walls:
                walls.append(coord)
    return walls

#####################################

def blank_maze(xy_coord):
    """
    Creates a new maze of xy_coord size.
    :return list: empty maze
    """

    assert xy_coord[0]>=5, "The maze must be larger."
    assert xy_coord[1]>=5, "The maze must be larger."

    maze=[[1 for x in range(xy_coord[1])]for y in range(xy_coord[0])]

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

def moves1(pos, maze, walls):
    """
    Search the unvisited neighbors 1 block around of pos
    :return list: list of unvisited points
    """
    y_len=len(maze)
    x_len=len(maze[0])

    #list of coordinates for 4 directional move
    pos_move=[go_n(pos),
              go_s(pos),
              go_e(pos),
              go_w(pos)]

    move=[]
    for index, coord in enumerate(pos_move):
        if y_len>coord[0]>=0 and x_len>coord[1]>=0:

            if coord not in walls:
                move.append(pos_move[index])
            elif maze[coord[0]][coord[1]]==0:
                move.append(pos_move[index])
             
    return move

def moves(pos, maze, walls):
    """
    Search the unvisited neighbors 2 blocks around of pos
    :return list: list of unvisited points
    """

    y_len=len(maze)
    x_len=len(maze[0])

    #list of couple of position for 4 direction move
    pos_move=[(go_n(pos), go_n(go_n(pos)) ),
              (go_s(pos), go_s(go_s(pos)) ),
              (go_e(pos), go_e(go_e(pos)) ),
              (go_w(pos), go_w(go_w(pos)) )]

    move=[]
    for index, coord in enumerate(pos_move):
        if y_len>coord[1][0]>=0 and x_len>coord[1][1]>=0:
            
            if coord[1] not in walls:
                move.append(pos_move[index])

            elif maze[coord[1][0]][coord[1][1]]==0:
                move.append(pos_move[index])

            if maze[coord[1][0]][coord[1][1]]==9:
                move.append(0)
    return move


def make_walls(maze):
    """
    Creates walls for a maze
    :return list: maze
    """

    outline=wall(maze)

    stack=[]
    walls=[]

    assert is_maze(maze), "The argument is not a maze"

    #We always start the maze from a random point
    start=outline[randint(0, len(outline)-1)]
    maze = mark_start(start, maze)
    stack.append(start)
    maze=rec_dfsa(start, maze, stack, walls)

    for y_pos,row in enumerate(maze):
        for x_pos,value in enumerate(row):
            if value==9:
                maze[y_pos][x_pos]=0

    maze=mark_exit(start, maze, walls)

    return maze


def rec_dfsa(pos, maze, stack, walls):
    """
    Recursive implementation of the depth-first search algorithm to create walls
    :return list: the maze full of walls
    """

    #If the stack is empty every accessible point have been reached
    if len(stack)==0:
        return maze
    pos_move=moves(pos, maze, walls)
    #If every neighbor is already visited we move backward
    if pos_move.count(0) == len(pos_move):
        pos=stack.pop()
        rec_dfsa(pos, maze, stack, walls)

    else:
        pos_move=[position for position in pos_move if position!=0]
        move=pos_move[randint(0,len(pos_move)-1)]
        for coord in move:
            maze=mark_visited(coord, maze)
            stack.append(coord)
        walls=add_wall(pos, maze, walls)

        walls=add_wall(stack[-2],maze, walls)


        rec_dfsa(move[1], maze, stack, walls)

    return maze

def new_maze(filename, xy_coord):
    """
    Creates a txt file with a xy_coord size maze implemented
    in python list of list in the same directory
    :return None:
    """

    maze = blank_maze(xy_coord)
    maze = make_walls(maze)

    with open(filename, 'w', encoding='utf-8') as maze_file:
        maze_file.write('[')
        for rows in maze:
            maze_file.writelines(str(rows)+', \n')
        maze_file.write(']')

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
    
    for e in range(100):
        new_maze('./maze.txt', (22,22) )

