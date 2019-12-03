import pygame
from Evenement import *
from Item import *
from Effets import *

bonus_force = 5
bonus_hauteur_vue = 5
bonus_largeur_vue = 5
bonus_pv = 50
bonus_radius_permanent = 1
bonus_radius = 3
temps_effet = 200

class Potion(Item):
    
    def __init__(self,position,cible):
        """fonction qui crée une potion
           à utiliser quand la potion spawn sur la map"""
        self.position = position
        self.cible = cible
        self.couleur = (255,255,0)
        self.effet=None

    #def récupère(self):
    #    """méthode appelée quand le joueur récupère la potion, qui la place dans l'inventaire"""

    def recupere(self):
        """méthode appelée quand le joueur récupère la potion, qui l'utilise instantannément"""
        self.position = None
        return(self.utiliser())

    def utiliser(self):
        """fonction qui agit quand on utilise la potion"""
        self.cible.add_evenement(self.effet)

    def getPosition(self):
        return self.position

class Potion_de_portee(Potion):

    def __init__(self,position,cible):
        Potion.__init__(self,position,cible)
        self.effet = Effet_potion_portee(temps_effet,self.cible)

    def __str__(self):
        return("Potion_de_portee")

class Potion_de_portee_permanente(Potion):

    def __init__(self,position,cible):
        Potion.__init__(self,position,cible)
        self.effet = Effet_potion_portee_permanente(temps_effet,self.cible)

    def __str__(self):
        return("Potion_de_portee_permanente")
        
class Potion_de_soin(Potion):

    def __init__(self,position,cible):
        Potion.__init__(self,position,cible)
        self.effet = Effet_potion_soin(temps_effet,self.cible)

    def __str__(self):
        return("Potion_de_soin")

class Potion_de_soin_permanente(Potion):

    def __init__(self,position,cible):
        Potion.__init__(self,position,cible)
        self.effet = Effet_potion_soin_permanente(temps_effet,self.cible)

    def __str__(self):
        return("Potion_de_soin_permanente")

class Potion_de_force(Potion):

    def __init__(self,position,cible):
        Potion.__init__(self,position,cible)
        self.effet = Effet_potion_force(temps_effet,self.cible)

    def __str__(self):
        return("Potion_de_force")

class Potion_de_force_permanente(Potion):

    def __init__(self,position,cible):
        Potion.__init__(self,position,cible)
        self.effet = Effet_potion_force_permanente(temps_effet,self.cible)

    def __str__(self):
        return("Potion_de_force_permanente")
        
class Potion_de_vision(Potion):

    def __init__(self,position,cible):
        Potion.__init__(self,position,cible)
        self.effet = Effet_potion_vision(temps_effet,self.cible)

    def __str__(self):
        return("Potion_de_vision")

class Potion_de_visibilite_permanente(Potion):

    def __init__(self,position,cible):
        Potion.__init__(self,position,cible)
        self.effet = Effet_potion_visibilite_permanente(temps_effet,self.cible)

    def __str__(self):
        return("Potion_de_visibilité_permanente")

