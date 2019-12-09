import pygame



class Bouton:
    def __init__(self,fenetre,positionHorizontale,positionVerticale,couleur,couleurTexte,texte,lien,largeur=20,longueur=40) :
        """Classe qui crée un bouton,
           largeur pour la largeur du bouton,
           longueur pour la longueur du bouton,
           positionHorizontale pour sa position par rapport a l'axe x,
           positionVerticale pour la position du bouton
           par rapport à l'axe des y et le texte pour le texte à l'intérieur du bouton,
           le lien pour renvoyer le cliqueur ailleurs
           """

        

        #position du bouton par rapport à l'écran
        self.positionHorizontale = positionHorizontale
        self.positionVerticale = positionVerticale

        #texte écrit sur le bouton
        self.texte = texte

        #Lien renvoyé par le bouton
        self.lien = lien

        #couleur du bouton
        self.couleur = couleur
        self.couleurTexte = couleurTexte

        #fenetre
        self.fenetre = fenetre
        
        #taille du bouton
        self.largeur = largeur
        self.longueur = longueur

        #pour créer un bouton start, start = Bouton(machin machin)

        #le texte du bouton est crée
        font=pygame.font.Font(None, 24)
        self.champs = font.render(self.texte,1,self.couleurTexte)


 
        corpsBouton = pygame.draw.rect(self.fenetre,self.couleur,[self.positionHorizontale, self.positionVerticale,self.longueur,self.largeur])
        fenetre.blit(self.champs,(self.positionHorizontale+3,self.positionVerticale+3))

        
        self.mouse_xy = pygame.mouse.get_pos()
        self.survolBouton = corpsBouton.collidepoint(self.mouse_xy)

        
