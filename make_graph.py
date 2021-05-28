import maze
from graph import *


def make_graph(laby, entree):
  graph = new_graph()
  add_vertex(graph, entree)
  return noeud_suiv(laby, graph, entree)


def noeud_suiv(laby, graph, noeud):
  nord = (noeud[0]-1, noeud[1])
  sud = (noeud[0]+1, noeud[1])
  est = (noeud[0], noeud[1]+1)
  ouest = (noeud[0], noeud[1]-1)
  try:
    if laby[nord[0]][nord[1]] == 0 or laby[nord[0]][nord[1]] == 3:
      if is_vertex(graph, nord):
        pass
      else:
        add_vertex(graph, nord)
        add_arc(graph, noeud, nord)
        noeud_suiv(laby, graph, nord)
  except IndexError:
    pass
  try:
    if laby[sud[0]][sud[1]] == 0 or laby[sud[0]][sud[1]] == 3:
      if is_vertex(graph, sud):
        pass
      else:
        add_vertex(graph, sud)
        add_arc(graph, noeud, sud)
        noeud_suiv(laby, graph, sud)
  except IndexError:
    pass
  try:
    if laby[est[0]][est[1]] == 0 or laby[est[0]][est[1]] == 3:
      if is_vertex(graph, est):
        pass
      else:
        add_vertex(graph, est)
        add_arc(graph, noeud, est)
        noeud_suiv(laby, graph, est)
  except IndexError:
    pass
  try:
    if laby[ouest[0]][ouest[1]] == 0 or laby[ouest[0]][ouest[1]] == 3:
      if is_vertex(graph, ouest):
        pass
      else:
        add_vertex(graph, ouest)
        add_arc(graph, noeud, ouest)
        noeud_suiv(laby, graph, ouest)
  except IndexError:
    pass
  return graph


if __name__ == "__main__":
  laby = maze.open_maze('./maze.txt')
  make_graph(laby)
