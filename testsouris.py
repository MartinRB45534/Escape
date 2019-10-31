import pygame
from Niveau import *
from Constantes import *

difficulté = HARD
mode_affichage = distance_max




pygame.init()
clock = pygame.time.Clock()

CIEL = 0, 200, 255
GREEN = 0, 255, 0
YELLOW = 255, 255, 0
BLACK = 0,0,0
def main():
    
    fenetre = pygame.display.set_mode((640, 300))
    #ici on prend les images contenues dans les fichiers pour les convertir vers pygame
    start = pygame.image.load("start.png").convert()
    reprendre = pygame.image.load("reprendre.png").convert()
    quitter = pygame.image.load("quitter.png").convert()


    loop = True
    
    green_color = GREEN
    yellow_color = YELLOW
    black_color = BLACK
    NIVEXIST= False
    while loop:
        #si le niveau est crée on évite d'en recréer un à chaque passage de boucle
        if not(NIVEXIST) :
            niv = Niveau(difficulté,mode_affichage)
            NIVEXIST = True

        background = pygame.Surface(fenetre.get_size())
        background.fill(CIEL)

        # Ajout du fond dans la fenêtre
        fenetre.blit(background, (0, 0))

        # ça crée des rectangles qui permettent de zoner les zones clickables...
        rect_green = pygame.draw.rect(fenetre, green_color, [250, 10, 100, 50])
        #...  puis sont remplacées par les boutons
        fenetre.blit(start, (250,10))

        rect_yellow = pygame.draw.rect(fenetre, yellow_color, [250, 85, 100, 50])
        fenetre.blit(reprendre, (250,85))

        rect_black= pygame.draw.rect(fenetre, black_color, [250, 160, 100, 50])
        fenetre.blit(quitter, (250,160))

        # retourne 1 si le curseur est au dessus du bouton
        mouse_xy = pygame.mouse.get_pos()
        
        over_green = rect_green.collidepoint(mouse_xy)
        over_yellow = rect_yellow.collidepoint(mouse_xy)
        over_black = rect_black.collidepoint(mouse_xy)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            # si clic, le jeu se lance
            elif event.type == pygame.MOUSEBUTTONDOWN and over_green:
                niv = Niveau(difficulté,mode_affichage)
                niv.run()

            elif event.type == pygame.MOUSEBUTTONDOWN and over_yellow:
                niv.run()

            elif event.type == pygame.MOUSEBUTTONDOWN and over_black:
                pygame.quit()

        # Actualisation de l'affichage
        pygame.display.flip()
        # 10 fps
        clock.tick(10)


if __name__ == '__main__':
    main()

    
