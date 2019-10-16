from Stats import *

bonus_force = 10
bonus_hauteur_vue = 5
bonus_largeur_vue = 5
temps_effet = 30

class Potion:
    
    def __init__(self,position,planning):
        """fonction qui crée une potion
           à utiliser quand la potion spawn sur la map"""
        self.position = position
        self.planning = planning

    def __init__(self,position,planning,stats):
        """fonction qui crée une potion
           à utiliser quand la potion est directement dans l'inventaire"""
        self.position = (-1,-1) #position factice, pour pouvoir différentier les deux __init__
        self.planning = planning
        self.stats = stats

    #def récupère(self):
    #    """méthode appelée quand le joueur récupère la potion, qui la place dans l'inventaire"""

    def récupère(self,stats):
        """méthode appelée quand le joueur récupère la potion, qui l'utilise instantannément"""
        self.stats = stats
        self.utilise

    def utilise(self):
        """Fonction à surdéfinir dans la classe fille"""
        print("Objet non défini une potion est un type pas une entitée")

    def __del__(self):
        self.fin_effet

    def fin_effet(self):
        """Fonction à surdéfinir dans la classe fille"""
        print("Objet non défini une potion est un type pas une entitée")
        
class Potion_de_force(Potion):
    
    def utilise(self):
        """fonction qui agit quand on utilise la potion"""
        self.stats.change_force(bonus_force)
        planning.ajoute_action(self.fin_effet,temps_effet)
        

    def fin_effet(self):
        """fonction qui agit quand la potion arrête de faire effet"""
        self.stats.change_force(-bonus_force)
        del self

class Potion_de_vision(Potion):

    def utilise(self):
        """fonction qui agit quand on utilise la potion"""
        self.stats.change_vue(bonus_hauteur_vue,bonus_largeur_vue)
        planning.ajoute_action(self.fin_effet,temps_effet)

    def fin_effet(self):
        """fonction qui agit quand la potion arrête de faire effet"""
        self.stats.change_vue(-bonus_hauteur_vue,-bonus_largeur_vue)
        del self

class Potion_de_visibilité_permanente(Potion):

    def utilise(self):
        """fonction qui agit quand on utilise la potion"""
        self.stats.change_vue(bonus_hauteur_vue,bonus_largeur_vue)
        del self


    
