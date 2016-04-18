import unittest
import Noeud as classNoeud

class test(unittest.TestCase):

    def testCreationNoeud(self):
        n0 = classNoeud.Noeud(100,0,0,None)
        self.assertEqual(n0.type, 2)


    def testCreation4Fils(self):
        n0 = classNoeud.Noeud(100, 0, 0, None)
        n0.division()
        self.assertEquals(n0.listeFils[0].type, 2)
        self.assertEquals(n0.listeFils[1].tailleDuCote, 50)
        self.assertEquals(n0.listeFils[2].noeudParent, n0)
        self.assertEquals(n0.listeFils[3].profondeur, 1)

    def testContientPoint(self):
        n0 = classNoeud.Noeud(100, 0, 0, None)
        n0.division()
        self.assertEquals(n0.contains((10,20)),True)

    def testFilsContientLePointDansLe4emeFils(self):
        n0 = classNoeud.Noeud(100,0,0,None)
        n0.division()
        x = 51
        y = 51
        self.assertEquals(n0.listeFils[0].contains((x, y)), False)
        self.assertEquals(n0.listeFils[1].contains((x, y)), False)
        self.assertEquals(n0.listeFils[2].contains((x, y)), False)
        self.assertEquals(n0.listeFils[3].contains((x, y)), True)

    def testAjouterUnPoint(self):
        n0 = classNoeud.Noeud(100, 0, 0, None)
        n0.ajouterUnPoint(10,10)
        self.assertEquals(len(n0.listePoints),1)

    def testAjouter5points(self):
        n0 = classNoeud.Noeud(100, 0, 0, None)
        n0.ajouterUnPoint(10, 10)
        n0.ajouterUnPoint(20, 10)
        n0.ajouterUnPoint(20, 20)
        n0.ajouterUnPoint(10, 20)
        n0.ajouterUnPoint(1, 1)
        self.assertEquals(n0.listeFils[0].listeFils[0].listeFils[3].listePoints,[(20,20)])

if __name__ == '__main__':
    unittest.main()

