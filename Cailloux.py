from Entitee import *
import pygame

class Caillou(Entitee):
    def dessine_toi(self,screen,decalage,LARGEUR_CASE,LARGEUR_MUR,position_screen):
        pygame.draw.circle(screen, (0,0,0),(int((decalage[0]+0.5)*(LARGEUR_CASE+LARGEUR_MUR))+LARGEUR_MUR+position_screen[0],int((decalage[1]+0.5)*(LARGEUR_CASE+LARGEUR_MUR))+LARGEUR_MUR+position_screen[1]),1)
