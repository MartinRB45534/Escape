import pygame
from Labyrinthe import *
from Joueur import *
from Constantes import *
from Patern import *

class Niveau:
    def __init__(self,difficulté,mode_affichage):

        self.mode_affichage = mode_affichage
        if self.mode_affichage == voir_tout :
            self.LARGEUR_CASE = 20
            self.LARGEUR_MUR = 1
        elif self.mode_affichage == aveugle :
            self.LARGEUR_CASE = 45
            self.LARGEUR_MUR = 5

        if difficulté == BEGINNER :
            self.CASES_X = 20
            self.CASES_Y = 20
            res = True
            self.salles=[Patern(10,10,self.LARGEUR_CASE,self.LARGEUR_MUR)]
        elif difficulté == EASY :
            self.CASES_X = 20
            self.CASES_Y = 20
            res = False
            self.salles=[Patern(5,5,self.LARGEUR_CASE,self.LARGEUR_MUR)]
        elif difficulté == AVERAGE :
            self.CASES_X = 40
            self.CASES_Y = 40
            res = False
            self.salles=[Patern(5,5,self.LARGEUR_CASE,self.LARGEUR_MUR)]
        elif difficulté == HARD :
            self.CASES_X = 60
            self.CASES_Y = 60
            res = False
            self.salles=[Patern(40,2,self.LARGEUR_CASE,self.LARGEUR_MUR)]
        elif difficulté == INSANE :
            self.CASES_X = 100
            self.CASES_Y = 100
            res = False
            self.salles=[Patern(2,40,self.LARGEUR_CASE,self.LARGEUR_MUR)]
        elif difficulté == IMPOSSIBLE :
            self.CASES_X = 1000
            self.CASES_Y = 1000
            res = False
            self.salles=[Patern(1,1,self.LARGEUR_CASE,self.LARGEUR_MUR)]

        pygame.init()
        #poids permettants de manipuler l'aléatoire
        self.poids=[2,6,2,1]



        self.lab=Labyrinthe(self.CASES_X,self.CASES_Y,self.CASES_X-1,self.CASES_Y-1,self.LARGEUR_CASE,self.LARGEUR_MUR,self.poids,self.salles)
        self.lab.generation()
        if res :
            self.lab.resolution(self.CASES_X-1,self.CASES_Y-1)

        pygame.display.set_caption("test")
        self.screen = pygame.display.set_mode((FENETRE_X,FENETRE_Y),pygame.RESIZABLE)
        self.screen.fill((0,0,0))

        self.joueur=Joueur()

        font = pygame.font.SysFont(None, 72)
        self.textWin = font.render("Vous avez gagné!! \(^o^)/", True, (128, 0, 0))

        #varaibles correspondants a la largeur et la hauteur du zoom
        self.zoom_largeur=11
        self.zoom_hauteur=11

        self.position_screen=(0,0)

    def run(self):
        run=True
        self.lab.dessine_toi(self.screen,self.joueur.position,self.position_screen,self.zoom_largeur,self.zoom_hauteur,self.mode_affichage)
        self.joueur.dessine_toi(self.screen,(self.zoom_largeur//2,self.zoom_hauteur//2),self.LARGEUR_CASE,self.LARGEUR_MUR,self.position_screen)

        #objet qui permet de gérer le temps en pygame
        clock = pygame.time.Clock()
        while run:
            #on cadence à 30 frames/sec
            clock.tick(15)

            move = False
            #si l'utilisateur décide de mettre fin au programme on sort de la boucle
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False

                if event.type == pygame.VIDEORESIZE:
                    self.zoom_largeur = event.w//(self.LARGEUR_CASE + self.LARGEUR_MUR)
                    self.zoom_hauteur = event.h//(self.LARGEUR_CASE + self.LARGEUR_MUR)
                    self.screen.fill((0,0,0))
                    self.lab.dessine_toi(self.screen,self.joueur.position,self.position_screen,self.zoom_largeur,self.zoom_hauteur,self.mode_affichage)
                    self.joueur.dessine_toi(self.screen,(self.zoom_largeur//2,self.zoom_hauteur//2),self.LARGEUR_CASE,self.LARGEUR_MUR,self.position_screen)

            #on récupère toutes les touches préssés sous forme de booléens
            keys=pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                move = self.joueur.va_vers_le_haut(self.lab)
            elif keys[pygame.K_DOWN]:
                move = self.joueur.va_vers_le_bas(self.lab)
            elif keys[pygame.K_RIGHT]:
                move = self.joueur.va_vers_la_droite(self.lab)
            if keys[pygame.K_LEFT]:
                move = self.joueur.va_vers_la_gauche(self.lab)

            #si on détecte un mouvement on redessine l'écran
            if move:
                self.screen.fill((0,0,0))
                self.lab.dessine_toi(self.screen,self.joueur.position,self.position_screen,self.zoom_largeur,self.zoom_hauteur,self.mode_affichage)
                self.joueur.dessine_toi(self.screen,(self.zoom_largeur//2,self.zoom_hauteur//2),self.LARGEUR_CASE,self.LARGEUR_MUR,self.position_screen)

            if self.lab.as_gagner(self.joueur.get_position()):
                self.screen.fill((255,255,255))
                self.screen.blit(self.textWin,(0,0))
                run=False
            pygame.display.update()
        pygame.quit()
#zoli seeds
#249080474072083266
#249080474072083266