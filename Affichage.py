import pygame
from Labyrinthe import *
from Joueur import *
from Constantes import *
from Patern import *
from Monstres import *
from Potion import *
from Evenement import *
from Animation import *

class Affichage:
    def __init__(self,screen,mode_affichage,LARGEUR_CASE,LARGEUR_MUR):
        #surface ou l'on dessine
        self.screen=screen
        
        self.mode_affichage=mode_affichage
        #constantes
        self.LARGEUR_MUR=LARGEUR_MUR
        self.LARGEUR_CASE=LARGEUR_CASE
        #decalage de la matrice du labyrinthe sur l'écran (decalage en px)
        self.decalage_matrice=[0,30]
        #liste des animations
        self.animations=[]
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
        self.reset_screen()
        self.dessine_hud(joueur)
        if self.mode_affichage==distance_max:
            self.distance_max(joueur,labyrinthe,entitees,evenements)
        else:
            print("le mode d'affichage selectionnée est incorrect")
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
        #récuoérer constantes
        largeur_vue=joueur.largeur_vue
        hauteur_vue=joueur.hauteur_vue

        joueur_x,joueur_y,position_x,position_y,min_x,max_x,min_y,max_y=self.getConstantes(joueur.getPosition(),[0,0],largeur_vue,hauteur_vue)

        position_joueur=[joueur_x,joueur_y]
        #récuperer vue joueur
        vue, position_vue = labyrinthe.construire_vue(position_joueur,largeur_vue,hauteur_vue)
        #récupérer mat vue visible joueur
        #on ne veut pas que le résolveur trouve de solution on veut juste qu'il explore la matrice
        resolveur = Resolveur(vue,largeur_vue,hauteur_vue,-1,-1,joueur_x-position_vue[0],joueur_y-position_vue[1],"Profondeur")

        mat_exploree=resolveur.resolution_en_largeur_distance_limitée(False,False,False,True,joueur.portee_vue)
        #dire au lab d'afficher la matrice correspondante
        labyrinthe.dessine_toi(self.screen,position_joueur,self.decalage_matrice,position_vue,largeur_vue,hauteur_vue,self.mode_affichage,self.LARGEUR_CASE,self.LARGEUR_MUR,mat_exploree)
        #afficher les entitées
        self.dessine_entitees(entitees,position_joueur,mat_exploree,position_vue,self.decalage_matrice)
        #afficher les animations
        self.dessine_animations(position_joueur,largeur_vue,hauteur_vue)
        #on supprime les animations qui ont expirées
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
        self.screen.blit(text_pv,(0,10))
        
        #on dessine la barre de vie du joueur
        pygame.draw.rect(self.screen, pygame.Color(255,0,0),(30,10,int(100*(joueur.pv/joueur.pv_max)),10))
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
                position_anim_x=(self.LARGEUR_CASE+self.LARGEUR_MUR)*(position_lab_anim[0]-position_joueur[0]+largeur_vue//2)+round((self.LARGEUR_CASE+self.LARGEUR_MUR)*0.5)+self.decalage_matrice[0]
                position_anim_y=(self.LARGEUR_CASE+self.LARGEUR_MUR)*(position_lab_anim[1]-position_joueur[1]+hauteur_vue//2)+round((self.LARGEUR_CASE+self.LARGEUR_MUR)*0.5)+self.decalage_matrice[1]

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
    def reset_screen(self):
        """
        Fonction qui "réinitialise la surface"
        """
        self.screen.fill((125,125,125))


