from Labyrinthe import *
from Constantes import *


class Lumiere:
    def __init__(self,position,direction,lab):
        self.position = position
        self.direction = direction
        self.lab = lab

    def avance(self,screen,position_joueur,position_screen,largeur,hauteur):
        
        mouvement, arrivée = self.lab.peut_passer(self.position, (self.direction+1)%4)
        if mouvement :
            self.lab.dessine_case(screen,position_joueur,position_screen,largeur,hauteur,arrivée)
            
        mouvement, arrivée = self.lab.peut_passer(self.position, (self.direction-1)%4)
        if mouvement :
            self.lab.dessine_case(screen,position_joueur,position_screen,largeur,hauteur,arrivée)
            
        mouvement, arrivée = self.lab.peut_passer(self.position, self.direction)
        if mouvement :
            self.lab.dessine_case(screen,position_joueur,position_screen,largeur,hauteur,arrivée)
            self.position = arrivée
            self.avance(screen,position_joueur,position_screen,largeur,hauteur)
