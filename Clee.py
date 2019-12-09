from Item import *
import pygame

class Clee(Item):
    
    def __init__(self,position=None,nom_clee="clee"):
        self.position=position
        self.nom_clee=nom_clee
        
    def __str__(self):
        return ("Clee")
    
    def dessine_toi(self,screen,decalage,LARGEUR_CASE,LARGEUR_MUR,position_screen):
        rayon=int((LARGEUR_CASE+LARGEUR_MUR)*0.25)
        pygame.draw.circle(screen,(249,202,36),(int((decalage[0]+0.5)*(LARGEUR_CASE+LARGEUR_MUR))+LARGEUR_MUR+position_screen[0],int((decalage[1]+0.5)*(LARGEUR_CASE+LARGEUR_MUR))+LARGEUR_MUR+position_screen[1]),rayon)

    def decrit_toi(cls):
        """Fonction qui décrit les effets de l'item"""
        return(["Une clée.","Sert à ouvrir une ou plusieurs portes."])
    def getCopie(self):
        """
        Fonction qui copie un item
        Entrées:
            Rien
        Sorties:
            -une copie de l'item indépendante de l'objet qui l'as générée
        """
        copie = Clee(self.position, self.nom_clee)

        return copie
