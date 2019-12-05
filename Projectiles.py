from Entitee import *

class Charge(Entitee):
    def __init__(self,radius,degats,position=None,temps_restant=-1):
        self.radius = radius
        self.degats = degats
        self.position = position
        self.temps_restant = temps_restant
        self.temps_max = temps_restant

class Fantome(Entitee):
    def __init__(self):
        print("Fantome ne doit pas être instanciée")

class Projectile(Entitee):
    def __init__(self,position,direction,vitesse,degats,couleur=(135,67,23)):
        self.position = position
        self.direction = direction
        self.vitesse = vitesse
        self.degats = degats
        self.couleur = couleur

    def dessine_toi(self,screen,decalage,LAURGEUR_CASE,LARGEUR_MUR,position_screen):
        if self.direction == HAUT or self.direction == BAS:
            pygame.draw.rect(screen,self.couleur,((decalage[0])*(LARGEUR_CASE+LARGEUR_MUR)+LARGEUR_MUR+position_screen[0] + (LARGEUR_CASE-2*LARGEUR_MUR)//2,(decalage[1])*(LARGEUR_CASE+LARGEUR_MUR)+LARGEUR_MUR+position_screen[1],2,LARGEUR_CASE-2*LARGEUR_MUR))
        else:
            pygame.draw.rect(screen,self.couleur,((decalage[0])*(LARGEUR_CASE+LARGEUR_MUR)+LARGEUR_MUR+position_screen[0],(decalage[1])*(LARGEUR_CASE+LARGEUR_MUR)+LARGEUR_MUR+position_screen[1] + (LARGEUR_CASE-2*LARGEUR_MUR)//2,LARGEUR_CASE-2*LARGEUR_MUR,2))

    def getVitesse(self):
        return self.vitesse

class Explosif(Projectile):
    def __init__(self,position,direction,vitesse,degats,couleur=(135,67,23),charge=Charge(1,5)):
        Projectile.__init__(self,position,direction,vitesse,degats,couleur)
        self.charge = charge

class Perçant(Projectile):
    def __init__(self,position,direction,vitesse,degats,couleur=(135,67,23)):
        Projectile.__init__(self,position,direction,vitesse,degats,couleur)

class Boule_de_feu(Explosif):
    def __init__(self,position,direction,vitesse=2,degats=0,couleur=(255,127,0),charge=Charge(1,20)):
        Projectile.__init__(self,position,direction,vitesse,degats,couleur)
        self.charge = charge

class Fleche(Perçant):
    def __init__(self,position,direction,vitesse=1,degats=5,couleur=(206, 206, 206)):
        Projectile.__init__(self,position,direction,vitesse,degats,couleur)

class Eclair_noir(Explosif,Perçant):
    def __init__(self,position,direction,vitesse=1,degats=25,couleur=(0,0,0),charge=Charge(5,30)):
        Projectile.__init__(self,position,direction,vitesse,degats,couleur)
        self.charge = charge

class Fleche_fantome(Fleche,Fantome):
    def __init__(self,position,direction,vitesse=1,degats=5,couleur=(206, 206, 206)):
        Projectile.__init__(self,position,direction,vitesse,degats,couleur)
