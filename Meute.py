from Cases import *
from Resolveur import *

class Meute:
    def __init__(self,largeur_lab,hauteur_lab,monstres,couleur=(255,0,0)):
        self.largeur_lab=largeur_lab
        self.hauteur_lab=hauteur_lab
        #les monstres sont uuniques a la horde
        self.monstres=monstres
        self.vue_globale=[[Case(0,0) for i in range(hauteur_lab)]for j in range(largeur_lab)]
        

    def prochaines_actions(self):
        """
        Fonction qui renvoie les actions voulues par les monstres
        Entrées:
            Rien
        Sorties:
            -les actions des monstres sous forme de tableau
        """
        actions=[]
        for monstre in self.monstres:
            monstre.prochaine_action()
            #actions+=[monstre.get_action()]

        #return actions
    def actualisation_vues(self,vues,positions_vues,position_joueur):
        """
        Fonction qui actualise la vue de chaque monstre avec la vue globale
        Entrées:
            -les différentes vues des monstres de la meute
            -les positions des vues des monstres de la meute
            -la position du joueur
        Sorties:
            Rien
        """
        #on construit la vue de la meute
        self.actualisation_vue_globale(vues,positions_vues)
        #on actualise la vue de chaque individu de la meute
        for monstre in self.monstres:
            monstre.setPosition_joueur(position_joueur)
            monstre.actualiser_vue(self.vue_globale,(0,0))
        
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
                self.vue_globale[x+position_vue[0]][y+position_vue[1]]=vue[x][y]
    def getDonneesVues(self):
        """
        Fonction qui renvoie les données nécessaires a la récupération des vues
        des monstres
        Entrées:
            Rien
        Sorties:
            -les positions des monstres
            -les largeurs et hauteurs des vues des monstres
        """
        positions=[]
        largeurs_vues=[]
        hauteurs_vues=[]

        for monstre in self.monstres:
            positions+=[monstre.getPosition()]
            largeurs_vues+=[monstre.getLargeurVue()]
            hauteurs_vues+=[monstre.getHauteurVue()]

        return positions,largeurs_vues,hauteurs_vues
    def getMonstres(self):
        return self.monstres
    def setMonstres(self,montres):
        self.monstres=monstres
