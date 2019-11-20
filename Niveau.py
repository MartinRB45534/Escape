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
from Minimap import *

class Niveau:
    def __init__(self,niveau,difficulté,mode_affichage,mode_minimap):
        
        self.mode_affichage = mode_affichage
        if self.mode_affichage == voir_tout :
            self.LARGEUR_CASE = 20
            self.LARGEUR_MUR = 1
        elif self.mode_affichage == aveugle :
            self.LARGEUR_CASE = 20
            self.LARGEUR_MUR = 1
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
                #self.salles=[Patern((8,8),10,10,self.LARGEUR_CASE,self.LARGEUR_MUR)]
                proba_murs = 0.5
            elif difficulté == EASY :
                self.CASES_X = 20
                self.CASES_Y = 20
                res = False
                #self.salles=[Patern((14,14),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR)]
                proba_murs = 0.4
            elif difficulté == AVERAGE :
                self.CASES_X = 40
                self.CASES_Y = 40
                res = False
                #self.salles=[Patern((17,17),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR)]
                proba_murs = 0.3
            elif difficulté == HARD :
                self.CASES_X = 60
                self.CASES_Y = 60
                res = False
                #self.salles=[Patern((10,29),40,2,self.LARGEUR_CASE,self.LARGEUR_MUR,[])]
                #on génère les entrées de manière a avoir un espace ouvert
                #self.salles[0].pre_gen_entrees_x(0,0,39)
                #self.salles[0].pre_gen_entrees_x(1,0,39)
                proba_murs = 0.2
            elif difficulté == INSANE :
                self.CASES_X = 100
                self.CASES_Y = 100
                res = False
                #self.salles=[Patern((49,30),2,40,self.LARGEUR_CASE,self.LARGEUR_MUR)]
                proba_murs = 0.1
            elif difficulté == IMPOSSIBLE :
                self.CASES_X = 1000
                self.CASES_Y = 1000
                res = False
                self.salles=[]
                proba_murs = 0

            self.depart = (0,0)
            self.arrivee = (self.CASES_X-1,self.CASES_Y-1)
            #variables correspondants a la largeur et la hauteur du zoom
            self.zoom_largeur=11
            self.zoom_hauteur=11

            self.force_joueur = 5
            self.hp_joueur = 100
            self.vitesse_joueur=3

            self.vitesse_montres=20

            inventaire_joueur = Inventaire()
        
            pygame.init()
            #poids permettants de manipuler l'aléatoire
            self.poids=[6,2,1,2]
        
            #salle pour exp monstres
            self.salles=[Patern((0,0),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR,[[1,0],[4,3]])]

            #exp avec les portes
            #mat_lab=self.lab.getMatrice_cases()
            #mat_lab[4][2].murs[DROITE].set_etat(INTOUCHABLE)
            #self.lab.matrice_cases=mat_lab

            monstres=[]#[Fatti([4,4])]#,Fatti([10,10])]
            self.entitees=[Clee((3,3),"goodooKey")]

        elif niveau == 1:
            #niveau labyrinthique sans monstres pour apprendre à se déplacer

            self.CASES_X = 40
            self.CASES_Y = 40
            self.arrivee = (39,39)
            self.depart = (0,0)
            res = False
            self.salles=[Patern((0,0),11,3,self.LARGEUR_CASE,self.LARGEUR_MUR,[[10,1],[8,2]])]
            proba_murs = 0.1

            #variables correspondants a la largeur et la hauteur du zoom
            self.zoom_largeur=13
            self.zoom_hauteur=13

            self.force_joueur = 10
            self.hp_joueur = 200
            self.vitesse_joueur=3

            self.vitesse_montres=20

            inventaire_joueur = Inventaire()
        
            pygame.init()
            #poids permettants de manipuler l'aléatoire
            self.poids=[6,2,1,2]
        
            monstres=[]
            self.entitees=[]

        elif niveau == 2:
            #niveau monstrueux sans labyrinthe pour apprendre à se battre

            self.CASES_X = 10
            self.CASES_Y = 60
            self.arrivee = (5,59)
            self.depart = (5,0)
            res = False
            self.salles=[Patern((4,0),2,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,9],[1,9]]),Patern((1,13),8,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,-1],[5,7]]),Patern((1,25),6,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,-1],[5,7]]),Patern((2,40),8,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,-1],[5,7]]),Patern((4,52),5,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,-1]])]
            proba_murs = 0.3

            #variables correspondants a la largeur et la hauteur du zoom
            self.zoom_largeur=13
            self.zoom_hauteur=13

            self.force_joueur = 10
            self.hp_joueur = 200
            self.vitesse_joueur=3

            self.vitesse_montres=20

            inventaire_joueur = Inventaire()
        
            pygame.init()
            #poids permettants de manipuler l'aléatoire
            self.poids=[6,2,1,2]

            monstres=[Fatti([5,17]),Fatti([8,25]),Fatti([3,48]),Fatti([5,59])]
            self.entitees=[]

        elif niveau == 3:
            #niveau monstrueux sans labyrinthe pour apprendre à se battre

            self.CASES_X = 10
            self.CASES_Y = 60
            self.arrivee = (5,59)
            self.depart = (5,0)
            res = False
            self.salles=[Patern((4,0),2,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,9],[1,9]]),Patern((1,13),8,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,-1],[5,7]]),Patern((1,25),6,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,-1],[5,7]]),Patern((2,40),8,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,-1],[5,7]]),Patern((4,52),5,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,-1]])]
            proba_murs = 0.2

            #variables correspondants a la largeur et la hauteur du zoom
            self.zoom_largeur=13
            self.zoom_hauteur=13

            self.force_joueur = 10
            self.hp_joueur = 200
            self.vitesse_joueur=3

            self.vitesse_montres=20

            inventaire_joueur = Inventaire()
        
            #poids permettants de manipuler l'aléatoire
            self.poids=[6,2,1,2]
        
            monstres=[Slime([5,17]),Fatti([8,25]),Fatti([5,59])]
            self.entitees=[]

        elif niveau == 4:
            #niveau monstrueux sans labyrinthe pour apprendre à se battre contre des meutes

            self.CASES_X = 15
            self.CASES_Y = 15
            self.arrivee = (13,13)
            self.depart = (1,1)
            res = False
            self.salles=[Patern((0,0),3,15,self.LARGEUR_CASE,self.LARGEUR_MUR,[[2,13]]),Patern((3,0),3,15,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,13],[2,1]]),Patern((6,0),3,15,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,1],[2,13]]),Patern((9,0),3,15,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,13],[2,1]]),Patern((12,0),3,15,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,1]])]
            proba_murs = 0

            #variables correspondants a la largeur et la hauteur du zoom
            self.zoom_largeur=13
            self.zoom_hauteur=13

            self.force_joueur = 10
            self.hp_joueur = 200
            self.vitesse_joueur=3

            self.vitesse_montres=20

            inventaire_joueur = Inventaire()

            #poids permettants de manipuler l'aléatoire
            self.poids=[6,2,1,2]
            
            meute1 = [Fatti([1,5],1),Fatti([2,12],1),Fatti([0,12],1),Fatti([1,13],1)]
            meute2 = [Slime([4,0],2),Slime([3,1],2),Slime([5,1],2),Slime([4,2],2),Slime([3,3],2),Slime([5,3],2),Slime([4,4],2),Slime([3,5],2),Slime([5,5],2),Slime([4,6],2),Slime([3,7],2),Slime([5,7],2),Slime([4,8],2)]
            meute3 = [Slime([7,8],3),Slime([8,9],3),Slime([6,9],3),Fatti([6,11],3),Fatti([7,11],3),Fatti([8,11],3)]
            meute4 = [Slime([10,5],4),Slime([10,6],4),Slime([10,7],4),Slime([10,8],4),Slime([10,9],4),Slime([10,10],4),Fatti([10,2],4,10,10,300,30)]
            meute5 = [Slime([13,8],5),Slime([14,9],5),Slime([12,9],5),Fatti([12,11],5),Fatti([13,11],5),Fatti([14,11],5)]
            monstres = meute1
            for meutenumerote in [meute2,meute3,meute4,meute5]:
                for monstre in meutenumerote:
                    monstres.append(monstre)
            self.entitees=[]

        elif niveau == 5:
            #niveau avec labyrinthe et montres pour apprendre l'utilité des potions

            self.CASES_X = 40
            self.CASES_Y = 40
            self.arrivee = (39,39)
            self.depart = (0,0)
            res = False
            self.salles=[Patern((0,0),11,11,self.LARGEUR_CASE,self.LARGEUR_MUR,[[10,1]])]
            proba_murs = 0.2

            #variables correspondants a la largeur et la hauteur du zoom
            self.zoom_largeur=13
            self.zoom_hauteur=13

            self.force_joueur = 10
            self.hp_joueur = 200
            self.vitesse_joueur=3

            self.vitesse_montres=20

            inventaire_joueur = Inventaire()
            monstres=self.spawn_aleatoire(Fatti,10,10,100,10,self.vitesse_montres,1,((10,10),(30,30)),0.1,5,0,(0,0,100))
            
            #poids permettants de manipuler l'aléatoire
            self.poids=[6,9,1,1]

        #génération du labyrinthe
        self.lab=Labyrinthe(self.CASES_X,self.CASES_Y,self.arrivee[0],self.arrivee[1],self.LARGEUR_CASE,self.LARGEUR_MUR,self.poids,self.salles)
        self.lab.generation(0.95)

        pygame.display.set_caption("test")
        self.screen = pygame.display.set_mode((FENETRE_X,FENETRE_Y),pygame.RESIZABLE)
        self.screen.fill((0,0,0))

        #entitées
        minimap = Minimap(self.lab.getMatrice_cases(),mode_minimap,self.depart,self.arrivee)
        self.joueur=Joueur(minimap,inventaire_joueur,self.hp_joueur,self.force_joueur,self.vitesse_joueur,2,self.zoom_largeur,self.zoom_hauteur,self.depart)
        self.monstres = monstres
        
        if niveau == 0:
            #exp avec les portes
            mat_lab=self.lab.getMatrice_cases()
            mat_lab[4][2].murs[DROITE]=Porte(self.LARGEUR_MUR,"goodooKey")
            self.lab.matrice_cases=mat_lab
        if niveau == 3:
            self.monstres.append(Runner(self.lab.getMatrice_cases(),5,59,[3,48]))
        if niveau == 4:
            meute5 = [Runner(self.lab.getMatrice_cases(),self.CASES_X-1,self.CASES_Y-1,[12,5]),Runner(self.lab.getMatrice_cases(),self.CASES_X-1,self.CASES_Y-1,[13,0]),Runner(self.lab.getMatrice_cases(),self.CASES_X-1,self.CASES_Y-1,[14,5])]
            for monstre in meute5:
                self.monstres.append(monstre)
        if niveau == 5:
            potions_vue=[Potion_de_vision((35,26),self.joueur),Potion_de_vision((27,38),self.joueur),Potion_de_vision((21,19),self.joueur),Potion_de_visibilite_permanente((8,7),self.joueur)]
            potions_combat=[Potion_de_force((i,j),self.joueur)for j in range(5,45,10) for i in range(5,45,10)] + [Potion_de_portee((i,j),self.joueur)for j in range (10,40,10) for i in range (10,40,10)] + [Potion_de_soin((20,20),self.joueur),Potion_de_portee_permanente((2,2),self.joueur)]
            potions=potions_vue+potions_combat
            self.entitees=potions

        self.entitees.append(self.joueur)
        
        if res :
            self.lab.resolution(self.arrivee[0],self.arrivee[1],self.depart[0],self.depart[1],"Largeur")
        
        for i in range(0,len(self.monstres)):
            self.entitees.append(self.monstres[i])

        #generation des meutes
        self.meutes=self.generation_meutes()
        #objet qui traite les collisions
        self.collision=Collision()

        #événements
        self.evenements=[]

        self.plus_lent=self.getPlusLent()
        #variable qui nous sert a exécuter les actions des entitées
        self.horloge_cycle=0

        #objet d'affichage
        self.affichage=Affichage(self.screen,self.mode_affichage,self.LARGEUR_CASE,self.LARGEUR_MUR,self.lab.largeur,self.lab.hauteur)
        
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
        
        while run:
            #on cadence à 60 frames/sec
            clock.tick(60)
            self.actualiser_temps()

            #si l'utilisateur décide de mettre fin au programme on sort de la boucle
            events = []
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    res = 0
                    run=False

                if event.type == pygame.VIDEORESIZE:
                    self.zoom_largeur = event.w//(self.LARGEUR_CASE + self.LARGEUR_MUR)
                    self.zoom_hauteur = event.h//(self.LARGEUR_CASE + self.LARGEUR_MUR)
                    self.redraw()
                else:
                    events.append(event)
            self.actions_entitees(events)

            #si on détecte un mouvement on redessine l'écran
            #if move_j or move_m:
            self.redraw()
            self.traitement_evenements()

            if self.lab.as_gagner(self.joueur.getPosition()):
                self.ecran_fin_niveau(self.textWin)
                res = 5000
                run=False
            if self.as_perdu():
                self.ecran_fin_niveau(self.textLose)
                res = 5000
                run=False
            pygame.display.update()
        return res
    def generation_meutes(self):
        """
        Fonction qui génère les meutes
        Sorties:
            -les meutes
        """
        meutes=[]
        id_meutes=[0]
        for monstre in self.monstres:
            if not(monstre.id_meute in id_meutes):
                #on génère une nouvelle meute
                nb_monstres=0
                id_meute=monstre.id_meute
                for monstre in self.monstres:
                    if monstre.id_meute==id_meute:
                        nb_monstres+=1
                id_meutes.append(id_meute)
                #on récupère les données de la vue de la meute
                vues,positions=self.recuperer_vues_meute(id_meute)
                
                meutes.append(Meute(self.CASES_X,self.CASES_Y,id_meute,nb_monstres,vues,positions))
        return meutes
                
    def actualiser_temps(self):
        """
        Fonction qui actualise la variable permettant de mesurer le temps pour
        les entitées
        """
        #on vérifie qu'on n'est pas a la fin d'un cycle
        if self.horloge_cycle<self.plus_lent+1:
            self.horloge_cycle+=1
        else:
            self.horloge_cycle=1
            
    
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
                
                 
    def action_joueur(self,events=[]):
        """
        Fonction qui exécute la partie du code ou le jpueur demande à agir
        et qui renvoie rien
        """
        for event in events:
            if event.type==pygame.KEYDOWN and event.key==pygame.K_a:
                if self.affichage.affiche != MINIMAP:
                    self.affichage.affiche = MINIMAP
                else :
                    self.affichage.affiche = LABYRINTHE
            if event.type==pygame.KEYDOWN and event.key==pygame.K_i:
                if self.affichage.affiche != INVENTAIRE:
                    self.affichage.affiche = INVENTAIRE
                else :
                    self.affichage.affiche = LABYRINTHE
                    
            if self.affichage.affiche == INVENTAIRE:
                if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
                    self.joueur.inventaire_vers_la_droite()
                elif event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
                    self.joueur.inventaire_vers_la_gauche()
                elif event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                    evenement = self.joueur.utilise_inventaire()
                    if evenement != None:
                        self.evenements.append()

        if self.affichage.affiche == LABYRINTHE:
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



    def actions_entitees(self,events):
        """
        Fonction qui exécute les actions des entitées
        renvoie un booléen indiquant si il y a besoin de redessiner l'écran
        """
        redessiner=False

        agissants=self.getAgissants()
        
        self.actualiser_vues_agissants(agissants)
        
        for agissant in agissants:
            if self.horloge_cycle % agissant.getVitesse()==0:
                if issubclass(type(agissant),Joueur):
                    self.action_joueur(events)
                    
                agissant=self.actualiser_donnee(agissant)

                agissant.prochaine_action()
                if redessiner:
                    self.traitement_action(agissant)
                else:
                    redessiner=self.traitement_action(agissant)

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
            elif issubclass(type(self.entitees[i-nbSupp]),Item) or issubclass(type(self.entitees[i-nbSupp]),Potion):
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
        for agissant in agissants:
            #on vérifie si on n'as pas déja executée la meute de l'entitée
            if issubclass(type(agissant),Monstre) and not(agissant.id_meute in id_meutes):
                id_meutes.append(agissant.id_meute)
                #on récupère les données de la vue de la meute
                vues,positions=self.recuperer_vues_meute(agissant.id_meute)
                #on obtient la meute du monstre
                meute=self.getMeute(agissant.id_meute)
                #on crée la vue de la meute
                vue_meute=meute.actualisation_vues(vues,positions)
                
                #on actualise les vues des monstres de la meute
                for agissant_bis in agissants:
                    if issubclass(type(agissant_bis),Monstre):
                        if agissant_bis.id_meute==agissant.id_meute:
                            agissant_bis.actualiser_vue(vue_meute,[0,0])

    def getMeute(self,id_meute):
        """
        Fonction qui renvoie la meute correspondant a l'identifiant entrer
        Entrée:
            -l'identifiant de la meute
        Sortie:
            -la meute qui correspond a l'indentifiant
        """
        meute=None
        for meute_tmp in self.meutes:
            if meute_tmp.id_meute==id_meute:
                meute=meute_tmp
        return meute

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
            if issubclass(type(entitee_bis),Monstre) and entitee_bis.id_meute==identifiant:
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
                            self.lab.matrice_cases[newcoord[0]][newcoord[1]].passage = True
                            for evenement in nouveaux_evenements :
                                self.evenements.append(evenement)
        elif id_action==ATTAQUER:
            self.affichage.ajout_animation(agissant.getPosition(),0,3,agissant.getRadius()*(self.LARGEUR_CASE+self.LARGEUR_MUR))
            succes=self.collision.tentative_attaque(agissant,self.entitees)
        return succes
    def getPlusLent(self):
        """
        Fonction qui permet d'obtenir la plus grande vitesse
        Sorties:
            -la vitesse de l'agissants le plus lent
        """
        agissants=self.getAgissants()
        vitesses=[]
        for agissant in agissants:
            vitesses.append(agissant.getVitesse())
        return max(vitesses)
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

    def spawn_aleatoire(self,monstre,largeur_vue,hauteur_vue,pv,degats,vitesse,radius,perimetre,proba,max_meute,premiere_meute,couleur=(255,0,0)):
        """
        Fonction qui génére des monstres aléatoirement
        Entrées :
            caractéristiques des monstres à spawner (type de monstre, vue, stats)
            zone où les monstres seront spawnés
            probabilité de spawn par case
            quelques détails pour les meutes (numéro de la première meute libre et nombre maximum de monstre par meute)
        Sorties :
            Un tableau avec les monstres demandés
        """
        nb_meute = premiere_meute
        taille_meute = 0
        res = []
        for i in range (perimetre[0][0],perimetre[1][0]):
            for j in range (perimetre[0][1],perimetre[1][1]):
                if random.random() <= proba :
                    res.append(monstre((i,j),largeur_vue,hauteur_vue,pv,degats,vitesse,radius,nb_meute,couleur))
                    taille_meute += 1
                    if taille_meute == max_meute :
                        nb_meute += 1
                        taille_meute = 0
        return res
