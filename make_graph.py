import main

def make_graph(laby):
  for i in range(len(laby)):
    for j in range(len(laby[i])):
      if laby[i][j] == 2:
        entree = (i, j)
      elif laby[i][j] == 3:
        sortie = (i, j)
  graph = {}
  return noeud_suiv(laby, graph, entree)


def noeud_suiv(laby, graph, noeud, noeud_precedent=None):
  if laby[noeud[0]][noeud[1]] == 3:
    graph[noeud] = None
    return graph
  nord = (noeud[0], noeud[1]-1)
  sud = (noeud[0], noeud[1]+1)
  est = (noeud[0]+1, noeud[1])
  ouest = (noeud[0]-1, noeud[1])
  graph[noeud] = None
  if laby[nord[0]][nord[1]] == 0 or laby[nord[0]][nord[1]] == 3:
    if noeud_precedent == (nord):
      pass
    else:
      graph[noeud]=nord
      noeud_suiv(laby, graph, nord, noeud)
  if laby[sud[0]][sud[1]] == 0 or laby[sud[0]][sud[1]] == 3:
    if noeud_precedent == (sud):
      pass
    else:
      if graph[noeud]==None:
        graph[noeud]=sud
      else:
        graph[noeud]=graph[noeud], sud
      noeud_suiv(laby, graph, sud, noeud)
  if laby[est[0]][est[1]] == 0 or laby[est[0]][est[1]] == 3:
    if noeud_precedent == (est):
      pass
    else:
      if graph[noeud]==None:
        graph[noeud]=est
      else:
        graph[noeud]=graph[noeud], est
      noeud_suiv(laby, graph, est, noeud)
  if laby[ouest[0]][ouest[1]] == 0 or laby[ouest[0]][ouest[1]] == 3:
    if noeud_precedent == (ouest):
      pass
    else:
      if graph[noeud]==None:
        graph[noeud]=ouest
      else:
        graph[noeud]=graph[noeud], ouest
      noeud_suiv(laby, graph, ouest, noeud)
  return graph


if __name__ == "__main__":
  laby = main.open_maze('./maze.txt')
  print(make_graph(laby))
