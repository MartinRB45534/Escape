class Menu:
    BLACK = 0,0,0
    def __init__(tailleFenetreX,tailleFenetreY,couleurDeFond = BLACK):
        """tailleFenetreX : taille horizontale de la fenètre du menu
        tailleFenetreY : taille verticale de la fenètre du menu 
        couleurDeFond : couleur de fond du menu(de basse noir)
        """

        #taille de la fenetre :
        self.tailleFenetreX = tailleFenetreX
        self.tailleFenetreY = tailleFenetreY

        #couleur de fond de la fenètre :
        self.couleurDeFond = couleurDeFond


    def MenuReglage(tailleFenetreX,tailleFenetreY,couleurDeFond = BLACK):
        """Menu pour les réglages
        """
        Menu.__init__(tailleFenetreX,tailleFenetreY,couleurDeFond = BLACK)
        

