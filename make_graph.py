def make_graph(list):
  for i in range(len(list)):
    for j in range(len(list[i])):
      if list[i][j] == 2:
        entree = (i, j)
      elif list[i][j] == 3:
        sortie = (i, j)
  graph = {}
  co_actuel = entré
