from Labyrinthe import *
from Constantes import *
import pygame
from Agissant import *

class Joueur(Agissant):

    def __init__(self,minimap,inventaire,pv,pv_max,degats,vitesse,radius,largeur_vue,hauteur_vue,position,portee_vue=11):
        self.minimap = minimap
        self.position = position
        self.inventaire = inventaire
        self.pv=pv
        self.pv_max=pv_max
        self.degats=degats
        self.vitesse=vitesse
        self.radius=radius
        #prochaine action
        self.next_action=None
        #id de l'action que l'on veut faire
        self.id_next=None
        #paramètres de la vue
        self.vue=None
        self.largeur_vue=largeur_vue
        self.hauteur_vue=hauteur_vue
        self.position_vue=None
        #la portée de la vue 
        self.portee_vue=portee_vue
        self.evenements=None

    def prochaine_action(self):
        pass
    def va_vers_la_gauche(self):
        """fonction qui demande d'aller vers la gauche"""

        self.next_action=GAUCHE
        self.id_next=BOUGER

    def va_vers_la_droite(self):
        """fonction qui demande d'aller vers la droite"""

        self.next_action=DROITE
        self.id_next=BOUGER

    def va_vers_le_haut(self):
        """fonction qui demande d'aller vers le haut"""

        self.next_action=HAUT
        self.id_next=BOUGER

    def va_vers_le_bas(self):
        """fonction qui demande d'aller vers le bas"""

        self.next_action=BAS
        self.id_next=BOUGER
    def attaque(self):
        """fonction qui demande d'attaquer"""

        self.next_action=None
        self.id_next=ATTAQUER

    def dépose_un_marqueur(self) -> bool:
        """fonction qui pose un marqueur sur la case si possible"""

        coordonnées = self.position
    
    def dessine_toi(self,screen,decalage,LARGEUR_CASE,LARGEUR_MUR,position_screen):
        pygame.draw.rect(screen, pygame.Color(0,255,0),((decalage[0])*(LARGEUR_CASE+LARGEUR_MUR)+LARGEUR_MUR+position_screen[0],(decalage[1])*(LARGEUR_CASE+LARGEUR_MUR)+LARGEUR_MUR+position_screen[1],LARGEUR_CASE-2*LARGEUR_MUR,LARGEUR_CASE-2*LARGEUR_MUR))

    def dessine_minimap(self,screen,position_screen):
        self.minimap.dessine_toi(screen,position_screen)

    def affiche_minimap(self,screen):
        self.minimap.affiche_toi(screen)

    def affiche_inventaire(self,screen):
        self.inventaire.affiche_toi(screen)

    def inventaire_vers_la_droite(self):
        self.inventaire.vers_la_droite()

    def inventaire_vers_la_gauche(self):
        self.inventaire.vers_la_gauche()

    def utilise_inventaire(self):
        self.inventaire.utilise_item()
