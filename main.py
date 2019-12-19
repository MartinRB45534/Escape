import pygame
from Niveau import *
from Constantes import *
from Bouton import *
from Session import *

niveau = 1
difficulté = HARD
mode_affichage = distance_max
mode_minimap = voir_tout

#nombres de niveaux (en excluant 0) que l'on a
nb_max_niv = 100




pygame.init()
clock = pygame.time.Clock()

CIEL = 0, 200, 255
GREEN = 0, 255, 0
YELLOW = 255, 255, 0
BLACK = 0,0,0
WHITE = 255,255,255

emplacement_Bouton_1 = (10,10)

emplacement_Bouton_2 = (10,40)

emplacement_Bouton_3 = (10,70)

emplacement_Bouton_4 = (10,100)

emplacement_Bouton_5 = (10,130)

xBoutonStart = 50
yBoutonStart = 10

xBoutonReprendre = 250
yBoutonReprendre = 10

xBoutonQuitter = 450
yBoutonQuitter = 10



def main():
    

    
    fenetre = pygame.display.set_mode((640, 600))
    #ici on prend les images contenues dans les fichiers pour les convertir vers pygame

    imgmenutest = pygame.image.load("images/imgmenutest.png").convert()
    
    #session
    session = Session(niveau,difficulté,mode_affichage,mode_minimap,nb_max_niv)

    loop = True
    
    green_color = GREEN
    yellow_color = YELLOW
    black_color = BLACK
    NIVEXIST= False
    partieEnCours = session.recupere
    while loop:
        pygame.display.set_caption("Menu")
        if fenetre.get_width() != 640 or fenetre.get_height() != 600:
            fenetre = pygame.display.set_mode((640, 600))
        background = pygame.Surface(fenetre.get_size())
        background.fill(BLACK)
        fenetre.blit(background, (0, 0))

        #Ajout du fond dans la fenêtre
        fenetre.blit(imgmenutest, (0, 0))

        tuto = Bouton(fenetre,emplacement_Bouton_1[0],emplacement_Bouton_1[1],WHITE,BLACK,"Tutoriel","test",20,130)
        start = Bouton(fenetre,emplacement_Bouton_2[0],emplacement_Bouton_2[1],WHITE,BLACK,"Nouvelle partie","test",20,130)
        if partieEnCours :
            reprendre = Bouton(fenetre,emplacement_Bouton_3[0],emplacement_Bouton_3[1],WHITE,BLACK,"Continuer","test",20,130)
            quitter = Bouton(fenetre,emplacement_Bouton_4[0],emplacement_Bouton_4[1],WHITE,BLACK,"Quitter","test",20,130)
        else :
            quitter = Bouton(fenetre,emplacement_Bouton_3[0],emplacement_Bouton_3[1],WHITE,BLACK,"Quitter","test",20,130)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            # si clic, le jeu se lance
            elif event.type == pygame.MOUSEBUTTONDOWN and start.survolBouton:
                session.reset_niveau()
                session.run()
                partieEnCours = True
            elif event.type == pygame.MOUSEBUTTONDOWN and quitter.survolBouton:
                loop = False
            elif event.type == pygame.MOUSEBUTTONDOWN and tuto.survolBouton:
                session.tuto_courant = 1
                session.reset_niveau_tuto()
                session.runtuto()

            elif partieEnCours:
                if event.type == pygame.MOUSEBUTTONDOWN and reprendre.survolBouton:
                    session.run()
            
                

        # Actualisation de l'affichage
        pygame.display.flip()
        # 10 fps
        clock.tick(10)

    pygame.quit()
    
main()

    
