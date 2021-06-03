# Projet-Labyrinthe_NSI
Projet de fin d'année de terminale NSI

# Participants  
Le projet est mené par:  
Théo  
Mallory  
et Gabin  

---

Génération et résolution de labyrinthes à l'aide d'un graphe.

# Utilisation
```sh
$ git clone https://github.com/styffstyff/Projet-Labyrinthe_NSI
$ cd Projet-Labyrinthe_NSI
$ python3 main.py
```

# Exemple
```
$ python3 main.py
MAZE :
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 1, 0, 1, 1, 1, 1]
[1, 0, 0, 0, 1, 0, 1, 0, 0, 2]
[1, 0, 1, 1, 1, 0, 1, 0, 1, 1]
[1, 0, 0, 0, 1, 0, 1, 0, 0, 0]
[1, 0, 1, 0, 1, 1, 1, 1, 1, 0]
[1, 0, 1, 0, 1, 0, 0, 0, 1, 0]
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
[1, 0, 1, 0, 0, 0, 1, 0, 0, 0]
[1, 3, 1, 1, 1, 1, 1, 1, 1, 1]
Solution with dead_end_filling : WWSSEESSSSWWNNWWSSWWNNNNWWSSSSS
Solution with depth_first_search : WWSSEESSSSWWNNWWSSWWNNNNWWSSSSS
```

# Représentations

Pour le labyrinthe :
- 0 : case libre
- 1 : mur
- 2 : départ
- 3 : arrivée

Pour les solutions :
- N : "North", Nord, aller en haut
- S : "South", Sud, aller en bas
- E : "East", Est, aller à droite
- W : "West", Ouest, aller à gauche


