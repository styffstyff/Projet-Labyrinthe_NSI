"""
Main module
"""

import maze
import make_graph
import solve


maze_example = maze.open_maze('./maze.txt')
graph = make_graph.make_graph(maze_example)
for pos, row in enumerate(maze_example):
    for value in row:
        if value == 2:
            entree=(pos,row.index(2))
        if value == 3:
            sortie = (pos, row.index(2))

solution = solve.dead_end_filling(graph, entree, sortie)

print(solution)
