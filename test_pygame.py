import pygame
import Labyrinthe
import Joueur
import Constantes

pygame.init()

lab=Labyrinthe.Labyrinthe(Constantes.CASES_X,Constantes.CASES_Y,Constantes.LARGEUR_CASE,Constantes.LARGEUR_MUR)
lab.generation()
#lab.resolution(Constantes.CASES_X-1,Constantes.CASES_Y-1)

pygame.display.set_caption("test")
screen = pygame.display.set_mode((601,601))
screen.fill((125,125,125))
run=True

joueur=Joueur.Joueur()

lab.dessine_toi(screen,0,0)
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
        lab.dessine_toi(screen,0,0)
        joueur.dessine_toi(screen)
    pygame.display.update()
pygame.quit()
#zoli seeds
#249080474072083266
#249080474072083266
