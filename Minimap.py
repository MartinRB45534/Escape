from Cases_minimap import *

class Minimap:
    
    def __init__(self,matrice_cases,mode_minimap,depart,arrivee=None):
        self.matrice_cases = matrice_cases
        self.largeur = len(self.matrice_cases)
        self.hauteur = len(self.matrice_cases[0])
        self.min_visible = depart
        self.max_visible = depart
        for x in range(self.largeur):
            for y in range(self.hauteur):
                self.matrice_cases[x][y] = Case_minimap(self.matrice_cases[x][y].tailleCase,self.matrice_cases[x][y].tailleMur,self.matrice_cases[x][y].murs,mode_minimap,arrivee == (x,y))

    def dessine_toi(self,screen,position_screen):
        """
        Fonction qui dessine la minimap sur l'écran dans le coin
        Entrées:
            l'écran, la surface sur laquelle on dessine(objet pygame)
            la position que l'on prend pour 0,0 sur l'écran (ex: un décalage de 20px sur la droite se traduit par (x+20,y))
        Sorties:
            Rien
        """
        position_x=position_screen[0]
        position_y=position_screen[1]
        for x in range(self.min_visible[0],self.max_visible[0]+1):
            for y in range(self.min_visible[1],self.max_visible[1]+1):
                self.matrice_cases[x][y].dessine_toi(screen,position_x,position_y)
                position_y+=3
            position_y=position_screen[1]
            position_x+=3
            
    def affiche_toi(self,screen):
        """
        Fonction qui affiche la minimap sur l'écran
        Entrées:
            l'écran, la surface sur laquelle on dessine(objet pygame)
        Sorties:
            Rien
        """
        position_x=5
        position_y=30
        for x in range(self.min_visible[0],self.max_visible[0]+1):
            for y in range(self.min_visible[1],self.max_visible[1]+1):
                self.matrice_cases[x][y].affiche_toi(screen,position_x,position_y)
                position_y+=21
            position_y=30
            position_x+=21
    def decouvre(self,position_vue,mat_exploree,position_joueur):
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
                    if x+position_vue[0] > self.max_visible[0] and x+position_vue[0] < self.largeur:
                        self.max_visible = (x+position_vue[0],self.max_visible[1])
                    elif x+position_vue[0] < self.min_visible[0] and x+position_vue[0] >= 0:
                        self.min_visible = (x+position_vue[0],self.min_visible[1])
                    if x+position_vue[1] > self.max_visible[1] and x+position_vue[1] < self.hauteur:
                        self.max_visible = (self.max_visible[0],x+position_vue[1])
                    elif x+position_vue[1] < self.min_visible[1] and x+position_vue[1] >= 0:
                        self.min_visible = (self.min_visible[0],x+position_vue[1])
        return (self.max_visible[0]-self.min_visible[0],self.max_visible[1]-self.min_visible[1])
