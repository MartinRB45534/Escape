import pygame
from Niveau import *
from Constantes import *

difficulté = HARD
#mode affichage peut valoir voir_tout, parcours_en_profondeur ou aveugle. A gérer dans le menu ?
mode_affichage = parcours_en_profondeur

niv = Niveau(difficulté,mode_affichage)


pygame.init()
clock = pygame.time.Clock()


CIEL = 0, 200, 255
GREEN = 0, 255, 0


def main():
    fenetre = pygame.display.set_mode((640, 300))
    loop = True
    green_color = GREEN
    while loop:
        background = pygame.Surface(fenetre.get_size())
        background.fill(CIEL)

        # Ajout du fond dans la fenêtre
        fenetre.blit(background, (0, 0))

        # ca crée un rectangle vert
        rect_green = pygame.draw.rect(fenetre, green_color, [250, 10, 100, 50])

        # retourne 1 si le curseur est au dessus du bouton
        mouse_xy = pygame.mouse.get_pos()
        
        over_green = rect_green.collidepoint(mouse_xy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            # si clic, le jeu se lance
            elif event.type == pygame.MOUSEBUTTONDOWN and over_green:
                niv.run()


        # Actualisation de l'affichage
        pygame.display.flip()
        # 10 fps
        clock.tick(10)

if __name__ == '__main__':
    main()
        


    
    
    

    
    
