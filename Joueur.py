from Labyrinthe import *
from Constantes import *
import pygame

class Joueur:

    #def __init__(self, niveau) -> None:
    #    """Initialisation à chaque début de niveau"""
    #
    #    self.inventaire = niveau.donne_inventaire(difficulté)
    #    self.position = niveau.donne_position(difficulté)

    def __init__(self, stats, inventaire, position=(0,0)):
        self.position = position
        self.stats = stats
        self.inventaire = inventaire


    def va_vers_la_gauche(self, labyrinthe) -> bool:
        """fonction qui déplace, si possible, le joueur vers la gauche"""

        coordonnées = self.position
        gauche = 3
        mouvement, arrivée = labyrinthe.peut_passer(coordonnées, gauche)
        if mouvement :
            self.position = arrivée
        return mouvement

    def va_vers_la_droite(self, labyrinthe) -> bool:
        """fonction qui déplace, si possible, le joueur vers la gauche"""

        coordonnées = self.position
        droite = 1
        mouvement, arrivée = labyrinthe.peut_passer(coordonnées, droite)
        if mouvement :
            self.position = arrivée
        return mouvement

    def va_vers_le_haut(self, labyrinthe) -> bool:
        """fonction qui déplace, si possible, le joueur vers la gauche"""

        coordonnées = self.position

        haut = 0
        mouvement, arrivée = labyrinthe.peut_passer(coordonnées, haut)
        if mouvement :
            self.position = arrivée
        return mouvement

    def va_vers_le_bas(self, labyrinthe) -> bool:
        """fonction qui déplace, si possible, le joueur vers la gauche"""

        coordonnées = self.position
        bas = 2
        mouvement, arrivée = labyrinthe.peut_passer(coordonnées, bas)
        if mouvement :
            self.position = arrivée
        return mouvement

    def dépose_un_marqueur(self) -> bool:
        """fonction qui pose un marqueur sur la case si possible"""

        coordonnées = self.position

    def dessine_toi(self,screen,decalage,LARGEUR_CASE,LARGEUR_MUR,position_screen):
        pygame.draw.rect(screen, pygame.Color(0,255,0),((decalage[0])*(LARGEUR_CASE+LARGEUR_MUR)+LARGEUR_MUR+position_screen[0],(decalage[1])*(LARGEUR_CASE+LARGEUR_MUR)+LARGEUR_MUR+position_screen[1],LARGEUR_CASE-2*LARGEUR_MUR,LARGEUR_CASE-2*LARGEUR_MUR))

    def get_position(self):
        return self.position
