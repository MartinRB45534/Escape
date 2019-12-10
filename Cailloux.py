from Entitee import *
from Skin import *
import pygame

class Caillou(Entitee):
    def dessine_toi(self,screen,decalage,LARGEUR_CASE,LARGEUR_MUR,position_screen):
        SKIN_CAILLOU.dessine_toi(screen,(decalage[0]*(LARGEUR_CASE+LARGEUR_MUR)+LARGEUR_MUR+position_screen[0],decalage[1]*(LARGEUR_CASE+LARGEUR_MUR)+LARGEUR_MUR+position_screen[1]))
