import pygame
from Evenement import *
from Item import *
from Effets import *

class Potion(Item):
    
    def __init__(self,position=None,cible=None):
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

    def decrit_toi(cls):
        """Fonction qui décrit les effets de l'item"""
        print("À surdéfinir !")

class Potion_de_portee(Potion):

    def __init__(self,position,cible):
        Potion.__init__(self,position,cible)
        self.effet = Effet_potion_portee(temps_effet,self.cible)

    def __str__(self):
        return("Potion_de_portee")

    def decrit_toi(cls):
        """Fonction qui décrit les effets de l'item"""
        return(["Une potion de portée.","Augmente la portée de {} pendant {} secondes.".format(bonus_radius,temps_effet),"Il est possible de la vendre au magicien."])

class Potion_de_portee_permanente(Potion):

    def __init__(self,position,cible):
        Potion.__init__(self,position,cible)
        self.effet = Effet_potion_portee_permanente(temps_effet,self.cible)

    def __str__(self):
        return("Potion_de_portee_permanente")

    def decrit_toi(cls):
        """Fonction qui décrit les effets de l'item"""
        return(["Une potion de portée permanente","Augmente la portée de {} définitivement.".format(bonus_radius_permanent),"Ne peut pas être vendue."])
        
class Potion_de_soin(Potion):

    def __init__(self,position,cible):
        Potion.__init__(self,position,cible)
        self.effet = Effet_potion_soin(temps_effet,self.cible)

    def __str__(self):
        return("Potion_de_soin")

    def decrit_toi(cls):
        """Fonction qui décrit les effets de l'item"""
        return(["Une potion de soin.","Soigne jusqu'à {} PV.".format(bonus_pv),"Ne peut pas soigner au-delà des PV max.","Il est possible de la vendre au magicien."])

class Potion_de_soin_permanente(Potion):

    def __init__(self,position,cible):
        Potion.__init__(self,position,cible)
        self.effet = Effet_potion_soin_permanente(temps_effet,self.cible)

    def __str__(self):
        return("Potion_de_soin_permanente")

    def decrit_toi(cls):
        """Fonction qui décrit les effets de l'item"""
        return(["Une potion de soin permanente","Augmente la régénération de {} définitivement.".format(bonus_soin),"Ne peut pas être vendue."])

class Potion_de_force(Potion):

    def __init__(self,position,cible):
        Potion.__init__(self,position,cible)
        self.effet = Effet_potion_force(temps_effet,self.cible)

    def __str__(self):
        return("Potion_de_force")

    def decrit_toi(cls):
        """Fonction qui décrit les effets de l'item"""
        return(["Une potion de force.","Augmente la force de {} pendant {} secondes.".format(bonus_force,temps_effet),"(La force représente les dégats infligés lors d'une attaque.)","Il est possible de la vendre au magicien."])

class Potion_de_force_permanente(Potion):

    def __init__(self,position,cible):
        Potion.__init__(self,position,cible)
        self.effet = Effet_potion_force_permanente(temps_effet,self.cible)

    def __str__(self):
        return("Potion_de_force_permanente")

    def decrit_toi(cls):
        """Fonction qui décrit les effets de l'item"""
        return(["Une potion de force permanente","Augmente la force de {} définitivement.".format(bonus_force_permanent),"(La force représente les dégats infligés lors d'une attaque.)","Ne peut pas être vendue."])
        
class Potion_de_vision(Potion):

    def __init__(self,position,cible):
        Potion.__init__(self,position,cible)
        self.effet = Effet_potion_vision(temps_effet,self.cible)

    def __str__(self):
        return("Potion_de_vision")

    def decrit_toi(cls):
        """Fonction qui décrit les effets de l'item"""
        return(["Une potion de vision.","Augmente le champ de vision de {} pendant {} secondes.".format(bonus_vue,temps_effet),"Il est possible de la vendre au magicien."])

class Potion_de_visibilite_permanente(Potion):

    def __init__(self,position,cible):
        Potion.__init__(self,position,cible)
        self.effet = Effet_potion_visibilite_permanente(temps_effet,self.cible)

    def __str__(self):
        return("Potion_de_visibilité_permanente")

    def decrit_toi(cls):
        """Fonction qui décrit les effets de l'item"""
        return(["Une potion de vision permanente","Augmente le champ de vision de {} définitivement.".format(bonus_vue_permanent),"Ne peut pas être vendue."])

