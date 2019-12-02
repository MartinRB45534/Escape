class Stats:

    def __init__(self,force,hauteur_vue,largeur_vue,points_de_vie):
        self.force = force
        self.hauteur_vue = hauteur_vue
        self.largeur_vue = largeur_vue
        self.points_de_vie = points_de_vie

    def change_force(self,bonus_force):
        self.force += bonus_force

    def change_vue(self,bonus_hauteur_vue,bonus_largeur_vue):
        self.hauteur_vue += bonus_hauteur_vue
        self.largeur_vue += bonus_largeur_vue

    def dégats(self,dégats):
        self.points_de_vie -= dégats
