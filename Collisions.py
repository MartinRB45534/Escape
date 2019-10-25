from Resolveur import *
class Collision:
    def __init__(self):
        """Les entitees ne sont pas des attributs"""
        pass
    def tentative_attaque(self,attaquant,entitees,meutes):
        """
        Fonction qui test si l'entitée qui essaie d'attaquer le peut
        Entrées:
            l'attaquant
            les potentiels victimes
            les potentiels victimes dans les meutes
        Sorties:
            booléen qui indique si l'attaque a réussi
        """
        succes=False

        entitees=self.actualisation_entitees(entitees,meutes)

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
        return succes
    def actualisation_entitees(self,old_entitees,meutes):
        """
        Fonction qui construit le vrai tableau des entitees
        Entrées:
            les entitees contenues normalement
            les meutes contenant d'autres entitees
        Sorties:
            un tableau avec toutes les entitees
        """
        entitees=[]

        for entitee in old_entitees:
            entitees+=[entitee]

        for meute in meutes:
            monstres=meute.getMonstres()
            for entitee in monstres:
                entitees+=[entitee]

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
