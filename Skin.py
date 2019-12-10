from Constantes import *
import pygame

class Skin:

    def __init__(self,nom_fichier,couleur=(0,0,0)):
        try:
            haut = pygame.image.load("haut_" + nom_fichier)
            bas = pygame.image.load("bas_" + nom_fichier)
            droite = pygame.image.load("droite_" + nom_fichier)
            gauche = pygame.image.load("gauche_" + nom_fichier)
            self.skins = [haut,droite,bas,gauche]
        except:
            self.skins = None
            self.couleur = couleur

    def dessine_toi(self,screen,position,direction):
        if self.skins == None:
            pygame.draw.rect(screen,self.couleur,(position[0],position[1],19,19))
        else:
            screen.blit(self.skins[direction],position)

class Skin_mur(Skin):

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
            self.skin = pygame.image.load(str(couleur) + nom_fichier)
        except:
            self.skin = None
            self.couleur = couleur

    def dessine_toi(self,screen,position):
        if self.skin == None:
            pygame.draw.rect(screen,self.couleur,(position[0],position[1],20,20))
        else:
            screen.blit(self.skin,position)

global SKIN_VIDE
SKIN_VIDE = Skin_mur("mur_vide.png",(255,255,255))
global SKIN_PLEIN
SKIN_PLEIN = Skin_mur("mur_plein.png",(0,0,0))

global SKIN_VIDE_PORTE
SKIN_VIDE_PORTE = Skin_mur("porte_vide.png",(225,95,65))
global SKIN_PLEIN_PORTE
SKIN_PLEIN_PORTE = Skin_mur("porte_plein.png",(0,0,0))

global SKIN_CASES
SKIN_CASES = [Skin_case("case.png",(255,255,255))]

global SKIN_JOUEUR
SKIN_JOUEUR = Skin("joueur.png",(0,255,0))
