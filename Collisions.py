from Resolveur import *
from Agissant import *
from Potion import *
from Clee import *
from Joueur import *

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
    def case_libre(self,entitee,position_voulue,entitees):
        """
        Fonction qui vérifie si la case désignée est libre (utilisée pour les déplacements)
        Entrées :
            l'entitee qui veut ce deplacer
            les occupants potentiels de la case
        Sorties:
            un booléen, si la case est libre ou pas
        """

        libre = True

        if entitees!=None:
            for entitee_bis in entitees:
                if tuple(entitee_bis.getPosition()) == tuple(position_voulue) and entitee_bis!=entitee:
                    libre,suppItem = self.collision_entitees(entitee,entitee_bis)
                    if suppItem:
                        i=0
                        pop=False
                        while i<len(entitees) and not(pop):
                            if entitees[i]==entitee_bis:
                                pop=True
                                entitees.pop(i)
                            i+=1
        return libre
    def collision_entitees(self,entitee1,entitee2):
        """
        Fonction qui gère la collision entre deux entitées
        Entrées:
            Les deux entitées
        Sorties:
            Un booléen indiquant si l'on valide le mouvement
            Un booléen indiquant si l'on doit supprimer un item (tjr l'entitee2)
        """
        valide=False
        suppItem=False
        #on vérifie si le joueur veut ramasser un item
        if isinstance(entitee1,Joueur) and issubclass(type(entitee2),Item):
            valide=True
            suppItem=True
            entitee2.ramasser()
            entitee1.inventaire.ramasse_item(entitee2)
            
        return valide,suppItem
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
