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
        self.taille_ecran_X = 0
        self.taille_ecran_Y = 0
        
        self.mode_affichage=mode_affichage
        self.hauteur = hauteur_lab
        self.largeur = largeur_lab
        #constantes
        self.LARGEUR_MUR=LARGEUR_MUR
        self.LARGEUR_CASE=LARGEUR_CASE
        self.TAILLE_CASE=LARGEUR_MUR+LARGEUR_CASE
        #decalage de la matrice du labyrinthe sur l'écran (decalage en px)
        self.hauteur_minimap = 1 * 3 + 13
        self.largeur_minimap = 1 * 3 + 13
        self.hauteur_HUD = 100
        self.decalage_matrice=[5,self.hauteur_HUD]
        self.affiche = LABYRINTHE
        self.affiche_precedent = None
        #liste des animations
        self.animations=[]
        #dialogue courant
        self.diag_cour = None#Replique("J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu J'ai perdu ",20)
        self.text_cour = None
        self.police_cour = None
        self.nb_chars_affichables = 0
        self.ecran_autres = (630,600)
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
        
        self.taille_minimap = joueur.minimap.decouvre(self.position_vue,self.mat_exploree,joueur.position)
        self.hauteur_minimap = self.taille_minimap[1] * 3 + 13
        self.largeur_minimap = self.taille_minimap[0] * 3 + 13
        self.hauteur_HUD = max(100,self.hauteur_minimap)
        self.decalage_matrice=[5,self.hauteur_HUD]

        taille_min_ecran_X = self.getBottomX(joueur.largeur_vue)
        taille_min_ecran_Y = self.getBottomY(joueur.hauteur_vue)
        if self.taille_ecran_X <= taille_min_ecran_X or self.taille_ecran_Y <= taille_min_ecran_Y :
            self.taille_ecran_X = taille_min_ecran_X + 33
            self.taille_ecran_Y = taille_min_ecran_Y + 33
            self.screen = pygame.display.set_mode((self.taille_ecran_X,self.taille_ecran_Y))

        if (self.affiche == MINIMAP or self.affiche == INVENTAIRE or self.affiche == ITEM) and (self.affiche_precedent == LABYRINTHE or self.affiche_precedent == DIALOGUE):
            self.screen = pygame.display.set_mode(self.ecran_autres)
        elif (self.affiche_precedent == MINIMAP or self.affiche_precedent == INVENTAIRE or self.affiche_precedent == ITEM) and (self.affiche == LABYRINTHE or self.affiche == DIALOGUE):
            self.screen = pygame.display.set_mode((self.taille_ecran_X,self.taille_ecran_Y))
            

        self.reset_screen(joueur)
        self.dessine_hud(joueur)
        if self.mode_affichage==distance_max and (self.affiche == LABYRINTHE or self.affiche == DIALOGUE):
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
        limite_haute = self.hauteur_HUD
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
        text_pv=police_pv.render("PV :",True,(0,0,0))
        vie = int(100*(joueur.pv/joueur.pv_max))
        if vie>75:
            couleur_PV = (158,253,56)
        elif vie>50:
            couleur_PV = (243,214,23)
        elif vie>25:
            couleur_PV = (244,102,27)
        else :
            couleur_PV = (237,0,0)

#        police_pm=police_pv
 #       text_pm=police_pm.render("PM :",True,(0,0,0))
  #      mana = int(100*(abs(joueur.mana)/joueur.mana_max))
   #     if mana<0:
    #        couleur_PM = (254,27,0)
     #   elif mana>75:
      #      couleur_PM = (108,2,119)
       # elif mana>50:
        #    couleur_PM = (223,115,255)
