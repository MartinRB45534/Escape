from Case_speciale import *

class Piques(Case_speciale):
    def execute(self,entitee):
        """
        Fonction qui exécute le piège
        Entrées:
            -L'entitée sur laquelle on applique le piège
        Sorties:
            -Rien
        """
        entitee.pv -= 10
