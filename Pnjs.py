from Cases import *
from Resolveur import *
from Agissant import *

class Pnj_passif(Agissant):
    def __init__(self,position, pv, couleur, repliques):
        self.position=position
        self.pv=pv
        self.couleur=couleur
        self.vitesse = 1
        self.largeur_vue = 0
        self.hauteur_vue = 0
        #prochaine action du pnj
        self.next_action=None
        self.id_next=None
        #paramètres de la vue
        self.vue=None
        self.position_vue=None
        self.position_joueur=None
        #événements auquels est soumis le pnj
        self.evenements=[]
        #les répliques du pnj
        self.repliques = repliques
        #nb qui nous indique dans quelle réplique on est
        self.indice_replique = 0
    def interaction(self):
        """
        Fonction qui réagit à une interaction du joueur
        Entrées:
            Rien
        Sorties:
            Rien
        """
        self.id_next = PARLER
        self.repliques[self.indice_replique].position_replique = 0
        self.next_action = self.repliques[self.indice_replique]
    def prochaine_action(self):
        """
        Fonction qui s'éxécute automatiquement
        mais vu que le pnj est passif on ne fait rien
        """
        pass
    def dessine_toi(self,screen,decalage,LARGEUR_CASE,LARGEUR_MUR,position_screen):
        pygame.draw.rect(screen, self.couleur,((decalage[0]*(LARGEUR_CASE+LARGEUR_MUR))+LARGEUR_MUR+position_screen[0],(decalage[1]*(LARGEUR_CASE+LARGEUR_MUR))+LARGEUR_MUR+position_screen[1],LARGEUR_CASE-2*LARGEUR_MUR,LARGEUR_CASE-2*LARGEUR_MUR))
