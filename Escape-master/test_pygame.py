import pygame
from Labyrinthe import *
from Joueur import *
from Constantes import *
from Patern import *

#mode affichage peut valoir voir_tout, parcours_en_profondeur ou aveugle. A gérer dans le menu ?
mode_affichage = aveugle

if mode_affichage == voir_tout :
    LARGEUR_CASE = 20
    LARGEUR_MUR = 1
elif mode_affichage == aveugle :
    LARGEUR_CASE = 45
    LARGEUR_MUR = 5

pygame.init()
#poids permettants de manipuler l'aléatoire
poids=[2,2,2,2]
#salles
salles=[Patern(10,10,LARGEUR_CASE,LARGEUR_MUR)]


lab=Labyrinthe(CASES_X,CASES_Y,CASES_X-1,CASES_Y-1,LARGEUR_CASE,LARGEUR_MUR,poids,salles)
lab.generation()
#lab.resolution(CASES_X-1,CASES_Y-1)

pygame.display.set_caption("test")
screen = pygame.display.set_mode((FENETRE_X,FENETRE_Y),pygame.RESIZABLE)
screen.fill((0,0,0))
run=True

joueur=Joueur()

font = pygame.font.SysFont(None, 72)
textWin = font.render("Vous avez gagné!! \(^o^)/", True, (128, 0, 0))

#varaibles correspondants a la largeur et la hauteur du zoom
zoom_largeur=11
zoom_hauteur=11

position_screen=(0,0)

lab.dessine_toi(screen,joueur.position,position_screen,zoom_largeur,zoom_hauteur,mode_affichage)
joueur.dessine_toi(screen,(zoom_largeur//2,zoom_hauteur//2),LARGEUR_CASE,LARGEUR_MUR,position_screen)

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
            zoom_largeur = event.w//(LARGEUR_CASE + LARGEUR_MUR)
            zoom_hauteur = event.h//(LARGEUR_CASE + LARGEUR_MUR)
            screen.fill((0,0,0))
            lab.dessine_toi(screen,joueur.position,position_screen,zoom_largeur,zoom_hauteur,mode_affichage)
            joueur.dessine_toi(screen,(zoom_largeur//2,zoom_hauteur//2),LARGEUR_CASE,LARGEUR_MUR,position_screen)

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
        screen.fill((0,0,0))
        lab.dessine_toi(screen,joueur.position,position_screen,zoom_largeur,zoom_hauteur,mode_affichage)
        joueur.dessine_toi(screen,(zoom_largeur//2,zoom_hauteur//2),LARGEUR_CASE,LARGEUR_MUR,position_screen)
    
    if lab.as_gagner(joueur.get_position()):
        screen.fill((255,255,255))
        screen.blit(textWin,(0,0))
        run=False
    pygame.display.update()
pygame.quit()
#zoli seeds
#249080474072083266
#249080474072083266
