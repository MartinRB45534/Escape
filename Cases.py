import Murs
import pygame
#constantes
HAUT=0
DROITE=1
BAS=2
GAUCHE=3

MUR_VIDE=0
MUR_PLEIN=1

class Case:
    def __init__(self,tailleCase,tailleMur,couleur=(255,255,255)):
        self.tailleCase=tailleCase
        self.tailleMur=tailleMur
        self.couleur=couleur
        #on sélectionne la classe Mur du fichier Murs (qui est un objet)
        self.murs = [Murs.Mur(MUR_PLEIN,tailleMur) for i in range(4)]
    def nb_murs_non_vides(self):
        pass
    def nb_murs_pleins(self):
        pleins=0

        for mur in self.murs:
            if mur.get_etat()==MUR_PLEIN:
                pleins+=1
        
        return pleins
    def dessine_toi(self,screen,x,y):
        pygame.draw.rect(screen,self.couleur,(x+self.tailleMur,y+self.tailleMur,self.tailleCase,self.tailleCase))
        #on dessine les murs vides en premiers pour éviter les bugs graphiques
        for i in range(0,len(self.murs)):
            if self.murs[i].get_etat()==MUR_VIDE:
                self.murs[i].dessine_toi(screen,x,y,self.tailleCase,i,self.couleur)
        #on dessine les autres murs
        for i in range(0,len(self.murs)):
            if self.murs[i].get_etat()!=MUR_VIDE:
                self.murs[i].dessine_toi(screen,x,y,self.tailleCase,i)
    def casser_mur(self,direction):
        self.murs[direction].set_etat(MUR_VIDE)

    def get_murs(self):
        return self.murs

    def get_mur_haut(self):
        return self.murs[0]
    def get_mur_droit(self):
        return self.murs[1]
    def get_mur_bas(self):
        return self.murs[2]
    def get_mur_gauche(self):
        return self.murs[3]

    def set_Couleur(self,couleur):
        self.couleur=couleur
    def toString(self):
        return "haut "+str(self.murs[0].get_etat())+" droite "+str(self.murs[1].get_etat())+" bas "+str(self.murs[2].get_etat())+" gauche "+str(self.murs[3].get_etat())+"  "
#case=Case(5,52)
