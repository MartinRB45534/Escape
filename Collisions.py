from Resolveur import *
class Collision:
    def __init__(self):
        """Les entitees ne sont pas des attributs"""
        pass
    def tentative_attaque(self,attaquant,entitees):
        """
        Fonction qui test si l'entitée qui essaie d'attaquer le peut
        Entrées:
            l'attaquant
            les potentiels victimes
        Sorties:
            booléen qui indique si l'attaque a réussi
            la liste des entitées actualisées
        """
        succes=False

        vue_attaquant=attaquant.getVue()
        position_vue=attaquant.getPosition_vue()
        position_attaquant=attaquant.getPosition()
        
        resol=Resolveur(vue_attaquant,len(vue_attaquant),len(vue_attaquant[0]),-1,-1,position_attaquant[0]-position_vue[0],position_attaquant[1]-position_vue[1])
        #on récupère la matrice accesible par l'attaque
        mat_explorable=resol.resolution_en_largeur_distance_limitée(False,False,False,True,attaquant.radius)
        
        if entitees!=None:
            for entitee in entitees:
                if entitee!=attaquant:
                    x=entitee.getPosition()[0]-position_vue[0]
                    y=entitee.getPosition()[1]-position_vue[1]
                    
                    if not(x>len(mat_explorable)-1 or x<0 or y>len(mat_explorable[0])-1 or y<0):
                        if mat_explorable[x][y]:
                            succes=True
                            self.attaque(entitee,attaquant)
        return succes,entitees
            
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
