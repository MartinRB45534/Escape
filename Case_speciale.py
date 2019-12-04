from Cases import *

class Case_speciale(Case):
    def __init__(self,tailleCase,tailleMur,cooldown = 10,couleur=(0,0,0)):
        Case.__init__(self,tailleCase,tailleMur,couleur)
        self.cooldown = cooldown
        self.compteur_interne = 0
    def passage(self,entitee):
        """
        Fonction qui est exécuter lors du passage d'une entitée sur le piège
        Entrées:
            -L'entitée qui marche sur le piège
        Sorties:
            -Rien
        """
        if self.compteur_interne == self.cooldown:
            self.execute(entitee)
            self.compteur_interne = 0
    def actualiser_cooldown(self):
        """
        Fonction exécuter à chaque frame pour actualiser le delai du piège
        """
        if self.compteur_interne < self.cooldown:
            self.compteur_interne += 1
    def execute(self,entitee):
        """
        Fonction qui exécute le piège=>à surdéfinir pour les classes filles
        Entrées:
            -L'entitée sur laquelle on applique le piège
        Sorties:
            -Rien
        """
        print("à surdéfinir")
