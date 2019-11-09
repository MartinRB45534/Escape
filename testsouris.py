import pygame
from Niveau import *
from Constantes import *

niveau = 4
difficulté = AVERAGE
mode_affichage = distance_max




pygame.init()
clock = pygame.time.Clock()

CIEL = 0, 200, 255
GREEN = 0, 255, 0
YELLOW = 255, 255, 0
BLACK = 0,0,0

xBoutonStart = 50
yBoutonStart = 10

xBoutonReprendre = 250
yBoutonReprendre = 10

xBoutonQuitter = 450
yBoutonQuitter = 10

def main():
    

    
    fenetre = pygame.display.set_mode((640, 300))
    #ici on prend les images contenues dans les fichiers pour les convertir vers pygame
    start = pygame.image.load("start.png").convert()
    reprendre = pygame.image.load("reprendre.png").convert()
    quitter = pygame.image.load("quitter.png").convert()
    imgmenutest = pygame.image.load("imgmenutest.png").convert()
    
    

    loop = True
    
    green_color = GREEN
    yellow_color = YELLOW
    black_color = BLACK
    NIVEXIST= False
    while loop:
        background = pygame.Surface(fenetre.get_size())
        background.fill(BLACK)
        fenetre.blit(background, (0, 0))
        #si le niveau est crée on évite d'en recréer un à chaque passage de boucle
        if not(NIVEXIST) :
            niv = Niveau(niveau,difficulté,mode_affichage)
            NIVEXIST = True


        # Ajout du fond dans la fenêtre
        fenetre.blit(imgmenutest, (0, 0))

        # ça crée des rectangles qui permettent de zoner les zones clickables...
        rect_green = pygame.draw.rect(fenetre, green_color, [xBoutonStart, yBoutonStart, 100, 50])
        #...  puis sont remplacées par les boutons
        fenetre.blit(start, (xBoutonStart,yBoutonStart))

        rect_yellow = pygame.draw.rect(fenetre, yellow_color, [xBoutonReprendre, yBoutonReprendre, 100, 50])
        fenetre.blit(reprendre, (xBoutonReprendre,yBoutonReprendre))

        rect_black= pygame.draw.rect(fenetre, black_color, [xBoutonQuitter, yBoutonQuitter, 100, 50])
        fenetre.blit(quitter, (xBoutonQuitter,yBoutonQuitter))

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
                niv = Niveau(niveau,difficulté,mode_affichage)
                niv.run()

            elif event.type == pygame.MOUSEBUTTONDOWN and over_yellow:
                niv.run()

            elif event.type == pygame.MOUSEBUTTONDOWN and over_black:
                loop = False
                

        # Actualisation de l'affichage
        pygame.display.flip()
        # 10 fps
        clock.tick(10)

    pygame.quit()
    
main()

    
