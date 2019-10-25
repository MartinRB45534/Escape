import pygame
from Evenement import *

class Animation(Evenement):
    def __init__(self,temps_restant,position,radius,surface):
        self.temps_restant=temps_restant
        self.temps_initial=temps_restant
        self.position=position
        #radius est en pixels
        self.radius_max=radius
        self.surface=surface
    def action(self):
        """
        Fonction qui exécute l'animation
        Entrées:
            La surface sur laquelle on dessine
        Sorties:
            Rien
        """
        print("a surdéfinir")
    def execute(self):
        """
        Fonction qui exécute un tic de l'animation(1 frame = 1 tic)
        Entrées:
            La surface sur laquelle on dessine
        Sorties:
            un booléen indiquant si l'événement est fini
        """
        self.temps_restant-=1
        #on exécute l'événement
        self.action()
        return (self.temps_restant<=0)

class Attaque(Animation):
    def action(self):
        """
        Fonction qui exécute l'animation d'attaque
        Entrées:
            La surface sur laquelle on dessine
        Sorties:
            Rien
        """
        radius=int(self.radius_max*(self.temps_initial/(self.temps_initial+self.temps_restant)))
        pygame.draw.circle(self.surface,(194,54,22),self.position,radius,1)
        
