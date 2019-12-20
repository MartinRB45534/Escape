from Cases_minimap import *

class Minimap:
    
    def __init__(self,matrice_cases,mode_minimap,depart,arrivee=None):
        self.matrice_cases = matrice_cases
        self.largeur = len(self.matrice_cases)
        self.hauteur = len(self.matrice_cases[0])
        self.min_visible = depart
        self.max_visible = depart
        self.min_visible_precedent = self.min_visible
        self.max_visible_precedent = self.max_visible
        for x in range(self.largeur):
            for y in range(self.hauteur):
                self.matrice_cases[x][y] = Case_minimap(self.matrice_cases[x][y].tailleCase,self.matrice_cases[x][y].tailleMur,self.matrice_cases[x][y].murs,mode_minimap,arrivee == (x,y))
        self.zoom = 3
        self.position_centre = depart
        self.decalage = 5

        self.mode_minimap = mode_minimap
        self.arrivee = arrivee
        self.accessible = True
        
    def dessine_toi(self,screen,position_screen,position_joueur,portee_vue,dessine=True):
        """
        Fonction qui dessine la minimap sur l'écran dans le coin
        Entrées:
            l'écran, la surface sur laquelle on dessine(objet pygame)
            la position que l'on prend pour 0,0 sur l'écran (ex: un décalage de 20px sur la droite se traduit par (x+20,y))
        Sorties:
            Rien
        """
        if TAILLE_FIXE:
            position_x=position_screen[0]+3
            position_y=position_screen[1]+3
            pygame.draw.rect(screen,(0,0,0),(position_x-3,position_y-3,taille_fixe*6+6,taille_fixe*6+6))
            for x in range(position_joueur[0]-taille_fixe,position_joueur[0]+taille_fixe):
                if x in range(self.min_visible[0],self.max_visible[0]+1):
                    for y in range(position_joueur[1]-taille_fixe,position_joueur[1]+taille_fixe):
                        if y in range(self.min_visible[1],self.max_visible[1]+1):
                            self.matrice_cases[x][y].dessine_toi(screen,position_x,position_y)
                            position_y+=3
                position_y=position_screen[1]
                position_x+=3
            self.min_visible_precedent = self.min_visible
            self.max_visible_precedent = self.max_visible
            
        elif self.min_visible_precedent != self.min_visible or self.max_visible_precedent != self.max_visible or dessine:
            position_x=position_screen[0]
            position_y=position_screen[1]
            for x in range(self.min_visible[0],self.max_visible[0]+1):
                for y in range(self.min_visible[1],self.max_visible[1]+1):
                    self.matrice_cases[x][y].dessine_toi(screen,position_x,position_y)
                    position_y+=3
                position_y=position_screen[1]
                position_x+=3
            self.min_visible_precedent = self.min_visible
            self.max_visible_precedent = self.max_visible

        else:
            self.redessine_toi(screen,position_screen)
        
    def redessine_toi(self,screen,position_screen):
        """
        Fonction qui dessine la minimap sur l'écran dans le coin
        Entrées:
            l'écran, la surface sur laquelle on dessine(objet pygame)
            la position que l'on prend pour 0,0 sur l'écran (ex: un décalage de 20px sur la droite se traduit par (x+20,y))
        Sorties:
            Rien
        """
        position_x=position_screen[0]
        position_y=position_screen[1]
        for x in range(self.min_visible[0],self.max_visible[0]+1):
            for y in range(self.min_visible[1],self.max_visible[1]+1):
                if (self.matrice_cases[x][y].decouvert != -1 and self.matrice_cases[x][y].decouvert < 3):
                    self.matrice_cases[x][y].dessine_toi(screen,position_x,position_y)
                position_y+=3
            position_y=position_screen[1]
            position_x+=3
            
    def affiche_toi(self,screen):
        """
        Fonction qui affiche la minimap sur l'écran
        Entrées:
            l'écran, la surface sur laquelle on dessine(objet pygame)
        Sorties:
            Rien
        """
        police_titre=pygame.font.SysFont(None,25)
        police_default = pygame.font.SysFont(None, 15)

        titre = police_titre.render("Minimap",True,(255,255,255))
        screen.blit(titre,(30,70))
        
        marge_x = 10
        marge_y = 90
        
        decalage = self.decalage * self.zoom
        cases_dispo = ((screen.get_width()-20)//decalage,(screen.get_height()-40)//decalage)
        coin_haut_droit = (self.position_centre[0]-cases_dispo[0]//2,self.position_centre[1]-cases_dispo[1]//2)
        coin_bas_gauche = (self.position_centre[0]+cases_dispo[0]//2,self.position_centre[1]+cases_dispo[1]//2)
        if coin_haut_droit[0] < self.min_visible[0]:
            marge_x += (self.min_visible[0] - coin_haut_droit[0]) * decalage
            coin_haut_droit = (self.min_visible[0],coin_haut_droit[1])
        if coin_haut_droit[1] < self.min_visible[1]:
            marge_y += (self.min_visible[1] - coin_haut_droit[1]) * decalage
            coin_haut_droit = (coin_haut_droit[0],self.min_visible[1])
        if coin_bas_gauche[0] > self.max_visible[0]+1:
            coin_bas_gauche = (self.max_visible[0]+1,coin_bas_gauche[1])
        if coin_bas_gauche[1] > self.max_visible[1]+1:
            coin_bas_gauche = (coin_bas_gauche[0],self.max_visible[1]+1)

        position_x = marge_x
        position_y = marge_y
        
        for x in range(coin_haut_droit[0],coin_bas_gauche[0]):
            for y in range(coin_haut_droit[1],coin_bas_gauche[1]):
                self.matrice_cases[x][y].affiche_toi(screen,position_x,position_y,self.zoom)
                position_y+=decalage
            position_y=marge_y
            position_x+=decalage

        text_ctrl = police_default.render("- Appuyer sur Entrée pour revenir au labyrinthe -",True,(255,255,255))
        screen.blit(text_ctrl,(30,position_y+decalage*(coin_bas_gauche[1]-coin_haut_droit[1])+30))
        text_ctrl = police_default.render("- Utilisez les touches directionnelles pour naviguer la minimap -",True,(255,255,255))
        screen.blit(text_ctrl,(30,position_y+decalage*(coin_bas_gauche[1]-coin_haut_droit[1])+55))

    def deplace_toi(self,direction):
        if direction == GAUCHE:
            if self.position_centre[0] > self.min_visible[0]:
                self.position_centre = (self.position_centre[0]-1,self.position_centre[1])
        if direction == DROITE:
            if self.position_centre[0] < self.max_visible[0]:
                self.position_centre = (self.position_centre[0]+1,self.position_centre[1])

        if direction == HAUT:
            if self.position_centre[1] > self.min_visible[1]:
                self.position_centre = (self.position_centre[0],self.position_centre[1]-1)

        if direction == BAS:
            if self.position_centre[1] < self.max_visible[1]:
                self.position_centre = (self.position_centre[0],self.position_centre[1]+1)

    def rezoom(self):
        self.zoom += 1

    def dezoom(self):
        if self.zoom > 1:
            self.zoom -= 1

    def decouvre(self,position_vue,mat_exploree,position_joueur):
        """
        Fonction qui decouvre la minimap
        Entrées:
            la position du joueur
            la position que l'on prend pour 0,0 sur l'écran (ex: un décalage de 20px sur la droite se traduit par (x+20,y))
            la position de la vue dans le labyrinthe
            la largeur en cases
            la hauteur en cases
            le mode d'affichage
            la largueur des cases
            la largeur des murs
            la matrice explorée
        Sorties:
            Rien
        """
        
        for x in range(len(mat_exploree)):
            for y in range(len(mat_exploree[0])):
                if mat_exploree[x][y]:
                    self.matrice_cases[x+position_vue[0]][y+position_vue[1]].decouvert = 0
                    if x+position_vue[0] > self.max_visible[0] and x+position_vue[0] < self.largeur:
                        self.max_visible = (x+position_vue[0],self.max_visible[1])
                    elif x+position_vue[0] < self.min_visible[0] and x+position_vue[0] >= 0:
                        self.min_visible = (x+position_vue[0],self.min_visible[1])
                    if x+position_vue[1] > self.max_visible[1] and x+position_vue[1] < self.hauteur:
                        self.max_visible = (self.max_visible[0],x+position_vue[1])
                    elif x+position_vue[1] < self.min_visible[1] and x+position_vue[1] >= 0:
                        self.min_visible = (self.min_visible[0],x+position_vue[1])
        if TAILLE_FIXE:
            return(taille_fixe*2,taille_fixe*2)
        else:
            return (self.max_visible[0]-self.min_visible[0],self.max_visible[1]-self.min_visible[1])
    def getCopie(self, position_joueur):
        """
        Fonction qui copie la minimap
        Entrées:
            -la position du joueur
        Sorties:
            -une copie de la minimap indépendante de l'objet qui l'as générée
        """
        copie = Minimap(self.matrice_cases, self.mode_minimap, position_joueur, self.arrivee)
        #set des contantes non pris en charge par l'initialisation
        copie.zoom = self.zoom
        copie.decalage = self.decalage

        return copie

