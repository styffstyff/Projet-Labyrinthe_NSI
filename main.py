"""
Main module
"""

import make_graph
import maze
import solve

import random

def debug(laby, solution):
    print("="*10, "DEBUG", "="*10)
    print(solution)
    for l in laby:
        print(l)

size = (random.randint(5, 10), random.randint(5, 10))
maze.new_maze("maze.txt", size)
laby, start, exit = maze.open_maze('./maze.txt')
graph = make_graph.make_graph(laby)

print(graph)

solution = solve.dead_end_filling(graph, start, exit)
print(size, solution)
if not solve.check(laby, start, exit, solution):
    debug(laby, solution)

solution = solve.depth_first_search(graph, start, exit)
print(size, solution)
if not solve.check(laby, start, exit, solution):
    debug(laby, solution)
