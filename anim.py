from tkinter import *
from random import randint
from maze import open_maze, new_maze
from solve import depth_first_search
from make_graph import make_graph

def go_n(pos):
    return (pos[0]-1, pos[1])

def go_s(pos):
    return (pos[0]+1, pos[1])

def go_e(pos):
    return (pos[0], pos[1]+1)

def go_w(pos):
    return (pos[0], pos[1]-1)
 
cell_size = 20 #pixels

new_maze('./maze.txt', (30,30) )

maze, start, stop =  open_maze('./maze.txt')
y_len = len(maze)
x_len = len(maze[0])
start_color='green'
stop_color='red'

G=make_graph(maze, start)
path=depth_first_search(G, start, stop)
 
def create():
    for row in range(y_len):
        for col in range(x_len):
            if maze[row][col] == 0:
                color = 'White'
            elif maze[row][col] == 1:
                color = 'black'
            draw(row, col, color)
 
def draw(row, col, color):
    x1 = col*cell_size
    y1 = row*cell_size
    x2 = x1+cell_size
    y2 = y1+cell_size
    ffs.create_rectangle(x1, y1, x2, y2, fill=color)

def sol(event):
    coord=[]
    
    pos=start
    for direction in path[:-1]:
        if direction == 'E':
            pos=go_e(pos)
        elif direction == 'W':
            pos=go_w(pos)
        elif direction == 'N':
            pos=go_n(pos)
        elif direction == 'S':
            pos=go_s(pos)
        coord.append(pos)
    


    for cell in coord:
        draw(cell[0], cell[1], 'blue')

 
window = Tk()
window.title('Maze')
ffs = Canvas(window, width = x_len*cell_size, height = y_len*cell_size, bg = 'grey')
ffs.pack()

window.bind("<Key>", sol)
 
create()
draw(start[0], start[1], start_color)
draw(stop[0], stop[1], stop_color)

window.mainloop()
