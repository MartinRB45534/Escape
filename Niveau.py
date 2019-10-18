import pygame
from Labyrinthe import *
from Joueur import *
from Constantes import *
from Patern import *
from Monstres import *
from Potion import *
from Inventaire import *
from Stats import *
from Planning import *
from Collisions import *

class Niveau:
    def __init__(self,difficulté,mode_affichage):

        self.mode_affichage = mode_affichage
        if self.mode_affichage == voir_tout :
            self.LARGEUR_CASE = 20
            self.LARGEUR_MUR = 1
        elif self.mode_affichage == aveugle :
            self.LARGEUR_CASE = 45
            self.LARGEUR_MUR = 5
        elif self.mode_affichage == parcours_en_profondeur :
            self.LARGEUR_CASE = 20
            self.LARGEUR_MUR = 1
        elif self.mode_affichage == distance_max :
            self.LARGEUR_CASE = 20
            self.LARGEUR_MUR = 1

        if difficulté == BEGINNER :
            self.CASES_X = 20
            self.CASES_Y = 20
            res = True
            self.salles=[Patern(10,10,self.LARGEUR_CASE,self.LARGEUR_MUR)]
        elif difficulté == EASY :
            self.CASES_X = 20
            self.CASES_Y = 20
            res = False
            self.salles=[Patern(5,5,self.LARGEUR_CASE,self.LARGEUR_MUR)]
        elif difficulté == AVERAGE :
            self.CASES_X = 40
            self.CASES_Y = 40
            res = False
            self.salles=[Patern(5,5,self.LARGEUR_CASE,self.LARGEUR_MUR)]
        elif difficulté == HARD :
            self.CASES_X = 60
            self.CASES_Y = 60
            res = False
            self.salles=[Patern(40,2,self.LARGEUR_CASE,self.LARGEUR_MUR)]
        elif difficulté == INSANE :
            self.CASES_X = 100
            self.CASES_Y = 100
            res = False
            self.salles=[Patern(2,40,self.LARGEUR_CASE,self.LARGEUR_MUR)]
        elif difficulté == IMPOSSIBLE :
            self.CASES_X = 1000
            self.CASES_Y = 1000
            res = False
            self.salles=[Patern(1,1,self.LARGEUR_CASE,self.LARGEUR_MUR)]

        #variables correspondants a la largeur et la hauteur du zoom
        self.zoom_largeur=11
        self.zoom_hauteur=11

        self.force_base = 10
        self.hp_base = 100

        self.planning = Planning()

        stats_joueur = Stats(self.force_base,self.zoom_hauteur,self.zoom_largeur,self.hp_base)
        inventaire_joueur = Inventaire(stats_joueur,self.planning)
        
        pygame.init()
        #poids permettants de manipuler l'aléatoire
        self.poids=[6,2,1,2]
        
        #salle pour exp monstres
        self.salles.append(Patern(5,5,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,3]]))

        self.lab=Labyrinthe(self.CASES_X,self.CASES_Y,self.CASES_X-1,self.CASES_Y-1,self.LARGEUR_CASE,self.LARGEUR_MUR,self.poids,self.salles)
        self.lab.generation()
        self.lab.casser_X_murs(0.1)

        if res :
            self.lab.resolution(self.CASES_X-1,self.CASES_Y-1,0,0,"Largeur")

        pygame.display.set_caption("test")
        self.screen = pygame.display.set_mode((FENETRE_X,FENETRE_Y),pygame.RESIZABLE)
        self.screen.fill((0,0,0))

        #entitées
        self.joueur=Joueur(stats_joueur,inventaire_joueur,100,5,2,self.zoom_largeur,self.zoom_hauteur)
        self.monstres=[Slime([5,5],10,10,100,5,1,(255,121,121))]
        self.entitees=[self.joueur,self.monstres[0]]

        #objet qui traite les collisions
        self.collision=Collision()
        
        #texte de fin
        font = pygame.font.SysFont(None, 72)
        self.textWin = font.render("Vous avez gagné!! \(^o^)/", True, (128, 0, 0))
        self.textLose = font.render("Vous avez perdu!! ;o;", True, (0, 128, 128))
        
        self.position_screen=(0,0)

    def run(self):
        run=True
        self.redraw()
        #objet qui permet de gérer le temps en pygame
        clock = pygame.time.Clock()
        #nb de frames que le joueur doit attendre entre chaque action
        cooldown_joueur=3
        compteur_j=0
        #nb de frames que les monstres doivent attendre entre chaque action
        cooldown_monstres=20
        compteur_m=0
        
        while run:
            #on cadence à 60 frames/sec
            clock.tick(60)
            self.planning.agit(clock.get_time())

            move_j = False
            move_m=False
            #si l'utilisateur décide de mettre fin au programme on sort de la boucle
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False

                if event.type == pygame.VIDEORESIZE:
                    self.zoom_largeur = event.w//(self.LARGEUR_CASE + self.LARGEUR_MUR)
                    self.zoom_hauteur = event.h//(self.LARGEUR_CASE + self.LARGEUR_MUR)
                    self.redraw()
            #partie gérant le joueur
            if compteur_j==0:
                compteur_j=cooldown_joueur
                self.action_joueur()
                self.joueur=self.actualiser_vue(self.joueur)
                self.joueur=self.actualiser_donnee(self.joueur)
                move_j=self.traitement_action(self.joueur)
            else:
                compteur_j-=1
            #partie gérant les monstres
            if compteur_m==0:
                compteur_m=cooldown_monstres

                move_m=self.actions_entitees() 
            else:
                compteur_m-=1

            #si on détecte un mouvement on redessine l'écran
            if move_j or move_m:
                self.redraw()

            if self.lab.as_gagner(self.joueur.getPosition()):
                self.ecran_fin_niveau(self.textWin)
                run=False
            if self.as_perdu():
                self.ecran_fin_niveau(self.textLose)
                run=False
            pygame.display.update()
        pygame.quit()

    
    def action_joueur(self):
        """
        Fonction qui exécute la partie du code ou le jpueur demande à agir
        et qui renvoie rien
        """
         #on récupère toutes les touches préssés sous forme de
        keys=pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.joueur.va_vers_le_haut()
        elif keys[pygame.K_DOWN]:
            self.joueur.va_vers_le_bas()
        elif keys[pygame.K_RIGHT]:
            self.joueur.va_vers_la_droite()
        elif keys[pygame.K_LEFT]:
            self.joueur.va_vers_la_gauche()
        elif keys[pygame.K_SPACE]:
            self.joueur.attaque()
            
    def actions_entitees(self):
        """
        Fonction qui exécute les actions des entitées
        renvoie un booléen indiquant si il y a besoin de redessiner l'écran
        """
        redessiner=False
        for entitee in self.entitees:
            entitee=self.actualiser_vue(entitee)
            entitee=self.actualiser_donnee(entitee)
            entitee.prochaine_action()
            if redessiner:
                self.traitement_action(entitee)
            else:
                redessiner=self.traitement_action(entitee)
            #print(redessiner,type(entitee))
        return redessiner

    def actualiser_vue(self,agissant):
        """
        Fonction qui actualise la vue d'un agissant
        Entrée:
            un agissant
        Sortie:
            un agissant avec sa vue actualiser
        """
        vue_agissant,position_vue=self.lab.construire_vue(agissant.getPosition(),agissant.getLargeurVue(),agissant.getHauteurVue())
        agissant.actualiser_vue(vue_agissant,position_vue)

        return agissant
    def actualiser_donnee(self,agissant):
        """
        Fonction qui actualise les données des agissant en fonction de leur
        type
        Entrée:
            un agissant
        Sortie:
            un agissant avec ces données actualisées
        """
        if type(agissant)==Slime:
            #on donne la position du joueur au monstre
            agissant.setPosition_joueur(self.joueur.getPosition())
        elif type(agissant)==Runner:
            #on donne la position du joueur au monstre
            agissant.setPosition_joueur(self.joueur.getPosition())
        elif type(agissant)==Fatti:
            #on donne la position du joueur au monstre
            agissant.setPosition_joueur(self.joueur.getPosition())
        elif type(agissant)==Joueur:
            self.action_joueur()

        return agissant
    def traitement_action(self,agissant):
        """
        Fonction qui traite une action donnée d'un agissant
        et qui renvoie un booléen indiquant si l'action à été exécutée
        """
        succes=False
        
        id_action,action=agissant.get_action()

        #print(type(agissant),id_action,action)
        
        if id_action==BOUGER:
            #print("veut bouger")
            direction_voulue=action
            if direction_voulue!=None:
                passe,newcoord=self.lab.peut_passer(agissant.getPosition(),direction_voulue)
                #print(passe)
                if passe:
                    succes=True
                    #print(succes)
                    agissant.setPosition(newcoord)
        elif id_action==ATTAQUER:
            succes,self.entitees=self.collision.tentative_attaque(agissant,self.entitees)
            
        return succes
        
    def as_perdu(self):
        """
        Fonction qui vérifie si le joueur as perdu(pv=0 ou soft lock)
        """
        return (self.joueur.pv<=0)
    def ecran_fin_niveau(self,text):
        """
        Fonction qui as pour but d'afficher l'écran de fin de niveau (stats etc)
        """
        self.screen.fill((255,255,255))
        self.screen.blit(text,(0,0))
    def redraw(self):
        """
        Fonction qui redessine l'entièreté de l'écran
        """
        self.screen.fill((0,0,0))
        self.lab.dessine_toi(self.screen,self.joueur.position,self.monstres,self.position_screen,self.joueur.stats.largeur_vue,self.joueur.stats.hauteur_vue,self.mode_affichage,self.LARGEUR_CASE,self.LARGEUR_MUR)
        self.joueur.dessine_toi(self.screen,(self.joueur.stats.largeur_vue//2,self.joueur.stats.hauteur_vue//2),self.LARGEUR_CASE,self.LARGEUR_MUR,self.position_screen)

