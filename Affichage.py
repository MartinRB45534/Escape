import pygame
from Labyrinthe import *
from Joueur import *
from Constantes import *
from Patern import *
from Monstres import *
from Potion import *
from Evenement import *
from Animation import *
from Replique import *

class Affichage:
    def __init__(self,screen,mode_affichage,LARGEUR_CASE,LARGEUR_MUR,largeur_lab,hauteur_lab):
        #surface ou l'on dessine
        self.screen=screen
        
        self.mode_affichage=mode_affichage
        self.hauteur = hauteur_lab
        self.largeur = largeur_lab
        #constantes
        self.LARGEUR_MUR=LARGEUR_MUR
        self.LARGEUR_CASE=LARGEUR_CASE
        self.TAILLE_CASE=LARGEUR_MUR+LARGEUR_CASE
        #decalage de la matrice du labyrinthe sur l'écran (decalage en px)
        self.hauteur_minimap = 1 * 3 + 11
        self.largeur_minimap = 1 * 3 + 11
        self.decalage_matrice=[11,self.hauteur_minimap]
        self.affiche = LABYRINTHE
        self.affiche_precedent = None
        #liste des animations
        self.animations=[]
        #dialogue courant
        self.diag_cour = Replique("J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu ",20)
    def dessine_frame(self,joueur,labyrinthe,entitees,evenements):
        """
        Fonction qui dessine une frame
        Entrées:
            -Le joueur
            -le Labyrinthe
            -Les entitées
            -Les événements
        Sorties:
            -rien
        """
        self.decouvre_joueur(joueur,labyrinthe)
        self.reset_screen(joueur)
        self.dessine_hud(joueur)
        if self.mode_affichage==distance_max and self.affiche == LABYRINTHE:
            self.distance_max(joueur,labyrinthe,entitees,evenements)
        elif self.affiche == LABYRINTHE:
            print("le mode d'affichage selectionnée est incorrect")
        if self.affiche != self.affiche_precedent:
            self.affiche_precedent = self.affiche
            
    def distance_max(self,joueur,labyrinthe,entitees,evenements):
        """
        Fonction qui dessine une frame avec la méthode de la distance maximum
        Entrées:
            -Le joueur
            -le Labyrinthe
            -Les entitées
            -Les événements
        Sorties:
            -rien
        """
        #récupérer constantes
        largeur_vue=joueur.largeur_vue
        hauteur_vue=joueur.hauteur_vue
        #on dessine le cadre autour du labyrinthe pour faire joli
        limite_gauche = self.decalage_matrice[0]
        limite_droite = (self.LARGEUR_MUR+self.LARGEUR_CASE) * (largeur_vue + self.decalage_bord_largeur)
        limite_haute = self.hauteur_minimap
        limite_basse = (self.LARGEUR_MUR+self.LARGEUR_CASE) * (hauteur_vue + self.decalage_bord_hauteur)
        pygame.draw.rect(self.screen,(150,150,150),(limite_gauche,limite_haute,limite_droite,limite_basse))
        pygame.draw.rect(self.screen,(50,50,50),(limite_gauche,limite_haute,limite_droite,limite_basse),2)

        joueur_x,joueur_y,position_x,position_y,min_x,max_x,min_y,max_y=self.getConstantes(joueur.getPosition(),[0,0],largeur_vue,hauteur_vue)

        position_joueur=[joueur_x,joueur_y]
        self.decalage = [self.decalage_matrice[0] + (self.LARGEUR_MUR+self.LARGEUR_CASE) * self.decalage_gauche,self.decalage_matrice[1] + (self.LARGEUR_MUR+self.LARGEUR_CASE) * self.decalage_haut]
        #dire au lab d'afficher la matrice correspondante
        labyrinthe.dessine_toi(self.screen,position_joueur,self.decalage,self.position_vue,largeur_vue,hauteur_vue,self.mode_affichage,self.LARGEUR_CASE,self.LARGEUR_MUR,self.mat_exploree)
        #afficher les entitées
        self.dessine_entitees(entitees,position_joueur,self.mat_exploree,self.position_vue,self.decalage)
        #afficher les animations
        self.dessine_animations(position_joueur,largeur_vue,hauteur_vue)
        #on supprime les animations qui ont expiré
        self.supprime_animations()
        
    def dessine_hud(self,joueur):
        """
        Fonction qui affiche les informations complémentaires
        (barre de vie, MINIMAP, etc)
        Entrées:
            -le joueur
        """
        police_pv=pygame.font.SysFont(None, 20)
        text_pv=police_pv.render("PV:",True,(0,0,0))
        if (self.affiche == MINIMAP) or (self.affiche == INVENTAIRE):
            self.screen.blit(text_pv,(0,10))
            #on dessine la barre de vie du joueur
            pygame.draw.rect(self.screen, pygame.Color(255,0,0),(30,10,int(100*(joueur.pv/joueur.pv_max)),10))
        else:
            self.screen.blit(text_pv,(joueur.largeur_vue*self.TAILLE_CASE-130+self.decalage_matrice[0],self.getBottomY(joueur.hauteur_vue)+10))
            #on dessine la barre de vie du joueur
            pygame.draw.rect(self.screen, pygame.Color(255,0,0),(joueur.largeur_vue*self.TAILLE_CASE-100+self.decalage_matrice[0],self.getBottomY(joueur.hauteur_vue)+10,int(100*(joueur.pv/joueur.pv_max)),10))

        #on dessine la minimap
        self.taille_minimap = joueur.minimap.decouvre(self.position_vue,self.mat_exploree,joueur.position)
        self.hauteur_minimap = self.taille_minimap[1] * 3 + 11
        self.largeur_minimap = self.taille_minimap[0] * 3 + 11
        self.decalage_matrice=[self.largeur_minimap,self.hauteur_minimap]
        if self.affiche == MINIMAP:
            joueur.affiche_minimap(self.screen)
        elif self.affiche == LABYRINTHE:
            joueur.redessine_minimap(self.screen,[5,5])
            self.dessine_dialogue(joueur.largeur_vue)
        #on dessine l'inventaire
        if self.affiche == INVENTAIRE:
            joueur.affiche_inventaire(self.screen)
    def dessine_dialogue(self, largeur_vue):
        """
        Fonction qui dessine le dialogue courant
        Entrée:
            -la largeur de la vue du joueur
        """
        largeur_bordure_externe = 2
        largeur_bordure_interne = 5
        
        limite_droite = (self.LARGEUR_MUR+self.LARGEUR_CASE) * (largeur_vue + self.decalage_bord_largeur)# + self.decalage_matrice[0]
        #fond blanc
        pygame.draw.rect(self.screen, pygame.Color(255,255,255),(self.decalage_matrice[0]+5,5,limite_droite-5,self.decalage_matrice[1]-5))
        #bord noir
        pygame.draw.rect(self.screen, pygame.Color(0,0,0),(self.decalage_matrice[0]+5,5,limite_droite-5,self.decalage_matrice[1]-5),largeur_bordure_externe)

        #taille alouée aux texte
        size_y = (self.decalage_matrice[1]-5-largeur_bordure_externe-largeur_bordure_interne)
        size_x =(limite_droite-5-largeur_bordure_externe-largeur_bordure_interne)# - (self.decalage_matrice[0]+5)
        size = [size_x, size_y]

        curseur = [self.decalage_matrice[0]+5+largeur_bordure_interne,5+largeur_bordure_interne]

        police_dialogue=pygame.font.SysFont(None, self.diag_cour.taille_ecriture)
        largeur_police, hauteur_police = police_dialogue.size("a")
        last_char = 0
        
        for y in range(0,self.taille_max_colonne(self.diag_cour,police_dialogue,size_y)):
            nb_chars = self.taille_max_ligne(self.diag_cour,police_dialogue,size_x,last_char)
            text_replique = self.diag_cour.get_contenu(nb_chars)
            text_dialogue = police_dialogue.render(text_replique,True,(0,0,0))
            self.screen.blit(text_dialogue,curseur)
            last_char += nb_chars
            curseur[1] += hauteur_police
            

        self.diag_cour.position_replique = 0

    def taille_max_colonne(self,replique,police,taille_y):
        """
        Fonction qui calcule le nombre max de charactères que l'on
        peut mettre sur une colonne
        Entrées:
            -la replique a afficher
            -la police avec laquelle on affiche la replique
            -la taille allouée en y
        Sortie:
            -le nombre de charactères max sur une colonne
        """
        largeur,hauteur = police.size(replique.contenu[0])
        
        return int(taille_y/hauteur)

    def taille_max_ligne(self,replique,police,taille_x,last_char):
        """
        Fonction qui calcule le nombre max de charactères que l'on
        peut mettre sur une ligne
        Entrées:
            -la replique a afficher
            -la police avec laquelle on affiche la replique
            -la taille allouée en x
            -le dernier charactère auquel on as pas touché
        Sortie:
            -le nombre de charactères max sur une ligne
        """
        nb_chars=0
        i=last_char
        contenu_rep=replique.contenu
        taille_px=0

        while i<len(contenu_rep) and taille_px<=taille_x:
            largeur,hauteur = police.size(contenu_rep[i])
            taille_px += largeur
            nb_chars += 1
            i += 1
            
        return nb_chars

    def getBottomY(self,hauteur_vue):
        """
        Fonction qui renvoie le y correspondant au bas de l'écran
        Entrées:
            -la hauteur de la vue du joueur
        Sorties:
            -un entier
        """
        #print(self.decalage_matrice[1]+(self.LARGEUR_MUR+self.LARGEUR_CASE)*(portee_joueur+2))
        return self.decalage_matrice[1]+(self.LARGEUR_MUR+self.LARGEUR_CASE)*(hauteur_vue)
    def getConstantes(self,position_joueur,position_screen,largeur,hauteur):
        """
        Fonction qui génère les constantes nécessaires au fonctionnement de l'affichage
        Entrées:
            -la position du joueur
            -la position que l'on prend pour 0,0 sur l'écran (ex: un décalage de 20px sur la droite se traduit par (x+20,y))
            -la largeur en cases
            -la hauteur en cases
        """
        joueur_x = position_joueur[0]
        joueur_y = position_joueur[1]

        position_x=position_screen[0]
        position_y=position_screen[1]

        min_x=joueur_x-largeur//2
        max_x=joueur_x+largeur-largeur//2

        min_y=joueur_y-hauteur//2
        max_y=joueur_y+hauteur-hauteur//2

        return joueur_x,joueur_y,position_x,position_y,min_x,max_x,min_y,max_y
        
    def dessine_entitees(self,entitees,position_joueur,mat_exploree,position_vue,position_screen):
        """
        Fonction qui dessine les entitees
        Entrées:
            -les entitees a dessiner
            -la position du joueur
            -la matrice explorée
            -la position de la vue dans le labyrinthe
            -la position du labyrinthe dans la fenetre
        """
        if entitees!=None:
            for entitee in entitees:
                x=entitee.getPosition()[0]-position_vue[0]
                y=entitee.getPosition()[1]-position_vue[1]
                
                if not(x>len(mat_exploree)-1 or x<0 or y>len(mat_exploree[0])-1 or y<0):
                    if mat_exploree[x][y]:
                        entitee.dessine_toi(self.screen,[x,y],self.LARGEUR_CASE,self.LARGEUR_MUR,position_screen)
        
    def ajout_animation(self,position_anim,type_anim,temps,radius):
        """
        Fonction qui ajoute une animation a exécuter
        Entrées:
            -position de l'animation en cases
            -le type de l'animation:
                -0=>Attaque 'classique'
            -le temps que l'animation va prendre
            -le radius en cases
        """
        new_animation=None
        if type_anim==0:
            #la position en pixels sera déterminée que lorsque
            #qu'on voudra la dessiner
            new_animation=Attaque(temps,position_anim,radius,self.screen)
        else:
            print("le type d'animation choisi est invalide")

        if new_animation!=None:
            self.animations.append(new_animation)

    def dessine_animations(self,position_joueur,largeur_vue,hauteur_vue):
        """
        Fonction qui dessine les animations
        Entrées:
            -la position du joueur
            -la largeur de la vue
            -la hauteur de la vue
        """
        for animation in self.animations:
            position_lab_anim=animation.getPosition()
            if self.est_dans_vue(position_lab_anim,position_joueur,largeur_vue,hauteur_vue):
                position_anim_x=(self.LARGEUR_CASE+self.LARGEUR_MUR)*(position_lab_anim[0]-position_joueur[0]+largeur_vue//2)+round((self.LARGEUR_CASE+self.LARGEUR_MUR)*0.5)+self.decalage[0]
                position_anim_y=(self.LARGEUR_CASE+self.LARGEUR_MUR)*(position_lab_anim[1]-position_joueur[1]+hauteur_vue//2)+round((self.LARGEUR_CASE+self.LARGEUR_MUR)*0.5)+self.decalage[1]

                position_anim=[position_anim_x,position_anim_y]

                animation.setPosition(position_anim)
            else:
                animation.setPosition(None)
    def supprime_animations(self):
        """
        Fonction qui supprime les animations qui sont fini
        """
        anims_tmps=[self.animations[i] for i in range(0,len(self.animations))]
        nbSup=0
        
        for i in range(0,len(anims_tmps)):
            if anims_tmps[i].execute():
                self.animations.pop(i-nbSup)
                nbSup+=1

    def est_dans_vue(self,position,joueur_position,largeur_vue,hauteur_vue):
        """
        Fonction qui détermine si l'entitee est en vue du joueur
        Entrées:
            -la position de l'entitée
            -la position du jouer
            -la largeur de la vue
            -la hauteur de la vue
        Sorties:
            -un booléen indiquant si l'entitée est en vue
        """
        joueur_x=joueur_position[0]
        joueur_y=joueur_position[1]

        min_x=joueur_x-largeur_vue//2
        max_x=joueur_x+largeur_vue-largeur_vue//2

        min_y=joueur_y-hauteur_vue//2
        max_y=joueur_y+hauteur_vue-hauteur_vue//2

        return (position[0]>=min_x and position[0]<max_x)and(position[1]>=min_y and position[1]<max_y)
    def reset_screen(self,joueur):
        """
        Fonction qui "réinitialise la surface"
        """
        if self.affiche_precedent == LABYRINTHE and self.affiche == LABYRINTHE:
            pygame.draw.rect(self.screen,(125,125,125),(0,self.hauteur_minimap,(self.LARGEUR_MUR+self.LARGEUR_CASE) * joueur.largeur_vue + 30,(self.LARGEUR_MUR+self.LARGEUR_CASE) * joueur.hauteur_vue + 30))
        else:
            self.screen.fill((125,125,125))

    def decouvre_joueur(self,joueur,labyrinthe):
        """
        Fonction qui détermine ce que le joueur voit (sur l'écran et dans la minimap)
        """
        #récupérer constantes
        largeur_vue=joueur.largeur_vue
        hauteur_vue=joueur.hauteur_vue
        position_joueur = joueur.getPosition()
        joueur_x = position_joueur[0]
        joueur_y = position_joueur[1]

        #récupérer vue joueur
        vue, self.position_vue = labyrinthe.construire_vue(position_joueur,largeur_vue,hauteur_vue)
        if self.position_vue[0] < 0:
            self.decalage_bord_largeur = self.position_vue[0]
            self.decalage_gauche = self.decalage_bord_largeur
        elif self.position_vue[0] + largeur_vue > self.largeur:
            self.decalage_bord_largeur = -self.position_vue[0] - largeur_vue + self.largeur
            self.decalage_gauche = 0
        else:
            self.decalage_bord_largeur = 0
            self.decalage_gauche = 0
        if self.position_vue[1] < 0:
            self.decalage_bord_hauteur = self.position_vue[1]
            self.decalage_haut = self.decalage_bord_hauteur
        elif self.position_vue[1] + hauteur_vue > self.hauteur:
            self.decalage_bord_hauteur = -self.position_vue[1] - hauteur_vue + self.hauteur
            self.decalage_haut = 0
        else:
            self.decalage_bord_hauteur = 0
            self.decalage_haut = 0
        #récupérer mat vue visible joueur
        #on ne veut pas que le résolveur trouve de solution on veut juste qu'il explore la matrice
        resolveur = Resolveur(vue,largeur_vue,hauteur_vue,-1,-1,joueur_x-self.position_vue[0],joueur_y-self.position_vue[1],"Profondeur")

        self.mat_exploree=resolveur.resolution_en_largeur_distance_limitée(False,False,False,True,joueur.portee_vue)
