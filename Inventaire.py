from Potion import *
from Clee import *


class Inventaire:

    def __init__(self,potions_force = [],potions_vision = [],potions_visibilité_permanente = [],potions_portee = [],potions_portee_permanente = [],potions_soin = [],clees = []):
        self.items={"Potion_de_force":potions_force,
                    "Potion_de_vision":potions_vision,
                    "Potion_de_visibilité_permanente":potions_visibilité_permanente,
                    "Potion_de_portee":potions_portee,
                    "Potion_de_portee_permanente":potions_portee_permanente,
                    "Potion_de_soin":potions_soin,
                    "Clee":clees}
        self.entree_dico = ["Potion_de_force","Potion_de_vision","Potion_de_visibilité_permanente","Potion_de_portee","Potion_de_portee_permanente","Potion_de_soin"]
        self.item_courant = 0
        self.longueur = len(self.items)
        
    def ramasse_item(self,new_item):
        """
        Fonction qui gère le ramassage d'un item
        Entrée:
            -l'item à ramasser
        """
        self.items[str(new_item)].append(new_item)

    def utilise_item(self):
        """
        Fonction qui utilise l'item actuellement sélectionné dans l'inventaire
        En sortie : Rien
        """
        if self.item_courant != 6:
            if self.items[self.entree_dico[self.item_courant]] != []:
                self.items[self.entree_dico[self.item_courant]][0].utiliser()
                self.items[self.entree_dico[self.item_courant]].pop()
            else:
                print ("Il n'y en a plus !")
        else:
            print ("On ne peut pas utiliser une clée !")
    def supprime_item(self,item_supp):
        """
        Fonction qui supprime un item spécifique
        Entrée:
            -l'item a supprimer
        """
        i=0
        pop=False
        
        while i<len(self.items[str(item_supp)]) and not(pop):
            if self.items[str(item_supp)][i]==item_supp:
                pop=True
                self.items[str(item_supp)].pop(i)
                
    def get_items_spe(self,type_item):
        """
        Fonction qui renvoie tout les items d'un certain type
        Entrée:
            -le type à chercher
        Sortie:
            -tous les items du type sélectionné
        """

        return self.items[type_item]
    
    def affiche_toi(self,screen):
        police_item=pygame.font.SysFont(None, 20)
        for i in range (self.longueur - 1):
            texte=police_item.render(self.entree_dico[i] + " : " + str(len(self.items[self.entree_dico[i]])),True,(255,255,255))
            if i == self.item_courant:
                pygame.draw.rect(screen,(0,0,0),(3,25*(i+1),255,25))
            screen.blit(texte,(5,25*(i+1)))

    def vers_la_droite(self):
        self.item_courant += 1
        if self.item_courant >= self.longueur-1:
            self.item_courant = 0

    def vers_la_gauche(self):
        self.item_courant -= 1
        if self.item_courant < 0:
            self.item_courant = self.longueur-2
