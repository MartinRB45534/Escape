from Resolveur import *
from Agissant import *
from Potion import *
from Clee import *
from Joueur import *
from Monstres import *
from Pnjs import *
from Cailloux import *
from Projectiles import *

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

        mat_explorable,position_vue=self.get_zone_attaque(attaquant)
        
        if agissants!=None:
            for agissant in agissants:
                if agissant!=attaquant and isinstance(agissant,Agissant):
                    x=agissant.getPosition()[0]-position_vue[0]
                    y=agissant.getPosition()[1]-position_vue[1]

                    if not(x>len(mat_explorable)-1 or x<0 or y>len(mat_explorable[0])-1 or y<0):
                        if mat_explorable[x][y]:
                            succes=True
                            self.attaque(agissant,attaquant)
        return succes, mat_explorable
    def tentative_interaction(self,agissant,entitees):
        """
        Fonction qui effectue une interaction entre un agissant et
        une entitée avec laquelle on peut intéragir
        Entrées:
            -l'agissant cherchant à interagir
            -les entitees avec lesquelles on peut intéragir
        Sorties:
            -un booléen indiquant si l'interaction s'est produite
        """
        succes = False

        if entitees != None:
            for entitee in entitees:
                if entitee!=agissant:
                    if self.est_voisin(agissant.getPosition(),entitee.getPosition()):
                        self.try_interaction(agissant,entitee)
        
        return succes
    def est_voisin(self,position1,position2):
        """
        Fonction qui définie si une entitée est au voisinage de l'autre
        Entrées:
            -la position d'une entitée
            -la position d'une autre entitée
        Sorties:
            -un booléen indiquant si les 2 entitées sont au voisinnages l'une de l'autre
        """
        voisins = False

        distance_x = abs(position1[0]-position2[0])
        distance_y = abs(position1[1]-position2[1])

        if distance_x == 1 and distance_y ==0:
            voisins = True
        elif distance_y == 1 and distance_x ==0:
            voisins = True
            
        return voisins
    def get_zone_attaque(self,attaquant):
        """
        Fonction qui détermine la zone de l'attaque
        Entrée:
            -l'attaquant
        Sortie:
            -la matrice correspondant a la zone ou l'attaque a eu lieu
            -la nouvelle position de la vue
        """
        vue_attaquant=attaquant.getVue()
        position_vue=attaquant.getPosition_vue()
        position_attaquant=attaquant.getPosition()


        new_position_vue=position_vue
        mat_attaque=None

        resol = Resolveur(vue_attaquant,len(vue_attaquant),len(vue_attaquant[0]),-1,-1,position_attaquant[0]-position_vue[0],position_attaquant[1]-position_vue[1])


        if attaquant.mode_attaque == HEAVY:
            mat_attaque = resol.resolution_undirectionnelle_limitee(False,attaquant.radius*2,attaquant.dir_regard)
        elif attaquant.mode_attaque == LIGHT:
            mat_attaque = resol.resolution_en_largeur_distance_limitée(False,False,False,True,attaquant.radius)
            
            
        return mat_attaque,new_position_vue
    def attaque(self,victime,attaquant):
        """
        Fonction qui applique les dégats de l'attaquant à la victime
        Entrées:
            la victime
            l'attaquant
        Sorties:
            Rien
        """
        if not(issubclass(type(attaquant),Joueur)):
            victime.pv-=attaquant.degats
        else:
            if attaquant.mode_attaque == HEAVY:
                victime.pv-=attaquant.degats*2
            elif attaquant.mode_attaque == LIGHT:
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
        items_deletes=[]
        if entitees!=None:
            for entitee_bis in entitees:
                if tuple(entitee_bis.getPosition()) == tuple(position_voulue) and entitee_bis!=entitee:
                    valide,suppItem = self.collision_entitees(entitee,entitee_bis,entitees)
                    libre=libre and valide
                    if suppItem:
                        items_deletes.append(entitee_bis)
            self.supp_items(items_deletes,entitees)
        return libre
    def collision_entitees(self,entitee1,entitee2,entitees):
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
        elif issubclass(type(entitee1),Monstre) and issubclass(type(entitee2),Item):
            valide=True
        elif issubclass(type(entitee1),Agissant) and issubclass(type(entitee2),Caillou):
            valide = True
        elif issubclass(type(entitee1),Projectile) and issubclass(type(entitee2),Agissant):
            valide = attaque_projectile(entitee1,entitee2,entitees)
        return valide,suppItem
    def try_interaction(self,agissant,entitee):
        """
        Fonction qui essaie de faire intéragir deux entitées entre elles
        Entrées:
            -l'agissant essayant d'intéragir
            -l'entitée avec laquelle l'agissant veut intéragir
        Sorites:
            -un booléen indiquant si l'intéraction à fonctionner
        """
        succes = False

        if issubclass(type(agissant),Joueur) and issubclass(type(entitee),Pnj_passif):
            #on fait parler le pnj
            entitee.interaction()
        
        return succes
    def supp_items(self,items_a_supp,entitees):
        """
        Fonction qui supprime les items ramassés
        Entrées:
            -les items a supprimer
            -le tableau des entitées
        """
        for item in items_a_supp:
            i=0
            pop=False
            while i<len(entitees) and not(pop):
                if entitees[i]==item:
                    pop=True
                    entitees.pop(i)
                i+=1
        
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
                if isinstance(entitee,Potion) and entitee.getPosition()==position:
                    #à modifier quand on pourra jouer avec l'inventaire
                    evenements.append(entitee.recupere())
        return evenements

    def attaque_projectile(self,projectile,cible,entitees):
        """
        Fonction qui calcule les effets de l'arrivée d'un projectile sur un agissant
        """
        valide = False
        self.attaque(cible,projectile)
        if issubclass(type(projectile),Explosif):
            self.tentative_attaque(projectile.charge,entitees)
        if cible.pv<=0:
            valide = True
            if not issubclass(type(projectile),Perçant):
                projectile.position = None
            
