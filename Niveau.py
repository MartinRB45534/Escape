import pygame
from Labyrinthe import *
from Joueur import *
from Constantes import *
from Patern import *
from Monstres import *
from Potion import *
from Inventaire import *
from Collisions import *
from Meute import *
from Evenement import *
from Animation import *
from Affichage import *
from Clee import *
from Murs import *

class Niveau:
    def __init__(self,niveau,difficulté,mode_affichage):

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

        if niveau == 0:
            if difficulté == BEGINNER :
                self.CASES_X = 20
                self.CASES_Y = 20
                res = True
                self.salles=[Patern((8,8),10,10,self.LARGEUR_CASE,self.LARGEUR_MUR)]
            elif difficulté == EASY :
                self.CASES_X = 20
                self.CASES_Y = 20
                res = False
                self.salles=[Patern((14,14),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR)]
            elif difficulté == AVERAGE :
                self.CASES_X = 40
                self.CASES_Y = 40
                res = False
                self.salles=[Patern((17,17),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR)]
            elif difficulté == HARD :
                self.CASES_X = 60
                self.CASES_Y = 60
                res = False
                self.salles=[Patern((10,29),40,2,self.LARGEUR_CASE,self.LARGEUR_MUR,[])]
                #on génère les entrées de manière a avoir un espace ouvert
                self.salles[0].pre_gen_entrees_x(0,0,39)
                self.salles[0].pre_gen_entrees_x(1,0,39)
            elif difficulté == INSANE :
                self.CASES_X = 100
                self.CASES_Y = 100
                res = False
                self.salles=[Patern((49,30),2,40,self.LARGEUR_CASE,self.LARGEUR_MUR)]
            elif difficulté == IMPOSSIBLE :
                self.CASES_X = 1000
                self.CASES_Y = 1000
                res = False
                self.salles=[]

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
            self.salles.append(Patern((0,0),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,3]]))

            #génération du labyrinthe
            self.lab=Labyrinthe(self.CASES_X,self.CASES_Y,self.CASES_X-1,self.CASES_Y-1,self.LARGEUR_CASE,self.LARGEUR_MUR,self.poids,self.salles)
            self.lab.generation()
            self.lab.casser_X_murs(0.1)
            #exp avec les portes
            mat_lab=self.lab.getMatrice_cases()
            mat_lab[4][2].murs[DROITE]=Porte(self.LARGEUR_MUR,"goodooKey")
            self.lab.matrice_cases=mat_lab
        
            if res :
                self.lab.resolution(self.CASES_X-1,self.CASES_Y-1,0,0,"Largeur")

            pygame.display.set_caption("test")
            self.screen = pygame.display.set_mode((FENETRE_X,FENETRE_Y),pygame.RESIZABLE)
            self.screen.fill((0,0,0))

            #entitées
            self.joueur=Joueur(inventaire_joueur,self.hp_joueur,self.force_joueur,2,self.zoom_largeur,self.zoom_hauteur)
        
            self.monstres=[Fatti([5,10],10,10,100,5,1,5,(0,0,100))]#,Fatti([10,10],10,10,100,5,1,5,(0,0,100))]
            self.entitees=[self.joueur,Clee((3,3),"goodooKey")]

        elif niveau == 1:
            #niveau labyrinthique sans monstres pour apprendre à se déplacer

            self.CASES_X = 40
            self.CASES_Y = 40
            res = False
            self.salles=[]

            #variables correspondants a la largeur et la hauteur du zoom
            self.zoom_largeur=13
            self.zoom_hauteur=13

            self.force_joueur = 10
            self.hp_joueur = 200

            inventaire_joueur = Inventaire()
        
            pygame.init()
            #poids permettants de manipuler l'aléatoire
            self.poids=[6,2,1,2]
        
            #salle pour exp monstres
            self.salles.append(Patern((0,0),11,3,self.LARGEUR_CASE,self.LARGEUR_MUR,[[10,1],[8,2]]))

            #génération du labyrinthe
            self.lab=Labyrinthe(self.CASES_X,self.CASES_Y,self.CASES_X-1,self.CASES_Y-1,self.LARGEUR_CASE,self.LARGEUR_MUR,self.poids,self.salles)
            self.lab.generation()
            self.lab.casser_X_murs(0.2)
            mat_lab=self.lab.getMatrice_cases()
            self.lab.matrice_cases=mat_lab
        
            if res :
                self.lab.resolution(self.CASES_X-1,self.CASES_Y-1,0,0,"Largeur")

            pygame.display.set_caption("test")
            self.screen = pygame.display.set_mode((FENETRE_X,FENETRE_Y),pygame.RESIZABLE)
            self.screen.fill((0,0,0))

            #entitées
            self.joueur=Joueur(inventaire_joueur,self.hp_joueur,self.force_joueur,2,self.zoom_largeur,self.zoom_hauteur)
        
            self.monstres=[]#Fatti([25,25],10,10,100,5,1,5,(0,0,100)),Fatti([25,30],10,10,100,5,1,5,(0,0,100)),Fatti([30,25],10,10,100,5,1,5,(0,0,100)),Fatti([30,30],10,10,100,5,1,5,(0,0,100))]
            self.entitees=[self.joueur]

        elif niveau == 2:
            #niveau monstrueux sans labyrinthe pour apprendre à se battre

            self.CASES_X = 10
            self.CASES_Y = 60
            res = False
            self.salles=[Patern((1,13),8,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,-1],[5,7]]),Patern((1,25),6,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,-1],[5,7]]),Patern((2,40),8,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,-1],[5,7]]),Patern((4,52),5,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,-1]])]

            #variables correspondants a la largeur et la hauteur du zoom
            self.zoom_largeur=13
            self.zoom_hauteur=13

            self.force_joueur = 10
            self.hp_joueur = 200

            inventaire_joueur = Inventaire()
        
            pygame.init()
            #poids permettants de manipuler l'aléatoire
            self.poids=[6,2,1,2]
        
            #salle pour exp monstres
            self.salles.append(Patern((4,0),2,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,9],[1,9]]))

            #génération du labyrinthe
            self.lab=Labyrinthe(self.CASES_X,self.CASES_Y,5,59,self.LARGEUR_CASE,self.LARGEUR_MUR,self.poids,self.salles)
            self.lab.generation()
            self.lab.casser_X_murs(0.2)
            mat_lab=self.lab.getMatrice_cases()
            self.lab.matrice_cases=mat_lab
        
            if res :
                self.lab.resolution(5,59,4,0,"Largeur")

            pygame.display.set_caption("test")
            self.screen = pygame.display.set_mode((FENETRE_X,FENETRE_Y),pygame.RESIZABLE)
            self.screen.fill((0,0,0))

            #entitées
            self.joueur=Joueur(inventaire_joueur,self.hp_joueur,self.force_joueur,2,self.zoom_largeur,self.zoom_hauteur,(4,0))
        
            self.monstres=[Fatti([5,17],10,10,100,5,1,0,(0,0,100)),Fatti([8,25],10,10,100,5,1,1,(0,0,100)),Fatti([3,48],10,10,100,5,1,2,(0,0,100)),Fatti([5,59],10,10,100,5,1,3,(0,0,100))]
            self.entitees=[self.joueur]

        elif niveau == 3:
            #niveau monstrueux sans labyrinthe pour apprendre à se battre

            self.CASES_X = 10
            self.CASES_Y = 60
            res = False
            self.salles=[Patern((1,13),8,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,-1],[5,7]]),Patern((1,25),6,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,-1],[5,7]]),Patern((2,40),8,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,-1],[5,7]]),Patern((4,52),5,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,-1]])]

            #variables correspondants a la largeur et la hauteur du zoom
            self.zoom_largeur=13
            self.zoom_hauteur=13

            self.force_joueur = 10
            self.hp_joueur = 200

            inventaire_joueur = Inventaire()
        
            pygame.init()
            #poids permettants de manipuler l'aléatoire
            self.poids=[6,2,1,2]
        
            #salle pour exp monstres
            self.salles.append(Patern((4,0),2,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,9],[1,9]]))

            #génération du labyrinthe
            self.lab=Labyrinthe(self.CASES_X,self.CASES_Y,5,59,self.LARGEUR_CASE,self.LARGEUR_MUR,self.poids,self.salles)
            self.lab.generation()
            self.lab.casser_X_murs(0.2)
            mat_lab=self.lab.getMatrice_cases()
            self.lab.matrice_cases=mat_lab
        
            if res :
                self.lab.resolution(5,59,4,0,"Largeur")

            pygame.display.set_caption("test")
            self.screen = pygame.display.set_mode((FENETRE_X,FENETRE_Y),pygame.RESIZABLE)
            self.screen.fill((0,0,0))

            #entitées
            self.joueur=Joueur(inventaire_joueur,self.hp_joueur,self.force_joueur,2,self.zoom_largeur,self.zoom_hauteur,(4,0))
        
            self.monstres=[Slime([5,17],10,10,100,5,1,0,(0,0,100)),Fatti([8,25],10,10,100,5,1,1,(0,0,100)),Runner(self.lab.getMatrice_cases(),5,59,[3,48],10,10,100,5,1,2,(0,0,100)),Fatti([5,59],10,10,100,5,1,3,(0,0,100))]
            self.entitees=[self.joueur]

        elif niveau == 4:
            #niveau monstrueux sans labyrinthe pour apprendre à se battre

            self.CASES_X = 15
            self.CASES_Y = 15
            res = False
            self.salles=[Patern((3,0),3,15,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,13],[2,1]]),Patern((6,0),3,15,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,1],[2,13]]),Patern((9,0),3,15,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,13],[2,1]]),Patern((12,0),3,15,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,1]])]

            #variables correspondants a la largeur et la hauteur du zoom
            self.zoom_largeur=13
            self.zoom_hauteur=13

            self.force_joueur = 10
            self.hp_joueur = 200

            inventaire_joueur = Inventaire()
        
            pygame.init()
            #poids permettants de manipuler l'aléatoire
            self.poids=[6,2,1,2]
        
            #salle pour exp monstres
            self.salles.append(Patern((0,0),3,15,self.LARGEUR_CASE,self.LARGEUR_MUR,[[2,13]]))

            #génération du labyrinthe
            self.lab=Labyrinthe(self.CASES_X,self.CASES_Y,self.CASES_X-1,self.CASES_Y-1,self.LARGEUR_CASE,self.LARGEUR_MUR,self.poids,self.salles)
            self.lab.generation()
            self.lab.casser_X_murs(0.0)
            mat_lab=self.lab.getMatrice_cases()
            self.lab.matrice_cases=mat_lab
        
            if res :
                self.lab.resolution(self.CASES_X-1,self.CASES_Y-1,0,0,"Largeur")

            pygame.display.set_caption("test")
            self.screen = pygame.display.set_mode((FENETRE_X,FENETRE_Y),pygame.RESIZABLE)
            self.screen.fill((0,0,0))

            #entitées
            self.joueur=Joueur(inventaire_joueur,self.hp_joueur,self.force_joueur,2,self.zoom_largeur,self.zoom_hauteur)
        
            self.monstres=[Slime([1,5],10,10,100,5,1,1,(0,0,100)),Slime([2,12],10,10,100,5,1,1,(0,0,100)),Slime([0,12],10,10,100,5,1,1,(0,0,100)),Slime([1,13],10,10,100,5,1,1,(0,0,100)),Slime([2,8],10,10,100,5,1,1,(0,0,100)),Slime([0,8],10,10,100,5,1,1,(0,0,100)),Slime([1,9],10,10,100,5,1,1,(0,0,100)),Slime([2,10],10,10,100,5,1,1,(0,0,100)),Slime([0,10],10,10,100,5,1,1,(0,0,100)),Slime([1,11],10,10,100,5,1,1,(0,0,100)),Slime([7,5],10,10,100,5,1,2,(0,0,100)),Slime([8,12],10,10,100,5,1,2,(0,0,100)),Slime([6,12],10,10,100,5,1,2,(0,0,100)),Slime([7,13],10,10,100,5,1,2,(0,0,100)),Slime([8,8],10,10,100,5,1,2,(0,0,100)),Slime([6,8],10,10,100,5,1,2,(0,0,100)),Slime([7,9],10,10,100,5,1,2,(0,0,100)),Slime([8,10],10,10,100,5,1,2,(0,0,100)),Slime([6,10],10,10,100,5,1,2,(0,0,100)),Slime([7,11],10,10,100,5,1,2,(0,0,100))]
            self.entitees=[self.joueur]
            
        
        for i in range(0,len(self.monstres)):
            self.entitees.append(self.monstres[i])

        #objet qui traite les collisions
        self.collision=Collision()

        #événements
        self.evenements=[]

        #objet d'affichage
        self.affichage=Affichage(self.screen,self.mode_affichage,self.LARGEUR_CASE,self.LARGEUR_MUR)
        
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


    def actions_entitees(self):
        """
        Fonction qui exécute les actions des entitées
        renvoie un booléen indiquant si il y a besoin de redessiner l'écran
        """
        redessiner=False

        agissants=self.getAgissants()
        
        self.actualiser_vues_agissants(agissants)
        
        for agissant in agissants:
            
            agissant=self.actualiser_donnee(agissant)

            agissant.prochaine_action()
            if redessiner:
                self.traitement_action(agissant)
            else:
                redessiner=self.traitement_action(agissant)
            #print(redessiner,type(entitee))

        self.delete_entitees()
        
        return redessiner
    def getAgissants(self):
        """
        Fonction qui renvoie un tableau contenant les agissants
        """
        agissants=[]
        
        for entitee in self.entitees:
            if issubclass(type(entitee),Agissant):
                agissants.append(entitee)

        return agissants
    def delete_entitees(self):
        """
        Fonction qui supprime les entitees mortes
        """
        nbSupp=0
        for i in range(0,len(self.entitees)):
            if issubclass(type(self.entitees[i-nbSupp]),Agissant):
                if self.entitees[i-nbSupp].pv<=0:
                    self.entitees.pop(i-nbSupp)
                    nbSupp+=1
            elif issubclass(type(self.entitees[i-nbSupp]),Item):
                if self.entitees[i-nbSupp].position==None:
                    self.entitees.pop(i-nbSupp)
                    nbSupp+=1
        
    def actualiser_vues_agissants(self,agissants):
        """
        Fonction qui actualise la vue de touts les agissants (meutes inclues)
        Entrée:
            -les agissants
        """
        for agissant in agissants:
            #l'id 0 indique que l'entitée n'appartient a aucune meute
            if not(issubclass(type(agissant),Monstre)) or agissant.id_meute==0:
                #on actualise la vue de l'entitée seule
                vue_entitee,position_vue=self.actualiser_vue(agissant.getPosition(),agissant.getLargeurVue(),agissant.getHauteurVue())
                agissant.actualiser_vue(vue_entitee,position_vue)

        id_meutes=[0]
        meute=Meute(self.CASES_X,self.CASES_Y)
        for agissant in agissants:
            #on vérifie si on n'as pas déja executée la meute de l'entitée
            if issubclass(type(agissant),Monstre) and not(agissant.id_meute in id_meutes):
                id_meutes.append(agissant.id_meute)
                #on récupère les données de la vue de la meute
                vues,positions=self.recuperer_vues_meute(agissant.id_meute)
                #on crée la vue de la meute
                vue_meute=meute.actualisation_vues(vues,positions)
                
                #on actualise les vues des monstres de la meute
                for agissant_bis in agissants:
                    if issubclass(type(agissant_bis),Monstre):
                        if agissant_bis.id_meute==agissant.id_meute:
                            agissant_bis.actualiser_vue(vue_meute,[0,0])
    def recuperer_vues_meute(self,identifiant):
        """
        Fonction qui doit renvoyer les vues nécessaires a une meute
        Entrées:
            -l'identifiant de la meute
        Sorties:
            -les vues des monstres
            -les positions des vues
        """
        vues=[]
        positions=[]
        for entitee_bis in self.entitees:
            if issubclass(type(entitee_bis),Monstre):
                if entitee_bis.id_meute==identifiant:
                    vue_entitee,position_vue=self.actualiser_vue(entitee_bis.getPosition(),entitee_bis.getLargeurVue(),entitee_bis.getHauteurVue())
                    vues.append(vue_entitee)
                    positions.append(position_vue)

        return vues,positions
    
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
        if issubclass(type(agissant),Monstre):
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
                if issubclass(type(agissant),Joueur):
                    passe,newcoord=self.lab.peut_passer(agissant.getPosition(),direction_voulue,agissant.inventaire)
                else:
                    passe,newcoord=self.lab.peut_passer(agissant.getPosition(),direction_voulue)
                #print(passe)
                if passe:
                    libre = self.collision.case_libre(agissant,newcoord,self.entitees)
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
            self.affichage.ajout_animation(agissant.getPosition(),0,3,agissant.getRadius()*(self.LARGEUR_CASE+self.LARGEUR_MUR))
            succes=self.collision.tentative_attaque(agissant,self.entitees)
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
        self.affichage.dessine_frame(self.joueur,self.lab,self.entitees,self.evenements)
