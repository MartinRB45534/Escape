import pygame
from Niveau import *
from Constantes import *
from Bouton import *

niveau = 4
difficulté = HARD
mode_affichage = distance_max
mode_minimap = voir_tout




pygame.init()
clock = pygame.time.Clock()

CIEL = 0, 200, 255
GREEN = 0, 255, 0
YELLOW = 255, 255, 0
BLACK = 0,0,0
WHITE = 255,255,255

xBoutonStart = 50
yBoutonStart = 10

xBoutonReprendre = 250
yBoutonReprendre = 10

xBoutonQuitter = 450
yBoutonQuitter = 10



def main():
    

    
    fenetre = pygame.display.set_mode((640, 300))
    #ici on prend les images contenues dans les fichiers pour les convertir vers pygame

    imgmenutest = pygame.image.load("imgmenutest.png").convert()
    
    

    loop = True
    
    green_color = GREEN
    yellow_color = YELLOW
    black_color = BLACK
    NIVEXIST= False
    partieEnCours = False
    while loop:
        background = pygame.Surface(fenetre.get_size())
        background.fill(BLACK)
        fenetre.blit(background, (0, 0))
        #si le niveau est crée on évite d'en recréer un à chaque passage de boucle
        if not(NIVEXIST) :
            niv = Niveau(niveau,difficulté,mode_affichage,mode_minimap)
            NIVEXIST = True


        #Ajout du fond dans la fenêtre
        fenetre.blit(imgmenutest, (0, 0))


        start = Bouton(fenetre,xBoutonStart,yBoutonStart,WHITE,BLACK,"START","test",50,100)
        if partieEnCours :
            reprendre = Bouton(fenetre,xBoutonReprendre,yBoutonReprendre,WHITE,BLACK,"Reprendre","test",50,100)
        else :
            reglage = Bouton(fenetre,xBoutonReprendre,yBoutonReprendre,WHITE,BLACK,"CommingSoon","test",50,100)
            
        quitter = Bouton(fenetre,xBoutonQuitter,yBoutonQuitter,WHITE,BLACK,"Quitter","test",50,100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            # si clic, le jeu se lance
            elif event.type == pygame.MOUSEBUTTONDOWN and start.survolBouton:
                niv = Niveau(niveau,difficulté,mode_affichage,mode_minimap)
                pygame.time.wait(niv.run())
                partieEnCours = True
            elif partieEnCours:
                
                if event.type == pygame.MOUSEBUTTONDOWN and reprendre.survolBouton:
                    pygame.time.wait(niv.run())

            elif event.type == pygame.MOUSEBUTTONDOWN and quitter.survolBouton:
                loop = False
                

        # Actualisation de l'affichage
        pygame.display.flip()
        # 10 fps
        clock.tick(10)

    pygame.quit()
    
main()

    
