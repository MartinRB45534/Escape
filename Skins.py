import pygame

class Brouillard:
    """L'objet utilisé pour représenter les parties invisibles du labyrinthe."""
    def __init__(self):
        self.skin = SKIN_BROUILLARD

    def affiche(self,screen,position,taille):
        self.skin.dessine_toi(screen,position,taille)

##class Case_vue:
##    """L'objet utilisé pour représenter les cases du labyrinthe."""
##    def __init__(self,murs,effets,clarte):
##        self.skin = SKIN_CASE #Il y a plein de cases différents ! Changer ça !
##        self.effets = effets
##        self.occupants = []
##        self.murs = murs
##
##    def affiche(self,screen,position,taille,observation):
##        self.skin.dessine_toi(screen,position,taille)
##        for occupant in self.occupants:
##            occupant.affiche(screen,position,taille,observation)
##        for mur in self.murs:
##            mur.affiche(screen,position,taille,observation)
##        for effet in self.effets:
##            effet.affiche(screen,position,taille,observation)
##
##class Agissant_vue:
##    """L'objet utilisé pour représenter les agissants."""
##    def __init__(self,items=[],effets=[]):
##        self.skin = SKIN_AGISSANT #Il y a plein d'agissants différents ! Changer ça !
##        self.items = items
##        self.effets = effets
##
##    def affiche(self,screen,position,taille,observation):
##        self.skin.dessine_toi(screen,position,taille)
##        for effet in self.effets:
##            effet.affiche(screen,position,taille,observation)
##
##class Item_vue:
##    """L'objet utilisé pour représenter les items."""
##    def __init__(self,skin,effets=[]):
##        self.skin = skin
##        self.effets = effets
##
##    def affiche(self,screen,position,taille,observation):
##        self.skin.dessine_toi(screen,position,taille)
##        for effet in self.effets:
##            effet.affiche(screen,position,taille,observation)
##
##class Effet_vue:
##    """L'objet utilisé pour représenter les effets."""
##    def __init__(self):
##        self.skin = SKIN_EFFET #Il y a plein d'effets différents ! Changer ça !
##
##    def affiche(self,screen,position,taille,observation):
##        self.skin.dessine_toi(screen,position,taille)
##
##class Mur_vue_haut:
##    """L'objet utilisé pour représenter les murs du labyrinthe."""
##    def __init__(self,effets=[]):
##        self.skin = SKIN_MUR_HAUT #Il y a plein de murs différents ! Changer ça !
##
##    def affiche(self,screen,position,taille,observation):
##        self.skin.dessine_toi(screen,position,taille)
##
##class Mur_vue_bas:
##    """L'objet utilisé pour représenter les murs du labyrinthe."""
##    def __init__(self,effets=[]):
##        self.skin = SKIN_MUR_BAS #Il y a plein de murs différents ! Changer ça !
##
##    def affiche(self,screen,position,taille,observation):
##        self.skin.dessine_toi(screen,position,taille)
##
##class Mur_vue_gauche:
##    """L'objet utilisé pour représenter les murs du labyrinthe."""
##    def __init__(self,effets=[]):
##        self.skin = SKIN_MUR_GAUCHE #Il y a plein de murs différents ! Changer ça !
##
##    def affiche(self,screen,position,taille,observation):
##        self.skin.dessine_toi(screen,position,taille)
##
##class Mur_vue_droite:
##    """L'objet utilisé pour représenter les murs du labyrinthe."""
##    def __init__(self,effets=[]):
##        self.skin = SKIN_MUR_DROITE #Il y a plein de murs différents ! Changer ça !
##
##    def affiche(self,screen,position,taille,observation):
##        self.skin.dessine_toi(screen,position,taille)

class Skin:
    def __init__(self,nom_fichier):
        self.image = pygame.image.load(nom_fichier).convert_alpha()

    def dessine_toi(self,screen,position,taille,direction=(0)):
        screen.blit(pygame.transform.scale(pygame.transform.rotate(self.image,direction*-90),(taille,taille)),position)



global SKIN_BROUILLARD
SKIN_BROUILLARD = Skin("brouillard.png")
global SKIN_CASE
SKIN_CASE = Skin("case.png")
global SKIN_AGISSANT
SKIN_AGISSANT = Skin("agissant.png")
global SKIN_ROUGE
SKIN_ROUGE = Skin("rouge.png")
global SKIN_VERT
SKIN_VERT = Skin("vert.png")
global SKIN_CADAVRE
SKIN_CADAVRE = Skin("cadavre.png")
global SKIN_BLESSURE
SKIN_BLESSURE = Skin("blessure.png")
global SKIN_JOUEUR
SKIN_JOUEUR = Skin("joueur.png")
global SKIN_HUMAIN
SKIN_HUMAIN = Skin("humain.png")
global SKIN_MYSTERE
SKIN_MYSTERE = Skin("mystere.png")
global SKIN_BOUCLIER
SKIN_BOUCLIER = Skin("bouclier.png")
global SKIN_CLE
SKIN_CLE = Skin("cle.png")
global SKIN_EPEE
SKIN_EPEE = Skin("epee.png")
global SKIN_LANCE
SKIN_LANCE = Skin("lance.png")
global SKIN_CASQUE
SKIN_CASQUE = Skin("casque.png")
global SKIN_EFFET
SKIN_EFFET = Skin("effet.png")
global SKIN_MUR
SKIN_MUR = Skin("mur.png")
global SKIN_PORTE
SKIN_PORTE = Skin("porte.png")
global SKIN_PORTE_OUVERTE
SKIN_PORTE_OUVERTE = Skin("porte_ouverte.png")
global SKIN_BARRIERE
SKIN_BARRIERE = Skin("barriere.png")
global SKIN_PORTAIL
SKIN_PORTAIL = Skin("portail.png")
