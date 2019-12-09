from Case_speciale import *
from Joueur import *

class Fontaine_heal(Case_speciale):
    def execute(self,entitee):
        """
        Fonction qui exécute le piège
        Entrées:
            -L'entitée sur laquelle on applique le piège
        Sorties:
            -Rien
        """
        if isinstance(entitee, Joueur):
            entitee.pv = entitee.pv_max
