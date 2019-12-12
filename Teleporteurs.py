from Case_speciale import *
from Constantes import *
import pygame

class Teleporteur_local(Case_speciale):
    def __init__(self,coord_cible,tailleCase,tailleMur,no_monster=False,couleur=(43,250,250),couleur_mur=(0,0,0),cooldown = 0):
        Case.__init__(self,tailleCase,tailleMur,no_monster,couleur,couleur_mur)
        self.coord_cible = coord_cible
        self.cooldown = cooldown
        self.compteur_interne = 0
        if self.couleur == (255,255,255):
            self.skin = 0
        else:
            self.skin = len(SKIN_CASES)
            SKIN_CASES.append(Skin_case("case.png",self.couleur))

    def execute(self,entitee):
        """
        Fonction qui exécute le piège=>à surdéfinir pour les classes filles
        Entrées:
            -L'entitée qu'on téléporte
        Sorties:
            -Rien
        """
        entitee.position = self.coord_cible

class Teleporteur_global(Teleporteur_local):
    def __init__(self,coord_cible,niveau_cible,tailleCase,tailleMur,no_monster=False,couleur=(43,250,250),couleur_mur=(0,0,0),cooldown = 0):
        Case.__init__(self,tailleCase,tailleMur,no_monster,couleur,couleur_mur)
        self.coord_cible = coord_cible
        self.niveau_cible = niveau_cible
        self.cooldown = cooldown
        self.compteur_interne = 0

    def getNiveau_cible(self):
        """
        Fonction qui renvoie le niveau cible
        Sortie:
            -le niveau cibler par le téléporteur
        """
        return self.niveau_cible
