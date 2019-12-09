from Labyrinthe import *
from Constantes import *


class Lumiere:
    def __init__(self,position,direction,lab):
        self.position = position
        self.direction = direction #La lumière se propage dans une direction
        self.lab = lab

    def avance(self,screen,position_joueur,position_screen,largeur,hauteur):
        """
        Fonction qui propage la lumière dans une direction voulue
        """

        #On éclaire autour de soi au passage :
        #   -d'un côté
        mouvement, arrivée = self.lab.peut_passer(self.position, (self.direction+1)%4)
        if mouvement :
            self.lab.dessine_case(screen,position_joueur,position_screen,largeur,hauteur,arrivée)

        #   -puis de l'autre
        mouvement, arrivée = self.lab.peut_passer(self.position, (self.direction-1)%4)
        if mouvement :
            self.lab.dessine_case(screen,position_joueur,position_screen,largeur,hauteur,arrivée)

        #   -puis on poursuit vers la case suivante
        mouvement, arrivée = self.lab.peut_passer(self.position, self.direction)
        if mouvement :
            self.lab.dessine_case(screen,position_joueur,position_screen,largeur,hauteur,arrivée)
            self.position = arrivée
            self.avance(screen,position_joueur,position_screen,largeur,hauteur)
