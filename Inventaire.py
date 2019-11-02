from Potion import *
from Clee import *


class Inventaire:

    def __init__(self,potions_force = [],potions_vision = [],potions_visibilité_permanente = []):
        self.potions_force = potions_force
        self.potions_vision = potions_vision
        self.potions_visibilité_permanente = potions_visibilité_permanente
        self.items=[]
    def ramasse_item(self,new_item):
        """
        Fonction qui gère le ramassage d'une item
        Entrée:
            -l'item a ramasser
        """
        self.items.append(new_item)
    def supprime_item(self,item_supp):
        """
        Fonction qui supprime un item spécifique
        Entrée:
            -l'item a supprimer
        """
        i=0
        pop=False
        
        while i<len(self.items) and not(pop):
            if self.items[i]==item_supp:
                pop=True
                self.items.pop(i)
    def get_items_spe(self,type_item):
        """
        Fonction qui renvoie tout lkes items d'un certain type
        Entrée:
            -le type a chercher
        Sortie:
            -tous les items du type sélectionner
        """
        items_voulus=[]

        for item in self.items:
            if issubclass(type(item),type_item):
                items_voulus.append(item)

        return items_voulus
    
