from Item import *
import pygame

class Clee(Item):
    def __init__(self,position,nom_cle):
        self.position=position
        self.nom_cle=nom_cle
        self.possesseur=None
    def dessine_toi(self,screen,decalage,LARGEUR_CASE,LARGEUR_MUR,position_screen):
        rayon=int((LARGEUR_CASE+LARGEUR_MUR)*0.25)
        pygame.draw.circle(screen,(249,202,36),(int((decalage[0]+0.5)*(LARGEUR_CASE+LARGEUR_MUR))+LARGEUR_MUR+position_screen[0],int((decalage[1]+0.5)*(LARGEUR_CASE+LARGEUR_MUR))+LARGEUR_MUR+position_screen[1]),rayon)
