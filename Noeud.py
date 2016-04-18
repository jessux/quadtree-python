import turtle

class Noeud():

    RACINE = 0
    BRANCHE = 1
    FEUILLE = 2
    tailleMin = 1

    def __init__(self,tailleCote,x,y,noeudParent):
        self.tailleDuCote = tailleCote
        self.x = x
        self.y = y
        self.type = Noeud.FEUILLE
        if noeudParent == None:
            self.profondeur = 0
        else:
            self.profondeur = noeudParent.profondeur + 1
        self.noeudParent = noeudParent
        self.listeFils = [None, None, None, None]
        self.listePoints = []
        self.carre()



    def division(self):
        n1 = Noeud(self.tailleDuCote / 2, self.x , self.y , self)
        n2 = Noeud(self.tailleDuCote / 2, self.x + self.tailleDuCote/2, self.y, self)
        n3 = Noeud(self.tailleDuCote / 2, self.x , self.y + self.tailleDuCote/2, self)
        n4 = Noeud(self.tailleDuCote / 2, self.x + self.tailleDuCote/2, self.y + self.tailleDuCote/2, self)
        self.type=Noeud.BRANCHE
        self.listeFils = [n1, n2, n3, n4]
        for point in self.listePoints :
            for fils in self.listeFils:
                if fils.contains(point):
                    fils.listePoints.append(point)
        self.listePoints = []

    def contains(self , (x , y)):
        if x > self.x and x < (self.x + self.tailleDuCote) and y > self.y and y < (self.y + self.tailleDuCote):
            return True
        return False

    def ajouterUnPoint(self,x,y):
        if self.type ==  1 :
            for fils in self.listeFils:
                if fils.contains((x,y)):
                    fils.ajouterUnPoint(x,y)
        else:
            if len(self.listePoints) <4  :
                self.ajouterUnPointDansLaListeDePoints(x,y)
            else:
                self.division()
                self.ajouterUnPoint(x,y)
        #self.points(x,y)

    def ajouterUnPointDansLaListeDePoints(self,x,y):
        self.listePoints.append((x, y))

    def carre(self):
        c=0
        turtle.up()
        turtle.goto(self.x,self.y)
        turtle.down()
        while c<4:
            turtle.forward(self.tailleDuCote)
            turtle.left(90)
            c=c+1

    def points(self,x,y):
        turtle.up()
        turtle.goto(x,y)
        turtle.down()
        turtle.circle(1)

    def afficheArbre(self):
        for fils in  self.listeFils:
            if fils.listeFils[0] != None:
                print "F",
            else:
                print "Feuille",
# Oblige d'avoir le cas des deux cases qui se supperposent
# wtf avec les 10 points aleatoires parmis les 50


