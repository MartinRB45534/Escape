from Evenement import *
from Skin import *

class Animation(Evenement):
    def __init__(self,temps_restant,position_lab,surface):
        self.temps_restant=temps_restant
        self.temps_initial=temps_restant
        self.position_lab=position_lab
        self.position_pixel=None
        self.surface=surface
    def setPosition(self,new_position):
        self.position_pixel=new_position
    def getPosition(self):
        return self.position_lab
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

class Attaque_omnidirectionnelle(Animation):
    def action(self):
        """
        Fonction qui exécute l'animation d'attaque
        Entrées:
            Rien
        Sorties:
            Rien
        """
        if self.temps_restant%2 == 0:
            SKIN_STOMP_1.dessine_toi(self.surface,self.position_pixel)
        else:
            SKIN_STOMP_2.dessine_toi(self.surface,self.position_pixel)
        
class Attaque_unidirectionnelle(Animation):
    def __init__(self,temps_restant,position_lab,direction,surface):
        self.temps_restant=temps_restant
        self.temps_initial=temps_restant
        self.position_lab=position_lab
        self.position_pixel=None
        self.surface=surface
        self.direction=direction
    def action(self):
        """
        Fonction qui exécute l'animation d'attaque
        Entrées:
            Rien
        Sorties:
            Rien
        """
        SKIN_MANCHE_LANCE.dessine_toi(self.surface,self.position_pixel,self.direction)

class Attaque_unidirectionnelle_fin(Animation):
    def __init__(self,temps_restant,position_lab,direction,surface):
        self.temps_restant=temps_restant
        self.temps_initial=temps_restant
        self.position_lab=position_lab
        self.position_pixel=None
        self.surface=surface
        self.direction=direction
    def action(self):
        """
        Fonction qui exécute l'animation d'attaque
        Entrées:
            Rien
        Sorties:
            Rien
        """
        SKIN_POINTE_LANCE.dessine_toi(self.surface,self.position_pixel,self.direction)
