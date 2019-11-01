from Entitee import *
class Item(Entitee):
    def __init__(self,position):
        self.position=position
        self.possesseur=None
    def utiliser(self):
        """
        Fonction qui applique l'item a l'entitée
        """
        print("a surdéfinir")
    def ramasser(self,entitee):
        """
        Fonction qui recupère les informations de l'entitee qui ramassse l'item
        Entrées:
            -l'entitée qui rammasse l'item
        """
        self.possesseur=entitee
        self.position=None
        
    def lacher(self):
        """
        Fonction qui lache l'item
        """
        self.position=self.possesseur.getPosition()
        self.possesseur=None
