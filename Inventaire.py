from Potion import *

class Inventaire:

    def __init__(self,stats,planning,nb_potion_force = 0,nb_potion_vision = 0,nb_potion_visibilité_permanente = 0):
        self.stats = stats
        self.nb_potion_force = nb_potion_force
        self.potions_force = [Potion_de_force((-1,-1),planning,self.stats)]*nb_potion_force
        self.nb_potion_vision = nb_potion_vision
        self.potions_vision = [Potion_de_vision((-1,-1),planning,self.stats)]*nb_potion_vision
        self.nb_potion_visibilité_permanente = nb_potion_visibilité_permanente
        self.potions_visibilité_permanente = [Potion_de_visibilité_permanente((-1,-1),planning,self.stats)]*nb_potion_visibilité_permanente
