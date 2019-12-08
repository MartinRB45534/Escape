from Potion import *
from Clee import *


class Inventaire:

    def __init__(self,items=[]):
        self.items={}
        self.entree_dico = []
        self.item_courant = 0
        self.longueur = 0
        for item in items:
            self.ramasse_item(item)
        
    def ramasse_item(self,new_item):
        """
        Fonction qui gère le ramassage d'un item
        Entrée:
            -l'item à ramasser
        """
        new_item.position == None
        type_item = str(new_item)
        if type_item in self.entree_dico:
            self.items[type_item].append(new_item)
        else:
            self.entree_dico.append(type_item)
            self.items[type_item]=[new_item]
            self.longueur += 1

    def utilise_item(self):
        """
        Fonction qui utilise l'item actuellement sélectionné dans l'inventaire
        En sortie : Rien
        """
        if self.entree_dico[self.item_courant] != "Clee":
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
        police_titre=pygame.font.SysFont(None,25)
        police_item=pygame.font.SysFont(None,20)
        police_default = pygame.font.SysFont(None, 15)

        titre = police_titre.render("Inventaire",True,(255,255,255))
        screen.blit(titre,(30,70))

        for i in range (self.longueur):
            texte=police_item.render(self.entree_dico[i] + " : " + str(len(self.items[self.entree_dico[i]])),True,(255,255,255))
            if i == self.item_courant:
                pygame.draw.rect(screen,(0,0,0),(3,25*(i+3)+30,255,25))
            screen.blit(texte,(5,25*(i+3)+30))

        text_ctrl = police_default.render("- Appuyer sur Entrée pour revenir au labyrinthe -",True,(255,255,255))
        screen.blit(text_ctrl,(30,25*(i+4)+30))
        text_ctrl = police_default.render("- Appuyer sur + pour voir la description de l'item courant -",True,(255,255,255))
        screen.blit(text_ctrl,(30,25*(i+5)+30))
        text_ctrl = police_default.render("- Appuyer sur Espace pour utiliser l'item courant -",True,(255,255,255))
        screen.blit(text_ctrl,(30,25*(i+6)+30))
        
    def precise_item(self,screen):
        police_titre=pygame.font.SysFont(None,25)
        police_item=pygame.font.SysFont(None,20)
        police_default = pygame.font.SysFont(None, 15)
        
        titre = police_titre.render(self.entree_dico[self.item_courant],True,(255,255,255))
        screen.blit(titre,(30,70))
        
        try:
            type_item = eval(self.entree_dico[self.item_courant])
            infos = type_item.decrit_toi(type_item)
        except:
            infos = ["Cet item n'a pas de description !","Est-ce un item mystère ou un oubli des développeurs ?"]

        for i in range (len(infos)):
            texte=police_item.render(infos[i],True,(255,255,255))
            screen.blit(texte,(5,25*(i+3)+30))

        text_ctrl = police_default.render("- Appuyer sur - pour revenir à l'inventaire -",True,(255,255,255))
        screen.blit(text_ctrl,(30,25*(i+4)+30))

        

    def vers_la_droite(self):
        self.item_courant += 1
        if self.item_courant >= self.longueur:
            self.item_courant = 0

    def vers_la_gauche(self):
        self.item_courant -= 1
        if self.item_courant < 0:
            self.item_courant = self.longueur-1
    def getCopie(self):
        """
        Fonction qui copie l'inventaire
        Entrées:
            Rien
        Sorties:
            -une copie de l'inventaire indépendante de l'objet qui l'as générée
        """
        copie_items = []
        for nom_item in self.items:
            for i in range(len(self.items[nom_item])):
                copie_items.append(self.items[nom_item][i].getCopie())

        copie = Inventaire(copie_items)

        return copie
