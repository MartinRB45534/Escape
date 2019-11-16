from Cases_minimap import *
from Lumiere import *

class Minimap:
    
    def __init__(self,matrice_cases,mode_minimap,arrivee=None):
        self.matrice_cases = matrice_cases
        self.largeur = len(self.matrice_cases)
        self.hauteur = len(self.matrice_cases[0])
        for x in range(self.largeur):
            for y in range(self.hauteur):
                self.matrice_cases[x][y] = Case_minimap(self.matrice_cases[x][y].tailleCase,self.matrice_cases[x][y].tailleMur,self.matrice_cases[x][y].murs,mode_minimap,arrivee == (x,y))

    def dessine_toi(self,screen,position_screen):
        """
        Fonction qui dessine le labyrinthe sur l'écran
        Entrées:
            l'écran, la surface sur laquelle on dessine(objet pygame)
            la position que l'on prend pour 0,0 sur l'écran (ex: un décalage de 20px sur la droite se traduit par (x+20,y))
        Sorties:
            Rien
        """

        position_x=position_screen[0]
        position_y=position_screen[1]

        for x in range(0,self.largeur):
            for y in range(0,self.hauteur):
                self.matrice_cases[x][y].dessine_toi(screen,position_x,position_y)
                position_y+=3
            position_y=position_screen[1]
            position_x+=3

    def decouvre(self,position_vue,mat_exploree):
        """
        Fonction qui dessine le labyrinthe sur l'écran
        Entrées:
            l'écran, la surface sur laquelle on dessine(objet pygame)
            la position du joueur
            la position que l'on prend pour 0,0 sur l'écran (ex: un décalage de 20px sur la droite se traduit par (x+20,y))
            la position de la vue dans le labyrinthe
            la largeur en cases
            la hauteur en cases
            le mode d'affichage
            la largueur des cases
            la largeur des murs
            la matrice explorée
        Sorties:
            Rien
        """

        for x in range(len(mat_exploree)):
            for y in range(len(mat_exploree[0])):
                if mat_exploree[x][y]:
                    self.matrice_cases[x+position_vue[0]][y+position_vue[1]].decouvert = 0
