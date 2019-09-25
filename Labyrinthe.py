import Generateur
import Cases

class Labyrinthe:
    def __init__(self,largeur,hauteur,tailleCase=20,tailleMur=1):
        self.largeur = largeur
        self.hauteur = hauteur
        self.matrice_cases = [[Cases.Case(tailleCase,tailleMur) for i in range(hauteur)]for i in range(largeur)]
        #paramètre graphiques
        self.tailleCase = tailleCase
        self.tailleMur = tailleMur

    def generation(self):
        #ini du tableau de case (4 murs pleins)
        #génération en profondeur via l'objet generateur
        gene=Generateur.Generateur(self.matrice_cases,self.largeur,self.hauteur)
        gene.generation()
        self.matrice_cases=gene.matrice_cases
        print(len(self.matrice_cases))
    def peut_passer(self):
        pass
    
    def dessine_toi(self,screen,joueur_x,joueur_y):
        for x in range(0,self.largeur):
            for y in range(0,self.hauteur):
                    self.matrice_cases[x][y].dessine_toi(screen,x*(self.tailleCase+self.tailleMur),y*(self.tailleCase+self.tailleMur))

#lab = Labyrinthe(5,5)
#lab.dessine_toi(0,0,0)
