from Cases import *
from Constantes import *

class Patern:
    def __init__(self,position,largeur,hauteur,tailleCase,tailleMur,entrees=[(1,0)],clees=[],vide = True):
        self.position = position
        self.hauteur = hauteur
        self.largeur = largeur
        self.matrice_cases = [[Case(tailleCase,tailleMur) for i in range(hauteur)]for i in range(largeur)]
        self.taille_mur = tailleMur
        self.entrees = entrees
        self.clees = clees
        self.vide = vide
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

    def post_gen_entrees(self,matrice_lab):
        """
        Fonction qui transforme les entrées en portes ou en murs vides
        """
        coordonnee_x = self.position[0]
        coordonnee_y = self.position[1]
        
        for nb in range(len(self.entrees)):
            i = self.entrees[nb][0]+coordonnee_x
            j = self.entrees[nb][1]+coordonnee_y
            for bord in self.contraintes_cases(self.entrees[nb][0],self.entrees[nb][1]):
                if self.get_voisin_dir(i,j,bord,matrice_lab)==None:
                    print("On ne peut pas ouvrir d'entrée sur l'extérieur du labyrinthe")
                elif nb < len(self.clees) :
                    matrice_lab[i][j].murs[bord]=Porte(self.taille_mur,self.clees[nb].nom_clee)
                    self.get_voisin_dir(i,j,bord,matrice_lab).murs[self.direction_opposee(bord)]=Porte(self.taille_mur,self.clees[nb].nom_clee)
                else :
                    matrice_lab[i][j].set_mur(bord,MUR_VIDE)
                    self.get_voisin_dir(i,j,bord,matrice_lab).set_mur(self.direction_opposee(bord),MUR_VIDE)

    def pre_generation(self,matrice_lab):
        """
        Fonction qui prend en entrée:
            la matrice de cases du labyrinthe
        et qui pre génère les cases du patern
        """
        coordonnee_x = self.position[0]
        coordonnee_y = self.position[1]
        for i in range(coordonnee_x,coordonnee_x+self.largeur):
            for j in range(coordonnee_y,coordonnee_y+self.hauteur):
                x_pat=i-coordonnee_x
                y_pat=j-coordonnee_y
                #on ne doit générer que les cases au bords
                #plus précisement on doit empêcher le générateur d'y toucher
                if not self.case_est_une_entree(x_pat,y_pat) and self.case_au_bord(x_pat,y_pat):
                    dirs_intouchables=self.contraintes_cases(x_pat,y_pat)
                    for direction in dirs_intouchables:
                        matrice_lab[i][j].set_mur(direction,INTOUCHABLE)
                        if self.get_voisin_dir(i,j,direction,matrice_lab)!=None:
                            self.get_voisin_dir(i,j,direction,matrice_lab).set_mur(self.direction_opposee(direction),INTOUCHABLE)

    def post_generation(self,matrice_lab):
        """
        Fonction qui prend en entrée:
            la matrice de cases du labyrinthe
        et qui clear la salle
        """
        coordonnee_x = self.position[0]
        coordonnee_y = self.position[1]
        for i in range(coordonnee_x,coordonnee_x+self.largeur):
            for j in range(coordonnee_y,coordonnee_y+self.hauteur):
                x_pat=i-coordonnee_x
                y_pat=j-coordonnee_y
                #on enlève les murs intouchables
                if not(self.case_est_une_entree(x_pat,y_pat)) and self.case_au_bord(x_pat,y_pat):
                    dirs_intouchables=self.contraintes_cases(x_pat,y_pat)
                    for direction in dirs_intouchables:
                        matrice_lab[i][j].set_mur(direction,MUR_PLEIN)
                        if self.get_voisin_dir(i,j,direction,matrice_lab)!=None:
                            self.get_voisin_dir(i,j,direction,matrice_lab).set_mur(self.direction_opposee(direction),MUR_PLEIN)
                            
                self.post_generation_case(x_pat,y_pat)
                if self.vide:
                    matrice_lab[i][j]=self.matrice_cases[i-coordonnee_x][j-coordonnee_y]
        self.post_gen_entrees(matrice_lab)

    def pre_generation_case(self,x,y):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
            et génère les murs en fonction de sa position
        """
        #on ne doit générer que les cases au bords
        #plus précisement on doit empêcher le générateur d'y toucher
        if not(self.case_est_une_entree(x,y)) and self.case_au_bord(x,y):
            dirs_intouchables=self.contraintes_cases(x,y)
            
            
    def post_generation_case(self,x,y):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
            et casse les murs les murs en fonction de sa position
        """
        #if not(self.case_au_bord(x,y)) or self.case_est_une_entree(x,y):
        if self.vide :
            if not(self.case_est_une_entree(x,y)):
                self.incorporation_case(x,y)
            else:
                self.clear_case(x,y)
            
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
    
    def incorporation_case(self,x,y):
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
    def get_voisin_dir(self,x,y,direction,matrice_lab):
        """
        Fonction qui prend en en entrées:
            les coordonnées de la case
            la direction du voisin que l'on veut récuperer
            la matrice du labyrinthe
        et renvoie le voisin conformément a la direction
        """

        largeur_lab=len(matrice_lab)
        hauteur_lab=len(matrice_lab[0])

        voisin=None

        if direction==HAUT and y>0:
            voisin=matrice_lab[x][y-1]
            
        elif direction==DROITE and x<largeur_lab-1:
            voisin=matrice_lab[x+1][y]
            
        elif direction==BAS and y<hauteur_lab-1:
            voisin=matrice_lab[x][y+1]
            
        elif direction==GAUCHE and x>0:
            voisin=matrice_lab[x-1][y]
            
        return voisin
    def case_bord(self,x,y,largeur_mat,hauteur_mat):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
            la largeur et la hauteur de la matrice
            et qui renvoie la/les direction/s des bords
        """
        bords=[]
        
        #on ajoute les murs qui ne sont pas aux extrèmes
        if x!=0:
            bords+=[GAUCHE]
            
        if x!=(largeur_mat-1):
            bords+=[DROITE]

        if y!=0:
            bords+=[HAUT]
            
        if y!=(hauteur_mat-1):
            bords+=[BAS]

        return bords
    def contraintes_cases(self,x,y):
        """
        Fonction qui renvoie les murs qui sont soumis a des contraintes
        venant de la salle
        Entrées:
            -les coordonnées de la case
        Sorties:
            -les directions des murs a ne pas caser
        """
        #pour l'instant les contraintes se limites justes au bords de la matrice
        bords=[]
        
        if x==0:
            bords+=[GAUCHE]
            
        if x==(self.largeur-1):
            bords+=[DROITE]

        if y==0:
            bords+=[HAUT]
            
        if y==(self.hauteur-1):
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
    def getCoins(self):
        """
        Fonction qui renvoie les coins de la salle
        """
        coin_haut_gauche=self.position
        coin_bas_gauche=[self.position[0],self.position[1]+self.hauteur-1]
        coin_haut_droite=[self.position[0]+self.largeur-1,self.position[1]+self.hauteur-1]
        coin_bas_droite=[self.position[0]+self.largeur-1,self.position[1]]
        return [coin_haut_gauche,coin_bas_gauche,coin_bas_droite,coin_haut_droite]
    def direction_opposee(self,direction):
        """
        Fonction qui renvoie la direction opposée à celle en entrée
        """
        direction_opposee=0
        
        if direction == HAUT:
            direction_opposee=BAS
        elif direction == DROITE:
            direction_opposee=GAUCHE
        elif direction == BAS:
            direction_opposee=HAUT
        elif direction == GAUCHE:
            direction_opposee=DROITE

        return direction_opposee
