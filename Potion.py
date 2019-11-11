import pygame
from Evenement import *
from Item import *

bonus_force = 5
bonus_hauteur_vue = 5
bonus_largeur_vue = 5
temps_effet = 300

class Potion:
    
    def __init__(self,position,cible):
        """fonction qui crée une potion
           à utiliser quand la potion spawn sur la map"""
        self.position = position
        self.cible = cible
        self.couleur = (255,255,0)

    #def récupère(self):
    #    """méthode appelée quand le joueur récupère la potion, qui la place dans l'inventaire"""

    def recupere(self):
        """méthode appelée quand le joueur récupère la potion, qui l'utilise instantannément"""
        return(self.utiliser())

    def utiliser(self):
        """fonction qui agit quand on utilise la potion"""
        return self.effet

    def getPosition(self):
        return self.position

    def dessine_toi(self,screen,decalage,LARGEUR_CASE,LARGEUR_MUR,position_screen):
        pygame.draw.rect(screen, self.couleur,((decalage[0]*(LARGEUR_CASE+LARGEUR_MUR))+LARGEUR_MUR+position_screen[0],(decalage[1]*(LARGEUR_CASE+LARGEUR_MUR))+LARGEUR_MUR+position_screen[1],LARGEUR_CASE-2*LARGEUR_MUR,LARGEUR_CASE-2*LARGEUR_MUR))
        
class Potion_de_force(Potion):

    def __init__(self,position,cible):
        Potion.__init__(self,position,cible)
        self.effet = Effet_potion_force(temps_effet,self.cible)

        
class Potion_de_vision(Potion):

    def __init__(self,position,cible):
        Potion.__init__(self,position,cible)
        self.effet = Effet_potion_vision(temps_effet,self.cible)


class Potion_de_visibilite_permanente(Potion):

    def __init__(self,position,cible):
        Potion.__init__(self,position,cible)
        self.effet = Effet_potion_visibilite_permanente(temps_effet,self.cible)


class Effet_potion(Evenement):
    def __init__(self,temps_restant,cible):
        self.temps_restant = temps_restant
        self.cible = cible
        self.utilise = False
        
class Effet_potion_force(Effet_potion):
    
    def action(self):
        if not self.utilise :
            self.utilise = True
            self.cible.degats += bonus_force
        if self.temps_restant == 0:
            self.cible.degats -= bonus_force
            
class Effet_potion_vision(Effet_potion):
    
    def action(self):
        if not self.utilise :
            self.utilise = True
            self.cible.largeur_vue += bonus_largeur_vue
            self.cible.hauteur_vue += bonus_hauteur_vue
        if self.temps_restant == 0:
            self.cible.largeur_vue -= bonus_largeur_vue
            self.cible.hauteur_vue -= bonus_hauteur_vue

class Effet_potion_visibilite_permanente(Effet_potion):
    
    def action(self):
        if not self.utilise :
            self.utilise = True
            self.cible.largeur_vue += bonus_largeur_vue
            self.cible.hauteur_vue += bonus_hauteur_vue
