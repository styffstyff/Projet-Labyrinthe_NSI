import maze
from graph import *


def make_graph(laby, entree):
  """
  Create graph and vertex of starting
  :return fonction: noeud_suivant
  """
  graph = new_graph()
  add_vertex(graph, entree)
  return noeud_suiv(laby, graph, entree)


def noeud_suiv(laby, graph, noeud):
  """
  Recursive fonction which use to create the graph
  :return fonction or graph:
  """
  nord = (noeud[0]-1, noeud[1])
  sud = (noeud[0]+1, noeud[1])
  est = (noeud[0], noeud[1]+1)
  ouest = (noeud[0], noeud[1]-1)
  if nord[0] >= 0:
    if laby[nord[0]][nord[1]] == 0 or laby[nord[0]][nord[1]] == 3:
      if is_vertex(graph, nord):
        pass
      else:
        add_vertex(graph, nord)
        add_arc(graph, noeud, nord)
        noeud_suiv(laby, graph, nord)
  if sud[0] < len(laby):
    if laby[sud[0]][sud[1]] == 0 or laby[sud[0]][sud[1]] == 3:
      if is_vertex(graph, sud):
        pass
      else:
        add_vertex(graph, sud)
        add_arc(graph, noeud, sud)
        noeud_suiv(laby, graph, sud)
  if est[1] < len(laby[0]):
    if laby[est[0]][est[1]] == 0 or laby[est[0]][est[1]] == 3:
      if is_vertex(graph, est):
        pass
      else:
        add_vertex(graph, est)
        add_arc(graph, noeud, est)
        noeud_suiv(laby, graph, est)
  if ouest[1] >= 0:
    if laby[ouest[0]][ouest[1]] == 0 or laby[ouest[0]][ouest[1]] == 3:
      if is_vertex(graph, ouest):
        pass
      else:
        add_vertex(graph, ouest)
        add_arc(graph, noeud, ouest)
        noeud_suiv(laby, graph, ouest)
  return graph


if __name__ == "__main__":
  laby = [[2, 0, 1],
          [1, 0, 3]]
  make_graph(laby, (0, 0)) == {(0, 0): {(0, 1)}, (0, 1): {(1, 1)}, (1, 1): {(1, 2)}, (1, 2): set()}
