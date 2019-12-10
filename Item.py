import pygame
from Entitee import *
class Item(Entitee):
    def __init__(self,position):
        self.position=position
        self.couleur=(255,255,0)
    def utiliser(self):
        """
        Fonction qui applique l'item a l'entitée
        """
        print("a surdéfinir")
    def ramasser(self):
        """
        Fonction qui fait les procédures nécessaires au ramassage
        """
        self.position=None
        
    def lacher(self,new_position):
        """
        Fonction qui lache l'item
        Entrée:
            -la nouvelle position de la potion
        """
        self.position=new_position

    def dessine_toi(self,screen,decalage,LARGEUR_CASE,LARGEUR_MUR,position_screen):
        pygame.draw.rect(screen, self.couleur,((decalage[0]*(LARGEUR_CASE+LARGEUR_MUR))+LARGEUR_MUR+position_screen[0],(decalage[1]*(LARGEUR_CASE+LARGEUR_MUR))+LARGEUR_MUR+position_screen[1],LARGEUR_CASE-2*LARGEUR_MUR,LARGEUR_CASE-2*LARGEUR_MUR))
    @classmethod
    def decrit_toi(cls):
        """Fonction qui décrit les effets de l'item"""
        print("À surdéfinir !")

    def getCopie(self):
        """
        Fonction qui copie un item
        Entrées:
            Rien
        Sorties:
            -une copie de l'item indépendante de l'objet qui l'as générée
        """
        print("a surdéfinir")
