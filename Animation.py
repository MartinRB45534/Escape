import pygame
from Evenement import *

class Animation(Evenement):
    def __init__(self,temps_restant,position_lab,radius,surface):
        self.temps_restant=temps_restant
        self.temps_initial=temps_restant
        self.position_lab=position_lab
        self.position_pixel=None
        #radius est en pixels
        self.radius_max=radius
        self.surface=surface
    def setPosition(self,new_position):
        self.position_pixel=new_position
    def getPosition(self):
        return self.position_lab
    def setRadius(self,new_radius):
        self.radius=new_radius
    def getRadius(self):
        return self.radius
    def execute(self):
        """
        Fonction qui exécute un tic de l'animation(1 frame = 1 tic)
        Entrées:
            Rien
        Sorties:
            un booléen indiquant si l'animation est fini
        """
        self.temps_restant-=1
        if self.position_pixel!=None:
            #on exécute l'animation
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
        pygame.draw.circle(self.surface,(194,54,22),self.position_pixel,radius,1)
        
