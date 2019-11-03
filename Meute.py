from Cases import *
from Resolveur import *

class Meute:
    def __init__(self,largeur_lab,hauteur_lab):
        self.largeur_lab=largeur_lab
        self.hauteur_lab=hauteur_lab
        self.vue_globale=[[Case(0,0) for i in range(hauteur_lab)]for j in range(largeur_lab)]
        

    def actualisation_vues(self,vues,positions_vues):
        """
        Fonction qui actualise la vue de chaque monstre avec la vue globale
        Entrées:
            -les différentes vues des monstres de la meute
            -les positions des vues des monstres de la meute
        Sorties:
            la vue globale de la meute
        """
        #on construit la vue de la meute
        self.actualisation_vue_globale(vues,positions_vues)

        return self.vue_globale
        
    def actualisation_vue_globale(self,vues,positions_vues):
        """
        Fonction qui actualise la vue globale
        Entrées:
            -les différentes vues des monstres de la meute
            -les positions des vues des monstres de la meute
        Sorties:
            Rien
        """
        self.vue_globale=[[Case(0,0) for i in range(self.hauteur_lab)]for j in range(self.largeur_lab)]
        for i in range(0,len(vues)):
            self.copie_vue(vues[i],positions_vues[i])
            
    
    def copie_vue(self,vue,position_vue):
        """
        Fonction qui copie une vue sur la vue globale
        Entrées:
            -la vue a copier
            -la position de la vue sur le labyrinthe
        Sorties:
            Rien
        """
        for x in range(0,len(vue)):
            for y in range(0,len(vue[0])):
                if x+position_vue[0] < self.largeur_lab and y+position_vue[1] < self.hauteur_lab and x+position_vue[0] >= 0 and y+position_vue[1] >= 0:
                    self.vue_globale[x+position_vue[0]][y+position_vue[1]]=vue[x][y]
