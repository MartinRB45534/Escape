import Labyrinthe
import Constantes
import pygame

class Joueur:

    #def __init__(self, niveau) -> None:
    #    """Initialisation à chaque début de niveau"""
    #
    #    self.inventaire = niveau.donne_inventaire(difficulté)
    #    self.position = niveau.donne_position(difficulté)

    def __init__(self, position=(0,0)):
        self.position = position


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

    def dessine_toi(self,screen):
        pygame.draw.rect(screen, pygame.Color(0,255,0), (self.position[0]*(Constantes.LARGEUR_CASE+Constantes.LARGEUR_MUR)+2*Constantes.LARGEUR_MUR,self.position[1]*(Constantes.LARGEUR_CASE+Constantes.LARGEUR_MUR)+2*Constantes.LARGEUR_MUR,Constantes.LARGEUR_CASE-2*Constantes.LARGEUR_MUR,Constantes.LARGEUR_CASE-2*Constantes.LARGEUR_MUR))

    def get_position(self):
        return self.position