#        elif mana>25:
 #           couleur_PM = (176,242,182)
  #      else :
   #         couleur_PM = (1,215,88)
        
        if (self.affiche == MINIMAP) or (self.affiche == INVENTAIRE) or (self.affiche == ITEM):
            self.screen.blit(text_pv,(0,10))
            #on dessine la barre de vie du joueur 
            pygame.draw.rect(self.screen,couleur_PV,(30,10,vie,10))
    #        self.screen.blit(text_pm,(0,40))
     #       #on dessine la barre de mana du joueur 
      #      pygame.draw.rect(self.screen,couleur_PM,(30,40,mana,10))
        else:
            self.screen.blit(text_pv,(joueur.largeur_vue*self.TAILLE_CASE-130+self.decalage_matrice[0],self.getBottomY(joueur.hauteur_vue)-20))
            #on dessine la barre de vie du joueur
            pygame.draw.rect(self.screen,couleur_PV,(joueur.largeur_vue*self.TAILLE_CASE-100+self.decalage_matrice[0],self.getBottomY(joueur.hauteur_vue)-20,vie,10))
       #     self.screen.blit(text_pm,(joueur.largeur_vue*self.TAILLE_CASE-130+self.decalage_matrice[0],self.getBottomY(joueur.hauteur_vue)+10))
        #    #on dessine la barre de mana du joueur
         #   pygame.draw.rect(self.screen,couleur_PM,(joueur.largeur_vue*self.TAILLE_CASE-100+self.decalage_matrice[0],self.getBottomY(joueur.hauteur_vue)+10,mana,10))

        #on dessine la minimap        
        if self.affiche == MINIMAP:
            joueur.affiche_minimap(self.screen)
        elif self.affiche == LABYRINTHE or self.affiche == DIALOGUE:
            joueur.dessine_minimap(self.screen,[5,5],(self.affiche==self.affiche_precedent))
            if self.affiche == DIALOGUE:
                self.dessine_dialogue(joueur.largeur_vue)
        #on dessine l'inventaire
        elif self.affiche == INVENTAIRE:
            joueur.affiche_inventaire(self.screen)
        elif self.affiche == ITEM:
            joueur.precise_item(self.screen)
    def dessine_dialogue(self, largeur_vue):
        """
        Fonction qui dessine le dialogue courant
        Entrée:
            -la largeur de la vue du joueur
        """
        if self.diag_cour != None:
            largeur_bordure_externe = 2
            largeur_bordure_interne = 5
            
            limite_droite = (self.LARGEUR_MUR+self.LARGEUR_CASE) * (largeur_vue + self.decalage_bord_largeur)
            #fond blanc
            pygame.draw.rect(self.screen, pygame.Color(255,255,255),(self.largeur_minimap+5,5,290,90))
            #bord noir
            pygame.draw.rect(self.screen, pygame.Color(0,0,0),(self.largeur_minimap+5,5,290,90),largeur_bordure_externe)

            #texte de base à écrire en bas
            police_default = pygame.font.SysFont(None, 15)
            text_next = police_default.render("- Appuyer sur Entrée pour continuer -",True,(0,0,0))
            taille_x, taille_y = police_default.size("- Appuyer pour continuer -")
            #taille alouée aux texte
            size_y = 90 - taille_y
            size_x = 290

            size = [size_x, size_y]

            curseur = [self.largeur_minimap+5+largeur_bordure_interne,5+largeur_bordure_interne]

            if self.police_cour == None:
                self.police_cour = pygame.font.SysFont(None, self.diag_cour.taille_ecriture)
            largeur_police, hauteur_police = self.police_cour.size("a")

            if self.text_cour == None:
                self.nb_lignes_affichables = self.taille_max_colonne(self.diag_cour,self.police_cour,size_y)
                self.text_cour = self.diag_cour.get_contenu(self.nb_lignes_affichables)

            #on essaie d'empêcher un potentiel soft lock
            if self.nb_lignes_affichables <= 0:
                self.diag_cour = None
                self.police_cour = None
                self.affiche = LABYRINTHE
                self.text_cour = None
                
            else:
                for i in range(len(self.text_cour)):
                    #affichage du texte
                    text_dialogue = self.police_cour.render(self.text_cour[i],True,(0,0,0))
                    self.screen.blit(text_dialogue,curseur)
                    curseur[1] += hauteur_police

                self.screen.blit(text_next, curseur)
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
        largeur,hauteur = police.size(replique.contenu[0][0])
        
        return int(taille_y/hauteur)

    def taille_max_ligne(self,contenu,police,taille_x,last_char):
        """
        Fonction qui calcule le nombre max de charactères que l'on
        peut mettre sur une ligne
        Entrées:
            -le contenu a afficher
            -la police avec laquelle on affiche la replique
            -la taille allouée en x
            -le dernier charactère auquel on as pas touché
        Sortie:
            -le nombre de charactères max sur une ligne
        """
        
        nb_chars=0
        i=last_char
        taille_px=0

        while i<len(contenu[0]) and taille_px<=taille_x:
            largeur,hauteur = police.size(contenu[0][i])
            taille_px += largeur
            nb_chars += 1
            i += 1
            
        return nb_chars
    def add_dialogue(self,new_dialogue):
        """
        Fonction qui si possible ajoute un dialogue à afficher
        Entrées:
            -la réplique à afficher
        Sorties:
            -un booléen indiquant si la demande à réussi
        """
        succes = False
        if self.diag_cour == None:
            self.diag_cour = new_dialogue
            self.affiche = DIALOGUE
            succes = True
            
        return succes
    def pass_replique(self):
        """
        Fonction qui passe une partie du dialogue
        et qui le réinitialise s'il est finit
        Entrées:
            -Rien
        Sorties:
            -Rien
        """
        if self.diag_cour != None:
            if self.diag_cour.est_fini():
                self.diag_cour = None
                self.police_cour = None
                self.affiche = LABYRINTHE
                res = True
            self.text_cour = None
        return res
    def dialogue_finit(self):
        """
        Fonction qui teste si le dialogue est finit
        Entrées:
            -Rien
        Sorties:
            -un booléen indiquant si le dialogue est finit
        """
        return (self.diag_cour==None)
    def getBottomY(self,hauteur_vue):
        """
        Fonction qui renvoie le y correspondant au bas de l'écran
        Entrées:
            -la hauteur de la vue du joueur
        Sorties:
            -un entier
        """
        #print(self.decalage_matrice[1]+(self.LARGEUR_MUR+self.LARGEUR_CASE)*(portee_joueur+2))
        return self.decalage_matrice[1]+(self.LARGEUR_MUR+self.LARGEUR_CASE)*(hauteur_vue) + 60
    def getBottomX(self,largeur_vue):
        """
        Fonction qui renvoie le x correspondant à la droite de l'écran
        Entrées:
            -la hauteur de la vue du joueur
        Sorties:
            -un entier
        """
        if self.largeur_minimap + 300 >(self.LARGEUR_MUR+self.LARGEUR_CASE)*(largeur_vue):
            return self.largeur_minimap + 300
        else:
            return (self.LARGEUR_MUR+self.LARGEUR_CASE)*(largeur_vue)+13
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
        
    def ajout_animation(self,position_anim,type_anim,mat_anim,direction):
        """
        Fonction qui ajoute une animation a exécuter
        Entrées:
            -position de l'animation en cases
            -le type de l'animation:
                -0=>Attaque 'classique'
            -la matrice des cases touchées
            -la direction de l'attaque
        """
        new_animation=None
        if type_anim == LIGHT:
            for x in range(len(mat_anim)):
                for y in range(len(mat_anim[0])):
                    if mat_anim[x][y]:
                        position = (position_anim[0] + x,position_anim[1] + y)
                        new_animation=Attaque_omnidirectionnelle(4,position,self.screen)
                        self.animations.append(new_animation)
                        #la position en pixels sera déterminée que lorsque
                        #qu'on voudra la dessiner
        elif type_anim == HEAVY:
            nb_anim = 0
            for x in range(len(mat_anim)):
                for y in range(len(mat_anim[0])):
                    if mat_anim[x][y]:
                        nb_anim += 1
            nb_anims = 0
            for x in range(len(mat_anim)):
                for y in range(len(mat_anim[0])):
                    if mat_anim[x][y]:
                        nb_anims += 1
                        position = (position_anim[0] + x,position_anim[1] + y)
                        if direction == GAUCHE or direction == HAUT:
                            if nb_anims == 1:
                                new_animation=Attaque_unidirectionnelle_fin(max(nb_anim,4),position,direction,self.screen)
                            else:
                                new_animation=Attaque_unidirectionnelle(max(nb_anim,4),position,direction,self.screen)
                        else:
                            if nb_anims == nb_anim:
                                new_animation=Attaque_unidirectionnelle_fin(max(nb_anim,4),position,direction,self.screen)
                            else:
                                new_animation=Attaque_unidirectionnelle(max(nb_anim,4),position,direction,self.screen)
                        self.animations.append(new_animation)
                        #la position en pixels sera déterminée que lorsque
                        #qu'on voudra la dessiner
                        
        else:
            print("le type d'animation choisi est invalide")

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
                position_anim_x=(self.LARGEUR_CASE+self.LARGEUR_MUR)*(position_lab_anim[0]-position_joueur[0]+largeur_vue//2)+self.decalage[0]+2
                position_anim_y=(self.LARGEUR_CASE+self.LARGEUR_MUR)*(position_lab_anim[1]-position_joueur[1]+hauteur_vue//2)+self.decalage[1]+2

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
            pygame.draw.rect(self.screen,(125,125,125),(0,self.hauteur_minimap-3,self.screen.get_width(),self.screen.get_height()+3-self.hauteur_minimap))
            pygame.draw.rect(self.screen,(125,125,125),(self.largeur_minimap-3,0,self.screen.get_width()+3-self.largeur_minimap,self.hauteur_minimap-3))
            pygame.draw.rect(self.screen,(125,125,125),(0,0,self.largeur_minimap-3,5))
            pygame.draw.rect(self.screen,(125,125,125),(0,5,5,self.hauteur_minimap-8))
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
