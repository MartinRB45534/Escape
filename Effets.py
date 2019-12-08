from Evenement import *
bonus_force = 5
bonus_force_permanent = 3
bonus_vue = 5
bonus_vue_permanent = 3
bonus_pv = 50
bonus_soin = 0.01
bonus_radius_permanent = 1
bonus_radius = 3
temps_effet = 200

class Effet_potion(Evenement):
    def __init__(self,temps_restant,cible,utilise=False):
        self.temps_restant = temps_restant
        self.cible = cible
        self.utilise = False
    def getCopie(self):
        """
        Fonction qui copie un item
        Entrées:
            Rien
        Sorties:
            -une copie de l'item indépendante de l'objet qui l'as générée
        """
        copie = Effet_potion(self.temps_restant, self.cible,self.utilise)
        
        return copie
       
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
            self.cible.soigne(bonus_pv)

class Effet_potion_soin_permanente(Effet_potion):
    
    def action(self):
        if not self.utilise :
            self.utilise = True
            self.cible.regeneration += bonus_soin
            
class Effet_potion_force(Effet_potion):
    
    def action(self):
        if not self.utilise :
            self.utilise = True
            self.cible.degats += bonus_force
        if self.temps_restant == 0:
            self.cible.degats -= bonus_force
            
class Effet_potion_force_permanente(Effet_potion):
    
    def action(self):
        if not self.utilise :
            self.utilise = True
            self.cible.degats += bonus_force_permanent
            
class Effet_potion_vision(Effet_potion):
    
    def action(self):
        if not self.utilise :
            self.utilise = True
            self.cible.largeur_vue += bonus_vue
            self.cible.hauteur_vue += bonus_vue
            self.cible.portee_vue += 2
        if self.temps_restant == 0:
            self.cible.largeur_vue -= bonus_vue
            self.cible.hauteur_vue -= bonus_vue
            self.cible.portee_vue -= 2

class Effet_potion_visibilite_permanente(Effet_potion):
    
    def action(self):
        if not self.utilise :
            self.utilise = True
            self.cible.largeur_vue += bonus_vue_permanent
            self.cible.hauteur_vue += bonus_vue_permanent
            self.cible.portee_vue += 1
