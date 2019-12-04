from Entitee import *
from Evenement import *
class Agissant(Entitee):
    def __init__(self,position,pv,degats,vitesse,radius):
        self.position=position
        self.pv=pv
        self.pv_max=self.pv
        self.regeneration=0
        self.degats=degats
        self.radius=radius
        self.vitesse=vitesse
        #prochaine action
        self.next_action=None
        #id de l'action que l'on veut faire
        self.id_next=None
        #paramètres de la vue
        self.vue=None
        self.largeur_vue=None
        self.hauteur_vue=None
        self.position_vue=None
        #évévnements auquel est soumi l'agissant
        self.evenements=[]
    def soigne_toi(self):
        self.pv+=self.regeneration
        if self.pv > self.pv_max:
            self.pv = self.pv_max
        
    def get_action(self):
        """
        Fonction qui renvoie la prochaine action voulue
        ainsi que l'id qui indique ce que l'on veut faire(attaquer déplacer)
        """
        id_renvoie=self.id_next
        next_action_renvoie=self.next_action

        self.id_next=None
        self.next_action=None
        
        return id_renvoie,next_action_renvoie
    def actualiser_vue(self,new_vue,position_new):
        """
        Fonction qui actualise la vue
        Entrées:
            la nouvelle vue
            la position de la nouvelle vue
        Sorties:Rien
        """
        self.vue=new_vue
        self.position_vue=position_new
    def prochaine_action(self):
        """
        Fonction a surdéfinir qui permet de définir l'action
        """
        print("a surdéfinir")
    def execute_evenements(self):
        """
        Fonction qui exécute les événements propre a l'entitée
        """
        if self.evenements!=None:
            for evenement in self.evenements:
                fini = evenement.execute()
                if fini:
                    self.evenements.pop(self.evenements.index(evenement))
    def add_evenement(self,new_evenement):
        """
        Fonction qui ajoute un evenement
        """
        if self.evenements==None:
            self.evenements=[new_evenement]
        else:
            self.evenements.append(new_evenement)
        
    def getVue(self):
        return self.vue
    def getPosition_vue(self):
        return self.position_vue
    def getLargeurVue(self):
        return self.largeur_vue
    def getHauteurVue(self):
        return self.hauteur_vue
    def getRadius(self):
        return self.radius
    def getVitesse(self):
        return self.vitesse
