from Resolveur import *
from Agissant import *
from Potion import *
class Collision:
    def __init__(self):
        """Les entitees ne sont pas des attributs"""
        pass
    def tentative_attaque(self,attaquant,agissants):
        """
        Fonction qui test si l'entitée qui essaie d'attaquer le peut
        Entrées:
            l'attaquant
            les potentiels victimes
        Sorties:
            booléen qui indique si l'attaque a réussi
        """
        succes=False

        vue_attaquant=attaquant.getVue()
        position_vue=attaquant.getPosition_vue()
        position_attaquant=attaquant.getPosition()
        
        resol=Resolveur(vue_attaquant,len(vue_attaquant),len(vue_attaquant[0]),-1,-1,position_attaquant[0]-position_vue[0],position_attaquant[1]-position_vue[1])
        #on récupère la matrice accesible par l'attaque
        mat_explorable=resol.resolution_en_largeur_distance_limitée(False,False,False,True,attaquant.radius)
        
        if agissants!=None:
            for agissant in agissants:
                if agissant!=attaquant and isinstance(agissant,Agissant):
                    x=agissant.getPosition()[0]-position_vue[0]
                    y=agissant.getPosition()[1]-position_vue[1]
                    
                    if not(x>len(mat_explorable)-1 or x<0 or y>len(mat_explorable[0])-1 or y<0):
                        if mat_explorable[x][y]:
                            succes=True
                            self.attaque(agissant,attaquant)
        return succes

        return entitees
    def attaque(self,victime,attaquant):
        """
        Fonction qui applique les dégats de l'attaquant à la victime
        Entrées:
            la victime
            l'attaquant
        Sorties:
            Rien
        """
        victime.pv-=attaquant.degats
    def attaque_mutuelle(self,entitee1,entitee2):
        """
        La Fonction qui applique des dégats d'une attaque affectant les deux entitées
        Entrées:
            les deux entitée en train de s'attaquer mutuellement
        Sorties:
            Rien
        
        """
        self.attaque(entitee1,entitee2)
        self.attaque(entitee2,entitee1)
    def case_libre(self,position,agissants):
        """
        Fonction qui vérifie si la case désignée est libre (utilisée pour les déplacements)
        Entrées :
            la position ciblée
            les occupants potentiels de la case
            les occupants potentiels dans les meutes
        Sorties:
            un booléen, si la case est libre ou pas
        """

        libre = True

        if agissants!=None:
            for agissant in agissants:
                if agissant.getPosition() == position:
                    libre = False
        return libre
    def visite_case(self,position,joueur,entitees):
        """
        Fonction qui place dans l'inventaire ou utilise tous les items sur la case
        Entrée :
            la position de la case à dévaliser
            le joueur
            les occupants potentiels de la case (on ne vérifie pas les meutes parce qu'on ne peut pas récupérer un monstre
        Sorties:
            Rien
        """

        evenements = []
        if entitees!=None:
            for entitee in entitees:
                if isinstance(entitee,Potion):
                    evenements.append(entitee.recupere(joueur))
        return evenements
