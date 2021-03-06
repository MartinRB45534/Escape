from Constantes import *
import pygame

class Skin:

    def __init__(self,nom_fichier,couleur=(0,0,0)):
        try:
            haut = pygame.image.load("images/haut_" + nom_fichier)
            bas = pygame.image.load("images/bas_" + nom_fichier)
            droite = pygame.image.load("images/droite_" + nom_fichier)
            gauche = pygame.image.load("images/gauche_" + nom_fichier)
            immobile = pygame.image.load("images/immobile_" + nom_fichier)
            self.skins = [haut,droite,bas,gauche,immobile]
        except:
            self.skins = None
            self.couleur = couleur

    def resize(self,dimensions):
        if self.skins != None:
            for i in range(len(self.skins)):
                self.skins[i] = pygame.transform.smoothscale(self.skins[i],dimensions)
                
    def dessine_toi(self,screen,position,direction):
        if self.skins == None:
            pygame.draw.rect(screen,self.couleur,(position[0],position[1],19,19))
        elif direction == None:
            screen.blit(self.skins[4],position)
        else:
            screen.blit(self.skins[direction],position)

class Skin_mur(Skin):

    def __init__(self,nom_fichier,couleur=(0,0,0)):
        try:
            haut = pygame.image.load("images/haut_" + nom_fichier)
            bas = pygame.image.load("images/bas_" + nom_fichier)
            droite = pygame.image.load("images/droite_" + nom_fichier)
            gauche = pygame.image.load("images/gauche_" + nom_fichier)
            self.skins = [haut,droite,bas,gauche]
        except:
            self.skins = None
            self.couleur = couleur
    
    def dessine_toi(self,screen,position,direction):
        if self.skins == None:
            if direction==HAUT:
                pygame.draw.line(screen,self.couleur,(position[0],position[1]),(position[0]+21,position[1]),2)
            elif direction==DROITE:
                pygame.draw.line(screen,self.couleur,(position[0]+20,position[1]),(position[0]+20,position[1]+21),2)
            elif direction==BAS:
                pygame.draw.line(screen,self.couleur,(position[0],position[1]+20),(position[0]+21,position[1]+20),2)
            else:
                pygame.draw.line(screen,self.couleur,(position[0],position[1]),(position[0],position[1]+21),2)
        else:
            if direction==HAUT:
                screen.blit(self.skins[direction],(position[0],position[1]-1))
            elif direction==DROITE:
                screen.blit(self.skins[direction],(position[0]+20,position[1]))
            elif direction==BAS:
                screen.blit(self.skins[direction],(position[0],position[1]+20))
            else:
                screen.blit(self.skins[direction],(position[0]-1,position[1]))

class Skin_case(Skin):
    def __init__(self,nom_fichier,couleur=(255,255,255)):
        try:
            self.skin = pygame.image.load("images/" + str(couleur) + nom_fichier)
        except:
            self.skin = None
            self.couleur = couleur

    def dessine_toi(self,screen,position):
        if self.skin == None:
            pygame.draw.rect(screen,self.couleur,(position[0],position[1],20,20))
        else:
            screen.blit(self.skin,position)

class Skin_potion(Skin):
    def __init__(self,nom_fichier,couleur=(255,255,0)):
        try:
            self.skin = pygame.image.load("images/potion_" + nom_fichier)
        except:
            self.skin = None
            self.couleur = couleur

    def dessine_toi(self,screen,position):
        if self.skin == None:
            pygame.draw.rect(screen,self.couleur,(position[0],position[1],19,19))
        else:
            screen.blit(self.skin,position)

class Skin_clee(Skin):
    def __init__(self,nom_fichier,couleur=(249,202,36)):
        try:
            self.skin = pygame.image.load("images/" + nom_fichier)
        except:
            self.skin = None
            self.couleur = couleur

    def dessine_toi(self,screen,position):
        if self.skin == None:
            rayon=5
            pygame.draw.circle(screen,self.couleur,(position[0] + 10,position[1] + 10),rayon)
        else:
            screen.blit(self.skin,position)

class Skin_lance(Skin):
    def __init__(self,nom_fichier):
        try:
            haut = pygame.image.load("images/haut_" + nom_fichier)
            bas = pygame.image.load("images/bas_" + nom_fichier)
            droite = pygame.image.load("images/droite_" + nom_fichier)
            gauche = pygame.image.load("images/gauche_" + nom_fichier)
            self.skins = [haut,droite,bas,gauche]
        except:
            self.skins = None
            print ("L'animation d'attaque directionnelle n'a pas pu être chargée.")

    def dessine_toi(self,screen,position,direction):
        if self.skins != None:
            screen.blit(self.skins[direction],position)

