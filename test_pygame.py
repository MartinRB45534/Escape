import pygame
import Labyrinthe

pygame.init()

pygame.display.set_caption("test")
screen = pygame.display.set_mode((500,500))
screen.fill((125,125,125))
run=True

lab=Labyrinthe.Labyrinthe(20,20)
lab.generation()
lab.dessine_toi(screen,0,0)
while run:
    #si l'utilisateur décide de mettre fin au programme on sort de la boucle
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()
