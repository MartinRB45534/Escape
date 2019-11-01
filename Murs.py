import pygame
from Constantes import *

class Mur:
    def __init__(self,etat,tailleMur):
        self.etat = etat
        self.tailleMur = tailleMur
    def dessine_toi(self,screen,case_x,case_y,tailleCase,direction,couleur=(0,0,0)):
        """
        Fonction qui dessine l'objet
            l'écran, la surface sur laquelle on dessine(objet pygame)
            la position de la case sur laquelle est le mur
            la taille de la case en px
            la position du mur par rapport à la case (Bas Haut....)
            éventuellement la couleur du mur
        """
        if self.etat==MUR_PLEIN or self.etat==MUR_VIDE:
            if direction==HAUT:
                pygame.draw.line(screen,couleur,(case_x-self.tailleMur//2,case_y),(case_x+tailleCase+self.tailleMur//2,case_y),self.tailleMur)
            elif direction==DROITE:
                pygame.draw.line(screen,couleur,(case_x+tailleCase,case_y-self.tailleMur//2),(case_x+tailleCase,case_y+tailleCase+self.tailleMur//2),self.tailleMur)
            elif direction==BAS:
                pygame.draw.line(screen,couleur,(case_x-self.tailleMur//2,case_y+tailleCase),(case_x+tailleCase+self.tailleMur//2,case_y+tailleCase),self.tailleMur)
            else:
                pygame.draw.line(screen,couleur,(case_x,case_y-self.tailleMur//2),(case_x,case_y+tailleCase+self.tailleMur//2),self.tailleMur)
    def set_etat(self,new):
        self.etat=new
    def get_etat(self):
        return self.etat

def Porte(Mur):
    def __init__(self,tailleMur):
        pass
