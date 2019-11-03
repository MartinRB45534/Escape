import pygame
from Constantes import *
from Clee import *
from Inventaire import *

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

class Porte(Mur):
    def __init__(self,tailleMur,nom_clee):
        self.tailleMur=tailleMur
        self.nom_clee=nom_clee
        self.etat=MUR_PLEIN

    def bonne_clee(self,clee_a_verifier):
        """
        Fonction qui vérifie si la clée est la bonne
        Entrées:
            -la clee a tester
        Sorties:
            -un booléen indiquant si la porte s'est ouverte
        """
        if str(self.nom_clee)==str(clee_a_verifier.nom_clee):
            ouverte=True
            self.etat=MUR_VIDE
        else:
            ouverte=False

        return ouverte
    
    def tentative_ouverture(self,inventaire):
        """
        Fonction qui simule une tentative d'ouverture par une entitée
        Entrée:
            -l'inventaire de l'entitée
        Sorties:
            -un booléen indiquant si l'entitée peut passer
        """
        #on récupère toute les clées de l'inventaire
        clees=inventaire.get_items_spe(Clee)
        peut_passer=False

        for clee in clees:
            if self.bonne_clee(clee):
                peut_passer=True
                inventaire.supprime_item(clee)

        return peut_passer
    def dessine_toi(self,screen,case_x,case_y,tailleCase,direction,couleur=(0,0,0)):
        """
        Fonction qui dessine l'objet
            l'écran, la surface sur laquelle on dessine(objet pygame)
            la position de la case sur laquelle est le mur
            la taille de la case en px
            la position du mur par rapport à la case (Bas Haut....)
            éventuellement la couleur du mur
        """
        if self.etat==MUR_PLEIN:
            couleur=(225, 95, 65)
        if self.etat==MUR_PLEIN or self.etat==MUR_VIDE:
            if direction==HAUT:
                pygame.draw.line(screen,couleur,(case_x-self.tailleMur//2,case_y),(case_x+tailleCase+self.tailleMur//2,case_y),self.tailleMur)
            elif direction==DROITE:
                pygame.draw.line(screen,couleur,(case_x+tailleCase,case_y-self.tailleMur//2),(case_x+tailleCase,case_y+tailleCase+self.tailleMur//2),self.tailleMur)
            elif direction==BAS:
                pygame.draw.line(screen,couleur,(case_x-self.tailleMur//2,case_y+tailleCase),(case_x+tailleCase+self.tailleMur//2,case_y+tailleCase),self.tailleMur)
            else:
                pygame.draw.line(screen,couleur,(case_x,case_y-self.tailleMur//2),(case_x,case_y+tailleCase+self.tailleMur//2),self.tailleMur)
        

        
