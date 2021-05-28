"""
Main module
"""

import maze
from make_graph import make_graph
import solve


maze_example = maze.open_maze('./maze.txt')
graph = make_graph(maze_example)
for pos_y, row in enumerate(maze_example):
    for pos_x,value in enumerate(row):
        if value == 2:
            entree=(pos_y, pos_x)
        if value == 3:
            sortie = (pos_y, pos_x)

solution = solve.dead_end_filling(graph, entree, sortie)

print(solution)

        
