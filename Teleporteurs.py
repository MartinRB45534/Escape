from Cases import *
from Constantes import *
import pygame

class Teleporteur(Case):
    def __init__(self,cible,tailleCase,tailleMur,couleur=(43,250,250),couleur_mur=(0,0,0)):
        Case.__init__(self,tailleCase,tailleMur,couleur,couleur_mur)
        self.cible = cible

    def teleporte(self):
        return self.cible