class Skin_stomp(Skin):
    def __init__(self,nom_fichier):
        try:
            self.skin = pygame.image.load("images/" + nom_fichier)
        except:
            self.skin = None
            print ("L'animation d'attaque non-directionnelle n'a pas pu être chargée.")

    def dessine_toi(self,screen,position):
        if self.skin != None:
            screen.blit(self.skin,position)

class Skin_caillou(Skin):
    def __init__(self,nom_fichier):
        try:
            self.skin = pygame.image.load("images/" + nom_fichier)
        except:
            self.skin = None
            self.couleur = (0,0,0)

    def dessine_toi(self,screen,position):
        if self.skin == None:
            pygame.draw.circle(screen, self.couleur,(int(0.5*LARGEUR_CASE+LARGEUR_MUR)+position[0],int(0.5*LARGEUR_CASE+LARGEUR_MUR)+position[1]),1)
        else:
            screen.blit(self.skin,position)

class Skin_pnj(Skin):
    def __init__(self,nom_fichier,couleur=(255,255,255)):
        try:
            self.skin = pygame.image.load("images/" + str(couleur) + nom_fichier)
        except:
            self.skin = None
            self.couleur = couleur

    def dessine_toi(self,screen,position):
        if self.skin == None:
            pygame.draw.rect(screen,self.couleur,(position[0],position[1],19,19))
        else:
            screen.blit(self.skin,position)

global SKIN_VIDE
SKIN_VIDE = Skin_mur("mur_vide.png",(255,255,255))
#SKIN_VIDE.resize((38,38))
global SKIN_PLEIN
SKIN_PLEIN = Skin_mur("mur_plein.png",(0,0,0))
#SKIN_PLEIN.resize((38,38))

global SKIN_VIDE_PORTE
SKIN_VIDE_PORTE = Skin_mur("porte_vide.png",(225,95,65))
global SKIN_PLEIN_PORTE
SKIN_PLEIN_PORTE = Skin_mur("porte_plein.png",(0,0,0))

global SKIN_CASES
SKIN_CASES = [Skin_case("case.png",(255,255,255))]

global SKIN_PNJS
SKIN_PNJS = []

global SKIN_JOUEUR
SKIN_JOUEUR = Skin("joueur.png",(0,255,0))
#SKIN_JOUEUR.resize((38,38))
global SKIN_ATTAQUE_JOUEUR
SKIN_ATTAQUE_JOUEUR = Skin("attaque_joueur.png",(0,255,0))
#SKIN_ATTAQUE_JOUEUR.resize((38,38))
global SKIN_FATTI
SKIN_FATTI = Skin("fatti.png",(0,0,100))
#SKIN_FATTI.resize((38,38))
global SKIN_SLIME
SKIN_SLIME = Skin("slime.png",(255,100,100))
global SKIN_RUNNER
SKIN_RUNNER = Skin("runner.png",(255,0,0))
global SKIN_POTION_SOIN
SKIN_POTION_SOIN = Skin_potion("soin.png")
global SKIN_POTION_PORTEE
SKIN_POTION_PORTEE = Skin_potion("portee.png")
global SKIN_POTION_FORCE
SKIN_POTION_FORCE = Skin_potion("force.png")
global SKIN_POTION_VISION
SKIN_POTION_VISION = Skin_potion("vision.png")
global SKIN_POTION_SUPER_SOIN
SKIN_POTION_SUPER_SOIN = Skin_potion("super_soin.png")
global SKIN_POTION_SUPER_PORTEE
SKIN_POTION_SUPER_PORTEE = Skin_potion("super_portee.png")
global SKIN_POTION_SUPER_FORCE
SKIN_POTION_SUPER_FORCE = Skin_potion("super_force.png")
global SKIN_POTION_SUPER_VISION
SKIN_POTION_SUPER_VISION = Skin_potion("super_vision.png")
global SKIN_CLEE
SKIN_CLEE = Skin_clee("clee.png")
#SKIN_CLEE.resize((38,38))
global SKIN_MANCHE_LANCE
SKIN_MANCHE_LANCE = Skin_lance("manche_lance.png")
global SKIN_POINTE_LANCE
SKIN_POINTE_LANCE = Skin_lance("pointe_lance.png")
global SKIN_STOMP_1
SKIN_STOMP_1 = Skin_stomp("stomp_1.png")
global SKIN_STOMP_2
SKIN_STOMP_2 = Skin_stomp("stomp_2.png")
global SKIN_CAILLOU
SKIN_CAILLOU = Skin_caillou("caillou.png")
