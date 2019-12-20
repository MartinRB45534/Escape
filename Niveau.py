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
from Pnjs import *
from Cailloux import *
from Fontaine_heal import *
from Projectiles import *

class Niveau:
    def __init__(self,niveau,difficulte,mode_affichage,mode_minimap,destination=None,debut_niveau=False,joueur=None,labyrinthe=None,entitees=None,evenements=None,horloge_cycle=None):

        self.greater_teleportation = False
        self.mode_affichage = mode_affichage
        self.difficulte = difficulte
        self.mode_minimap = mode_minimap
        self.niveau = niveau
        if self.mode_affichage == voir_tout :
            self.LARGEUR_CASE = 20
            self.LARGEUR_MUR = 2
        elif self.mode_affichage == aveugle :
            self.LARGEUR_CASE = 20
            self.LARGEUR_MUR = 2
        elif self.mode_affichage == parcours_en_profondeur :
            self.LARGEUR_CASE = 20
            self.LARGEUR_MUR = 2
        elif self.mode_affichage == distance_max :
            self.LARGEUR_CASE = 20
            self.LARGEUR_MUR = 2

        if labyrinthe == None:
            if niveau == 0:
                if difficulte == BEGINNER :
                    self.CASES_X = 20
                    self.CASES_Y = 20
                    res = True
                    #self.salles=[Patern((8,8),10,10,self.LARGEUR_CASE,self.LARGEUR_MUR)]
                    proba_murs = 0.5
                    self.cases_speciales = []
                elif difficulte == EASY :
                    self.CASES_X = 20
                    self.CASES_Y = 20
                    res = False
                    #self.salles=[Patern((14,14),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR)]
                    proba_murs = 0.4
                    self.cases_speciales = []
                elif difficulte == AVERAGE :
                    self.CASES_X = 40
                    self.CASES_Y = 40
                    res = False
                    #self.salles=[Patern((17,17),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR)]
                    proba_murs = 0.3
                    self.cases_speciales = []
                elif difficulte == HARD :
                    self.CASES_X = 60
                    self.CASES_Y = 60
                    res = False
                    #self.salles=[Patern((10,29),40,2,self.LARGEUR_CASE,self.LARGEUR_MUR,[])]
                    #on génère les entrées de manière a avoir un espace ouvert
                    #self.salles[0].pre_gen_entrees_x(0,0,39)
                    #self.salles[0].pre_gen_entrees_x(1,0,39)
                    proba_murs = 0.2
                    self.cases_speciales = []
                elif difficulte == INSANE :
                    self.CASES_X = 100
                    self.CASES_Y = 100
                    res = False
                    #self.salles=[Patern((49,30),2,40,self.LARGEUR_CASE,self.LARGEUR_MUR)]
                    proba_murs = 0.1
                    self.cases_speciales = []
                elif difficulte == IMPOSSIBLE :
                    self.CASES_X = 1000
                    self.CASES_Y = 1000
                    res = False
                    self.salles=[]
                    proba_murs = 0
                self.teleporteurs = [[ [4,4], Teleporteur_local((10,10),self.LARGEUR_CASE,self.LARGEUR_MUR) ], [ [14,14], Teleporteur_local((0,0),self.LARGEUR_CASE,self.LARGEUR_MUR) ]]
                self.cases_speciales = self.teleporteurs
                self.cases_inaccessibles = []

                self.clees = [Clee((3,3),"goodooKey")]
                
                self.salles=[Patern((0,0),10,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[9,9]],self.clees),Patern((10,10),10,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,0]],self.clees)]
                self.depart = (0,0)
                self.arrivee = (self.CASES_X-1,self.CASES_Y-1)
                #variables correspondants a la largeur et la hauteur du zoom

            elif not(isinstance(niveau,str)) and int(niveau) == niveau:
                self.CASES_X = 20 + 10*int(niveau)
                self.CASES_Y = 20 + 10*int(niveau)
                self.arrivee = (self.CASES_X-1,self.CASES_Y-1)
                self.depart = (0,0)
                res = False
                self.clees = []
                self.salles = [Patern((0,0),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,3]]),Patern((self.CASES_X-5,self.CASES_Y-5),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,1]])]
                proba_murs = 1/(niveau+1)
                self.cases_speciales = []
                self.cases_inaccessibles = []

            elif niveau == "tuto1":
                self.CASES_X = 15
                self.CASES_Y = 3
                self.arrivee = (14,1)
                self.depart = (1,1)
                res = False
                self.clees = []
                self.salles = [Patern((0,0),14,3,self.LARGEUR_CASE,self.LARGEUR_MUR,[])]
                proba_murs = 1
                self.teleporteurs = [[(13,1),Teleporteur_global((0,0),"tuto2",self.LARGEUR_CASE,self.LARGEUR_MUR,False,(255,255,255))]]
                self.cases_speciales = self.teleporteurs
                self.cases_inaccessibles = []
                
            elif niveau == "tuto2":
                #niveau labyrinthique sans monstres pour apprendre à se déplacer

                self.CASES_X = 40
                self.CASES_Y = 40
                self.arrivee = (39,39)
                self.depart = (0,0)
                res = False
                self.clees = [Clee((1,1),"Nord"),Clee((3,18),"Ouest"),Clee((5,35),"Est"),Clee((35,18),"Sud")]
                self.salles=[Patern((0,0),20,20,self.LARGEUR_CASE,self.LARGEUR_MUR,[[15,19],[16,19],[17,19],[18,19],[19,19],[19,18],[19,17],[19,16],[19,15]],[],False),Patern((20,20),20,20,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,0],[3,0],[2,0],[1,0],[0,0],[0,1],[0,2],[0,3],[0,4]],[],False),Patern((0,0),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,3]]),Patern((15,15),10,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,1],[0,8],[9,1],[9,8]],self.clees)]
                self.clee_bonus_1 = Clee((19,1),"Bonus_1")
                proba_murs = 0.1
                self.teleporteurs = [[(39,39),Teleporteur_global([5,0],"tuto3",self.LARGEUR_CASE,self.LARGEUR_MUR,False,ARRIVEE)]]
                self.cases_speciales = self.teleporteurs
                self.cases_inaccessibles = []

            elif niveau == "tuto3":
                #niveau monstrueux sans trop de labyrinthe pour apprendre à se battre

                self.CASES_X = 10
                self.CASES_Y = 60
                self.arrivee = (5,59)
                self.depart = (5,0)
                res = False
                self.clees = [Clee((0,59),"Bonus_2")]
                self.salles=[Patern((4,0),2,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,9],[1,9]]),Patern((1,13),8,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,0],[5,7]]),Patern((1,25),6,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,0],[5,7]]),Patern((2,40),8,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,0],[5,7]]),Patern((4,52),5,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,0]]),Patern((0,0),4,4,self.LARGEUR_CASE,self.LARGEUR_MUR,[[2,3]],[Clee(None,"Bonus_1")])]
                proba_murs = 0.3
                self.teleporteurs = [[(5,59),Teleporteur_global([5,0],"tuto4",self.LARGEUR_CASE,self.LARGEUR_MUR,False,ARRIVEE)]]
                self.cases_speciales = self.teleporteurs
                self.cases_inaccessibles = []

            elif niveau == "tuto4":
                #niveau monstrueux sans labyrinthe pour apprendre à se battre

                self.CASES_X = 10
                self.CASES_Y = 60
                self.arrivee = (5,59)
                self.depart = (5,0)
                res = False
                self.clees = [Clee((0,59),"Bonus_3")]
                self.salles=[Patern((4,0),2,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,9],[1,9]]),Patern((1,13),8,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,0],[5,7]]),Patern((1,25),6,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,0],[5,7]]),Patern((2,40),8,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,0],[5,7]]),Patern((4,52),5,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,0]]),Patern((0,56),4,4,self.LARGEUR_CASE,self.LARGEUR_MUR,[]),Patern((0,52),4,4,self.LARGEUR_CASE,self.LARGEUR_MUR,[[1,0],[2,3]],[Clee(None,"Bonus_2"),Clee(None,"Bonus_1")])]
                proba_murs = 0.2
                self.teleporteurs = [[(5,59),Teleporteur_global([1,2],"tuto5",self.LARGEUR_CASE,self.LARGEUR_MUR,False,ARRIVEE)]]
                self.cases_speciales = self.teleporteurs
                self.cases_inaccessibles = []

            elif niveau == "tuto5":
                #niveau monstrueux sans labyrinthe pour apprendre à se battre contre des meutes

                self.CASES_X = 16
                self.CASES_Y = 16
                self.arrivee = (13,14)
                self.depart = (1,2)
                res = False
                self.salles=[Patern((0,0),16,16,self.LARGEUR_CASE,self.LARGEUR_MUR,[]),Patern((0,1),3,15,self.LARGEUR_CASE,self.LARGEUR_MUR,[[1,0],[2,13]],[Clee(None,"Bonus_3")]),Patern((3,1),3,15,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,13],[2,1]]),Patern((6,1),3,15,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,1],[2,13]]),Patern((9,1),3,15,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,13],[2,1]]),Patern((12,1),3,15,self.LARGEUR_CASE,self.LARGEUR_MUR,[[2,13],[0,1]],[Clee(None,"Bonus_3")])]
                proba_murs = 0
                self.teleporteurs = [[(13,14),Teleporteur_global([0,0],"tuto6",self.LARGEUR_CASE,self.LARGEUR_MUR,False,ARRIVEE)]]
                self.cases_speciales = self.teleporteurs
                self.cases_inaccessibles = []

            elif niveau == "tuto6":
                #niveau avec labyrinthe et montres pour apprendre l'utilité des potions

                self.CASES_X = 40
                self.CASES_Y = 40
                self.arrivee = (39,39)
                self.depart = (0,0)
                res = False
                self.clees = [Clee((3,38),"Porte_1_niveau_6_tutoriel"),Clee((37,4),"Porte_2_niveau_6_tutoriel"),Clee((25,7),"Porte_3_niveau_6_tutoriel"),Clee((8,22),"Porte_4_niveau_6_tutoriel"),Clee((17,38),"Porte_5_niveau_6_tutoriel"),Clee((38,13),"Porte_6_niveau_6_tutoriel"),Clee((21,22),"Porte_7_niveau_6_tutoriel"),Clee((17,23),"Porte_8_niveau_6_tutoriel")]
                self.salles=[Patern((0,0),11,11,self.LARGEUR_CASE,self.LARGEUR_MUR,[[10,1]]),Patern((0,30),10,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[8,0],[9,0],[9,1]]),Patern((8,27),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR,[[3,0],[0,4]],[Clee(None,"Bonus_2"),Clee(None,"Bonus_3")]),Patern((30,0),10,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,8],[0,9],[1,9]]),Patern((27,8),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR,[[3,4],[4,0]],[Clee(None,"Bonus_1"),Clee(None,"Bonus_3")]),Patern((35,35),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,4],[0,3],[0,2],[0,1],[1,0],[2,0],[3,0],[4,0]],self.clees),Patern((24,5),3,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[1,9]]),Patern((5,19),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR,[[2,0]]),Patern((15,35),10,5,self.LARGEUR_CASE,self.LARGEUR_MUR,[[5,0]],[Clee(None,"Porte_7_niveau_6_tutoriel")]),Patern((35,15),5,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,5]],[Clee(None,"Porte_3_niveau_6_tutoriel")])]
                self.clees = self.clees + [Clee((5,6),"Bonus_4"),Clee((28,37),"Bonus_5"),Clee((38,17),"Bonus_6")]
                proba_murs = 0.2
                self.teleporteurs = [[(39,39),Teleporteur_global([20,20],"tuto7",self.LARGEUR_CASE,self.LARGEUR_MUR,False,ARRIVEE)]]
                self.cases_speciales = self.teleporteurs
                self.cases_inaccessibles = []

            elif niveau == "tuto7":
                #niveau téléportation (et pièges)

                self.CASES_X = 40
                self.CASES_Y = 40
                self.arrivee = (0,0)
                self.depart = (20,20)
                res = False
                self.clees = []
                self.salles = [Patern((16,16),8,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[]),Patern((0,0),16,9,self.LARGEUR_CASE,self.LARGEUR_MUR,[[1,8]],[Clee((None),"Cheat code")],False),Patern((5,6),8,24,self.LARGEUR_CASE,self.LARGEUR_MUR,[]),Patern((12,3),10,9,self.LARGEUR_CASE,self.LARGEUR_MUR,[]),Patern((8,4),7,7,self.LARGEUR_CASE,self.LARGEUR_MUR,[]),Patern((9,16),4,16,self.LARGEUR_CASE,self.LARGEUR_MUR,[]),Patern((17,27),15,2,self.LARGEUR_CASE,self.LARGEUR_MUR,[]),Patern((15,30),1,2,self.LARGEUR_CASE,self.LARGEUR_MUR,[]),Patern((32,25),6,6,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,2],[0,3]]),Patern((14,25),3,5,self.LARGEUR_CASE,self.LARGEUR_MUR,[[2,2],[2,3],[1,4]]),Patern((14,32),4,4,self.LARGEUR_CASE,self.LARGEUR_MUR,[[1,0]]),Patern((2,31),6,6,self.LARGEUR_CASE,self.LARGEUR_MUR,[]),Patern((20,30),8,6,self.LARGEUR_CASE,self.LARGEUR_MUR,[]),Patern((26,3),10,21,self.LARGEUR_CASE,self.LARGEUR_MUR,[])]
                proba_murs = 0.3
                self.teleporteurs_officiels = [[(0,0),Teleporteur_global([0,0],"tuto8",self.LARGEUR_CASE,self.LARGEUR_MUR,False,ARRIVEE)],[(23,23),Teleporteur_local([39,39],self.LARGEUR_CASE,self.LARGEUR_MUR,True)],[(23,16),Teleporteur_local([26,23],self.LARGEUR_CASE,self.LARGEUR_MUR,True)],[(28,23),Teleporteur_local((20,20),self.LARGEUR_CASE,self.LARGEUR_MUR,True)],[(16,16),Teleporteur_local((12,3),self.LARGEUR_CASE,self.LARGEUR_MUR,True)],[(12,11),Teleporteur_local((10,13),self.LARGEUR_CASE,self.LARGEUR_MUR,True)],[(5,29),Teleporteur_local((2,36),self.LARGEUR_CASE,self.LARGEUR_MUR,True)],[(7,31),Teleporteur_local((27,35),self.LARGEUR_CASE,self.LARGEUR_MUR,True)],[(20,30),Teleporteur_local((20,20),self.LARGEUR_CASE,self.LARGEUR_MUR,True)],[(16,23),Teleporteur_local((10,16),self.LARGEUR_CASE,self.LARGEUR_MUR,True)],[(11,31),Teleporteur_local((8,4),self.LARGEUR_CASE,self.LARGEUR_MUR,True)],[(8,10),Teleporteur_local((37,27),self.LARGEUR_CASE,self.LARGEUR_MUR,True)],[(14,35),Teleporteur_local((20,20),self.LARGEUR_CASE,self.LARGEUR_MUR,True)],[(14,13),Teleporteur_local((15,0),self.LARGEUR_CASE,self.LARGEUR_MUR,True)]]
                self.teleporteurs_officieux = [[(32,35),Teleporteur_local([20,20],self.LARGEUR_CASE,self.LARGEUR_MUR,True,(255,255,255))],[(11,35),Teleporteur_local((20,20),self.LARGEUR_CASE,self.LARGEUR_MUR,True,(255,255,255))],[(2,12),Teleporteur_local((20,20),self.LARGEUR_CASE,self.LARGEUR_MUR,True,(255,255,255))],[(3,6),Teleporteur_local([20,20],self.LARGEUR_CASE,self.LARGEUR_MUR,True,(255,255,255))]]
                self.fontaines = [[(21,23),Fontaine_heal(self.LARGEUR_CASE,self.LARGEUR_MUR,0,False,(20,20,125))]]
                self.cases_speciales = self.teleporteurs_officiels + self.teleporteurs_officieux + self.fontaines
                self.cases_inaccessibles = [(39,39),(26,23),(26,22),(27,22),(27,23),(12,3),(13,3),(14,3),(10,13),(11,13),(9,13),(10,12),(11,12),(9,12),(10,14),(9,14),(11,14),(27,35),(26,35),(27,34),(26,34),(10,16),(9,16),(11,16),(10,17),(9,17),(11,17),(8,4),(9,4),(8,5),(9,5),(37,27),(37,28),(37,26),(36,27),(36,28),(36,26)]
            
            elif niveau == "tuto8":
                #fin du tuto
                self.CASES_X = 4
                self.CASES_Y = 4
                self.arrivee = (3,3)
                self.depart = (0,0)
                res = False
                self.clees = []
                self.salles = [Patern((0,0),4,4,self.LARGEUR_CASE,self.LARGEUR_MUR,[])]
                proba_murs = 0
                self.cases_speciales = []
                self.cases_inaccessibles = []

            elif niveau == "demo":
                self.CASES_X = 20
                self.CASES_Y = 20
                self.arrivee = (19,0)
                self.depart = (0,0)
                res = False
                self.clees = [Clee((4,4),"Demo")]
                self.salles = [Patern((10,10),10,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[7,0],[0,1]],[],False),Patern((15,10),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR,[[2,4],[2,0]],self.clees),Patern((15,0),5,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[2,9]],self.clees),Patern((0,10),10,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[9,1],[0,0]],self.clees),Patern((0,5),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,4],[4,0]],self.clees),Patern((1,6),4,1,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,0]]),Patern((1,8),4,1,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,0]]),Patern((5,0),10,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,5],[0,2]],[],False),Patern((0,0),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,2]],self.clees)]
                proba_murs = 0.2
                self.teleporteurs = [[(14,9),Teleporteur_local([4,5],self.LARGEUR_CASE,self.LARGEUR_MUR)]]
                self.pieges = [[(i,j),Piques(self.LARGEUR_CASE,self.LARGEUR_MUR,6,False,(0,0,0))] for i in range(15,20) for j in range(2,8)]
                self.pieges[15] = [self.pieges[15][0],Fontaine_heal(self.LARGEUR_CASE,self.LARGEUR_MUR,0,False,(20,20,125))]
                self.cases_speciales = self.pieges + self.teleporteurs
                self.cases_inaccessibles = []
            
            self.poids=[6,2,1,2]
            #génération du labyrinthe
            self.lab=Labyrinthe(self.CASES_X,self.CASES_Y,self.arrivee,self.depart,self.LARGEUR_CASE,self.LARGEUR_MUR,self.poids,self.salles,self.cases_speciales,self.cases_inaccessibles)
            self.lab.generation(None,proba_murs,None,None)
            

        else:
            self.lab = labyrinthe
            self.arrivee = self.lab.arrivee
            self.depart = self.lab.depart
        #test pour les portes fermantees
        if niveau == 0:
            self.lab.getMatrice_cases()[9][9].get_murs()[BAS] = Porte(self.LARGEUR_MUR,"goodooKey",True)
            self.lab.getMatrice_cases()[9][10].get_murs()[HAUT] = Porte(self.LARGEUR_MUR,"goodooKey",True)
        elif niveau == "demo":
            self.lab.getMatrice_cases()[4][5].get_murs()[DROITE].set_etat(MUR_PLEIN)
            self.lab.getMatrice_cases()[5][5].get_murs()[GAUCHE].set_etat(MUR_PLEIN)

        if destination != None:
            minimap = Minimap(self.lab.getMatrice_cases(),mode_minimap,self.depart,self.arrivee)
            self.joueur = joueur
            self.joueur.minimap = minimap
        elif joueur == None:
            if niveau == 0:
                inventaire_joueur = Inventaire()
            elif not(isinstance(niveau,str)) and int(niveau) == niveau:
                inventaire_joueur = Inventaire()
            elif niveau == "tuto1":
                inventaire_joueur = Inventaire([Clee(None,"Premier pas")])
            elif niveau == "tuto2":
                inventaire_joueur = Inventaire()
            elif niveau == "tuto3":
                inventaire_joueur = Inventaire([Clee(None,"Bonus_1")])
            elif niveau == "tuto4":
                inventaire_joueur = Inventaire([Clee(None,"Bonus_1"),Clee(None,"Bonus_2")])
            elif niveau == "tuto5":
                inventaire_joueur = Inventaire([Clee(None,"Bonus_1"),Clee(None,"Bonus_2"),Clee(None,"Bonus_3")])
            elif niveau == "tuto6":
                inventaire_joueur = Inventaire([Clee(None,"Bonus_1"),Clee(None,"Bonus_2"),Clee(None,"Bonus_3")])
            elif niveau == "tuto7":
                inventaire_joueur = Inventaire([Clee(None,"Bonus_1"),Clee(None,"Bonus_2"),Clee(None,"Bonus_3")])
            elif niveau == "tuto8":
                inventaire_joueur = Inventaire()
            elif niveau == "demo":
                inventaire_joueur = Inventaire([Clee(None,"Clee_bidon")])
                
            self.force_joueur = 10
            self.hp_joueur = 200
            self.mana_joueur = 50
            self.vitesse_joueur_lab=4
            self.vitesse_joueur_autres=12
            minimap = Minimap(self.lab.getMatrice_cases(),mode_minimap,self.depart,self.arrivee)

            #variables correspondants a la largeur et la hauteur du zoom
            self.zoom_largeur=13
            self.zoom_hauteur=13

            self.joueur=Joueur(minimap,inventaire_joueur,self.hp_joueur,self.hp_joueur,self.mana_joueur,self.force_joueur,self.vitesse_joueur_lab,self.vitesse_joueur_autres,2,self.zoom_largeur,self.zoom_hauteur,self.depart)
            
        elif debut_niveau:
            minimap = Minimap(self.lab.getMatrice_cases(),mode_minimap,self.depart,self.arrivee)
            self.joueur = Joueur(minimap,joueur.inventaire,joueur.pv_max,joueur.pv_max,joueur.mana_max,joueur.degats,joueur.vitesse_lab,joueur.vitesse_autres,joueur.radius,joueur.largeur_vue,joueur.hauteur_vue,self.depart)
            self.joueur.mana = joueur.mana
            self.joueur.regeneration = joueur.regeneration

        else:
            self.joueur = joueur

        #on récupère une copie du joueur ou cas ou il perd
        self.precedent_joueur = self.joueur.getCopie()


        if entitees == None:

            if niveau == 0:
                
                self.vitesse_montres=20
            
                monstres=[]

                self.entitees = self.clees

                #pnj d'expérimentation
                self.pnj = Pnj_passif([5,5],100,(125,255,125),[Replique(["Teswwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwt"],20)])
                self.entitees.append(self.pnj)

                potions_vue=[Potion_de_vision((35,26),self.joueur),Potion_de_vision((27,38),self.joueur),Potion_de_vision((21,19),self.joueur),Potion_de_visibilite_permanente((8,7),self.joueur)]
                potions_combat=[Potion_de_force((i,j),self.joueur)for j in range(5,45,10) for i in range(5,45,10)] + [Potion_de_portee((i,j),self.joueur)for j in range (10,40,10) for i in range (10,40,10)] + [Potion_de_soin((20,20),self.joueur),Potion_de_portee_permanente((2,2),self.joueur)]
                potions=potions_vue+potions_combat
                for potion in potions:
                    self.entitees.append(potion)
                #on place les indices
                positions = self.lab.petit_poucet(20)
                for position in positions:
                    self.entitees.append(Caillou(position))

            elif not(isinstance(niveau,str)) and int(niveau) == niveau:
                self.vitesse_monstres=20

                easy_drops = [Potion_de_force,Potion_de_vision,Potion_de_portee]
                hard_drops = [Potion_de_force_permanente,Potion_de_visibilite_permanente,Potion_de_portee_permanente,Potion_de_soin_permanente]
                self.drops = []
                for i in range(niveau):
                    self.drops.append(easy_drops[random.randrange(0,3)](None,self.joueur))
                self.drops.append(Potion_de_soin(None,self.joueur))
                monstres=self.spawn_aleatoire(Fatti,10,10,200,20,20,1,((10,10),(self.CASES_X-10,self.CASES_Y-10)),min(0.02*niveau,0.15),niveau,0,(0,0,100),self.drops + [hard_drops[random.randrange(0,4)](None,self.joueur)])

                if niveau > 8:
                    self.drops = []
                    for i in range(niveau):
                        self.drops.append(easy_drops[random.randrange(0,3)](None,self.joueur))
                    self.drops.append(Potion_de_soin(None,self.joueur))
                    monstres_1=self.spawn_aleatoire(Slime,5,5,50,3,6,1,((20,20),(self.CASES_X-20,self.CASES_Y-20)),min(0.04*niveau,0.5),niveau,0,(0,0,100),self.drops + [hard_drops[random.randrange(0,4)](None,self.joueur)])
                    monstres = monstres + monstres_1

                if niveau > 14:
                    self.drops = []
                    for i in range(niveau):
                        self.drops.append(easy_drops[random.randrange(0,3)](None,self.joueur))
                    self.drops.append(Potion_de_soin(None,self.joueur))
                    monstres_1=self.spawn_aleatoire(Runner,15,15,75,10,10,1,((25,25),(self.CASES_X-25,self.CASES_Y-25)),min(0.01*niveau,0.25),niveau,0,(255,0,0),self.drops + [hard_drops[random.randrange(0,4)](None,self.joueur)])
                    monstres = monstres + monstres_1
                
                self.entitees=self.clees

            elif niveau == "tuto1":
                self.vitesse_monstres=20

                monstres=[]
                self.entitees=self.clees

                self.pnj = Pnj_passif((1,0),1000,(125,255,125),[Replique(["Tu as déjà découvert comment te déplacer ?","Essaies les touches directionnelles !"],20),Replique(["Tu devrais chercher la sortie de cette grotte.","La porte au bout du couloir me semble","suspecte."],20)])
                self.entitees.append(self.pnj)

            elif niveau == "tuto2":

                self.vitesse_montres=20

                monstres=[]
                self.entitees=self.clees

                self.pnj = Pnj_passif((2,3),1000,(190,255,56),[Replique(["J'ai peur j'ai peur j'ai peur !","J'ai peeeeuuurrr ! ! !"],20),Replique(["Cet endroit est horrible ! Je veux remonter à","la surface, mais avec ce labyrinthe je risque","de me perdre, ce serait terrible !"],20),Replique(["Quelqu'un est passé avant, il a dit que la","sortie était en bas à droite et qu'il avait laissé","des cailloux sur le chemin, mais je n'ose","pas y aller..."],20),Replique(["Je crois aussi qu'il a parlé de clées, je crois","qu'il faut les trouver pour ouvrir des portes."],20),Replique(["L'une d'elle est sur la case de coordonnées","(19,1), mais je ne sais pas ce que ça veut","dire..."],20),Replique(["Oooh! Tu fais une carte au fur et à mesure de","tes déplacements ? Appuie sur A pour la","consulter."],20),Replique(["Tu veux bien cartographier tout le niveau et","revenir me voir ? Avec ça, je serais plus","rassuré."],20)])
                self.entitees.append(self.pnj)
                
                self.cailloux_1 = []
                positions = self.lab.petit_poucet(5,self.clees[0].position,(14,16))
                for position in positions:
                    self.cailloux_1.append(Caillou(position))

                self.cailloux_2 = []
                positions = self.lab.petit_poucet(5,(14,16),self.clees[1].position)
                for position in positions:
                    self.cailloux_2.append(Caillou(position))

                self.cailloux_3 = []
                positions = self.lab.petit_poucet(5,self.clees[1].position,self.clees[2].position)
                for position in positions:
                    self.cailloux_3.append(Caillou(position))

                self.cailloux_4 = []
                positions = self.lab.petit_poucet(5,self.clees[2].position,self.clees[3].position)
                for position in positions:
                    self.cailloux_4.append(Caillou(position))

                self.cailloux_5 = []
                positions = self.lab.petit_poucet(5,self.clees[3].position)
                for position in positions:
                    self.cailloux_5.append(Caillou(position))
                    
            elif niveau == "tuto3":

                self.vitesse_montres=20

                monstres=[Fatti([5,17]),Fatti([5,28]),Fatti([3,43]),Fatti([5,59])]
                self.entitees=self.clees

                self.pnj = Pnj_passif((5,3),1,(56,255,190),[Replique(["Bonjour ! Fais très attention, il y des","monstres là-bas. Heureusement que je","cours plus vite qu'eux !"],20),Replique(["Ces labyrinthes sont ridiculement faciles,","seul un idiot s'y perdrait, mais les monstres","sont dangeureux !"],20),Replique(["Tu peux attaquer les monstres avec la","touche espace, mais ne fait pas ça trop près","de moi. C'est une attaque de zone qui me","tuerait aussi."],20),Replique(["Je peux voir tes armes ? Mais tu as une","lance ! Utilise les touches WASD pour une","attaque plus puissante dans la direction de","ton choix."],20),Replique(["Tu peux essayer d'éviter les monstres en","les coutournant, car ceux-ci ont une moins","bonne vue que toi, mais je préférerais que","tu les tues tous. Tu veux bien ?"],20)])
                self.entitees.append(self.pnj)

                self.pnj_bonus = Pnj_passif((0,2),100,(0,255,125),[Replique(["Qu'est-ce que tu fais là ? Personne ne vient","jamais ici d'habitude !"],20),Replique(["Mais tu as raison. Il faut toujours explorer","tout le labyrinthe, écouter toutes les","répliques de tous les PNJs, ne rien négliger."],20),Replique(["C'est le seul moyen de gagner..."],20)])
                self.entitees.append(self.pnj_bonus)
                
                positions = self.lab.petit_poucet(6,self.depart,self.arrivee)
                for position in positions:
                    self.entitees.append(Caillou(position))

            elif niveau == "tuto4":

                self.vitesse_montres=20

                monstres=[Slime([5,17]),Fatti([8,25]),Runner(self.lab.getMatrice_cases(),5,59,[3,48]),Fatti([5,59])]
                self.entitees=self.clees

                self.pnj = Pnj_passif((5,3),1,(56,255,190),[Replique(["Eh bah, je suis contente d'avoir survécu."],20),Replique(["Ici, les monstres sont différents. Tu devrais","aller voir chaque salle puis revenir pour que","je t'explique."],20),Replique(["Tu as vu le premier ? C'est un slime !","Il est faible, ne voit pas très loin, se déplace","au hasard pour te trouver et agit très vite."],20),Replique(["Tu as vu le monstre suivant ? C'est un fatti.","Il est lent et ne bouge pas tant qu'il ne","t'a pas repéré, mais il est très fort."],20),Replique(["La salle suivante est vide ? Normal, elle était","habitée par un runner. Il s'est précipité","jusqu'à la sortie pour t'attendre."],20),Replique(["Un fatti sur la sortie et un runner juste à côté,","voilà un combo qui les rend très dangereux."],20)])
                self.entitees.append(self.pnj)

                positions = self.lab.petit_poucet(7,self.depart,self.arrivee)
                for position in positions:
                    self.entitees.append(Caillou(position))

            elif niveau == "tuto5":

                self.vitesse_montres=20

                meute1 = [Fatti([1,6],1),Fatti([2,13],1),Fatti([0,13],1),Fatti([1,14],1)]
                meute2 = [Slime([4,1],2),Slime([3,2],2),Slime([5,2],2),Slime([4,1],2),Slime([3,4],2),Slime([5,4],2),Slime([4,5],2),Slime([3,6],2),Slime([5,6],2),Slime([4,7],2),Slime([3,8],2),Slime([5,8],2),Slime([4,9],2)]
                meute3 = [Slime([7,9],3),Slime([8,10],3),Slime([6,10],3),Fatti([6,12],3),Fatti([7,12],3),Fatti([8,12],3)]
                meute4 = [Slime([10,6],4),Slime([10,7],4),Slime([10,8],4),Slime([10,9],4),Slime([10,10],4),Slime([10,11],4),Fatti([10,3],4,10,10,300,30)]
                meute5 = [Slime([13,9],5),Slime([14,10],5),Slime([12,10],5),Fatti([12,12],5),Fatti([13,12],5),Fatti([14,12],5),Runner(self.lab.getMatrice_cases(),self.CASES_X-1,self.CASES_Y-1,[12,6]),Runner(self.lab.getMatrice_cases(),self.CASES_X-1,self.CASES_Y-1,[13,1]),Runner(self.lab.getMatrice_cases(),self.CASES_X-1,self.CASES_Y-1,[14,6])]
                monstres = meute1
                for meutenumerote in [meute2,meute3,meute4,meute5]:
                    for monstre in meutenumerote:
                        monstres.append(monstre)

                self.pnj = Pnj_passif((2,2),1,(56,255,190),[Replique(["Le comportement de ces monstres est","étrange, c'est comme s'ils communiquaient !"],20),Replique(["Tu vois les trois que tu ne voyais pas au","départ ? Ils ne te voyaient pas non plus,","pourtant ils savaient que tu étais là et ils","sont venus."],20),Replique(["C'est probablement l'autre qui te voyait qui","leur a révélé ta position !"],20),Replique(["D'ailleurs, as-tu remarqué que tu ne peux ni","te battre, ni te déplacer quand tu parles à","quelqu'un ?"],20)])
                self.entitees=[self.pnj]

                positions = self.lab.petit_poucet(8,self.depart,self.arrivee)
                for position in positions:
                    self.entitees.append(Caillou(position))

            elif niveau == "tuto6":

                self.vitesse_montres=20

                fattis=self.spawn_aleatoire(Fatti,10,10,200,20,20,1,((10,10),(30,30)),0.05,5,0,(0,0,100),[Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_vision(None,self.joueur),Potion_de_vision(None,self.joueur),Potion_de_vision(None,self.joueur),Potion_de_vision(None,self.joueur),Potion_de_vision(None,self.joueur),Potion_de_vision(None,self.joueur),Potion_de_vision(None,self.joueur)])
                slimes=self.spawn_aleatoire(Slime,5,5,50,3,6,1,((15,15),(25,25)),0.15,5,0,(255,100,100),[Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_vision(None,self.joueur),Potion_de_vision(None,self.joueur),Potion_de_vision(None,self.joueur),Potion_de_vision(None,self.joueur),Potion_de_vision(None,self.joueur)])

                potions_vue=[Potion_de_vision((35,26),self.joueur),Potion_de_vision((27,38),self.joueur),Potion_de_vision((21,19),self.joueur)]
                potions_combat=[Potion_de_force((i,j),self.joueur)for j in range(5,45,10) for i in range(5,45,10)] + [Potion_de_portee((i,j),self.joueur)for j in range (10,40,10) for i in range (10,40,10)]
                potions_bonus=[Potion_de_visibilite_permanente((8,23),self.joueur),Potion_de_visibilite_permanente((8,31),self.joueur),Potion_de_portee_permanente((23,37),self.joueur),Potion_de_portee_permanente((7,35),self.joueur),Potion_de_force_permanente((24,13),self.joueur),Potion_de_force_permanente((32,2),self.joueur),Potion_de_soin_permanente((39,0),self.joueur),Potion_de_soin_permanente((37,16),self.joueur),Potion_de_soin((20,20),self.joueur),Potion_de_soin((35,5),self.joueur),Potion_de_soin((5,35),self.joueur)]
                potions=potions_vue+potions_combat+potions_bonus

                self.pnj = Pnj_passif((3,4),250,(255,200,20),[Replique(["Malheureux ! Jamais tu ne sortiras d'ici","vivant !"],20),Replique(["Moi-même, qui ait atteint le plus haut niveau","qu'un mage puisse atteindre, j'ai été forcé de","fuir face au boss final qui garde la sortie !"],20),Replique(["Mes potions me permettent d'annihiler tous","les monstres sur mon passage, de voir au","travers des murs de ces labyrinthes et","même de les briser !"],20),Replique(["Mais elles n'ont pas suffit face à lui..."],20),Replique(["Le plus terrible, c'est que j'ai perdu mes","potions dans ma fuite, et qu'elles sont","dispersées dans les labyrinthes. Si tu me","les ramènes, je te remercierais !"],20),Replique(["Hélas, je n'ai pas assez pour racheter les","potions permanentes, ce sont de vrais","trésors qui coutent une fortune. Si tu en","trouve, tu peux les garder."],20),Replique(["D'ailleurs, garde toutes les potions si ça","peut te permettre d'éliminer le boss final","une bonne fois pour toute."],20),Replique(["Certain de ces monstres ont récupéré mes","potions. Elimine-les, s'il te plait."],20)])
                self.entitees=potions+self.clees
                self.entitees.append(self.pnj)
                monstres = fattis + slimes

                positions = self.lab.petit_poucet(9,self.depart,self.arrivee)
                for position in positions:
                    self.entitees.append(Caillou(position))

            elif niveau == "tuto7":

                self.vitesse_monstres=20

                equipe_1 = self.spawn_aleatoire(Fatti,10,10,200,20,20,1,((5,6),(7,29)),0.05,1,0,(0,0,100),[Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur)])
                equipe_2_fatti = self.spawn_aleatoire(Fatti,10,10,200,20,20,1,((26,3),(35,23)),0.05,1,0,(0,0,100),[Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur)])
                equipe_2_slime = self.spawn_aleatoire(Slime,5,5,50,3,6,1,((26,3),(35,23)),0.15,1,0,(255,100,100),[Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur)])
                equipe_2 = equipe_2_fatti + equipe_2_slime
                equipe_3_fatti = self.spawn_aleatoire(Fatti,10,10,200,20,20,1,((15,6),(21,11)),0.05,1,0,(0,0,100),[Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur)])
                equipe_3_slime = self.spawn_aleatoire(Slime,5,5,50,3,6,1,((16,4),(21,11)),0.15,1,0,(255,100,100),[Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur)])
                equipe_3 = equipe_3_fatti + equipe_3_slime
                equipe_4_fatti = self.spawn_aleatoire(Fatti,10,10,200,20,20,1,((20,30),(26,34)),0.05,1,0,(0,0,100),[Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur)])
                equipe_4_slime = self.spawn_aleatoire(Slime,5,5,50,3,6,1,((20,30),(26,34)),0.15,1,0,(255,100,100),[Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur)])
                equipe_4 = equipe_4_fatti + equipe_4_slime
                equipe_5_fatti = self.spawn_aleatoire(Fatti,10,10,200,20,20,1,((0,9),(4,30)),0.05,1,0,(0,0,100),[Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur)])
                equipe_5_slime = self.spawn_aleatoire(Slime,5,5,50,3,6,1,((0,9),(4,30)),0.15,1,0,(255,100,100),[Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur)])
                equipe_5 = equipe_5_fatti + equipe_5_slime
                equipe_6_fatti = self.spawn_aleatoire(Fatti,10,10,200,20,20,1,((13,12),(25,15)),0.04,1,0,(0,0,100),[Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur)])
                equipe_6_slime = self.spawn_aleatoire(Slime,5,5,50,3,6,1,((13,12),(25,15)),0.12,1,0,(255,100,100),[Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur)])
                equipe_6 = equipe_6_fatti + equipe_6_slime
                equipe_7_fatti = self.spawn_aleatoire(Fatti,10,10,200,20,20,1,((8,32),(13,37)),0.05,1,0,(0,0,100),[Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur)])
                equipe_7_slime = self.spawn_aleatoire(Slime,5,5,50,3,6,1,((8,32),(13,37)),0.15,1,0,(255,100,100),[Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur)])
                equipe_7 = equipe_7_fatti + equipe_7_slime
                equipe_8_fatti = self.spawn_aleatoire(Fatti,10,10,200,20,20,1,((36,0),(39,24)),0.05,1,0,(0,0,100),[Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur)])
                equipe_8_slime = self.spawn_aleatoire(Slime,5,5,50,3,6,1,((36,0),(39,24)),0.15,1,0,(255,100,100),[Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur)])
                equipe_8 = equipe_8_fatti + equipe_8_slime
                equipe_9 = self.spawn_aleatoire(Slime,5,5,50,3,6,1,((14,25),(16,29)),1,15,0,(255,100,100),[Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur)])
                equipe_10 = self.spawn_aleatoire(Slime,5,5,50,3,6,1,((9,16),(13,31)),0.15,1,0,(255,100,100),[Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_force(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur),Potion_de_portee(None,self.joueur)])
                
                
                self.pnj = Pnj_passif((21,20),250,(255,200,20),[Replique(["Tu vois ces cases bleues autour de toi ?","Mais non, il n'y a pas plusieurs sorties,","ce sont des téléporteurs."],20),Replique(["J'en ai placé de partout pour échapper aux","monstres. Tu peux les utiliser, mais","pas eux."],20),Replique(["Fais attention, il y a aussi des pièges. Ce","n'est pas moi qui les ai placés..."],20),Replique(["Essaye d'emprunter le téléporteur en haut à","droite. De toute façon, tu devras bien","le faire un jour pour sortir d'ici."],20)])
                monstres = equipe_1 + equipe_2 + equipe_3 + equipe_4 + equipe_5 + equipe_6 + equipe_7 + equipe_8 + equipe_9 + equipe_10
                self.entitees=[]
                self.entitees.append(self.pnj)

            elif niveau == "tuto8":

                monstres = []
                self.entitees = [Pnj_passif((2,3),1000,(0,255,125),[Replique(["Tu as terminé le tutoriel.","Bonne chance pour la suite !"],20)])]

            elif niveau == "demo":

                self.pnj = Pnj_passif((16,0),10000000,(125,255,125),[Replique(["Voilà, c'est la fin de notre","démonstration ! Merci","de votre attention !"],20)])
                monstres = [Fatti([7,17]),Runner(self.lab.getMatrice_cases(),19,19,[10,10]),Slime([17,12])]
                self.entitees = self.clees + [Potion_de_vision((2,6),self.joueur),Potion_de_visibilite_permanente((4,6),self.joueur),Potion_de_force((2,7),self.joueur),Potion_de_force_permanente((4,7),self.joueur),Potion_de_portee((2,8),self.joueur),Potion_de_portee_permanente((4,8),self.joueur),Potion_de_soin((2,9),self.joueur),Potion_de_soin_permanente((4,9),self.joueur)]
                self.entitees.append(self.pnj)

            self.monstres = monstres

            self.entitees.append(self.joueur)

            if res :
                self.lab.resolution(self.arrivee[0],self.arrivee[1],self.depart[0],self.depart[1],"Largeur")

            for i in range(0,len(self.monstres)):
                self.entitees.append(self.monstres[i])

            #generation des meutes
            self.meutes=self.generation_meutes()

        else:
            self.entitees = entitees




        if evenements == None:
            self.evenements=[]
        else:
            self.evenements = evenements

        self.missions=[]
        if not(isinstance(niveau,str)) and int(niveau) == niveau:
            self.mission_1 = ["self.mission_monstres()","self.joueur.augmente_regen(0.1),self.ajout(self.missions,[self.mission_1],self.ajout(self.entitees,self.monstres),self.ajout(self.meutes,self.generation_meutes()"]
            self.mission_2 = ["self.mission_minimap()","self.joueur.augmente_pv(5)"]
            
        elif niveau == "tuto2":
            self.mission_1 = ["self.pnj.indice_replique == 3","self.petits_cailloux(5,self.joueur.position,(14,16)),self.ajout(self.missions,[self.mission_2])"]
            self.mission_2 = ["self.lab.matrice_cases[14][16].murs[DROITE].etat == MUR_VIDE","self.petits_cailloux(5,self.joueur.position,(3,18)),self.ajout(self.missions,[self.mission_3])"]
            self.mission_3 = ["self.mission_clee('Ouest')","self.petits_cailloux(5,self.joueur.position,(5,35)),self.ajout(self.missions,[self.mission_4])"]
            self.mission_4 = ["self.mission_clee('Est')","self.petits_cailloux(5,self.joueur.position,(35,18)),self.ajout(self.missions,[self.mission_5])"]
            self.mission_5 = ["self.mission_clee('Sud')","self.petits_cailloux(5,self.joueur.position,self.arrivee)"]
            self.missions.append(self.mission_1)
            
            self.mission_6 = ["self.pnj.indice_replique == 5","self.ajout(self.entitees,[self.clee_bonus_1])"]
            self.missions.append(self.mission_6)

            self.mission_7 = ["self.pnj.indice_replique == 6","self.ajout(self.missions,[self.mission_8])"]
            self.mission_8 = ["self.mission_minimap()","self.ajout(self.missions,[self.mission_9]),self.ajout(self.pnj.repliques,self.repliques_mission_8)"]
            self.repliques_mission_8 = [Replique(["Oh, merci ! Je vais peut-être trouver le","courage de traverser ce labyrinthe","maintenant !"],20),Replique(["Tu devrais aller à la sortie. C'est une case","bleue, elle doit apparaître sur ta carte","puisque tu l'a vue."],20)]
            self.mission_9 = ["self.pnj.indice_replique == 8","self.joueur.augmente_pv(5)"]
            self.missions.append(self.mission_7)
            
        elif niveau == "tuto3":
            self.mission_1 = ["self.mission_minimap()","self.joueur.augmente_pv(5)"]
            self.missions.append(self.mission_1)

            self.mission_2 = ["self.pnj.indice_replique == 4","self.ajout(self.missions,[self.mission_3])"]
            self.mission_3 = ["self.mission_monstres()","self.ajout(self.pnj.repliques,self.repliques_mission_3),self.ajout(self.missions,[self.mission_4])"]
            self.repliques_mission_3 = [Replique(["Tu les as tous tués ? Merci beaucoup, tu me","sauves la vie !"],20),Replique(["Il n'y a plus de monstres, on peut y aller","maintenant."],20)]
            self.mission_4 = ["self.pnj.indice_replique == 6","self.joueur.augmente_regen(0.1)"]
            self.missions.append(self.mission_2)
            
        elif niveau == "tuto4":
            self.mission_1 = ["self.mission_minimap()","self.joueur.augmente_pv(5)"]
            self.missions.append(self.mission_1)

            self.mission_2 = ["self.mission_monstres()","self.ajout(self.pnj.repliques,self.repliques_mission_2),self.ajout(self.missions,[self.mission_3])"]
            self.repliques_mission_2 = [Replique(["Tu as pensé à tous les tuer sans même que","je te demande ? Comme c'est gentil !"],20),Replique(["Il n'y a plus de monstres, on peut y aller","maintenant."],20)]
            self.mission_3 = ["self.pnj.indice_replique == 7","self.joueur.augmente_regen(0.1)"]
            self.missions.append(self.mission_2)

        elif niveau == "tuto5":
            self.mission_1 = ["self.mission_minimap()","self.joueur.augmente_pv(5)"]
            self.missions.append(self.mission_1)

            self.mission_2 = ["self.mission_monstres()","self.joueur.augmente_regen(0.1)"]
            self.missions.append(self.mission_2)

        elif niveau == "tuto6":
            self.mission_1 = ["self.mission_minimap()","self.joueur.augmente_pv(5)"]
            self.missions.append(self.mission_1)

            self.mission_2 = ["self.mission_monstres()","self.joueur.augmente_regen(0.1)"]
            self.missions.append(self.mission_2)

            self.mission_3 = ["self.mission_drops()","self.joueur.augmente_mana(5)"]
            self.missions.append(self.mission_3)

        elif niveau == "tuto7":
            self.mission_1 = ["self.mission_minimap()","self.joueur.augmente_pv(5)"]
            self.missions.append(self.mission_1)

            self.mission_2 = ["self.mission_monstres()","self.joueur.augmente_regen(0.1)"]
            self.missions.append(self.mission_2)

            self.mission_3 = ["self.mission_drops()","self.joueur.augmente_mana(5)"]
            self.missions.append(self.mission_3)

            self.mission_4 = ["self.mission_position((39,39))","self.ajout(self.pnj.repliques,self.repliques_mission_4)"]
            self.repliques_mission_4 = [Replique("Tu as remarqué ? Il y a des téléporteurs cachés qui te ramènent ici. N'oublie pas leur position si tu ne veux pas te faire avoir à nouveau.",20)]
            self.missions.append(self.mission_4)
            


        if horloge_cycle == None:
            self.horloge_cycle=0
        else:
            self.horloge_cycle = horloge_cycle

        if niveau == "tuto1":
            self.chaine = "Atterrissage difficile !"
        elif niveau == "tuto2":
            self.chaine = "Premiers pas"
        elif niveau == "tuto3":
            self.chaine = "Les attaques"
        elif niveau == "tuto4":
            self.chaine = "Les monstres"
        elif niveau == "tuto5":
            self.chaine = "Les meutes"
        elif niveau == "tuto6":
            self.chaine = "Le magicien"
        elif niveau == "tuto7":
            self.chaine = "Téléportation !"
        elif niveau == "demo":
            self.chaine = "Démonstration"
        else:
            self.chaine = "Niveau " + str(niveau)


        pygame.display.set_caption(self.chaine)
        self.screen = pygame.display.set_mode((FENETRE_X,FENETRE_Y),pygame.RESIZABLE)
        self.screen.fill((0,0,0))

        
        #objet qui traite les collisions
        self.collision=Collision()

        self.plus_lent=self.getPlusLent()
        #variable qui nous sert a exécuter les actions des entitées

        #objet d'affichage
        self.affichage=Affichage(self.screen,self.mode_affichage,self.LARGEUR_CASE,self.LARGEUR_MUR,self.lab.largeur,self.lab.hauteur)

        if niveau == "tuto1":
            self.affichage.affiche = DIALOGUE
            self.affichage.diag_cour = Replique(["Tu va bien ? Quand je t'ai vu tomber de","là-haut j'ai cru que tu allais mourir...","Bon, je te laisse te reposer. N'hésite pas à","revenir me parler avec  la touche x."],20)
            


        #texte de fin
        font = pygame.font.SysFont(None, 72)
        self.textWin = font.render("Vous avez gagné ! ! \(^o^)/", True, (128, 0, 0))
        self.textLose = font.render("Vous avez perdu ! ! ;o;", True, (0, 128, 128))
        self.textTel = font.render("Vous allez être redirigés, veuillez patienter",True, (0,0,0))
        
        self.position_screen=(0,0)

    def sauve(self):
        return [self.niveau,self.difficulte,self.mode_affichage,self.mode_minimap,self.lab.as_gagner(self.joueur.getPosition()) or self.as_perdu(),self.joueur,self.lab,self.entitees,self.evenements,self.horloge_cycle]



    def run(self):
        """
        Boucle principale du niveau
        Sorties:
            -le temps a attendre si le joueur as finit la niveau
            -un booléen indiquant si le joueur a gagné ou perdu
            -le joueur
        """
        run=True
        self.redraw()
        #objet qui permet de gérer le temps en pygame
        clock = pygame.time.Clock()
        
        while run:
            #on cadence à 60 frames/sec
            clock.tick(60)
            self.actualiser_temps()

            #si l'utilisateur décide de mettre fin au programme on sort de la boucle
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    res = -1
                    run=False

                if event.type == pygame.VIDEORESIZE:
                    self.zoom_largeur = event.w//(self.LARGEUR_CASE + self.LARGEUR_MUR)
                    self.zoom_hauteur = event.h//(self.LARGEUR_CASE + self.LARGEUR_MUR)
                    self.redraw()
                    
            self.actions_entitees()

            #avant de redessiner l'écran on trie les entitées (ça influe sur l'affichage)
            self.trie_entitees()
            #on redessine l'écran
            self.redraw()
            self.traitement_evenements()
            self.check_missions()
            self.lab.refresh_speciales()

            if self.lab.as_gagner(self.joueur.getPosition()) and self.affichage.affiche == LABYRINTHE:
                self.screen = pygame.display.set_mode((640, 300))
                self.ecran_fin_niveau(self.textWin)
                res = 1000
                run=False
            if self.as_perdu():
                self.screen = pygame.display.set_mode((640, 300))
                self.ecran_fin_niveau(self.textLose)
                res = 1000
                run=False
            if self.greater_teleportation:
                self.screen = pygame.display.set_mode((640, 300))
                self.ecran_fin_niveau(self.textTel)
                res = 0
                run=False
            pygame.display.update()
        self.fin_niveau(self.as_perdu())

        return res,self.lab.as_gagner(self.joueur.getPosition()),self.joueur

    def fin_niveau(self, as_perdu):
        """
        Fonction qui gère la fin du niveau
        Entrées:
            -un booéen indiquant si le joueur as perdu (comme vous d'ailleurs)
        """
        #on met fin a tout les événements
        for evenement in self.evenements:
            evenement.temps_restant=0
            evenement.action()
        if as_perdu:
            self.joueur = self.precedent_joueur
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
        Fonction qui traite les événements à déclenchement temporel
        """
        events_tmps=[self.evenements[i] for i in range(0,len(self.evenements))]
        nbSup=0
        
        for i in range(0,len(events_tmps)):
            #print (events_tmps)
            if events_tmps[i].execute():
                self.evenements.pop(i-nbSup)
                nbSup+=1

    def check_missions(self):
        """
        Fonction qui traite les événements à déclenchement conditionnel
        """
        missions_tmps=[self.missions[i] for i in range(0,len(self.missions))]
        nbSup=0
        
        for i in range(0,len(missions_tmps)):
            if eval(missions_tmps[i][0]):
                eval(missions_tmps[i][1])
                self.missions.pop(i-nbSup)
                nbSup+=1
                
                 
    def action_joueur(self):
        """
        Fonction qui exécute la partie du code ou le joueur demande à agir
        et qui renvoie rien
        """
                    


        #on récupère toutes les touches préssés sous forme de booléen
        keys=pygame.key.get_pressed()
        
        if keys[pygame.K_q]:
            self.joueur.consulte_minimap()
        elif keys[pygame.K_i]:
            self.joueur.consulte_inventaire()
        elif keys[pygame.K_RETURN]:
            self.joueur.revient()
        if keys[pygame.K_EQUALS]:
            self.joueur.precise()
        if keys[pygame.K_MINUS]:
            self.joueur.postcise()

        if self.affichage.affiche == INVENTAIRE:
            if keys[pygame.K_RIGHT]:
                self.joueur.inventaire_vers_la_droite()
            elif keys[pygame.K_LEFT]:
                self.joueur.inventaire_vers_la_gauche()
            elif keys[pygame.K_SPACE]:
                self.joueur.utilise_inventaire()

        elif self.affichage.affiche == MINIMAP:
            if keys[pygame.K_UP]:
                self.joueur.minimap_vers_le_haut()
            elif keys[pygame.K_DOWN]:
                self.joueur.minimap_vers_le_bas()
            elif keys[pygame.K_RIGHT]:
                self.joueur.minimap_vers_la_droite()
            elif keys[pygame.K_LEFT]:
                self.joueur.minimap_vers_la_gauche()

        elif self.affichage.affiche == LABYRINTHE:
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
            elif keys[pygame.K_SPACE]:
                self.joueur.attaque()
            elif keys[pygame.K_w]:
                self.joueur.attaque_lourde(HAUT)
            elif keys[pygame.K_a]:
                self.joueur.attaque_lourde(GAUCHE)
            elif keys[pygame.K_s]:
                self.joueur.attaque_lourde(BAS)
            elif keys[pygame.K_d]:
                self.joueur.attaque_lourde(DROITE)
            elif keys[pygame.K_x]:
                self.joueur.tentative_interaction()


    def actions_entitees(self):
        """
        Fonction qui exécute les actions des entitées
        renvoie un booléen indiquant si il y a besoin de redessiner l'écran
        """
        redessiner=False

        projectiles = self.getProjectiles()

        for projectile in projectiles:
            if self.horloge_cycle % projectile.getVitesse()==0:
                redessiner=True

                self.traitement_mouvement(projectile)

        agissants=self.getAgissants()
        
        self.actualiser_vues_agissants(agissants)
        
        for agissant in agissants:
            if issubclass(type(agissant),Joueur):
                self.action_joueur()

            if self.horloge_cycle % agissant.getVitesse()==0:

#                    agissant.regen_mana()
                agissant.soigne_toi()
                
                agissant=self.actualiser_donnee(agissant)

                agissant.prochaine_action()

                agissant.execute_evenements()
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
    def getProjectiles(self):
        """
        Fonction qui renvoie un tableau contenant les projectiles
        """
        projectiles=[]

        for entitee in self.entitees:
            if issubclass(type(entitee),Projectile):
                projectiles.append(entitee)

        return projectiles
    def delete_entitees(self):
        """
        Fonction qui supprime les entitees mortes
        """
        nbSupp=0
        for i in range(0,len(self.entitees)):
            if issubclass(type(self.entitees[i-nbSupp]),Agissant):
                if self.entitees[i-nbSupp].pv<=0:
                    for new_item in self.entitees[i-nbSupp].drops:
                        new_item.position = self.entitees[i-nbSupp].position
                        self.entitees.append(new_item)
                    self.entitees.pop(i-nbSupp)
                    nbSupp+=1
            elif issubclass(type(self.entitees[i-nbSupp]),Item) or issubclass(type(self.entitees[i-nbSupp]),Potion):
                if self.entitees[i-nbSupp].position==None:
                    self.entitees.pop(i-nbSupp)
                    nbSupp+=1
    def trie_entitees(self):
        """
        Fonction qui trie les entitees selon l'endroit où on veut les afficher
        """
        new_entitees = []
        for type_entitee in [Caillou,Item,Pnj_passif,Monstre,Projectile,Joueur]:
            for entitee in self.entitees:
                if issubclass(type(entitee),type_entitee):
                    new_entitees.append(entitee)
        self.entitees = new_entitees
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
                    passe,newcoord=self.lab.peut_passer(agissant,direction_voulue,agissant.inventaire)
                else:
                    passe,newcoord = self.lab.peut_passer(agissant,direction_voulue)
                #print(passe)
                if passe:
                    libre = self.collision.case_libre(agissant,newcoord,self.entitees)
                    #print(libre)
                    if libre:
                        succes=True
                        #print(succes)
                        agissant.setPosition(newcoord)
                        info_comp = self.lab.execute_special(agissant)
                        if agissant == self.joueur:
                            nouveaux_evenements = self.collision.visite_case(newcoord,agissant,self.entitees)
                            self.lab.matrice_cases[newcoord[0]][newcoord[1]].passage = True
                            for evenement in nouveaux_evenements :
                                self.evenements.append(evenement)
                            if info_comp != None:
                                self.greater_teleportation = True
                                self.destination = info_comp
                                
        elif id_action==ATTAQUER:
            succes,mat_attaque=self.collision.tentative_attaque(agissant,self.entitees)
            direction=agissant.dir_regard
            self.affichage.ajout_animation(agissant.position_vue,agissant.mode_attaque,mat_attaque,direction)
        elif id_action==INTERAGIR:
            succes = self.collision.tentative_interaction(agissant,self.entitees)
        elif id_action==PARLER:
            succes = self.affichage.add_dialogue(action)
        elif id_action==CONSULTER_MINIMAP:
            self.affichage.affiche = MINIMAP
            agissant.vitesse = agissant.vitesse_autres
        elif id_action==CONSULTER_INVENTAIRE:
            self.affichage.affiche = INVENTAIRE
            agissant.vitesse = agissant.vitesse_autres
        elif id_action==PRECISION:
            if self.affichage.affiche == INVENTAIRE:
                self.affichage.affiche = ITEM
            elif self.affichage.affiche == MINIMAP:
                agissant.minimap.rezoom()
        elif id_action==POSTCISION:
            if self.affichage.affiche == ITEM:
                self.affichage.affiche = INVENTAIRE
            elif self.affichage.affiche == MINIMAP:
                agissant.minimap.dezoom()
        elif id_action==RETOUR:
            if self.affichage.affiche == DIALOGUE:
                if self.affichage.pass_replique():
                    agissant.vitesse = agissant.vitesse_lab
            else:
                self.affichage.affiche = LABYRINTHE
                agissant.vitesse = agissant.vitesse_lab
        elif id_action==BOUGER_MINIMAP:
            direction_voulue=action
            agissant.minimap.deplace_toi(direction_voulue)
        elif id_action==BOUGER_INVENTAIRE:
            direction_voulue=action
            agissant.inventaire.deplace_toi(direction_voulue)
        elif id_action==UTILISER:
            if self.affichage.affiche == INVENTAIRE:
                agissant.inventaire.utilise_item()
            
        return succes

    def traitement_mouvement(self,projectile):
        """
        Fonction qui déplace un projectile selon sa trajectoire
        """
        direction = projectile.direction
        passe,newcoord,tel=self.lab.peut_passer(projectile,direction)
        if passe:
            libre = self.collision.case_libre(agissant,newcoord,self.entitees)
            if libre:
                projectile.setPosition(newcoord)
            else:
                projectile.setPosition(None)
        else:
            projectile.setPosition(None)
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
            if issubclass(type(agissant),Joueur):
                vitesses.append(agissant.vitesse_autres)
        return self.ppcm(vitesses)
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

    def spawn_aleatoire(self,monstre,largeur_vue,hauteur_vue,pv,degats,vitesse,radius,perimetre,proba,max_meute,premiere_meute,couleur=(255,0,0),drops=[]):
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
        while res == []:
            for i in range (perimetre[0][0],perimetre[1][0]):
                for j in range (perimetre[0][1],perimetre[1][1]):
                    if random.random() <= proba :
                        if monstre == Runner:
                            res.append(monstre(self.lab.getMatrice_cases,self.arrivee[0],self.arrivee[1],(i,j),nb_meute,largeur_vue,hauteur_vue,pv,degats,vitesse,radius,couleur))
                        else:
                            res.append(monstre((i,j),nb_meute,largeur_vue,hauteur_vue,pv,degats,vitesse,radius,couleur))
                        taille_meute += 1
                        if taille_meute == max_meute :
                            nb_meute += 1
                            taille_meute = 0
        for drop in drops:
            res[random.randint(0,len(res)-1)].drops.append(drop)
        return res

    def ppcm(self,vitesses):
        """Calcul du 'Plus Petit Commun Multiple' des vitesses"""
        def _pgcd(a,b):
            while b != 0:
                a,b = b,a%b
            return a
        if len(vitesses) == 1:
            res = vitesses[0]
        else:
            res = (vitesses[0]*vitesses[1])//_pgcd(vitesses[0], vitesses[1])
            for x in vitesses[2:]:
                res = (res*x)//_pgcd(res, x)
        return res

    def __str__(self):
        return "Niveau("+str(self.niveau)+","+str(self.difficulte)+","+str(self.mode_affichage)+","+str(self.mode_minimap)+","+str(self.joueur)+")"


    def mission_minimap(self):
        """
        Mission qui consiste à découvrir toute la minimap
        """
        check = True
        matrice = self.joueur.minimap.matrice_cases
        for ligne in matrice:
            for case in ligne:
                if case.decouvert == -1:
                    check = False
        return check

    def mission_monstres(self):
        """
        Mission qui consiste à tuer tous les monstres
        """
        check = True
        for entitee in self. entitees:
            if isinstance(entitee,Monstre):
                check = False
        return check

    def mission_drops(self):
        """
        Mission qui consiste à tuer tous les monstres avec des drops
        """
        check = True
        for entitee in self. entitees:
            if isinstance(entitee,Monstre):
                if entitee.drops != []:
                    check = False
        return check

    def mission_position(self,position):
        """
        Mission qui consiste à se rendre à une position donnée
        """
        return self.joueur.position == position

    def mission_clee(self,nom):
        """
        Mission qui consiste à posséder une clé avec un nom donné
        """
        check = False
        if "Clee" in self.joueur.inventaire.entree_dico:
            clees = self.joueur.inventaire.items["Clee"]
            for clee in clees:
                if clee.nom_clee == nom:
                    check = True
        return check

    def mission_item(self,type_item):
        """
        Mission qui consiste à posséder un item d'un type donné
        """
        check = False
        if type_item in self.joueur.inventaire.entree_dico:
            if len(self.joueur.inventaire.items[type_item])>0:
                check = True
        return check

    def petits_cailloux(self,distance,position_1,position_2):
        """
        Récompense qui ajoute des petits cailloux dans le labyrinthe
        """
        positions = self.lab.petit_poucet(distance,position_1,position_2)
        for position in positions:
            self.entitees.append(Caillou(position))

    def ajout(self,recipient,ajouts):
        for ajout in ajouts:
            recipient.append(ajout)

    def affectation(self,receveur,donneur):
        receveur = donneur

    def incremente(self,somme,ajout):
        somme += ajout
