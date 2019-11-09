import Murs
import pygame
from Constantes import *

class Case:
    def __init__(self,tailleCase,tailleMur,couleur=(255,255,255)):
        self.tailleCase=tailleCase
        self.tailleMur=tailleMur
        self.couleur=couleur
        self.decouvert=-1 #le temps depuis que le joueur a vu cette case
        self.passage=False
        self.couleur_minimap=(100,100,100)
        #on sélectionne la classe Mur du fichier Murs (qui est un objet)
        self.murs = [Murs.Mur(MUR_PLEIN,tailleMur) for i in range(4)]
    def nb_murs_non_vides(self):
        pass
    def nb_murs_pleins(self):
        """
        Fonction qui renvoie le nombre de murs pleins dans la case
        """
        pleins=0

        for mur in self.murs:
            if mur.get_etat()==MUR_PLEIN:
                pleins+=1
        
        return pleins
    def dessine_toi(self,screen,x,y):
        """
        Fonction qui dessine l'objet
        Entrées:
            l'écran, la surface sur laquelle on dessine(objet pygame)
            la position de la case
        """
        pygame.draw.rect(screen,self.couleur,(x,y,self.tailleCase,self.tailleCase))
        #on dessine les murs vides en premiers pour éviter les bugs graphiques

        for i in range(0,len(self.murs)):
            if self.murs[i].get_etat()==MUR_VIDE:
                self.murs[i].dessine_toi(screen,x,y,self.tailleCase,i,self.couleur)
        #on dessine les autres murs
        for i in range(0,len(self.murs)):
            if self.murs[i].get_etat()!=MUR_VIDE:
                self.murs[i].dessine_toi(screen,x,y,self.tailleCase,i)

        #on modifie quelques variables pour la minimap
        self.decouvert = 0
        
    def dessine_tout(self,screen,x,y):
        """
        Fonction qui dessine l'objet
        Entrées:
            l'écran, la surface sur laquelle on dessine(objet pygame)
            la position de la case
        """
        pygame.draw.rect(screen,self.couleur_minimap,(x,y,2,2))
        self.set_couleur_minimap()
        #on dessine les murs vides en premiers pour éviter les bugs graphiques

        for i in range(0,len(self.murs)):
            if self.murs[i].get_etat()==MUR_VIDE:
                self.murs[i].dessine_toi(screen,x,y,2,i,self.couleur_minimap)
        #on dessine les autres murs
        for i in range(0,len(self.murs)):
            if self.murs[i].get_etat()!=MUR_VIDE:
                self.murs[i].dessine_toi(screen,x,y,2,i)
                
    def casser_mur(self,direction):
        """
        Fonction qui casse le mur dans la direction indiquée
        """
        self.murs[direction].set_etat(MUR_VIDE)
    def construire_mur(self,direction):
        """
        Fonction qui construit le mur dans la direction indiquée
        """
        self.murs[direction].set_etat(MUR_PLEIN)

    def mur_plein(self,direction):
        """
        Fonction qui indique si le mur indiquée par la direction est plein ou non
        """
        mur_plein=False
        if self.murs[direction].get_etat()==MUR_PLEIN:
            mur_plein=True
        return mur_plein
    def set_couleur_minimap(self):
        if self.passage:
            self.couleur_minimap = (0,100,0)
        elif self.decouvert == 0:
            self.couleur_minimap = (255,255,255)
            self.decouvert = 1
        elif self.decouvert == 1:
            self.couleur_minimap = (200,200,200)

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
