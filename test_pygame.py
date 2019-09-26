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
while run:
    #si l'utilisateur décide de mettre fin au programme on sort de la boucle
    move = False
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
            move = joueur.va_vers_le_haut(lab)
        if event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN:
            move = joueur.va_vers_le_bas(lab)
        if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
            move = joueur.va_vers_la_droite(lab)
        if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
            move = joueur.va_vers_la_gauche(lab)
    if move:
        lab.dessine_toi(screen,0,0)
        joueur.dessine_toi(screen)
    pygame.display.update()
pygame.quit()
#zoli seeds
#249080474072083266
#249080474072083266
