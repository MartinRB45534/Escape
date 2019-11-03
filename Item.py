from Entitee import *
class Item(Entitee):
    def __init__(self,position):
        self.position=position
    def utiliser(self):
        """
        Fonction qui applique l'item a l'entitée
        """
        print("a surdéfinir")
    def ramasser(self):
        """
        Fonction qui fait les procvédures nécessaires au ramassage
        """
        self.position=None
        
    def lacher(self,new_position):
        """
        Fonction qui lache l'item
        Entrée:
            -la nouvelle position de la potion
        """
        self.position=new_position
