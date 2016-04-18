import Noeud
import random

class Quadtree():

    profondeurMax = 1
    feuilles = []
    listeDesNoeuds = []

    def __init__(self):
        n0 = Noeud.Noeud(100,0,0,None)
        self.listeDesNoeuds.append(n0)
        for i in range(50):
            n0.ajouterUnPoint(random.randrange(0,100),random.randrange(0,100))


if __name__ == '__main__':
    q= Quadtree()

