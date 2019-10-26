import pygame
from Labyrinthe import *
from Joueur import *
from Constantes import *
from Patern import *
from Monstres import *
from Potion import *
from Inventaire import *
from Planning import *
from Collisions import *
from Meute import *
from Evenement import *
from Animation import *

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
            self.salles=[Patern(40,2,self.LARGEUR_CASE,self.LARGEUR_MUR,[])]
            #on génère les entrées de manière a avoir un espace ouvert
            self.salles[0].pre_gen_entrees_x(0,0,39)
            self.salles[0].pre_gen_entrees_x(1,0,39)
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

        self.force_joueur = 5
        self.hp_joueur = 100

        inventaire_joueur = Inventaire()
        
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
        self.joueur=Joueur(inventaire_joueur,self.hp_joueur,self.force_joueur,2,self.zoom_largeur,self.zoom_hauteur)
        #self.monstres=[Slime([5,5],10,10,100,5,1,(255,121,121))]
        self.monstres=[]
        self.entitees=[self.joueur]
        self.meutes=[Meute(self.CASES_X,self.CASES_Y,[Fatti([5,10],10,10,100,5,1,(0,0,100)),Fatti([10,10],10,10,100,5,1,(0,0,100))])]

        #objet qui traite les collisions
        self.collision=Collision()

        #événements
        self.evenements=[]
        
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
                
                vue,position=self.actualiser_vue(self.joueur.getPosition(),self.joueur.largeur_vue,self.joueur.hauteur_vue)
                self.joueur.actualiser_vue(vue,position)
                
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
            #if move_j or move_m:
            self.redraw()
            self.traitement_evenements()

            if self.lab.as_gagner(self.joueur.getPosition()):
                self.ecran_fin_niveau(self.textWin)
                run=False
            if self.as_perdu():
                self.ecran_fin_niveau(self.textLose)
                run=False
            pygame.display.update()
        pygame.quit()

    def traitement_evenements(self):
        """
        Fonction qui traite les événements
        """
        events_tmps=[self.evenements[i] for i in range(0,len(self.evenements))]
        nbSup=0
        
        for i in range(0,len(events_tmps)):
            #print (events_tmps)
            if events_tmps[i].execute():
                self.evenements.pop(i-nbSup)
                nbSup+=1
                
                 
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
            
    def ajout_anim_attaque(self,position_entitee):
        """
        Fonction qui ajoute un ajoute une animation d'attaque a la pile d'événements
        Entrées:
            -la position de l'entitée
        Sorties:
            Rien
        """
        if self.est_dans_vue(position_entitee):
            radius=(self.LARGEUR_CASE+self.LARGEUR_MUR)*2
            position_anim_x=(self.LARGEUR_CASE+self.LARGEUR_MUR)*(position_entitee[0]-self.joueur.getPosition()[0]+self.joueur.largeur_vue//2)
            position_anim_y=(self.LARGEUR_CASE+self.LARGEUR_MUR)*(position_entitee[1]-self.joueur.getPosition()[1]+self.joueur.hauteur_vue//2)

            position_anim=[position_anim_x,position_anim_y]
            self.evenements.append(Attaque(10,position_anim,radius,self.screen))
    def est_dans_vue(self,position):
        """
        Fonction qui détermine si l'entitee est en vue du joueur
        Entrées:
            -la position de l'entitée
        Sorties:
            -un booléen indiquant si l'entitée est en vue
        """
        joueur_position=self.joueur.getPosition()

        joueur_x=joueur_position[0]
        joueur_y=joueur_position[1]

        min_x=joueur_x-self.joueur.largeur_vue//2
        max_x=joueur_x+self.joueur.largeur_vue-self.joueur.largeur_vue//2

        min_y=joueur_y-self.joueur.hauteur_vue//2
        max_y=joueur_y+self.joueur.hauteur_vue-self.joueur.hauteur_vue//2

        return (position[0]>=min_x and position[0]<max_x)and(position[1]>=min_y and position[1]<max_y)
        
    def actions_meutes(self):
        """
        Fonction qui exécute les actions des meutes
        renvoie un booléen indiquant si il y a besoin de redessiner l'écran
        """
        redessiner=False

        for meute in self.meutes:
            positions,largeurs_vues,hauteur_vues=meute.getDonneesVues()

            vues,positions_vues=self.actualiser_vue_meute(positions,largeurs_vues,hauteur_vues)

            meute.actualisation_vues(vues,positions_vues,self.joueur.getPosition())

            meute.prochaines_actions()
            
            monstres_meute=meute.getMonstres()
            for monstre in monstres_meute:
                if redessiner:
                    self.traitement_action(monstre)
                else:
                    redessiner=self.traitement_action(monstre)
            
        return redessiner
    def actualiser_vue_meute(self,positions,largeurs_vues,hauteur_vues):
        """
        Fonction qui doit renvoyer les vues nécessaires a une meute
        Entrées:
            -les positions des monstres de la meute
            -les largeurs et hauteurs des vues des monstres de la meute
        Sorties:
            -les vues des monstres
            -les positions des vues
        """
        vues=[]
        positions_vues=[]

        for i in range(0,len(positions)):
            vue,position_vue=self.actualiser_vue(positions[i],largeurs_vues[i],hauteur_vues[i])
            vues+=[vue]
            positions_vues+=[position_vue]

        return vues,positions_vues


    def actions_entitees(self):
        """
        Fonction qui exécute les actions des entitées
        renvoie un booléen indiquant si il y a besoin de redessiner l'écran
        """
        redessiner=False
        
        for entitee in self.entitees:
            #on actualise la vue de l'entitée
            vue_entitee,position_vue=self.actualiser_vue(entitee.getPosition(),entitee.getLargeurVue(),entitee.getHauteurVue())
            entitee.actualiser_vue(vue_entitee,position_vue)
            
            entitee=self.actualiser_donnee(entitee)

            entitee.prochaine_action()
            if redessiner:
                self.traitement_action(entitee)
            else:
                redessiner=self.traitement_action(entitee)
            #print(redessiner,type(entitee))
        
        if redessiner:
            self.actions_meutes()
        else:
            redessiner=self.actions_meutes()

        self.delete_entitees()
        
        return redessiner

    def delete_entitees(self):
        """
        Fonction qui supprime les entitees mortes
        """
        nbSupp=0
        for i in range(0,len(self.entitees)):
            if self.entitees[i-nbSupp].pv<=0:
                self.entitees.pop(i-nbSupp)
                nbSupp+=1
        #on traite les meutes
        if self.meutes!=None:
            for meute in self.meutes:
                monstres=meute.getMonstres()
                nbSupp=0
                for i in range(0,len(monstres)):
                    if monstres[i-nbSupp].pv<=0:
                        nbSupp+=1
                        monstres.pop(i-nbSupp)
        
    def actualiser_vue(self,position,largeur_vue,hauteur_vue):
        """
        Fonction qui construit la vue d'un agissant
        Entrée:
            -la position de la vue de l'agissant
            -la largeur de la vue de l'agissant
            -la hauteur de la vue de l'agissant
        Sortie:
            -la vue de l'agissant
            -la position de la vue de l'agissant
        """
        vue_agissant,position_vue=self.lab.construire_vue(position,largeur_vue,hauteur_vue)

        return vue_agissant,position_vue
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
                    libre = self.collision.case_libre(newcoord,self.entitees,self.meutes)
                    #print(libre)
                    if libre:
                        succes=True
                        #print(succes)
                        agissant.setPosition(newcoord)
                        if agissant == self.joueur:
                            nouveaux_evenements = self.collision.visite_case(newcoord,agissant,self.entitees)
                            for evenement in nouveaux_evenements :
                                self.evenements.append(evenement)
        elif id_action==ATTAQUER:
            self.ajout_anim_attaque(agissant.getPosition())
            succes=self.collision.tentative_attaque(agissant,self.entitees,self.meutes)
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
        entitees=[]
        
        for monstre in self.monstres:
            entitees+=[monstre]
            
        for meute in self.meutes:
            monstres=meute.getMonstres()
            for monstre in monstres:
                entitees+=[monstre]
                
        self.screen.fill((0,0,0))
        self.lab.dessine_toi(self.screen,self.joueur.position,entitees,self.position_screen,self.joueur.largeur_vue,self.joueur.hauteur_vue,self.mode_affichage,self.LARGEUR_CASE,self.LARGEUR_MUR)
        self.joueur.dessine_toi(self.screen,(self.joueur.largeur_vue//2,self.joueur.hauteur_vue//2),self.LARGEUR_CASE,self.LARGEUR_MUR,self.position_screen)

