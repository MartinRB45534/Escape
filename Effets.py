from Evenement import *
bonus_force = 5
bonus_hauteur_vue = 5
bonus_largeur_vue = 5
bonus_pv = 50
bonus_radius_permanent = 1
bonus_radius = 3
temps_effet = 200

class Effet_potion(Evenement):
    def __init__(self,temps_restant,cible):
        self.temps_restant = temps_restant
        self.cible = cible
        self.utilise = False
       
class Effet_potion_portee(Effet_potion):
    
    def action(self):
        if not self.utilise :
            self.utilise = True
            self.cible.radius += bonus_radius
        if self.temps_restant == 0:
            self.cible.radius -= bonus_radius

class Effet_potion_portee_permanente(Effet_potion):
    
    def action(self):
        if not self.utilise :
            self.utilise = True
            self.cible.radius += bonus_radius_permanent

class Effet_potion_soin(Effet_potion):
    
    def action(self):
        if not self.utilise :
            self.utilise = True
            self.cible.pv += bonus_pv
            if self.cible.pv > self.cible.pv_max:
                self.cible.pv = self.cible.pv_max
            
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
            self.cible.portee_vue += 1