from Labyrinthe import *
from Constantes import *
from Skin import *
from Agissant import *
import pygame

class Joueur(Agissant):

    def __init__(self,minimap,inventaire,pv,pv_max,mana_max,degats,vitesse_lab,vitesse_autres,radius,largeur_vue,hauteur_vue,position,portee_vue=11):
        self.minimap = minimap
        self.position = position
        self.inventaire = inventaire
        self.pv=pv
        self.regeneration=0
        self.pv_max=pv_max
        self.mana=0
        self.mana_max=mana_max
        self.regeneration_mana=1
        self.degats=degats
        self.vitesse_lab=vitesse_lab
        self.vitesse_autres=vitesse_autres
        self.vitesse=self.vitesse_lab
        self.radius=radius
        #prochaine action
        self.next_action=None
        #id de l'action que l'on veut faire
        self.id_next=None
        self.id_last=None
        #paramètres de la vue
        self.vue=None
        self.largeur_vue=largeur_vue
        self.hauteur_vue=hauteur_vue
        self.position_vue=None
        #la portée de la vue 
        self.portee_vue=portee_vue
        self.evenements=None
        #la direction du regard du joueur
        self.dir_regard = None
        self.drops=[]
        self.mode_attaque=None
        

    def prochaine_action(self):
        pass
    def va_vers_la_gauche(self):
        """fonction qui demande d'aller vers la gauche"""
        self.next_action=GAUCHE
        self.dir_regard = GAUCHE
        self.id_next=BOUGER

    def va_vers_la_droite(self):
        """fonction qui demande d'aller vers la droite"""
        self.next_action=DROITE
        self.dir_regard = DROITE
        self.id_next=BOUGER

    def va_vers_le_haut(self):
        """fonction qui demande d'aller vers le haut"""
        self.next_action=HAUT
        self.dir_regard = HAUT
        self.id_next=BOUGER

    def va_vers_le_bas(self):
        """fonction qui demande d'aller vers le bas"""
        self.next_action=BAS
        self.dir_regard = BAS
        self.id_next=BOUGER
    def attaque(self):
        """fonction qui demande de faire une attaque légère"""
        self.dir_regard = None
        self.mode_attaque=LIGHT
        self.id_next=ATTAQUER
        
    def attaque_lourde(self, direction):
        """fonction qui demande de faire une attaque lourde"""
        self.dir_regard = direction
        self.mode_attaque=HEAVY
        self.id_next=ATTAQUER
        
    def tentative_interaction(self):
        """Fonction qui essaie d'interagir"""
        self.next_action = None
        self.id_next = INTERAGIR

    def dépose_un_marqueur(self) -> bool:
        """fonction qui pose un marqueur sur la case si possible"""

        coordonnées = self.position

    def regen_mana(self):
        self.mana = min(self.mana+self.regeneration_mana,self.mana_max)        
    
    def dessine_toi(self,screen,decalage,LARGEUR_CASE,LARGEUR_MUR,position_screen):
        
        if self.id_last == ATTAQUER:
            SKIN_ATTAQUE_JOUEUR.dessine_toi(screen,((decalage[0])*(LARGEUR_CASE+LARGEUR_MUR)+LARGEUR_MUR+position_screen[0],(decalage[1])*(LARGEUR_CASE+LARGEUR_MUR)+LARGEUR_MUR+position_screen[1]),self.dir_regard)
        else:
            SKIN_JOUEUR.dessine_toi(screen,((decalage[0])*(LARGEUR_CASE+LARGEUR_MUR)+LARGEUR_MUR+position_screen[0],(decalage[1])*(LARGEUR_CASE+LARGEUR_MUR)+LARGEUR_MUR+position_screen[1]),self.dir_regard)

    def dessine_minimap(self,screen,position_screen,dessine):
        self.minimap.dessine_toi(screen,position_screen,self.position,self.portee_vue,dessine)

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

    def precise_item(self,screen):
        self.inventaire.precise_item(screen)

    def getCopie(self):
        """
        Fonction qui copie le joueur
        Entrées:
            Rien
        Sorties:
            -une copie du joueur indépendante de l'objet qui l'as générée
        """
        copie = Joueur(self.minimap.getCopie(self.position), self.inventaire.getCopie(), self.pv, self.pv_max, self.mana_max, self.degats, self.vitesse_lab, self.vitesse_autres, self.radius,self.largeur_vue, self.hauteur_vue, self.position, self.portee_vue)

        return copie
