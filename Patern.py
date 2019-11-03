from Cases import *
from Constantes import *

class Patern:
    def __init__(self,position,largeur,hauteur,tailleCase,tailleMur,entrees=[[1,0]]):
        self.position = position
        self.hauteur = hauteur
        self.largeur = largeur
        self.matrice_cases = [[Case(tailleCase,tailleMur) for i in range(hauteur)]for i in range(largeur)]
        self.entrees = entrees
    def pre_gen_entrees_x(self,colonne,depart_x,arrivee_x):
        """
        Fonction qui facilite la génération des entrées sur une ligne
        Entrées:
            -la colonne sur laquelle on veut générée les entrées
            -la première en x des entrées générées
            -la dernière en x des entrées générées
        Sorties:
            Rien
        """
        for x in range(depart_x,arrivee_x+1):
            self.entrees.append([x,colonne])
    def pre_gen_entrees_y(self,ligne,depart_y,arrivee_y):
        """
        Fonction qui facilite la génération des entrées sur une colonne
        Entrées:
            -la ligne sur laquelle on veut générée les entrées
            -la première en y des entrées générées
            -la dernière en y des entrées générées
        Sorties:
            Rien
        """
        for y in range(depart_y,arrivee_y+1):
            self.entrees.append([ligne,y])

        
    def pre_generation(self,matrice_lab):
        """
        Fonction qui prend en entrée:
            les coordonnées de base du patern dans le labyrinthe
            la matrice de cases du labyrinthe
        et qui pre génère les cases du patern
        """
        coordonnee_x = self.position[0]
        coordonnee_y = self.position[1]
        for i in range(coordonnee_x,coordonnee_x+self.largeur):
            for j in range(coordonnee_y,coordonnee_y+self.hauteur):
                self.pre_generation_case(i-coordonnee_x,j-coordonnee_y)
                matrice_lab[i][j]=self.matrice_cases[i-coordonnee_x][j-coordonnee_y]

    def post_generation(self,matrice_lab):
        """
        Fonction qui prend en entrée:
            les coordonnées de base du patern dans le labyrinthe
            la matrice de cases du labyrinthe
        et qui clear la salle
        """
        coordonnee_x = self.position[0]
        coordonnee_y = self.position[1]
        for i in range(coordonnee_x,coordonnee_x+self.largeur):
            for j in range(coordonnee_y,coordonnee_y+self.hauteur):
                self.post_generation_case(i-coordonnee_x,j-coordonnee_y)
                matrice_lab[i][j]=self.matrice_cases[i-coordonnee_x][j-coordonnee_y]

    def pre_generation_case(self,x,y):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
            et génère les murs en fonction de sa position
        """
        #on ne doit générer que les cases au bords
        #plus précisement on doit empêcher le générateur d'y toucher
        if not(self.case_est_une_entree(x,y)) and self.case_au_bord(x,y):
            self.incorpotation_case(x,y)
    def post_generation_case(self,x,y):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
            et casse les murs les murs en fonction de sa position
        """
        if not(self.case_au_bord(x,y)) or self.case_est_une_entree(x,y):
            self.incorpotation_case(x,y)
            
    def case_est_une_entree(self,x,y):
        """
        Fonction qui prend en entrées:
            les coordonnées de la case
        et qui renvoie un booléen indiquant si elle est une entrée ou pas
        """
        est_entree=False
        for entree in self.entrees:
            if entree[0]==x and entree[1]==y:
                est_entree=True

        return est_entree
    def case_au_bord(self,x,y):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
        et qui renvoie un booléen indiquant si la case est au bord ou non
        """
        return (x==0 or x==self.largeur-1)or(y==0 or y==self.hauteur-1)
        
    def clear_case(self,x,y):
        """
        Fonction qui clear la case selectionner
        """
        for i in range(0,4):
            self.matrice_cases[x][y].casser_mur(i)
        
    def incorpotation_case(self,x,y):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
            et génère les murs en fonction de sa position
        """
        #on casse les murs qui ne sont pas aux extrèmes
        #print(x,y)
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
        bords=self.case_bord(x,y,len(matrice_lab),len(matrice_lab[0]))
        
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
    
    def case_bord(self,x,y,largeur_lab,hauteur_lab):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
            la largeur et la hauteur du labyrinthe
            et qui renvoie la/les direction/s des bords
        """
        bords=[]
        
        #on casse les murs qui ne sont pas aux extrèmes
        if x!=0:
            bords+=[GAUCHE]
            
        if x!=(largeur_lab-1):
            bords+=[DROITE]

        if y!=0:
            bords+=[HAUT]
            
        if y!=(hauteur_lab-1):
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

    def get_pos(self):
        return self.position

p=Patern(0,0,0,0,[[0,0],[152,152]])
print(p.case_est_une_entree(0,0))

print(p.case_est_une_entree(1,1))
