import Generateur
import Cases
import Constantes
from Resolveur import *


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
        self.matrice_cases=gene.generation()
    def peut_passer(self,coord,sens):
        newcoord = coord
        case = self.matrice_cases[coord[0]][coord[1]]
        passe = True
        if sens == GAUCHE and not case.mur_plein(GAUCHE):
            newcoord = (coord[0]-1,coord[1])
        elif sens == DROITE and not case.mur_plein(DROITE):
            newcoord = (coord[0]+1,coord[1])
        elif sens == BAS and not case.mur_plein(BAS):
            newcoord = (coord[0],coord[1]+1)
        elif sens == HAUT and not case.mur_plein(HAUT):
            newcoord = (coord[0],coord[1]-1)
        else :
            passe = False
        return passe, newcoord
    
    def dessine_toi(self,screen,joueur_x,joueur_y):
        for x in range(0,self.largeur):
            for y in range(0,self.hauteur):
                    self.matrice_cases[x][y].dessine_toi(screen,x*(self.tailleCase+self.tailleMur),y*(self.tailleCase+self.tailleMur))
    def resolution(self,arrivee_x,arrivee_y):
        resol = Resolveur(self.matrice_cases,self.largeur,self.hauteur,arrivee_x,arrivee_y)
        solution=resol.resolution()
        print(solution)
        
#lab = Labyrinthe(5,5)
#lab.dessine_toi(0,0,0)
