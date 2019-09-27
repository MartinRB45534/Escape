import pygame
from Labyrinthe import *
from Joueur import *
from Constantes import *

pygame.init()
lab=Labyrinthe(CASES_X,CASES_Y,CASES_X-1,CASES_Y-1,LARGEUR_CASE,LARGEUR_MUR)
lab.generation()
lab.resolution(CASES_X-1,CASES_Y-1)

pygame.display.set_caption("test")
screen = pygame.display.set_mode((FENETRE_X,FENETRE_Y))
screen.fill((125,125,125))
run=True

joueur=Joueur()

font = pygame.font.SysFont(None, 72)
textWin = font.render("Vous avez gagné!! \(^o^)/", True, (128, 0, 0))

lab.dessine_toi(screen,joueur.position)
joueur.dessine_toi(screen)

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

    #on récupère toutes les touches préssés sous forme de booléens
    keys=pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        move = joueur.va_vers_le_haut(lab)
    elif keys[pygame.K_DOWN]:
        move = joueur.va_vers_le_bas(lab)
    elif keys[pygame.K_RIGHT]:
        move = joueur.va_vers_la_droite(lab)
    if keys[pygame.K_LEFT]:
        move = joueur.va_vers_la_gauche(lab)
    
    #si on détecte un mouvement on redessine l'écran
    if move:
        screen.fill((125,125,125))
        lab.dessine_toi(screen,joueur.position)
        joueur.dessine_toi(screen)
    
    if lab.as_gagner(joueur.get_position()):
        screen.fill((255,255,255))
        screen.blit(textWin,(0,0))
        run=False
    pygame.display.update()
pygame.quit()
#zoli seeds
#249080474072083266
#249080474072083266
