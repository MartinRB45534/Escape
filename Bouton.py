import pygame



class Bouton:
    def __init__(self,fenetre,positionHorizontale,positionVerticale,couleur,texte,lien,largeur=20,longueur=40) :
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

        #fenetre
        self.fenetre = fenetre
        
        #taille du bouton
        self.largeur = largeur
        self.longueur = longueur

        #pour créer un bouton start, start = Bouton(machin machin)

        font=pygame.font.Font(None, 24)
        text = font.render("Texte",1,(255,255,255))


 
        rect = pygame.draw.rect(fenetre,couleur,[positionHorizontale, positionVerticale,longueur,largeur])
        fenetre.blit(text,(largeur/2,longueur/10))



#class BoutonMenu(Bouton):
    """Bouton type du menu"""

#    def __init__(positionHorizontale,positionVerticale,texte,lien,largeur,longueur) :
#    Bouton.__init__(positionHorizontale,positionVerticale,texte,lien,largeur,longueur)
    

        
