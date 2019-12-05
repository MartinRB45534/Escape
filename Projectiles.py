from Entitee import *

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
