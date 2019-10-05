from Cases import *
from Constantes import *

class Patern:
    def __init__(self,largeur,hauteur,tailleCase,tailleMur):
        self.hauteur=hauteur
        self.largeur=largeur
        self.matrice_cases = [[Case(tailleCase,tailleMur) for i in range(hauteur)]for i in range(largeur)]
    def generation(self):
        for i in range(0,self.largeur):
            for j in range(0,self.hauteur):
                self.generation_case(i,j)
    def generation_case(self,x,y):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
            et génère les murs en fonction de sa position
        """
        #on casse les murs qui ne sont pas aux extrèmes
        if x!=0:
            self.matrice_cases[x][y].casser_mur(GAUCHE)
            
        if x!=(self.largeur-1):
            self.matrice_cases[x][y].casser_mur(DROITE)

        if y!=0:
            self.matrice_cases[x][y].casser_mur(HAUT)
            
        if y!=(self.hauteur-1):
            self.matrice_cases[x][y].casser_mur(BAS)
    
    def integration_case(self,x,y,matrice_lab):
        """
        Fonction qui prend en enetrées:
            les coordonnées de la case
            les coordonnées de base du patern
            la matrice du labyrinthe

        et casse les murs qui empêches la navigation dans le labyrinthe
        """
        bords=[]
        bords=self.case_bord(x,y)
        
        if len(bords)!=0:
            for i in range(0,len(bords)):
                mur=self.mur_opposee(x,y,bords[i],matrice_lab)
                if mur!=None and mur.get_etat()==MUR_VIDE:
                    matrice_lab[x][y].casser_mur(bords[i])

    def mur_opposee(self,x,y,direction,matrice_lab):
        """
        Fonction qui prend en enetrées:
            les coordonnées de la case
            la direction du mur que l'on veut tester
            la matrice du labyrinthe
        et renvoie le mur opposée (s'il existe) à la direction
        """


        largeur_lab=len(matrice_lab)
        hauteur_lab=len(matrice_lab[0])

        mur=None

        if direction==HAUT and y>0:
            mur=matrice_lab[x][y-1].get_mur_bas()
            
        elif direction==DROITE and x<largeur_lab-1:
            mur=matrice_lab[x+1][y].get_mur_gauche()
            
        elif direction==BAS and y<hauteur_lab-1:
            mur=matrice_lab[x][y+1].get_mur_haut()
            
        elif direction==GAUCHE and x>0:
            mur=matrice_lab[x-1][y].get_mur_droit()

        return mur
    
    def case_bord(self,x,y):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
            et qui renvoie la/les direction/s des bords
        """
        bords=[]
        
        #on casse les murs qui ne sont pas aux extrèmes
        if x!=0:
            bords+=[GAUCHE]
            
        if x!=(self.largeur-1):
            bords+=[DROITE]

        if y!=0:
            bords+=[HAUT]
            
        if y!=(self.hauteur-1):
            bords+=[BAS]

        return bords
    def copie(self,coordonnee_x,coordonnee_y,matrice_lab):
        """
        Fonction qui prend en entrée:
            les coordonnées de base du patern dans le labyrinthe
            la matrice de cases du labyrinthe
        et qui copie les cases du patern dans le labyrinthe
        """
        for i in range(coordonnee_x,coordonnee_x+self.largeur):
            for j in range(coordonnee_y,coordonnee_y+self.hauteur):
                matrice_lab[i][j]=self.matrice_cases[i-coordonnee_x][j-coordonnee_y]
                self.integration_case(i,j,matrice_lab)
        return matrice_lab

