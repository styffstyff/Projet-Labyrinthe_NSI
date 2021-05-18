def make_graph(laby):
  for i in range(len(laby)):
    for j in range(len(laby[i])):
      if laby[i][j] == 2:
        entree = (i, j)
      elif laby[i][j] == 3:
        sortie = (i, j)
  graph = {}
  co_actuel = entree
  return


def noeud_suiv(laby, graph, noeud, noeud_precedent=None):
  if laby[noeud[0],noeud[1]] == 3:
    graph[noeud] = None
    return graph
  nord = (noeud[0], noeud[1]-1)
  sud = (noeud[0], noeud[1]+1)
  est = (noeud[0]+1, noeud[1])
  ouest = (noeud[0]-1, noeud[1])
  if [laby[nord], laby[sud], laby[est], laby[ouest]].count(1) == 3:
    graph[noeud] = Non
    return graph
  if nord == 0 or nord == 3:
    if noeud_precedent == (nord):
      pass
    else:
      graph[noeud] += nord
