"""
Main module
"""

from make_graph import make_graph
import maze
import solve

import random

size = (random.randint(5, 25), random.randint(5, 25))
maze.new_maze("maze.txt", size)
maze_example, start, exit = maze.open_maze('./maze.txt')
graph = make_graph(maze_example, start)

solution = solve.dead_end_filling(graph, start, exit)
print(size, solution)
assert solve.check(maze_example, start, exit, solution)

solution = solve.depth_first_search(graph, start, exit)
print(size, solution)
print(graph)
assert solve.check(maze_example, start, exit, solution), maze_example
