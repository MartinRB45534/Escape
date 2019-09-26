import pygame
import Labyrinthe

pygame.init()

lab=Labyrinthe.Labyrinthe(200,200,2,1)
lab.generation()
lab.resolution(199,199)

pygame.display.set_caption("test")
screen = pygame.display.set_mode((601,601))
screen.fill((125,125,125))
run=True

lab.dessine_toi(screen,0,0)
while run:
    #si l'utilisateur décide de mettre fin au programme on sort de la boucle
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()
#zoli seeds
#249080474072083266
#249080474072083266
