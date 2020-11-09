from Classe import *
from Skins import *

# Contenu du fichier :
# La classe Controleur (lignes 0-500) ;
# La classe Labyrinthe (lignes 500-900), avec :
#    La classe Generateur (lignes 900-1200) ;
#    La classe Case (lignes 1200-1300) ;
#    La classe Murs (lignes 1300-1400) ;
#    La classe Pattern (lignes 1400-1700) ;
# La classe Entitee (lignes 1700), avec ;
#    La classe Entitee_superieure (lignes 1700) ;
#    La classe Fantome (lignes 1700) ;
#    La classe Cadavre (lignes 1700) ;
#    La classe Oeuf (lignes 1700) ;
#    La classe Agissant (lignes 1700-2000) ;
#    La classe Joueur (lignes 2000-2200) ;
#    La classe Item et ses multiples sous-classes (lignes 2200-2500) ;
#    La classe Inventaire (lignes 2500-2700) ;
# La classe Esprit (lignes 2700-2900) ;
# Les mutiples classes de Magie_* (lignes 2900-3900) ;
# La classe Effet et ses multiples sous-classes (lignes 3900-4800) ;
# La classe Sort et ses multiples sous-classes (lignes 4800-5100) ;
# La classe Affichage (lignes 5100-5300).

# Conseil de navigation : Ctrl+f + "Class Bidule" vous enverra au début de la classe Bidule


#    .
#   / \     Je ne respecte absolument pas les régles de base de la programmation objet, puisque je vais donner à tous les objets de mon univers (ou presque) ce controleur qui les contient tous (ou presque).
#  / ! \    S'attendre à de vives ciritques !
# /_____\

class Controleur():
    def __init__(self):
        #print("Initialisation du controleur")
        self.labs = {} #Un dictionnaire avec tous les labyrinthes, indéxés par leur identifiant dans les positions.
        #print("Labyrinthe : check")
        self.entitees = {}
        #print("Entitées : check")
        self.esprits = {}
        self.labs_courants = []
        self.entitees_courantes = []
        self.esprits_courants = []
        self.nb_tours = 0

    def jeu(self,screen):
        self.labs[0] = Labyrinthe(0,20,20,(0,0,0),[Patern((0,2,3),10,8,[(0,0,1),(0,5,7),(0,5,0)],["test_code"])])
        self.labs[1] = Labyrinthe(1,20,20,(1,0,0),[Patern((1,5,6),2,12,[(1,1,3),(1,1,6),(1,0,8),(1,0,10)]),Patern((1,2,4),12,2,[(1,3,1),(1,4,1),(1,1,0),(1,10,0)])])
        self.labs["test_barriere"] = Labyrinthe("test_barriere",20,20,("test_barriere",0,0),[Patern(("test_barriere",0,0),10,20,[]),Patern(("test_barriere",10,0),10,20,[("test_barriere",0,6)])])
        self.labs["test_esprit"] = Labyrinthe("test_esprit",10,10,("test_esprit",0,0),[Patern(("test_esprit",0,0),10,10,[],[],True)])
        self.entitees[2] = Joueur((0,1,1),100,100,1,100,100,1,10,10,1,1,1,1,1,Classe_principale([],[],True,"joueur"),screen) #Ne fonctionne que si on vient de faire l'init
        self.set_barriere_classe(("test_barriere",9,6),DROITE,Item)
        self.ajoute_entitee(Cle((0,0,0),["test_code"]))
        self.ajoute_entitee(Potion((0,8,9),Poison(1,30,3)))
##        agissant1 = Agissant(("test_esprit",0,1),10,10,0.05,0,0,0,10,1,1,1,1,1,1,Classe([None]*10,[Skill_deplacement(),Skill_vision()],[Skill_stomp()]))
##        self.ajoute_entitee(agissant1)
##        agissant2 = Agissant(("test_esprit",1,4),10,10,0.05,0,0,0,10,1,1,1,1,1,1,Classe([None]*10,[Skill_deplacement(),Skill_vision()],[Skill_stomp()]))
##        self.ajoute_entitee(agissant2)
##        agissant3 = Agissant(("test_esprit",9,7),10,10,0.05,0,0,0,10,1,1,1,1,1,1,Classe([None]*10,[Skill_deplacement(),Skill_vision()],[Skill_stomp()]))
##        agissant3.latence+=1
##        self.ajoute_entitee(agissant3)
##        agissant4 = Agissant(("test_esprit",9,8),10,10,0.05,0,0,0,10,1,1,1,1,1,1,Classe([None]*10,[Skill_deplacement(),Skill_vision()],[Skill_stomp()]))
##        agissant4.latence+=2
##        self.ajoute_entitee(agissant4)
        self.set_teleport((0,0,4),(1,19,17),GAUCHE,DROITE)
        self.set_teleport((1,0,10),("test_barriere",19,17),GAUCHE,DROITE)
##        self.set_barriere_classe(("test_esprit",8,8),HAUT,Agissant)
##        self.set_barriere_classe(("test_esprit",9,8),HAUT,Agissant)
##        self.set_barriere_classe(("test_esprit",10,8),HAUT,Agissant)
##        self.set_barriere_classe(("test_esprit",7,8),DROITE,Agissant)
##        self.set_barriere_classe(("test_esprit",7,9),DROITE,Agissant)
##        self.set_barriere_classe(("test_esprit",7,10),DROITE,Agissant)
##        self.set_barriere_classe(("test_esprit",8,10),BAS,Agissant)
##        self.set_barriere_classe(("test_esprit",9,10),BAS,Agissant)
##        self.set_barriere_classe(("test_esprit",10,10),BAS,Agissant)
##        self.set_barriere_classe(("test_esprit",11,8),GAUCHE,Agissant)
##        self.set_barriere_classe(("test_esprit",11,9),GAUCHE,Agissant)
##        self.set_barriere_classe(("test_esprit",11,10),GAUCHE,Agissant)
##        esprit_test = Esprit("Premier_esprit")
##        esprit_jaloux = Esprit("Deuxieme_esprit")
##        self.esprits["Premier_esprit"]=esprit_test
##        self.esprits["Deuxieme_esprit"]=esprit_jaloux
        self.active_lab(self.entitees[2].position[0])
##        esprit_test.controleur = self
##        esprit_test.ajoute_corps([agissant1.ID,agissant2.ID])
##        esprit_jaloux.controleur = self
##        esprit_jaloux.ajoute_corps([agissant3.ID,agissant4.ID])
##        esprit_jaloux.ennemis[agissant1.ID]=1

    def duel(self,esprit1,esprit2,niveau_1=1,niveau_2=1,tailles_lab=(20,20),vide=True,vue=False,screen=None):
        """Fonction qui crée les conditions d'un duel."""

        if vue : # On peut avoir des spectateurs, mais pas forcément
            self.ajoute_entitee(Joueur(("arène",tailles_lab[0]//2,tailles_lab[1]//2),0,1,0,0,0,0,0,0,0,100,1,1,1,Classe_principale([],[],True,"joueur"),screen))
        # Première étape : créer l'arène
        self.labs["arène"]=Labyrinthe("arène",tailles_lab[0],tailles_lab[1],("arène",0,0),[Patern(("arène",0,0),tailles_lab[0],tailles_lab[1],[],[],vide)])
        # Deuxième étape : créer les opposants
        self.esprits["1"] = esprit1("1",niveau_1,self,("arène",0,0))
        self.esprits["2"] = esprit2("2",niveau_2,self,("arène",tailles_lab[0]-1,0))
        # Troisième étape : créer un conflit
        self.esprits["1"].antagonise("2")
        self.esprits["2"].antagonise("1")
        # Quatrième étape : admirer
        self.active_lab("arène")

    def set_barriere_classe(self,position,direction,classe):
        self.active_lab(position[0])
        mur = self.labs[position[0]].matrice_cases[position[1]][position[2]].murs[direction]
        mur.brise()
        mur.effets.append(Barriere_classe(classe))
        mur_opp = mur.get_mur_oppose()
        if mur_opp != None:
            mur_opp.brise()
            mur_opp.effets.append(Barriere_classe(classe))
        self.desactive_lab([position[0]])

    def active_lab(self,key): #Non utilisé dans la version de mi-juillet
        """Fonction appelée pour activer un nouveau labyrinthe. En entrée, la clé du labyrinthe à activer.
           Un étage, en règle générale, est "inactif", c'est à dire que ses occupants ne bougent pas. Il devient "actif" quand une entitée y entre, pour 5 tours si c'est une entitée basique, et jusqu'à 5 tours après son départ si c'est une entitée supérieure (joueur, dev, kumoko, etc.).
           Lorsque le labyrinthe est "activé", sa clé (qui l'indexe dans le dictionnaire des labs et se retrouve dans la coordonées de position verticale de ses occupants) est ajoutée aux labs_courants. On cherche parmis les entitées celles qui se trouvent dans ce lab et on rajoute leur identifiant aux entitées courantes.
           Dans la version définitive, cette fonction sera appelée à la fin de la chute pour passer le joueur dans le niveau 1."""
        #On active le lab :
        self.labs[key].active(self) #On lui donne le controleur pour qu'il puisse l'appeler au besoin.
        #On cherche ses occupants :
        for ke in self.entitees.keys() :
            entitee = self.get_entitee(ke)
            position = entitee.get_position()
            if position != None: #Il y a des entitees dans les inventaires
                if position[0] == key : #La position commence par la coordonnée verticale.
                    if not ke in self.entitees_courantes:
                        self.entitees_courantes.append(ke)
                    entitee.active(self)
        if not key in self.labs_courants:
            self.labs_courants.append(key)

    def desactive_lab(self,key): #Non utilisé dans la version de mi-juillet
        """Fonction appelée pour désactiver un labyrinthe actif. En entrée, la clé du labyrinthe à désactiver.
           Tout labyrinthe se désactive après 5 tours d'absence d'entitée supérieure (joueur, dev, kumoko, etc.).
           Le lab actif possédant le controleur en attribut, il appelle cette fonction lui-même quand son compteur interne tombe à 0."""
        #On desactive les occupants du lab :
        for ke in self.entitees.keys() : #Normalement on a déjà vérifié qu'il n'y a pas d'entitée supérieure...
            entitee = self.get_entitee(ke)
            position = entitee.get_position()
            if position != None: #Il y a des entitees dans les inventaires
                if position[0] == key : #La position commence par la coordonnée verticale.
                    if ke in self.entitees_courantes:
                        self.entitees_courantes.remove(ke)
                    entitee.desactive()
        if key in self.labs_courants:
            self.labs_courants.remove(key)

    def move(self,position,entitee): #Non utilisé dans la version de mi-juillet
        """Fonction appelée quand une entitée change de labyrinthe. En entrée, la position cible et l'entitée avant son déplacement.
           Si le labyrinthe de départ n'a plus d'entitée supérieure, on va devoir préparer sa désactivation. Si le labyrinthe d'arrivée n'avait pas d'entitée supérieure, il va falloir l'activer."""
        ancien_lab = entitee.get_position()[0]
        nouveau_lab = position[0]
        if isinstance(entitee,Entitee_superieure): #Si on a une entitée supérieure :
            if not(nouveau_lab in self.labs_courants) : #On active si nécessaire
                self.active_lab(nouveau_lab)
            elif self.labs[nouveau_lab].temps_restant != -1: #On maintient activé jusqu'à nouvel ordre si nécessaire (sinon, c'est qu'il y a déjà une entitée supérieure dans le labyrinthe, on a rien à faire)
                self.labs[nouveau_lab].temps_restant = -1
        else : #Si on a une entitée normale :
            if not(nouveau_lab in self.labs_courants) :
                self.active_lab(nouveau_lab) #On active si nécessaire...
                self.labs[nouveau_lab].quitte() #...Mais on quittera bientôt
            elif self.labs[nouveau_lab].temps_restant != -1:
                self.labs[nouveau_lab].quitte() #On quittera un peu plus tard si nécessaire (sinon, c'est qu'il y a une entitée supérieure dans le labyrinthe, on a rien à faire)
            
        entitee.set_position(position) #L'entitée se déplace, elle et toutes ses possessions (notamment l'inventaire !)
        #On cherche une éventuelle entitée supérieure dans l'ancien labyrinthe :
        sup = False
        for key_entitee in self.entitees_courantes :
            position = self.entitees[key_entitee].get_position()
            if position != None:
                if (position[0] == ancien_lab) and isinstance(self.entitees[key_entitee],Entitee_superieure):
                    sup = True
        if not(sup): #On n'a pas d'entitee supérieure dans le labyrinthe
            self.labs[ancien_lab].quitte() #On lance le décompte de 5 tours (faire + de 5 tours ?)

    def get_lab(self,num_lab):
        return self.labs[num_lab]

    def set_teleport(self,pos_dep,pos_arr,dir_dep,dir_arr):
        case_dep = self.get_case(pos_dep)
        case_arr = self.get_case(pos_arr)
        mur_dep = case_dep.get_mur_dir(dir_dep)
        mur_arr = case_arr.get_mur_dir(dir_arr)
        mur_dep.detruit()
        mur_arr.detruit()
        mur_dep.set_cible(pos_arr,True)
        mur_arr.set_cible(pos_dep,True)

    def get_case(self,position):
        return self.get_lab(position[0]).get_case(position)

    def make_vue(self,agissant):
        position = agissant.get_position()
        num_lab = position[0]
        labyrinthe = self.get_lab(num_lab)
        vue = labyrinthe.get_vue(agissant)
        for i in range(len(vue)):
            for j in range(len(vue[0])):
                if vue[i][j][1] > 0:
                    vue[i][j][7] = self.trouve_occupants((num_lab,i,j)) #À changer quand les positions seront tridimensionnelles !
        agissant.vue = vue

    def voit_occupants(self,position): #Pour l'instant le joueur est le seul agissant.
        occupants = self.trouve_occupants(position)
        images = []
        for occupant in occupants:
            images.append(self.get_entitee(occupant).get_image())
        return images

    def trouve_items(self,position):
        occupants = self.trouve_occupants(position)
        items = []
        for occupant in occupants:
            if issubclass(self.get_entitee(occupant).get_classe(),Item):
                items.append(occupant)
        return items

    def trouve_occupants(self,position):
        occupants = []
        for entitee in self.entitees:
            if self.get_entitee(entitee).get_position() == position:
                occupants.append(entitee)
        return occupants

    def fait_agir(self,agissant):
        type_skill = agissant.skill_courant
        skill = trouve_skill(agissant.classe_principale,type_skill)
        if skill == None :
            print("On ne peut pas utiliser un skill que l'on n'a pas... et on ne devrait pas pouvoir le choisir d'ailleurs : "+type_skill)
        else :



            if type_skill == Skill_analyse: #À améliorer !
                mallus,niveau,cible = skill.utilise()
                self.lance_analyse(mallus,niveau,cible)



            elif type_skill == Skill_vol:
                possesseur,item = self.selectionne_item_vol()
                latence,reussite = skill.utilise(possesseur.priorite,agissant.priorite)
                agissant.set_latence(latence)
                if reussite :
                    possesseur.inventaire.supprime_item(item)
                    agissant.inventaire.ramasse_item(item)
                    if isinstance(agissant,Joueur):
                        affichage = agissant.affichage
                        affichage.message("Tu as volé avec succès un "+item+" à "+victime+" !")
                else :
                    possesseur.persecuteurs.append(agissant.ID)
                #refaire les autres vols sur le même modèle



            elif type_skill == Skill_ramasse:
                items = self.trouve_items(agissant.get_position())
                latence = 0
                for ID_item in items:
                    item = self.get_entitee(ID_item)
                    latence_item,reussite = skill.utilise(item.priorite-agissant.get_priorite())
                    latence += latence_item
                    if reussite:
                        agissant.inventaire.ramasse_item(ID_item)
                agissant.set_latence(latence)



            elif type_skill == Skill_stomp:
                #Une attaque qui se fait sans arme.
                force,affinite,direction,ID = agissant.get_stats_attaque(TERRE)
                latence,taux,portee = skill.utilise()
            
                degats = force*taux*affinite
                attaque = Attaque(ID,degats,TERRE,portee)

                agissant.set_latence(latence)
                agissant.effets.append(attaque)



            elif type_skill == Skill_attaque:
                #Une attaque qui se fait avec une arme.
                arme = agissant.get_arme()
                if arme == None:
                    if isinstance(agissant,Joueur):
                        affichage = agissant.affichage
                        affichage.message("Tu n'as pas d'arme ?") #Sans arme, on devrait utiliser le stomp.
                        affichage.message("Appuie sur la barre espace !")
                else:
                    element,tranchant,portee = arme.get_stats_attaque()
                    force,affinite,direction,ID = agissant.get_stats_attaque(element)
                    latence,taux = skill.utilise()

                    taux_manipulation = 1
                    manipulation = trouve_skill(agissant.classe_principale,Skill_manipulation_arme)
                    if manipulation != None :
                        taux_manipulation = manipulation.utilise_attaque()

                    if isinstance(arme,Epee) :
                        if manipulation == None :
                            manipulation = trouve_skill(agissant.classe_principale,Skill_manipulation_epee)
                            if manipulation != None :
                                taux_manipulation = manipulation.utilise()

                        forme = "Sd_S___" #Dans un monde idéal, les skills de manipulation donnerait accès à d'autres formes

                    elif isinstance(arme,Lance) :
                        if manipulation == None :
                            manipulation = trouve_skill(agissant.classe_principale,Skill_manipulation_lance)
                            if manipulation != None :
                                taux_manipulation = manipulation.utilise()

                        forme = "R__S___" #Dans un monde idéal, les skills de manipulation donnerait accès à d'autres formes
                    else :
                        print("Quelle est cette arme ? " + agissant.arme)

                    degats = force*affinite*tranchant*taux*taux_manipulation
                    attaque = Attaque(ID,degats,element,portee,forme,direction)

                    agissant.set_latence(latence)
                    agissant.effets.append(attaque)



            elif type_skill == Skill_blocage :
                #Pour être protégé par le bouclier pendant les tours suivants.
                bouclier = agissant.get_bouclier()
                if bouclier == None:
                    if isinstance(agissant,Joueur):
                        affichage = agissant.affichage
                        affichage.message("Tu n'as pas de bouclier !") #Sans bouclier, on devrait se mettre à couvert.
                        affichage.message("Tu devrais esquiver, plutôt.")
                else:
                    latence,taux_skill = skill.utilise()

                    taux_manipulation = 1
                    duree = 3
                    manipulation = trouve_skill(agissant.classe_principale,Skill_manipulation_arme)
                    if manipulation != None :
                        taux_manipulation,duree = manipulation.utilise()
                    else :
                        manipulation = trouve_skill(agissant.classe_principale,Skill_manipulation_bouclier)
                        if manipulation != None :
                            taux_manipulation,duree = manipulation.utilise()

                    taux = taux_skill * taux_manipulation

                    effet = Protection(duree,bouclier) #Dans un monde idéal, les skills de manipulation donnerait accès à d'autres effets

                    for effet_prec in agissant.effets :
                        if isinstance(effet_prec,Protection):
                            agissant.effets.remove(effet_prec) #On ne peut pas avoir deux protections à la fois !

                    agissant.set_latence(latence)
                    agissant.effets.append(effet)
                    effet.execute(agissant) #On passe l'effet en phase "en cours"
                    bouclier.taux_defense["protection"] = taux



            elif type_skill == Skill_lancer :
                projectile = agissant.get_item_lancer()

                if projectile != None :
                    latence,hauteur,vitesse = skill.utilise(projectile)
                    agissant.set_latence(latence*projectile.poids)
                    projectile.position = agissant.get_position()
                    projectile.hauteur = hauteur*agissant.force/projectile.poids
                    projectile.taux_vitesse["lancementv"]=vitesse
                    projectile.direction = agissant.direction
                    projectile.lanceur = agissant.ID
                    self.items.append(projectile)
                else :
                    if isinstance(agissant,Joueur):
                        affichage = agissant.affichage
                        affichage.message("J'ai dû mal comprendre...")
                        affichage.message("Tu veux lancer un item que tu n'as pas ?")



            elif type_skill in [Skill_deplacement,Skanda,Lesser_Skanda]:
                latence,niveau = skill.utilise()
                direction = agissant.get_direction()
                position = agissant.get_position()
                agissant.set_latence(latence)

                lab = self.get_lab(position[0])
                lab.veut_passer(agissant,direction)



            elif type_skill == Skill_soin :
                latence,soin,portee = skill.utilise()
                agissant.set_latence(latence)
                self.soigne(agissant,agissant.get_position(),portee,soin)



            elif type_skill == Skill_regeneration_MP :
                latence,regen,portee = skill.utilise()
                agissant.set_latence(latence)
                self.regenere(agissant,agissant.get_position(),portee,regen)



            elif type_skill in [Skill_reanimation,Skill_reanimation_renforcee] :
                cadavre = selectionne_item_cadavre()
                taux,sup = skill.utilise()
                cadavre.pv = cadavre.pv_max*taux
                if cadavre.priorite + sup < agissant.priorite :
                    esprit_cadavre = get_esprit(cadavre)
                    esprit = get_esprit(agissant)
                    esprit_cadavre.retire_corp(cadavre)
                    esprit.ajoute_corp(cadavre) #L'ex cadavre rejoint l'esprit du nécromancien. Sinon, l'intégration dans l'ancien esprit se fait tout seul.



            elif type_skill in [Skill_magie,Height_of_Occultism,Lesser_Height_of_Occultism] :
                nom_magie = agissant.magie_courante
                latence,magie = skill.utilise(nom_magie)
                cout = magie.cout_mp
                if agissant.peut_payer(cout) :
                    reussite = True
                    cible_acquise = True
                    direction_acquise = True
                    cout_acquis = True
                    if isinstance(agissant,Joueur):
                        malchance = trouve_skill(agissant.classe_principale,Skill_malchanceux)
                    else:
                        malchance = None
                    if malchance != None:
                        reussite = malchance.utilise("cast_magic")
                    if isinstance(magie,Magie_cible) :
                        self.select_cible(magie,agissant)
                        cible_acquise = magie.cible_acquise
                    if isinstance(magie,Magie_dirigee) :
                        self.select_direction(magie,agissant)
                        direction_acquise = magie.direction_acquise
                    if isinstance(magie,Magie_cout) :
                        self.select_cout(magie,agissant)
                        cout_acquis = magie.cout_acquis
                    agissant.paye(cout)
                    agissant.set_latence(latence)
                    if reussite and cible_acquise and direction_acquise and cout_acquis:
                        magie.responsable = agissant.ID
                        self.tentative_magie(magie) #Modifier agissants pour y accéder normalement
                    else :
                        self.miss_fire(magie,agissant)



            elif type_skill in [Divine_Thread_Weaving,Lesser_Divine_Thread_Weaving] :
                action = agissant.action
                latence,item = skill.utilise(action)
                agissant.set_latence(latence)
                self.items.append(item)



            elif type_skill in [Scythe,Lesser_Scythe] :
                perce,element,taux = skill.utilise()
                attaque = Attaque(agissant.ID,agissant.force*taux,element,1,"R__T_Pb",agissant.direction,"piercing",perce)
                self.tentative_attaque(attaque)



            elif type_skill == Egg_Laying:
                latence, oeuf = skill.utilise()
                agissant.set_latence(latence)
                if oeuf != None :
                    self.items.append(oeuf)



    def select_cible(self,magie,agissant):
        if isinstance(agissant,Joueur):
            cibles = get_cibles_potentielles(magie,agissant)
            cible_courante = 0 #L'indice de la cible sous le curseur.
            affichage = agissant.affichage
            affichage.draw_magie(agissant.vue,agissant.entitee_vues,cibles,cible_courante) #Rajouter tous les autres trucs à afficher, comme les pv et pm, une fois que j'aurai retravaillé affichage.
            multi = isinstance(magie,Multi_cible)
            current_time = pygame.time.get_ticks()
            too_late = curent_time + magie.temps
            while pygame.time.get_ticks() < too_late:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP] :
                    cible_courante -= 1
                elif keys[pygame.K_DOWN] :
                    cible_courante += 1
                elif keys[pygame.K_SPACE] :
                    cible = cibles[cible_courante]
                    if multi : #Si jamais une magie peut cibler plusieurs cibles.
                        if cible in magie.cible :
                            magie.cible.remove(cible)
                        else :
                            magie.cible.append(cible)
                    elif magie.cible == cible :
                        magie.cible = None
                    else :
                        magie.cible = cible
                affichage.redraw_magie(cible_courante) #On ne change pas le reste de l'affichage.
        elif random.random() < agissant.talent :
            magie.cible = agissant.cible_magie
        magie.check_cibles()
        
    def select_direction(self,magie,agissant):
        if isinstance(agissant,Joueur):
            affichage = trouve_skill(agissant.classe_principale,Skill_affichage).affichage
            affichage.draw_magie_dir(agissant.vue,agissant.entitee_vues) #Rajouter tous les autres trucs à afficher, comme les pv et pm, une fois que j'aurai retravaillé affichage.
            current_time = pygame.time.get_ticks()
            too_late = curent_time + magie.temps
            while pygame.time.get_ticks() < too_late:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP] :
                    magie.direction = HAUT
                elif keys[pygame.K_DOWN] :
                    magie.direction = BAS
                elif keys[pygame.K_LEFT] :
                    magie.direction = GAUCHE
                elif keys[pygame.K_RIGHT] :
                    magie.direction = DROITE
                affichage.redraw_magie_dir(magie.direction) #On ne change pas le reste de l'affichage.
        elif random.random() < agissant.talent :
            magie.direction = agissant.direction_magie
        magie.check_direction()

    def select_cout(self,magie,agissant):
        if isinstance(agissant,Joueur):
            affichage = trouve_skill(agissant.classe_principale,Skill_affichage).affichage
            affichage.draw_magie_cout(agissant.vue) #Rajouter tous les autres trucs à afficher, comme les pv et pm, une fois que j'aurai retravaillé affichage.
            mana_dispo = agissant.get_mana_dispo()
            current_time = pygame.time.get_ticks()
            too_late = curent_time + magie.temps
            while ppygame.time.get_ticks() < too_late:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP] and magie.cout_mana < mana_dispo:
                    magie.cout_mana += agissant.precision_cout_magie
                elif keys[pygame.K_DOWN] and magie.cout_mana > 0:
                    magie.direction -= agissant.precision_cout_magie
                elif keys[pygame.K_LEFT] and agissant.precision_cout_magie > 0:
                    agissant.precision_cout_magie -= 1
                elif keys[pygame.K_RIGHT] :
                    agissant.precision_cout_magie == 1
                affichage.redraw_magie_cout(magie.direction)
        else :
            magie.cout_mana = agissant.cout_magie
        magie.check_cout()

    def miss_fire(self,magie,agissant):
        # Qu'est-ce qui se passe quand une magie miss-fire ? Rien ? la cible et/ou la direction sont choisies au hasard ? Une autre magie est utilisée à la place ?
        back_fire = random.random() < 0.2 #Ajuster cette probabilité
        malchance = trouve_skill(agissant.classe_principale,Skill_malchanceux)
        if not(back_fire) and malchance != None:
            back_fire = random.random() < malchance.utilise("back_fire")
        if back_fire :
            agissant.pv -= magie.cout #Peut-être ne pas se baser sur le coût de mana de la magie ?

    def get_esprit(self,nom):
        if nom != None:
            return self.esprits[nom]
        else:
            return None

    def get_nom_esprit(self,corp):
        return self.get_entitee(corp).get_esprit()

    def get_entitee(self,ID):
        return self.entitees[ID]

    def ajoute_entitees(self,entitees):
        for entitee in entitees:
            self.ajoute_entitee(entitee)

    def ajoute_entitee(self,entitee):
        self.entitees[entitee.ID]=entitee

    def get_entitees_etage(self,num_lab):
        entitees = []
        for ID_entitee in self.entitees_courantes:
            entitee = self.get_entitee(ID_entitee)
            if entitee.position != None:
                if self.get_entitee(ID_entitee).position[0]==num_lab:
                    entitees.append(ID_entitee)
        return entitees

    def get_agissants_items_labs_esprits(self):
        self.nb_tours+=1
        agissants = []
        items = []
        labs = []
        esprits = []
        noms_esprits = []
        for ID_entitee in self.entitees_courantes :
            entitee = self.get_entitee(ID_entitee)
            if isinstance(entitee,Agissant):
                if entitee.etat == "vivant" or isinstance(entitee,Joueur):
                    agissants.append(entitee)
                    esprit = entitee.get_esprit()
                    if esprit != None:
                        if not esprit in noms_esprits:
                            noms_esprits.append(esprit)
                else:
                    items.append(entitee)
            elif isinstance(entitee,Item):
                items.append(entitee)
        for niveau_lab in self.labs_courants:
            labs.append(self.labs[niveau_lab])
        for nom in noms_esprits:
            esprits.append(self.get_esprit(nom))
        return agissants, items, labs, esprits

    def inflige(self,degats,victime):
        victime.inflige(degats)

    def instakill(self,victime):
        immortel = trouve_skill(victime.classe_principale,Skill_immortel)
        if immortel == None :
            victime.pv = 0
            perseverance = trouve_skill(victime.classe_principale,Skill_essence_magique)
            if perseverance != None :
                victime.pm = 0

    def get_touches(self,responsable,position,porte=1,propagation="CD_S___",direction=None):
        attaquant = self.get_entitee(responsable)
        nom_esprit = attaquant.esprit
        intouchables = []
        if nom_esprit != None:
            esprit = self.get_esprit(nom_esprit)
            intouchables = esprit.get_corps()
        else:
            intouchables = [responsable]
        position = attaquant.get_position()
        labyrinthe = self.labs[position[0]]
        victimes_possibles = self.get_entitees_etage(position[0])
        obstacles = []
        for i in range(len(victimes_possibles)-1,-1,-1) :
            victime_possible = victimes_possibles[i]
            if victime_possible in intouchables :
                victimes_possibles.remove(victime_possible)
            else:
                victime = self.get_entitee(victime_possible)
                position_v = victime.get_position()
                obstacles.append(position_v)
        labyrinthe.attaque(position,porte,propagation,direction,obstacles)
        victimes = []
        for victime_possible in victimes_possibles :
            victime = self.get_entitee(victime_possible)
            position_v = victime.get_position()
            if labyrinthe.matrice_cases[position_v[1]][position_v[2]].clarte > 0 :
                victimes.append(victime)
        return victimes

    def tentative_magie(self,magie):
        if isinstance(magie,Sort_de_soin):
            cible = self.get_entitee(magie.cible)
            cible.soigne(magie.gain_pv)

class Labyrinthe:
    def __init__(self,ID,largeur,hauteur,depart,patterns=None,durete = 1):
        #print("Initialisation du labyrinthe")
        self.id = ID #Correspond à la clé du labyrinthe. Créer un init différend pour chaque lab ?
        self.largeur = largeur
        self.hauteur = hauteur
        self.durete = durete

        self.depart = depart

        self.matrice_cases = [[Case((self.id,j,i)) for i in range(hauteur)]for j in range(largeur)] #self.matrice_cases = [[Case((self.id,(i,j))) for i in range(hauteur)]for j in range(largeur)] 

        for i in range(self.largeur):
            self.matrice_cases[i][0].murs[HAUT].effets = [Mur_impassable()]
            self.matrice_cases[i][self.largeur-1].murs[BAS].effets = [Mur_impassable()]

        for j in range(self.hauteur):
            self.matrice_cases[0][j].murs[GAUCHE].effets = [Mur_impassable()]
            self.matrice_cases[self.hauteur-1][j].murs[DROITE].effets = [Mur_impassable()]

        self.patterns=patterns
        self.cases_visitees = None

        self.temps_restant = -1 #Devient positif quand le labyrinthe est actif sans entitée supérieure
        self.controleur = None #Tant qu'il n'est pas actif, il n'a pas de controleur à qui se référer

        self.generation(0.1,None,None)
        #print("Génération : check")

    def generation(self,proba=None,nbMurs=None,pourcentage=None):
        """
        Fonction qui génère la matrice du labyrinthe
            Entrées:
                -Les cases spéciales sous la forme suivante:[coord_case,objet]
                -L'éventuelle probabilité pour casser des murs
                -L'éventuel nombre de murs casser
                -L'éventuelle pourcentage de murs a casser
            Sorties:
                rien
        """
        #ini du tableau de case (4 murs pleins)
        for colone in self.matrice_cases:
            for case in colone:
                for mur in case.murs:
                    mur.effets.append(Mur_plein(self.durete))
        #génération en profondeur via l'objet generateur
        #print("Génération du labyrinthe")
        gene=Generateur(self.matrice_cases,self.depart,self.largeur,self.hauteur,self.patterns)
        #print("Générateur : check")
        self.matrice_cases=gene.generation(proba,nbMurs,pourcentage)

    def veut_passer(self,intrus,direction):
        """Fonction qui tente de faire passer une entitée.
           Se réfère à la case compétente, qui gère tout."""
        self.matrice_cases[intrus.get_position()[1]][intrus.get_position()[2]].veut_passer(intrus,direction)

    def step(coord,entitee):
        self.matrice_cases[coord[0]][coord[1]].step(entitee)

    def get_vue(self,agissant):
        return self.resoud(agissant.get_position(),agissant.get_portee_vue())
            
    def getMatrice_cases(self):
        #on obtient une copie indépendante du labyrinthe
        new_mat = [[self.matrice_cases[j][i].get_copie() for i in range(self.hauteur)]for j in range(self.largeur)]
        return new_mat

    def get_case(self,position):
        return self.matrice_cases[position[1]][position[2]]

    #Découvrons le déroulé d'un tour, avec Labyrinthe-ni :
    def debut_tour(self): #On commence le tour
        for i in range(self.largeur):
            for j in range(self.hauteur):
                self.matrice_cases[i][j].debut_tour()

    def post_action(self): #On agit sur les actions en suspens (les attaques en particulier)
        for i in range(self.largeur):
            for j in range(self.hauteur):
                self.matrice_cases[i][j].post_action((i,j))

    def fin_tour(self):
        if self.temps_restant >= 0:
            if self.temps_restant == 0:
                self.controleur.desactive_lab(self.id)
                self.controleur = None
                for i in range(self.largeur):
                    for j in range(self.hauteur):
                        self.matrice_cases[i][j].desactive()
            self.temps_restant -= 1
    #Et c'est la fin du tour !

    def quitte(self):
        self.temps_restant = 5

    def active(self,controleur):
        self.controleur = controleur
        self.temps_restant = -1 #Au cas où
        for i in range(self.largeur):
            for j in range(self.hauteur):
                self.matrice_cases[i][j].active(controleur)

    def attaque(self,position,portee,propagation,direction,obstacles):
        return self.resoud(position,portee,"attaque",propagation,direction,obstacles)

    def resoud(self,position,portee,action="vue",propagation="C__S_Pb",direction=None,dead_ends=[],reset=True):
        #Les possibilités de propagation sont :
        #                           Circulaire, le mode de propagation de la vision
        #                           Rectiligne, dans une unique direction
        #                           Semi-circulaire, dans trois directions fixées
        #                           Quarter-circulaire, dans deux directions fixées
        #                           Circulaire dégénéré, commence dans toutes les directions puis devient Semi-circulaire pour interdire les demi-tours
        #                           Semi-circulaire dégénéré, commence dans trois directions puis devient Quarter-circulaire pour interdire les demi-tours
        #                           Circulaire double dégénéré, devient Semi-circulaire dégénéré
        #                           Spatial, se déplace selon les coordonées comme la vue
        #                           Teleporte, se déplace par les téléporteurs comme les attaques magiques
        #                           Passe-porte, passe au travers des portes
        #                           Passe_barrières, passe au travers de certaines portes
        #                           Passe_mur, ignore les murs
        #Exemple de syntaxe du mode de propagation : "Sd_T_Pp", "CD_S_Pm" ou "R__T___"

        if reset:
            for i in range(len(self.matrice_cases)):
                for j in range(len(self.matrice_cases[0])):
                    self.matrice_cases[i][j].clarte = 0

        dirs = [HAUT,DROITE,BAS,GAUCHE]
        forme = propagation[0]
        if forme == "R":
            dirs = [direction]
        elif forme == "S":
            dirs.remove(dirs[direction-2])
        elif forme == "Q":
            dirs.remove(dirs[direction-2])
            dirs.remove(dirs[direction-3])

        #la queue est une liste de positions
        queue=[(position,dirs,propagation)]

        self.matrice_cases[position[1]][position[2]].clarte = portee

        retrait = 1

        

        while len(queue)!=0 :

            
            data=queue[0]
            position = data[0]
            if action == "vue":
                retrait = self.matrice_cases[position[1]][position[2]].opacite
            clarte = self.matrice_cases[position[1]][position[2]].clarte - retrait
            #enlever position dans queue
            queue.pop(0)

            if not position in dead_ends:
                #trouver les positions explorables
                positions_voisins=self.voisins_case(data)

                datas_explorables = self.positions_utilisables(positions_voisins,data)

                for data_explorable in datas_explorables:
                    pos = data_explorable[0]
                    if clarte > self.matrice_cases[pos[1]][pos[2]].clarte :
                        #on marque la case comme visitée
                        self.matrice_cases[pos[1]][pos[2]].clarte = clarte
                        
                        #on ajoute toutes les directions explorables
                        queue.append(data_explorable)

        if action == "vue":
            matrice_cases = [[self.matrice_cases[i][j].get_infos((self.id,i,j)) for j in range(len(self.matrice_cases[0]))] for i in range(len(self.matrice_cases))]
        else :
            matrice_cases = self.matrice_cases

        return matrice_cases

    def voisins_case(self,data):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
        et qui renvoie les voisins de la case
        ainsi que leurs coordonnées
        """
        position = data[0]
        propagation = data[2]
        deplacement = propagation[3]
        positions_voisins=[]
        #on élimine les voisins aux extrémitées
        if deplacement == "S":
            if position[2]-1>=0:
                positions_voisins.append((position[0],position[1],position[2]-1))
            else:
                positions_voisins.append(None)
                
            if position[1]+1<self.largeur:
                positions_voisins.append((position[0],position[1]+1,position[2]))
            else:
                positions_voisins.append(None)
                
            if position[2]+1<self.hauteur:
                positions_voisins.append((position[0],position[1],position[2]+1))
            else:
                positions_voisins.append(None)
                
            if position[1]-1>=0:
                positions_voisins.append((position[0],position[1]-1,position[2]))
            else:
                positions_voisins.append(None)
        elif deplacement == "T":
            for i in range(4):
                cible = self.matrice_cases[position[1]][position[2]].murs[i].get_cible()
                if cible != None:
                    if cible[0] != position[0]:
                        cible = None
                positions_voisins.append(cible)
        else:
            print("Propagation inconnue")

        return positions_voisins

    def positions_utilisables(self,positions_voisins,data):
        """
        Fonction qui prend en entrées:
            les voisins de la case
            les positions des voisins
            la position de la case
            le chemin deja exploré
        et qui renvoie les directions ou l'on peut passer
        """
        position = data[0]
        directions = data[1]
        propagation = data[2]
        forme = propagation[0]
        degenerescence = propagation[1]
        deplacement = propagation[3]
        passage = propagation[6]
        datas_utilisables=[]
        cardinaux = [HAUT,DROITE,BAS,GAUCHE]

        for direction in directions:
            if positions_voisins[direction]!=None:
                voisin = positions_voisins[direction]

                #on vérifie si on peut passer
                blocage = self.matrice_cases[position[1]][position[2]].get_mur_dir(direction).get_blocage()
                if blocage != "Imp" and (passage=="m" or (blocage!="Ple" and ((passage=="p" and (blocage == "Por" or blocage == "P_b")) or (passage=="b" and (blocage == "Bar" or blocage == "P_b")) or blocage == None))):

                    #On détermine éventuellement la nouvelle forme de propagation
                    if degenerescence == "d":
                        if forme == "C":
                            nouv_prop = "S_"+propagation[2:]
                        elif forme == "S":
                            nouv_prop = "Q_"+propagation[2:]
                        elif forme == "Q":
                            nouv_prop = "R_"+propagation[2:]
                    elif degenerescence == "D":
                        if forme == "C":
                            nouv_prop = "Sd"+propagation[2:]
                        elif forme == "S":
                            nouv_prop = "Qd"+propagation[2:]
                    else:
                        nouv_prop = propagation

                    if forme=="R":
                        nouv_dir=[direction]
                    elif forme!="C":
                        #On détermine la direction d'où l'on vient
                        if deplacement=="S":
                            dir_back = cardinaux[direction-2]
                        elif deplacement=="T":
                            dir_back = 0
                            for i in cardinaux:
                                if self.matrice_cases[voisin[1]][voisin[2]].get_mur_dir(i).get_cible()==position:
                                    dir_back = i
                        #On n'y retournera pas !
                        nouv_dir=[]
                        for i in directions:
                            if i!=dir_back:
                                nouv_dir.append(i)
                    else:
                        nouv_dir=[HAUT,DROITE,BAS,GAUCHE]

                    nouv_data=(voisin,nouv_dir,nouv_prop)

                    datas_utilisables.append(nouv_data)
        return datas_utilisables

class Generateur:
    def __init__(self,matrice_cases,depart,largeur,hauteur,paterns,modeGeneration="Profondeur"):
        #print("Initialisation du générateur")
        self.depart = depart
        self.largeur = largeur
        self.hauteur = hauteur
        self.matrice_cases = matrice_cases
        self.modeGeneration = modeGeneration
        self.paterns = paterns
        self.poids = [1,1,1,1]

    def generation(self,proba=None,nbMurs=None,pourcentage=None):
        """
        Fonction qui permet de générer une matrice conformément au paramètres
        et au paterns
        Entrées:
            -L'éventuelle probabilité pour casser des murs
            -L'éventuel nombre de murs casser
            -L'éventuelle pourcentage de murs a casser
        Sorties:une matrice de cases générée
        """
        #print("Génération")
        matrice=None
        
        self.pre_gene_paterns()
        if self.modeGeneration=="Profondeur":
            #print("Mode de génération : profondeur")
            matrice= self.generation_en_profondeur()
            #print("Génération en profondeur : check")
            #on casse les murs conformément aux paramètres
            self.casser_X_murs(proba,nbMurs,pourcentage)
        else:
            print("mode de génération choisi incompatible")

        self.post_gene_paterns()
        
        return matrice

    def pre_gene_paterns(self):
        """
        Fonction qui pregenere les paterns
        (on génère le squelette)
        """
        if self.paterns != None:
            for patern in self.paterns :
                patern.pre_generation(self.matrice_cases)

    def post_gene_paterns(self):
        """
        Fonction qui postgenere les paterns
        (on remplie les patterns)
        """
        if self.paterns != None:
            for patern in self.paterns :
                patern.post_generation(self.matrice_cases)

    def generation_en_profondeur(self):
        """
        Fonction qui génère la matrice avec la méthode du parcours en profondeur
        Entrées:Rien
        Sorties:une matrice de cases générée avec le parcours en profondeur
        """
        rdm=random.randrange (1,10**18,1)

        #on définit la seed de notre générateur
        #cela permet d'avoir le meme résultat
        #rdm=851353618387733257
        #print("seed ",rdm)
        random.seed(rdm)

        #print("Début de la génération")
        #position dans la matrice
        position = self.depart
        #le stack est une liste de positions
        stack=[position]
    

        while len(stack)!=0 :
            
            #on récupère les coords de là où l'on est cad la dernière case dans le stack
            position = stack[len(stack)-1]
            
            murs_generables = self.murs_utilisables(position)

            if len(murs_generables) > 0 : 
                
                #randrange est exclusif
                num_mur=self.randomPoids(murs_generables)
                
                #direction du mur à casser
                direction_mur=murs_generables[num_mur]

                mur = self.matrice_cases[position[1]][position[2]].murs[direction_mur]

                self.casser_mur(mur)

                new_pos = mur.get_cible()
                #on ajoute les nouvelles coordonnées de la case au stack
                stack.append(new_pos)
            else:
                #on revient encore en arrière
                stack.pop()

        #print("Fini")
        
        return self.matrice_cases

    def murs_utilisables(self,position,murs_requis = 4):
        """
        Fonction qui prend en entrées:
            les voisins de la case
        et qui renvoie les directions ou les murs sont cassables
        """
        murs_utilisables=[]

        for i in range(4):
            mur = self.matrice_cases[position[1]][position[2]].murs[i] #mur = self.matrice_cases[position[1][0]][position[1][1]].murs[i]
            cible = mur.get_cible()
            if cible != None and cible[0]==self.depart[0]:
                case_cible = self.matrice_cases[cible[1]][cible[2]]
                mur_oppose = self.get_mur_oppose(mur)
                if mur_oppose != None and case_cible.nb_murs_pleins()>=murs_requis and mur_oppose.is_touchable() and mur.is_touchable():
                    murs_utilisables.append(i)
        return murs_utilisables

    def randomPoids(self,murs_utilisables):
        """
        Fonction qui prend en entrée:
            les murs utilisables par la fonction
        et qui renvoie le numéro d'un mur générée avec un alétoire modifié
        """

        nbrandom=0
        res=-1
        
        poids_selectionnees=[]
        poids_total=0

        for i in range (0,len(murs_utilisables)):
            poids_selectionnees+=[poids_total+self.poids[murs_utilisables[i]]]
            poids_total+=self.poids[murs_utilisables[i]]

        nbrandom=random.randrange(0,poids_total)

        i=0

        while i<len(poids_selectionnees) and res==-1:
            if nbrandom < poids_selectionnees[i]:
                res=i
            i+=1
        return res

    def casser_X_murs(self,proba=None,nbMurs=None,pourcentage=None):
        """
        Fonction qui doit casser des murs sur la matrice
        on peut déterminer le nombre de murs avec un probabilité (proba*nb murs au total)
        ou selon un nombre défini en entrée
        ou un pourcentage
        """
        if proba!=None:
            self.casser_murs_selon_proba(proba)
        elif nbMurs!=None:
            self.casser_murs(nbMurs)
        elif pourcentage!=None:
            self.casser_murs(int(pourcentage/100*self.nb_murs_total()))
        else:
            print("mauvaise utilisation de la fonction, on ne sait que faire")

    def casser_murs(self,nb_murs_a_casser):
        """
        Fonction qui casse un certains nombre de murs aléatoirement
        Entrées:
            -le nombre de murs a casser
        """
        nb_murs_casser=0

        while nb_murs_casser<=nb_murs_a_casser:
            coord_case=[random.randrange(0,len(self.matrice_cases)),random.randrange(0,len(self.matrice_cases[0]))]

            if self.casser_mur_random_case(coord_case):
                nb_murs_casser+=1


    def restrictions_case(self,coord_case):
        """
        Fonction qui renvoie les murs intouchables
        Entrées:
            -les coordonnées de le case
        Sorties:
            -les directions ou les murs ne sont pas touchables
        """
        directions_interdites=[]

        murs=self.matrice_cases[coord_case[0]][coord_case[1]].get_murs()
        for i in range(0,4):
            if not(murs[i].is_touchable):
                directions_interdites.append(i)
            
        return directions_interdites

    def casser_mur_random_case(self,position_case):
        """
        Fonction qui prend en entrée la position de la case dont on veut casser un mur
        et qui renvoie un booléen indiquant si l'on as pu casser un mur
        """
        casser = False

        murs=self.murs_utilisables(self.voisins_case(position_case[0],position_case[1]))
        if len(murs)!=0:
            mur_a_casser=random.randrange(0,len(murs))
            self.casser_mur(self.matrice_cases[position_case[0]][position_case[1]].murs[murs[mur_a_casser]])
            casser = True
        return casser

    def casser_murs_selon_proba(self,proba):
        """
        Fonction qui casse des murs selon une probabilité donnée
        Entrée:
            -la probabilité de casser un mur
        """
        for x in range(1,self.largeur) :
            for y in range(1,self.hauteur) :
                case = self.matrice_cases[x][y]
                murs=self.murs_utilisables((self.depart[0],x,y),0)
                if HAUT in murs and random.random() <= proba :
                    self.casser_mur(case.murs[HAUT])
                if GAUCHE in murs and random.random() <= proba :
                    self.casser_mur(case.murs[GAUCHE])
                    
    def casser_mur(self,mur):
        """
        Fonction qui casse un mur spécifique
        Entrées:
            la direction du mur
            la position de la case
        Sorites:Rien
        """
        #on casse les murs de la case et de la case d'en face
        autre_mur = self.get_mur_oppose(mur)
        if autre_mur ==  None :
            print("On a un mur non réciproque !")
        else :
            mur.brise()
            autre_mur.brise()

    def nb_murs_total(self):
        """
        Fonction qui renvoie le nombres de murs pleins contenus dans le labyrinthe
        """
        murs_pleins=0
        for x in range(0,self.largeur):
            for y in range(0,self.hauteur):
                murs_pleins+=self.matrice_cases[x][y].nb_murs_pleins()
        
        return int((murs_pleins-self.hauteur*2-self.largeur*2)/2)

    def get_mur_oppose(self,mur):
        cible = mur.get_cible()
        mur_oppose = None
        if cible != None and cible[0] == self.depart[0]:
            for mur_potentiel in self.matrice_cases[cible[1]][cible[2]].murs :
                cible_potentielle = mur_potentiel.get_cible()
                if cible_potentielle != None and cible_potentielle[0] == self.depart[0]:
                    if mur in self.matrice_cases[cible_potentielle[1]][cible_potentielle[2]].murs : #Les murs sont réciproques (attention deux murs d'une même case ne peuvent pas mener à la même autre case !
                        mur_oppose = mur_potentiel
        return mur_oppose

class Case:
    def __init__(self,position,effets = [],opacite = 1):
        # Par défaut, pas de murs.
        self.murs = [Mur([Teleport((position[0],position[1],position[2]-1))]),Mur([Teleport((position[0],position[1]+1,position[2]))]),Mur([Teleport((position[0],position[1],position[2]+1))]),Mur([Teleport((position[0],position[1]-1,position[2]))])]
        self.opacite = opacite
        self.clarte = 0
        self.effets = effets #Les cases ont aussi des effets !
        self.controleur = None

    #Découvrons le déroulé d'un tour, avec case-chan :
    def debut_tour(self):
        #Un nouveau tour commence, qui s'annonce remplit de bonnes surprises et de nouvelles rencontres ! On commence par activer les effets réguliers :
        for effet in self.effets:
            if isinstance(effet,On_debut_tour):
                effet.execute(self) #On exécute divers effets
            if isinstance(effet,Time_limited):
                effet.wait()

    #Les agissants prennent des décisions, agissent, se déplacent, les items se déplacent aussi.
    def veut_passer(self,intrus,direction):
        """Fonction qui tente de faire passer une entitée.
           Se réfère au mur compétent, qui gère tout."""
        self.murs[direction].veut_passer(intrus)

    def step_out(self,entitee):
        for effet in self.effets:
            if isinstance(effet,On_step_out):
                effet.execute(entitee)

    def step_in(self,entitee):
        for effet in self.effets:
            if isinstance(effet,On_step_in):
                effet.execute(entitee) #On agit sur les agissants qui arrivent (pièges, téléportation, etc.)

    #Tout le monde a fini de se déplacer.
    def post_action(self,position):
        for effet in self.effets:
            if isinstance(effet,On_post_action):
                effet.execute(position) #On exécute divers effets, principalement protéger ses occupants.

    #Le tour se termine gentiment, et on recommence !

#Pour la génération, quand on a pas encore les barrières, portes et compagnie.
    def nb_murs_pleins(self):
        """
        Fonction qui renvoie le nombre de murs pleins dans la case
        """
        pleins=0

        for mur in self.murs :
            if mur.is_ferme() :
                pleins+=1
        
        return pleins
                
    def casser_mur(self,direction):
        """
        Fonction qui casse le mur dans la direction indiquée
        """
        self.murs[direction].brise()

    def construire_mur(self,direction,durete):
        """
        Fonction qui construit le mur dans la direction indiquée
        """
        self.murs[direction].construit(durete)

    def interdire_mur(self,direction):
        """
        Fonction qui construit le mur impassable dans la direction indiquée
        """
        self.murs[direction].interdit()

    def mur_plein(self,direction):
        """
        Fonction qui indique si le mur indiquée par la direction est plein ou non
        """
        return self.murs[direction].is_ferme()

    def murs_pleins(self):
        directions = []
        for direction in [HAUT,DROITE,BAS,GAUCHE]:
            if self.mur_plein[direction]:
                directions.append(direction)
        return directions

    def get_mur_dir(self,direction):
        return self.murs[direction]

    def get_murs(self):
        return self.murs

    def get_mur_haut(self):
        return self.murs[0]

    def get_mur_droit(self):
        return self.murs[1]

    def get_mur_bas(self):
        return self.murs[2]

    def get_mur_gauche(self):
        return self.murs[3]

    def toString(self):
        return "haut "+str(self.murs[0].get_etat())+" droite "+str(self.murs[1].get_etat())+" bas "+str(self.murs[2].get_etat())+" gauche "+str(self.murs[3].get_etat())+"  "

    def get_opacite(self):
        return self.opacite

    def get_infos(self,position):
        return [position,self.clarte,0,0,0,self.calcule_code(),[not self.mur_plein(i) for i in range(4)],[]]

    def calcule_code(self):#La fonction qui calcule le code correpondant à l'état de la case. De base, 0. Modifié d'après les effets subits par la case.
        return 0

    def get_image(self): #À changer plus tard
        images_effets = []
        for effet in self.effets:
            images_effets.append(effet.get_image())
        images_murs = []
        if self.mur_plein(HAUT):
            images_murs.append(Mur_vue_haut())
        if self.mur_plein(BAS):
            images_murs.append(Mur_vue_bas())
        if self.mur_plein(DROITE):
            images_murs.append(Mur_vue_droite())
        if self.mur_plein(GAUCHE):
            images_murs.append(Mur_vue_gauche())
        return Case_vue(images_murs,images_effets,self.clarte)

    def get_copie(self):
        copie = Case((0,0,0),self.effets,self.opacite)
        copie.murs = self.murs
        return copie

    def active(self,controleur):
        self.controleur = controleur
        for mur in self.murs :
            mur.active(controleur)

    def desactive(self):
        self.controleur = None
        for effet in self.effets :
            effet.desactive()
        for mur in self.murs :
            mur.desactive()

class Mur:
    def __init__(self,effets):
        self.effets = effets
        self.peut_passer = False
        self.controleur = None

    def is_ferme(self):
        ferme = False
        for effet in self.effets :
            if isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not(effet.casse)) or (isinstance(effet,Porte) and effet.ferme):
                ferme = True
        return ferme

    def get_blocage(self):
        blocage = None
        for effet in self.effets :
            if isinstance(effet,Mur_impassable):
                blocage = "Imp"
            elif blocage != "Imp" and (isinstance(effet,Mur_plein) and not(effet.casse)):
                blocage = "Ple"
            elif blocage != "Imp" and blocage != "Ple" and (isinstance(effet,Porte_barriere) and effet.ferme):
                blocage = "P_b"
            elif blocage != "Imp" and blocage != "Ple" and blocage != "P_b" and (isinstance(effet,Porte) and effet.ferme):
                blocage = "Por"
            elif blocage != "Imp" and blocage != "Ple" and blocage != "P_b" and isinstance(effet,Barriere):
                blocage = "Bar"
        return blocage

    def is_touchable(self):
        touchable = True
        for effet in self.effets :
            if isinstance(effet,(Mur_impassable)):
                touchable = False
        return touchable

    def veut_passer(self,intrus):
        self.peut_passer = True
        for effet in self.effets :
            if isinstance(effet,On_try_through):
                effet.execute(self,intrus) #On vérifie que rien n'empêche le passage de l'intrus
        if self.peut_passer :
            for effet in self.effets :
                if isinstance(effet,On_through):
                    effet.execute(intrus) #Il est conseillé d'avoir un seul effet de déplacement, comme un seul effet d'autorisation de passage...

    def interdit(self):
        self.effets.append(Mur_impassable())

    def construit(self,durete):
        self.effets.append(Mur_plein(durete))

    def detruit(self):
        for i in range(len(self.effets)-1,-1,-1) :
            effet = self.effets[i]
            if isinstance(effet,On_try_through):
                self.effets.remove(effet)
                del(effet)

    def brise(self):
        for i in range(len(self.effets)-1,-1,-1) :
            effet = self.effets[i]
            if isinstance(effet,On_try_through) and not isinstance(effet,Mur_impassable) :
                self.effets.remove(effet)
                del(effet)

    def get_cible(self):
        cible = None
        en_cours = True
        i = 0
        while en_cours and i < len(self.effets) :
            effet = self.effets[i]
            if isinstance(effet,Teleport) :
                en_cours = False
                cible = effet.position
            i += 1
        return cible

    def set_cible(self,position,surnaturel = False):
        for effet in self.effets:
            if isinstance(effet,Teleport):
                self.effets.remove(effet)
        self.effets.append(Teleport(position,surnaturel))

    def get_mur_oppose(self):
        mur_oppose = None
        cible = self.get_cible()
        if cible != None:
            case_cible = self.controleur.get_case(cible)
            for mur in case_cible.murs :
                cible_potentielle = mur.get_cible()
                if cible_potentielle != None:
                    case_cible_potentielle = self.controleur.get_case(cible_potentielle)
                    if self in case_cible_potentielle.murs:
                        mur_oppose = mur
        return mur_oppose
        

    def active(self,controleur):
        self.controleur = controleur

    def desactive(self):
        self.controleur = None

class Patern:
    def __init__(self,position,largeur,hauteur,entrees=[(0,1,0)],codes=[],vide = True,durete = 1):
        self.position = position
        self.hauteur = hauteur
        self.largeur = largeur
        self.matrice_cases = [[Case((self.position[0],j+self.position[1],i+self.position[2])) for i in range(hauteur)]for j in range(largeur)]
        self.entrees = entrees
        self.codes = codes
        self.vide = vide
        self.durete = durete

    def post_gen_entrees(self,matrice_lab):
        """
        Fonction qui transforme les entrées en portes ou en murs vides
        """
        
        for nb in range(len(self.entrees)):
            x = self.entrees[nb][1]+self.position[1]
            y = self.entrees[nb][2]+self.position[2]
            case = matrice_lab[x][y]
            for bord in self.contraintes_cases(self.entrees[nb]):
                mur = case.murs[bord]
                if nb < len(self.codes) :
                    mur.brise()
                    mur.effets.append(Porte(self.durete,self.codes[nb]))
                    mur_oppose = self.get_mur_oppose(mur,matrice_lab)
                    if mur_oppose != None :
                        mur_oppose.brise()
                        mur_oppose.effets.append(Porte(self.durete,self.codes[nb]))
                else :
                    mur.brise()
                    mur_oppose = self.get_mur_oppose(mur,matrice_lab)
                    if mur_oppose != None :
                        mur_oppose.brise()

    def pre_generation(self,matrice_lab):
        """
        Fonction qui prend en entrée:
            la matrice de cases du labyrinthe
        et qui pre génère les cases du patern
        """
        coordonnee_x = self.position[1]
        coordonnee_y = self.position[2]
        for i in range(coordonnee_x,coordonnee_x+self.largeur):
            for j in range(coordonnee_y,coordonnee_y+self.hauteur):
                x_pat=i-coordonnee_x
                y_pat=j-coordonnee_y
                #on ne doit générer que les cases au bords
                #plus précisement on doit empêcher le générateur d'y toucher
                if not self.case_est_une_entree((self.position[0],x_pat,y_pat)) and self.case_au_bord((self.position[0],x_pat,y_pat)):
                    dirs_intouchables=self.contraintes_cases((self.position[0],x_pat,y_pat))
                    for direction in dirs_intouchables:
                        mur = matrice_lab[i][j].murs[direction]
                        mur.interdit()
                        mur_oppose = self.get_mur_oppose(mur,matrice_lab)
                        if mur_oppose != None :
                            mur_oppose.interdit()

    def post_generation(self,matrice_lab):
        """
        Fonction qui prend en entrée:
            la matrice de cases du labyrinthe
        et qui clear la salle
        """
        for i in range(self.position[1],self.position[1]+self.largeur):
            for j in range(self.position[2],self.position[2]+self.hauteur):
                pos_pat = (self.position[0],i-self.position[1],j-self.position[2])
                #on enlève les murs intouchables
                dirs_intouchables=[]
                if self.case_au_bord(pos_pat):
                    dirs_intouchables=self.contraintes_cases(pos_pat)
                for direction in [HAUT,DROITE,BAS,GAUCHE]:
                    mur = matrice_lab[i][j].murs[direction]
                    if direction in dirs_intouchables:
                        mur.detruit()
                        mur.construit(self.durete)
                        mur_oppose = self.get_mur_oppose(mur,matrice_lab)
                        if mur_oppose != None :
                            mur_oppose.detruit()
                            mur_oppose.construit(self.durete)
                    elif self.vide:
                        mur.detruit()
        self.post_gen_entrees(matrice_lab)
            
    def case_est_une_entree(self,position):
        """
        Fonction qui prend en entrées:
            les coordonnées de la case
        et qui renvoie un booléen indiquant si elle est une entrée ou pas
        """
        est_entree=False
        for entree in self.entrees:
            if entree == position:
                est_entree=True

        return est_entree
    def case_au_bord(self,position):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
        et qui renvoie un booléen indiquant si la case est au bord ou non
        """
        return (position[1] == 0 or position[1] == self.largeur-1)or(position[2] == 0 or position[2] == self.hauteur-1)
        
    def clear_case(self,position):
        """
        Fonction qui clear la case selectionner
        """
        for i in range(0,4):
            self.matrice_cases[position[1]][position[2]].casser_mur(i)
    
    def incorporation_case(self,position):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
            et génère les murs en fonction de sa position
        """
        #on casse les murs qui ne sont pas aux extrèmes
        if position[1]!=0:
            self.matrice_cases[position[1]][position[2]].casser_mur(GAUCHE)
            
        if position[1]!=(self.largeur-1):
            self.matrice_cases[position[1]][position[2]].casser_mur(DROITE)

        if position[2]!=0:
            self.matrice_cases[position[1]][position[2]].casser_mur(HAUT)
            
        if position[2]!=(self.hauteur-1):
            self.matrice_cases[position[1]][position[2]].casser_mur(BAS)

    
    
    def integration_case(self,position,matrice_lab):
        """
        Fonction qui prend en enetrées:
            les coordonnées de la case
            la matrice du labyrinthe

        et casse les murs qui empêches la navigation dans le labyrinthe
        """

        bords=self.case_bord(position,len(matrice_lab),len(matrice_lab[0]))

        for bord in bords:
            mur = matrice_lab[position[1]][position[2]].murs[bord]
            mur_oppose=self.get_mur_oppose(mur,matrice_lab)
            if mur_oppose!=None and not(mur.is_ferme()):
                mur.briser()

    def case_bord(self,position,largeur_mat,hauteur_mat):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
            la largeur et la hauteur de la matrice
            et qui renvoie la/les direction/s des bords
        """
        bords=[]
        
        #on ajoute les murs qui ne sont pas aux extrèmes
        if position[1]!=0:
            bords+=[GAUCHE]
            
        if position[1]!=(largeur_mat-1):
            bords+=[DROITE]

        if position[2]!=0:
            bords+=[HAUT]
            
        if position[2]!=(hauteur_mat-1):
            bords+=[BAS]

        return bords

    def contraintes_cases(self,position):
        """
        Fonction qui renvoie les murs qui sont soumis a des contraintes
        venant de la salle
        Entrées:
            -les coordonnées de la case
        Sorties:
            -les directions des murs a ne pas caser
        """
        #pour l'instant les contraintes se limites justes au bords de la matrice
        bords=[]
        
        if position[1]==0:
            bords+=[GAUCHE]
            
        if position[1]==(self.largeur-1):
            bords+=[DROITE]

        if position[2]==0:
            bords+=[HAUT]
            
        if position[2]==(self.hauteur-1):
            bords+=[BAS]

        return bords

    def copie(self,position,matrice_lab):
        """
        Fonction qui prend en entrée:
            les coordonnées de base du patern dans le labyrinthe
            la matrice de cases du labyrinthe
        et qui copie les cases du patern dans le labyrinthe
        """
        for i in range(position[1],position[1]+self.largeur):
            for j in range(position[2],position[2]+self.hauteur):
                matrice_lab[i][j]=self.matrice_cases[i-position[1]][j-position[2]]
                self.integration_case((self.position[0],i,j),matrice_lab)
        return matrice_lab

    def get_pos(self):
        return self.position

    def get_mur_oppose(self,mur,matrice_lab):
        cible = mur.get_cible()
        mur_oppose = None
        if cible != None:
            if cible[0] == self.position[0]:
                for mur_potentiel in matrice_lab[cible[1]][cible[2]].murs :
                    cible_potentielle = mur_potentiel.get_cible()
                    if cible_potentielle != None:
                        if cible_potentielle[0] == self.position[0]:
                            if mur in matrice_lab[cible_potentielle[1]][cible_potentielle[2]].murs : #Les murs sont réciproques (attention deux murs d'une même case ne peuvent pas mener à la même autre case !
                                mur_oppose = mur_potentiel
        return mur_oppose

class Entitee:
    """La classe des entitées physiques."""
    def __init__(self,position):
        self.position = position
        self.latence = 0
        self.effets = []
        self.controleur = None
        global ID_MAX
        ID_MAX += 1
        self.ID = ID_MAX

    def set_position(self,position):
        self.position = position

    def ajoute_effet(self,effet):
        self.effets.append(effet)

    def get_position(self):
        return self.position

    def get_direction(self):
        return HAUT

    def get_skin(self):
        return SKIN_MYSTERE

    def set_latence(self,latence):
        self.latence = latence

    def active(self,controleur):
        self.controleur = controleur

    def desactive(self):
        self.controleur = None

class Entitee_superieure(Entitee):
    """La classe des entitées qui font bouger le labyrinthe autour d'eux."""
    pass

class Fantome(Entitee):
    """La classe des entitées qui traversent les murs."""
    pass

class Agissant(Entitee): #Tout agissant est un cadavre, tout cadavre n'agit pas.
    """La classe des entitées animées. Capable de décision, de différentes actions, etc. Les principales caractéristiques sont l'ID, les stats, et la classe principale."""
    def __init__(self,position,pv,pv_max,regen_pv,pm,pm_max,regen_pm,force,priorite,vitesse,affinite_ombre,affinite_feu,affinite_terre,affinite_glace,classe_principale):

        Entitee.__init__(self,position)

        self.pv=pv
        self.pv_max=pv_max
        self.regen_pv=regen_pv
        self.taux_regen_pv = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à la régénération des pv. Correspond aux effets passager sur la régénération des pv.
        self.pm=pm
        self.pm_max=pm_max
        self.regen_pm=regen_pm
        self.taux_regen_pm = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à la régénération des pm. Correspond aux effets passager sur la régénération des pm.
        self.force=force
        self.taux_force = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à la force. Correspond aux effets passager sur la force.
        self.priorite=priorite
        self.taux_priorite = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à la priorité. Correspond aux effets passager sur la priorité.
        self.vitesse = vitesse
        self.taux_vitesse = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à la vitesse. Correspond aux effets passager sur la vitesse.
        self.aff_o=affinite_ombre
        self.taux_aff_o = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à l'affinité à l'ombre. Correspond aux effets passager sur l'affinité à l'ombre.
        self.aff_f=affinite_feu
        self.taux_aff_f = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à l'affinité au feu. Correspond aux effets passager sur l'affinité au feu.
        self.aff_t=affinite_terre
        self.taux_aff_t = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à l'affinité à la terre. Correspond aux effets passager sur l'affinité à la terre.
        self.aff_g=affinite_glace
        self.taux_aff_g = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à l'affinité à la glace. Correspond aux effets passager sur l'affinité à la glace.
        self.taux_stats = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer aux statistiques. Correspond aux effets passager sur les statistiques. (Inclure les regen dans les stats ?)
        self.classe_principale = classe_principale
        self.classe_principale.evo()
        self.etat = "vivant"

        #vue de l'agissant
        self.vue = None
        self.position_vue = None
        self.vue_nouvelle = False

        self.offenses=[]
        self.esprit=None

        #possessions de l'agissant
        self.inventaire = Inventaire(self.ID,0)

        #la direction du regard
        self.skill_courant = None
        self.dir_regard = 0
        self.latence = 0

    def active(self,controleur):
        self.controleur = controleur
        self.inventaire.active(controleur)

    def desactive(self):
        self.inventaire.desactive()
        self.controleur = None

    def get_stats_attaque(self,element):
        force = self.force
        for taux in self.taux_force.values():
            force *= taux
        affinite = self.get_aff(element)
        for taux in self.taux_stats.values():
            force *= taux
            affinite *= taux
        return force,affinite,self.dir_regard,self.ID

    def get_direction(self):
        return self.dir_regard

    def get_arme(self):
        return self.inventaire.get_arme()

    def get_bouclier(self):
        return self.inventaire.get_bouclier()

    def get_clees(self):
        return self.inventaire.get_clees()

    def get_item_lancer(self):
        return self.inventaire.get_item_courant()

    def insurge(self,offenseur,gravite):
        self.offenses.append([offenseur,gravite])

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        etat = "vivant" #Rajouter des précisions
        if self.etat != "vivant" or self.controleur == None:
            etat = "incapacite"
        return offenses, etat

    def get_aff(self,element):
        affinite = 1
        if element == OMBRE :
            affinite = self.aff_o
            for taux in self.taux_aff_o.values():
                affinite *= taux
        elif element == FEU :
            affinite = self.aff_f
            for taux in self.taux_aff_f.values():
                affinite *= taux
        elif element == TERRE :
            affinite = self.aff_t
            for taux in self.taux_aff_t.values():
                affinite *= taux
        elif element == GLACE :
            affinite = self.aff_g
            for taux in self.taux_aff_g.values():
                affinite *= taux
        else :
            print(element + "... quel est donc cet élément mystérieux ?")
        return affinite

    def peut_payer(self,cout):
        skill = trouve_skill(self.classe_principale,Skill_magie_infinie)
        res = True
        if skill == None:
            res = self.get_total_pm() >= cout
        return res

    def paye(self,cout):
        #On paye d'abord avec le mana directement accessible
        if self.pm >= cout:
            self.pm -= cout #Si on peut tout payer, tant mieux.
        else :
            cout_restant = cout
            if self.pm > 0:
                self.pm = 0
                cout_restant -= self.pm
            if cout_restant > 0: #Sinon, on fait appel aux éventuelles réserves de mana
                i = 0
                while cout_restant > 0 and i < len(self.effets):
                    if isinstance(self.effets[i],Reserve_mana):
                        reserve = self.effets[i]
                        if reserve.mana >= cout_restant:
                            reserve.execute(cout_restant)
                            cout_restant = 0
                        else :
                            cout_restant -= reserve.mana
                            reserve.execute(reserve.mana)
                    i += 1
            if cout_restant > 0: # Si ce n'est toujours pas assez, on utilise la magie infinie (on aurait pas pu payer plus sans ça, donc on l'a forcement !)
                self.pm -= cout_restant

    def get_total_pm(self):
        total = self.pm
        for effet in self.effets:
            if isinstance(effet,Reserve_mana):
                total += effet.mana
        return total

    def get_total_regen_pv(self):
        regen_pv = self.regen_pv
        for taux in self.taux_regen_pv.values() :
            regen_pv *= taux
        for taux in self.taux_stats.values() :
            regen_pv *= taux
        return regen_pv

    def get_total_regen_pm(self):
        regen_pm = self.regen_pm
        for taux in self.taux_regen_pm.values() :
            regen_pm *= taux
        for taux in self.taux_stats.values() :
            regen_pm *= taux
        return regen_pm

    def get_vitesse(self):
        vitesse = self.vitesse
        for taux in self.taux_vitesse.values() :
            vitesse *= taux
        for taux in self.taux_stats.values() :
            vitesse *= taux
        return vitesse

    def get_priorite(self):
        priorite = self.priorite
        for taux in self.taux_priorite.values() :
            priorite *= taux
        for taux in self.taux_stats.values() :
            priorite *= taux
        return priorite

    def subit(self,degats,ID=0): #L'ID 0 ne correspond à personne
        gravite = degats/self.pv_max
        if gravite > 1: #Si c'est de l'overkill, ce n'est pas la faute de l'attaquant non plus !
            gravite = 1
        if self.pv <= self.pv_max//3: #Frapper un blessé, ça ne se fait pas !
            gravite += 0.2
        if self.pv <= self.pv_max//9: #Et un mourrant, encore moins !!
            gravite += 0.3
        self.pv -= degats
        if self.pv <= 0: #Alors tuer les gens, je ne vous en parle pas !!!
            gravite += 0.5
        self.insurge(ID,gravite)

    def soigne(self,soin):
        self.pv += soin

    def rejoint(self,nom_esprit):
        self.esprit = nom_esprit

    def meurt(self):
        self.pv = self.pm = 0
        self.etat = "mort"
        self.dir_regard = HAUT
        self.taux_regen_pv = self.taux_regen_pm = self.taux_force = self.taux_priorite = self.taux_vitesse = self.taux_aff_o = self.taux_aff_f = self.taux_aff_t = self.taux_aff_g = self.taux_stats = {}
        self.effets = []
        self.inventaire.drop_all(self.position)

    def get_esprit(self):
        return self.esprit

    def get_classe(self):
        if self.etat == "vivant":
            return Agissant
        if self.etat == "mort":
            return Cadavre
        if self.etat == "oeuf":
            return Oeuf

    def get_portee_vue(self):
        skill = trouve_skill(self.classe_principale,Skill_vision)
        if skill == None:
            print("Oups, je n'ai pas de skill vision ! Pourquoi ?")
            portee = 0
        else :
            portee = skill.utilise()
            portee *= self.get_aff(OMBRE) #Puisque c'est le manque de lumière qui réduit le champ de vision !
        return portee

    def get_skin(self):
        if self.etat == "vivant":
            if self.esprit == "1":
                return SKIN_VERT
            elif self.esprit == "2":
                return SKIN_ROUGE
            else:
                return SKIN_AGISSANT
        else:
            return SKIN_CADAVRE

    # Découvrons le déroulé d'un tour, avec agissant-san :
    def debut_tour(self):
        #Un nouveau tour commence, qui s'annonce remplit de bonnes surprises et de nouvelles rencontres ! Pour partir du bon pied, on a quelques trucs à faire :
        #La régénération ! Plein de nouveaux pm et pv à gaspiller ! C'est pas beau la vie ?
        self.pv += self.get_total_regen_pv()
        self.pm += self.get_total_regen_pm() #Et oui, les pm après, désolé...
        if self.pv > self.pv_max:
            self.pv = self.pv_max
        if self.pm > self.pm_max:
            self.pm = self.pm_max
        #Et les effets. Vous les voyez tous les beaux enchantements qui nous renforcent ?
        for effet in self.effets:
            if isinstance(effet,On_debut_tour):
                effet.execute(self) #On exécute divers effets
            if isinstance(effet,Time_limited):
                effet.wait()
        self.inventaire.debut_tour()
        self.latence -= self.get_vitesse()

    # Les esprits gambergent, tergiversent et hésitent.

    def post_decision(self):
        #On a pris de bonnes décisions pour ce nouveau tour ! On va bientôt pouvoir agir, mais avant ça, peut-être quelques effets à activer ?
        for effet in self.effets:
            if isinstance(effet,On_post_decision):
                effet.execute(self) #On exécute divers effets

    # Les agissants agissent, les items projetés se déplacent, éventuellement explosent.
    def on_action(self):
        #Si on a de la chance, on pourra jouer plusieurs fois dans le tour ! (Enfin, une fois que j'aurais modifié tout ça et créé les esprits...)
        self.skill_courant = None

    def post_action(self):
        #Le controleur nous a encore forcé à agir ! Quel rabat-joie, avec ses cout de mana, ses latences, ses "Vous ne pouvez pas utiliser un skill que vous n'avez pas." !
        attaques = []
        dopages = []
        for effet in self.effets:
            if isinstance(effet,On_post_action): #Les protections (générales) par exemple
                effet.execute(self)
            elif isinstance(effet,On_attack):
                dopages.append(effet)
            elif isinstance(effet,Attaque):
                attaques.append(effet)
        for attaque in attaques :
            for dopage in dopages:
                dopage.execute(attaque)
            attaque.execute(self.controleur) #C'est à dire qu'on attaque autour de nous. On n'en est pas encore à subir.

    # Tout le monde s'est préparé, a placé ses attaques sur les autres, etc. Les cases ont protégé leurs occupants.

    def pre_attack(self):
        #On est visé par plein d'attaques ! Espérons qu'on puisse se protéger.
        attaques = []
        on_attaques = []
        for effet in self.effets:
            if isinstance(effet,On_pre_attack): #Principalement les effets qui agissent sur les attaques
                on_attaques.append(effet)
            elif isinstance(effet,Attaque_particulier):
                attaques.append(effet)
        skill = trouve_skill(self.classe_principale,Skill_defense)
        taux = 1
        if skill != None :
            taux *= skill.utilise()
        for attaque in attaques :
            attaque.degats *= taux
            for on_attaque in on_attaques:
                on_attaque.execute(attaque)
            attaque.execute(self)

    # Les autres subissent aussi des attaques.

    def fin_tour(self):
        #Il est temps de voir si on peut encore recoller les morceaux.
        if self.pv <= 0:
            immortel = trouve_skill(self.classe_principale,Skill_immortel)
            if immortel != None :
                self.taux_stats["immortalité"] = immortel.utilise()
            else :
                essence = trouve_skill(self.classe_principale,Skill_essence_magique)
                if essence != None :
                    cout = essence.utilise(self.pv)
                    if peut_payer(cout):
                        paye(cout)
                    else :
                        self.meurt()
                else :
                    self.meurt()
        else :
            immortel = trouve_skill(self.classe_principale,Skill_immortel)
            if immortel != None :
                self.taux_stats.pop("immortalité")
        for effet in self.effets :
            if isinstance(effet,On_fin_tour):
                effet.execute(self)
            elif isinstance(effet,Maladie):
                effet.contagion(self)
            if effet.phase == "terminé":
                self.effets.remove(effet)
        self.inventaire.fin_tour()
        self.classe_principale.gagne_xp()

class Tank(Agissant):
    """La classe des agissants forts en défense."""
    def __init__(self,position,niveau):
        if niveau == 1:
            Agissant.__init__(self,position,150,150,0,0,0,0,3,1,1,1,1,2,1,Classe_principale([],[],False,"Tank",niveau))

        elif niveau == 2:
            Agissant.__init__(self,position,200,200,0,0,0,0,3,1,1,1,1,2,1,Classe_principale([],[],False,"Tank",niveau))

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur == None:
            etat = "incapacite"
        elif self.pv <= self.pv_max//9:
            etat = "fuite"
        else:
            etat = "attaque"
        return offenses, etat

    def get_skin(self):
        if self.etat == "vivant":
            if self.esprit == "1":
                return SKIN_VERT
            elif self.esprit == "2":
                return SKIN_ROUGE
            else:
                return SKIN_AGISSANT
        else:
            return SKIN_CADAVRE

class Dps(Agissant):
    """La classe des agissants forts en attaque."""
    def __init__(self,position,niveau):
        if niveau == 1:
            Agissant.__init__(self,position,50,50,0,0,0,0,5,1,2.1,1,1,1,1,Classe_principale([],[],False,"Dps",niveau))

        elif niveau == 2:
            Agissant.__init__(self,position,75,75,0,0,0,0,15,1,2.1,1,1,1,1,Classe_principale([],[],False,"Dps",niveau))

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur == None:
            etat = "incapacite"
        elif self.pv <= self.pv_max//2:
            etat = "fuite"
        else:
            etat = "attaque"
        return offenses, etat

    def get_skin(self):
        if self.etat == "vivant":
            if self.esprit == "1":
                return SKIN_VERT
            elif self.esprit == "2":
                return SKIN_ROUGE
            else:
                return SKIN_AGISSANT
        else:
            return SKIN_CADAVRE

class Soigneur(Agissant):
    """La classe des agissants qui soignent les autres."""
    def __init__(self,position,niveau):
        if niveau == 1:
            Agissant.__init__(self,position,50,50,0,100,100,0.1,1,1,0.9,1.5,1,1,1,Classe_principale([],[],False,"Soigneur",niveau))
            self.talent = 1
            self.magie_courante = None
            self.cible_magie = None
            magie = trouve_skill(self.classe_principale,Skill_magie)
            magie.ajoute(Magie_soin())
            magie.ajoute(Magie_auto_soin())
        if niveau == 2:
            Agissant.__init__(self,position,75,75,0,120,120,0.2,1,1,0.9,1.5,1,1,1,Classe_principale([],[],False,"Soigneur",niveau))
            self.talent = 1
            self.magie_courante = None
            self.cible_magie = None
            magie = trouve_skill(self.classe_principale,Skill_magie)
            magie.ajoute(Magie_soin())
            magie.ajoute(Magie_auto_soin())

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur == None:
            etat = "incapacite"
        elif self.pv <= 3*self.pv_max//4 or self.pm < 50:
            etat = "fuite"
        else:
            etat = "soin"
        return offenses, etat

    def get_skin(self):
        if self.etat == "vivant":
            if self.esprit == "1":
                return SKIN_VERT
            elif self.esprit == "2":
                return SKIN_ROUGE
            else:
                return SKIN_AGISSANT
        else:
            return SKIN_CADAVRE

class Renforceur(Agissant):
    """La classe des agissants qui renforcent les autres."""
    def __init__(self,position,niveau):
        if niveau == 1:
            Agissant.__init__(self,position,50,50,0.05,100,100,0.1,1,1,0.6,1.5,1.2,1,1.3,Classe_principale([],[],False,"Soigneur",niveau))
            self.talent = 1
            self.magie_courante = None
            self.cible_magie = None
            magie = trouve_skill(self.classe_principale,Skill_magie)
            magie.ajoute(Magie_enchantement_force())
        if niveau == 2:
            Agissant.__init__(self,position,75,75,0.05,120,120,0.2,1,1,0.7,1.6,1.3,1.1,1.4,Classe_principale([],[],False,"Soigneur",niveau))
            self.talent = 1
            self.magie_courante = None
            self.cible_magie = None
            magie = trouve_skill(self.classe_principale,Skill_magie)
            magie.ajoute(Magie_enchantement_force())
                
class Joueur(Agissant,Entitee_superieure):
    """La classe du joueur."""
    def __init__(self,position,pv,pv_max,regen_pv,pm,pm_max,regen_pm,force,priorite,vitesse,affinite_ombre,affinite_feu,affinite_terre,affinite_glace,classe_principale,screen):
        Agissant.__init__(self,position,pv,pv_max,regen_pv,pm,pm_max,regen_pm,force,priorite,vitesse,affinite_ombre,affinite_feu,affinite_terre,affinite_glace,classe_principale)
        print("Initialisation du joueur")
        self.affichage = Affichage(screen)
        print("Affichage : check")
        self.curseur = CARRE #Le curseur est sur le carré central

        self.count_down = 8

        self.last_key = None
        self.hold = 0

        self.lab = {pygame.K_UP:Skill_deplacement,
                    pygame.K_DOWN:Skill_deplacement,
                    pygame.K_LEFT:Skill_deplacement,
                    pygame.K_RIGHT:Skill_deplacement,
                    pygame.K_SPACE:Skill_stomp,
                    pygame.K_m:Skill_ramasse,
                    pygame.K_q:Skill_attaque,
                    pygame.K_z:Skill_attaque,
                    pygame.K_d:Skill_attaque,
                    pygame.K_s:Skill_attaque,
                    pygame.K_x:Skill_blocage,
                    pygame.K_1:Skill_magie,
                    pygame.K_2:Skill_magie,
                    pygame.K_3:Skill_magie} #Je considère que le joueur commence avec 3 magies pré-apprises

        self.lab_dir = {pygame.K_UP:HAUT,
                        pygame.K_DOWN:BAS,
                        pygame.K_LEFT:GAUCHE,
                        pygame.K_RIGHT:DROITE,
                        pygame.K_q:DROITE,
                        pygame.K_z:HAUT,
                        pygame.K_d:GAUCHE,
                        pygame.K_s:BAS} #Certains skills sont directionnels

        self.magies = {pygame.K_1:None,
                       pygame.K_2:None,
                       pygame.K_3:None} #Insérer les noms des premières magies.

        self.fleches = {} #Le joueur ne peut pas lancer de flèche au début.

        self.explosif = {} #Le joueur ne peut pas lancer d'explosif au début.

        self.autre_dir = {pygame.K_UP:HAUT,
                          pygame.K_DOWN:BAS,
                          pygame.K_LEFT:GAUCHE,
                          pygame.K_RIGHT:DROITE} #Les directions pour se déplacer dans la minimap, l'inventaire, les menus de choix ou l'analyse

        self.change_affichage = {pygame.K_l:LABYRINTHE,
                                 pygame.K_m:MINIMAP,
                                 pygame.K_i:INVENTAIRE} #Les différentes options d'affichage

    def get_skin(self):
        return SKIN_JOUEUR

    def ajoute_skill(self,touche,skill):
        """Fonction qui ajoute un skill et la touche correspondante. Renvoie un booléen, selon que l'ajout a fonctionné ou pas."""
        if touche in self.lab:
            print("Cette touche est déjà utilisée ! Non au cumul des mandats !")
            res = False
        elif touche in self.change_affichage:
            print("Cette touche est utilisée pour changer d'affichage !")
            res = False
        else:
            self.lab[touche]=skill
            res = True
        return res

    def retire_skill(self,touche):
        """Fonction qui retire un skill de sa touche. Peut servir quand on a trop de skills, de magies et de projectiles pour garder un raccourci clavier pour chacun en permanence."""
        res = self.lab[touche]
        self.lab.pop(touche)
        return res

    def deplace_skill(self,touche_actuelle,touche_voulue):
        """Fonction qui déplace un skill d'une touche à une autre."""
        skill = self.retire_skill(touche_actuelle)
        res = self.ajoute_skill(touche_voulue,skill)
        if not(res):
            self.ajoute_skill(touche_actuelle,skill) #On remet le skill sur sa touche d'origine si le transfert n'a pas fonctionné.
        return res

    def ajoute_magie(self,touche,magie):
        """Fonction qui ajoute une magie et la touche correspondante. Renvoie un booléen, selon que l'ajout a fonctionné ou pas."""
        res = self.ajoute_skill(touche,Skill_magie)
        if res :
            self.magies[touche]=magie
        return res

    def retire_magie(self,touche):
        """Fonction qui retire une magie de sa touche. Peut servir quand on a trop de skills, de magies et de projectiles pour garder un raccourci clavier pour chacun en permanence."""
        res = self.magies[touche]
        self.lab.pop(touche)
        self.magies.pop(touche)
        return res

    def deplace_magie(self,touche_actuelle,touche_voulue):
        """Fonction qui déplace une magie d'une touche à une autre."""
        magie = self.retire_magie(touche_actuelle)
        res = self.ajoute_magie(touche_voulue,magie)
        if not(res):
            self.ajoute_magie(touche_actuelle,magie) #On remet la magie sur sa touche d'origine si le transfert n'a pas fonctionné.
        return res

    def ajoute_fleche(self,touche,fleche):
        """Fonction qui ajoute une fleche et la touche correspondante. Renvoie un booléen, selon que l'ajout a fonctionné ou pas."""
        res = self.ajoute_skill(touche,Lancer)
        if res :
            self.fleches[touche]=fleche
        return res

    def retire_fleche(self,touche):
        """Fonction qui retire une fleche de sa touche. Peut servir quand on a trop de skills, de magies et de projectiles pour garder un raccourci clavier pour chacun en permanence."""
        res = self.fleches[touche]
        self.lab.pop(touche)
        self.fleches.pop(touche)
        return res

    def deplace_fleche(self,touche_actuelle,touche_voulue):
        """Fonction qui déplace une fleche d'une touche à une autre."""
        fleche = self.retire_fleche(touche_actuelle)
        res = self.ajoute_fleche(touche_voulue,fleche)
        if not(res):
            self.ajoute_fleche(touche_actuelle,fleche) #On remet la fleche sur sa touche d'origine si le transfert n'a pas fonctionné.
        return res

    def ajoute_explosif(self,touche,explosif):
        """Fonction qui ajoute un explosif et la touche correspondante. Renvoie un booléen, selon que l'ajout a fonctionné ou pas."""
        res = self.ajoute_skill(touche,Lancer)
        if res :
            self.explosifs[touche]=explosif
        return res

    def retire_explosif(self,touche):
        """Fonction qui retire un explosif de sa touche. Peut servir quand on a trop de skills, de magies et de projectiles pour garder un raccourci clavier pour chacun en permanence."""
        res = self.explosifs[touche]
        self.lab.pop(touche)
        self.explosifs.pop(touche)
        return res

    def deplace_explosif(self,touche_actuelle,touche_voulue):
        """Fonction qui déplace un explosif d'une touche à une autre."""
        explosif = self.retire_explosif(touche_actuelle)
        res = self.ajoute_explosif(touche_voulue,explosif)
        if not(res):
            self.ajoute_explosif(touche_actuelle,explosif) #On remet l'explosif sur sa touche d'origine si le transfert n'a pas fonctionné.
        return res

    def debut_tour(self):
        Agissant.debut_tour(self)
        events = pygame.event.get() #Les évènements qui ont eu lieu depuis le dernier tour.
        for event in events :
            if event.type == pygame.KEYDOWN :
                self.last_key = event.key
                self.hold = 1
            elif event.type == pygame.KEYUP and self.last_key == event.key :
                self.hold = 0
            elif event.type == pygame.QUIT :
                quitte()
        if self.last_key != None and self.latence <= 0 and self.hold != 2 and self.etat == "vivant":
            self.skill_courant,complement = self.choix(self.last_key)
            if self.skill_courant in [Skill_deplacement,Skill_attaque]:
                self.dir_regard = complement
            elif self.skill_courant == Skill_magie:
                self.magie_courante = complement
        if self.hold == 0 :
            self.last_key = None
        else :
            self.hold += 1
        #Et on affiche !
        self.affichage.dessine(self)
        
    def choix(self,touche):
        if touche in self.lab.keys():
            self.skill_courant = self.lab[touche]
            if self.skill_courant in [Skill_deplacement,Skill_attaque]:
                complement = self.lab_dir[touche]
            elif self.skill_courant == Skill_magie:
                complement = self.magies[touche]
            else :
                complement = None
            #print (self.skill_courant,complement)
        else:
            self.skill_courant = None
            complement = None
        return self.skill_courant, complement

class Item(Entitee):
    """La classe des entitées inanimées. Peuvent se situer dans un inventaire. Peuvent être lancés (déconseillé pour les non-projectiles)."""
    def __init__(self,position):
        Entitee.__init__(self,position)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0 #Pour avoir le droit de la ramasser.
        self.porteur = None
        self.lanceur = None
        self.direction = None #Utile uniquement quand l'item se déplace.
        self.latence = 0 #Utile uniquement quand l'item se déplace.
        self.vitesse = 1 #La quantitée soustraite à la latence chaque tour.
        self.taux_vitesse = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à la vitesse. Correspond aux effets passager sur la vitesse.
        self.poids = 10 #Utile uniquement quand l'item est lancé. Détermine le temps qu'il faut à l'agissant pour le lancer et le temps que l'item se déplacera.
        self.frottements = 10 #Utile uniquement quand l'item se déplace. Détermine la latence entre deux déplacements.
        self.hauteur = 0 #Utile uniquement quand l'item se déplace. Diminue à chaque tour. L'item s'immobilise à 0 (éventuellement déclenche des effets).

    def heurte_agissant(self,agissant):
        for effet in self.effet :
            if isinstance(effet,On_hit) :
                effet.execute(self.lanceur,self.position,self.controleur)
        if isinstance(self,Percant) :
            self.ajoute_effet(En_sursis())
        elif isinstance(self,[Fragile,Evanescent]):
            self.etat = "brisé"
        else :
            self.arret()

    def heurte_mur(self):
        for effet in self.effet :
            if isinstance(effet,On_hit):
                effet.execute(self.lanceur,self.position,self.controleur)
        if isinstance(self,[Fragile,Evanescent]):
            self.etat = "brisé"
        else :
            self.arret()

    def atterit(self):
        for effet in self.effet :
            if isinstance(effet,On_hit) :
                effet.execute(self.lanceur,self.position,self.controleur)
        if isinstance(self,[Evanescent]):
            self.etat = "brisé"
        else :
            self.arret()

    def arret(self):
        self.latence = 0
        self.taux_vitesse.pop("lancementv")
        self.hauteur = 0

    #Découvrons le déroulé d'un tour, avec item-kun :
    def debut_tour(self):
        #Un nouveau tour commence, qui s'annonce remplit de bonne surprises et de nouvelles rencontres ! Pour partir du bon pied, on a quelques trucs à faire :
        for effet in self.effets:
            if isinstance(effet,On_debut_tour):
                effet.execute(self) #On exécute divers effets

    #Les agissants font leurs trucs, le controleur nous déplace, nous heurte (aïe !), tout le monde s'étripe...

    def fin_tour(self):
        #C'est déjà fini ? Vivement le prochain !
        for effet in self.effets:
            if isinstance(effet,On_fin_tour):
                effet.execute(self) #À condtion qu'il y ait un prochain...

class Cadavre(Item):
    pass

class Oeuf(Item):
    pass

class Cle(Item):
    """La classe des items qui ouvrent les portes (et les coffres ?)."""
    def __init__(self,position,codes):
        Item.__init__(self,position)
        self.codes = codes

    def get_codes(self):
        return self.codes

    def get_classe(self):
        return Cle

    def get_skin(self):
        return SKIN_CLE

class Consommable(Item):
    """La classe des items qui peuvent être consommés. Ajoute à l'agissant un effet. Disparait après usage."""
    def __init__(self,position,effet):
        Item.__init__(self,position)
        self.effet = effet

class Potion(Consommable):
    """La classe des consommables qui peuvent se boire."""
    def utilise(self,agissant):
        agissant.ajoute_effet(self.effet)
        self.etat = "brisé"

    def get_classe(self):
        return Potion

class Parchemin(Consommable):
    """La classe des consommables qui s'activent avec du mana."""
    def __init__(self,position,effet,cout):
        Item.__init__(self,position)
        self.effet = effet
        self.cout = cout

    def utilise(self,agissant):
        if agissant.peut_payer(self.cout) :
            agissant.paye(self.cout)
            agissant.ajoute_effet(self.effet)
            self.etat = "brisé"
        elif isinstance(agissant,Joueur):
            affichage = trouve_skill(agissant.classe_principale,Skill_affichage).affichage
            affichage.message(Message(["manque","mana"]))

    def get_classe(self):
        return Parchemin
        
class Equipement(Item):
    """La classe des items qui peuvent être portés. Sont toujours actifs tant qu'ils sont portés."""
    pass

class Defensif(Equipement):
    """La classe des équipements défensifs. Réduit les dégats."""
    def __init__(self,position,taux_degats):
        Item.__init__(self,position)
        self.taux_degats = taux_degats
        self.taux_stats = {}

    def intercepte(self,attaque):
        for taux in taux_stats.values():
            attaque.degats *= taux
        attaque.degats *= self.taux_degats

class Regeneration_pm(Equipement):
    """La classe des équipements régénérateurs de mana. Augmentent les pm récupérés à chaque tour."""
    def __init__(self,position,taux_regen_pm):
        Item.__init__(self,position)
        self.taux_regen_pm = taux_regen_pm

    def get_taux(self):
        return self.taux_regen_mana

class Regeneration_pv(Equipement):
    """La classe des équipements régénérateurs de vie. Augmentent les pv récupérés à chaque tour."""
    def __init__(self,position,taux_regen_pv):
        Item.__init__(self,position)
        self.taux_regen_pv = taux_regen_pv

    def get_taux(self):
        return self.taux_regen_pv

class Armure(Equipement):
    """La classe des équipements défensifs de type armure. On ne peut en porter qu'une à la fois. Réduit les dégats."""
    def __init__(self,position):
        Item.__init__(self,position)
        self.poids = 10 #C'est lourd !
        self.frottements = 8 #Il y a pire.

    def get_classe(self):
        return Armure

    def get_skin(self):
        return SKIN_ARMURE

class Haume(Equipement):
    """La classe des équipements défensifs de type haume. On ne peut en porter qu'un à la fois. Réduit les dégats."""
    def __init__(self,position):
        Item.__init__(self,position)
        self.poids = 3 #C'est plutôt léger.
        self.frottements = 6

    def get_classe(self):
        return Haume

    def get_skin(self):
        return SKIN_CASQUE

class Anneau(Equipement):
    """La classe des équipements de type anneau. Le nombre d'anneaux qu'on peut porter dépend de l'espèce. Les anneaux peuvent avoir des effets très différends (magiques pour la plupart)."""
    def __init__(self,position):
        Item.__init__(self,position)
        self.poids = 1 #C'est très léger !
        self.frottement = 2 #Il y a mieux.

    def get_classe(self):
        return Anneau

class Degainable(Item):
    """La classe des items qui doivent être dégainés. Sont utilisés en complément d'un skill, n'ont pas d'effet le reste du temps."""
    pass

class Arme(Degainable):
    """La classe des équipements qui augmentent la force d'attaque."""
    def __init__(self,position,element,tranchant,portee):
        Item.__init__(self,position)
        self.element = element
        self.tranchant = tranchant
        self.taux_tranchant = {}
        self.portee = portee
        self.taux_portee = {}
        self.taux_stats = {}

    def get_stats_attaque(self):
        tranchant = self.tranchant
        for taux in self.taux_tranchant.values():
            tranchant *= taux
        portee = self.portee
        for taux in self.taux_portee.values():
            portee *= taux
        for taux in self.taux_stats.values():
            tranchant *= taux
            portee *= taux
        return self.element,tranchant,portee

    def get_classe(self):
        return Arme

class Epee(Arme):
    """La classe des armes de type épée. Permettent de porter des coups semi-circulaires devant l'agissant."""
    def __init__(self,position,element,tranchant,portee):
        Arme.__init__(self,position,element,tranchant,portee)
        self.poids = 5
        self.frottements = 4

    def get_skin(self):
        return SKIN_EPEE

class Lance(Arme):
    """La classe des armes de type lance. Permettent de porter des coups rectilignes devant l'agissant."""
    def __init__(self,position,element,tranchant,portee):
        Arme.__init__(self,position,element,tranchant,portee)
        self.poids = 3
        self.frottements = 3

    def get_skin(self):
        return SKIN_LANCE

class Bouclier(Degainable):
    """La classe des boucliers. Permettent de se protéger des attaques lorsqu'ils sont utilisés."""
    def __init__(self,position,degats_bloques,taux_degats):
        Item.__init__(self,position)
        self.degats_bloques = degats_bloques
        self.taux_degats = taux_degats
        self.taux_stats = {}
        self.poids = 5
        self.frottements = 1 #En mode frisbee ça volle très bien !

    def intercepte(self,attaque):
        attaque.degats -= self.degats_bloques
        if attaque.degats < 0:
            attaque.degats = 0
        else :
            for taux in taux_stats.values():
                attaque.degats *=  taux
            attaque.degats *= self.taux_degats

    def get_classe(self):
        return Bouclier

    def get_skin(self):
        return SKIN_BOUCLIER

class Projectile(Item):
    """La classe des items destinés à être lancés. Possèdent naturellement une vitesse non nulle."""
    def __init__(self,position,vitesse,effets):
        Item.__init__(self,ID,position)
        self.vitesse_possible = vitesse
        self.effets += effets #Les effets déclenché lors du choc avec un agissant.

class Explosif(Projectile):
    """La classe des projectiles qui explosent. Affectés différemment par certains skills."""
    pass

class Percant(Item):
    """La classe des projectiles qui peuvent transpercer un ennemi."""
    pass

class Fleche(Percant):
    """La classe des projectiles de type flèche. Affectés différemment par certains skills."""
    pass

class Fleche_fantome(Fleche,Fantome):
    """La classe des flèches qui peuvent traverser les murs."""
    pass

class Perce_armure(Item):
    """La classe des items qui peuvent infliger des dégats sans être affectés par les défenses comme l'armure ou le bouclier."""

class Fragile(Item):
    """La classe des items qui se brisent lors d'un choc."""
    pass

class Evanescent(Item):
    """La classe des items qui disparaissent s'ils ne sont pas en mouvement (les sorts de projectiles, par exemple, qui sont des items...)."""
    pass

class Projectile_magique(Projectile,Evanescent):
    """La classe des projectiles créés par magie."""
    pass

class Magie_explosive(Explosif,Projectile_magique):
    """La classe des projectiles explosifs créés par magie."""
    pass

class Fleche_magique(Fleche,Projectile_magique):
    """La classe des flèches créées par magie."""

class Perce_armure_magique(Perce_armure,Projectile_magique):
    """La classe des projectiles perce_armures créés par magie."""

class Magie_explosive_percante(Magie_explosive,Percant):
    """La classe des projectiles explosifs perçant créés par magie."""

class Inventaire:

    def __init__(self,ID_possesseur,nb_doigts):
        self.possesseur = ID_possesseur
        self.items = {Potion:[], #Une liste qui contient les ID de toutes les potions possédées
                      Parchemin:[], #Une liste qui contient les ID de tous les parchemins possédées
                      Cle:[], #Une liste qui contient les ID de toutes les clés possédées
                      Arme:[], #Une liste qui contient les ID de toutes les armes possédées
                      Bouclier:[], #Une liste qui contient les ID de tous les boucliers possédées
                      Armure:[], #Une liste qui contient les ID de toutes les armures possédées
                      Haume:[], #Une liste qui contient les ID de tous les haumes possédées
                      Anneau:[], #Une liste qui contient les ID de tous les anneaux possédées
                      Cadavre:[], #Oui, on peut récupérer des cadavres, et alors, circluez, ya rien à voir...
                      Oeuf:[] #Vous allez quand même pas me dire que c'est l'oeuf qui vous choque ! Il y a marqué cadavre juste au dessus !
                      }
        self.kiiz = [Potion,Parchemin,Cle,Arme,Bouclier,Armure,Haume,Anneau,Cadavre,Oeuf]
        self.arme = None #L'arme équipée
        self.bouclier = None #Le bouclier équipé
        self.armure = None #L'armure équipée
        self.haume = None #Le haume équipé
        self.anneau = [None]*nb_doigts #Les anneaux équipés
        self.cat_courante = 0
        self.item_courant = 0
        self.controleur = None

    def active(self,controleur):
        self.controleur = controleur
        for key in self.items.keys():
            for item in self.items[key]:
                controleur.get_entitee(item).active(controleur)

    def desactive(self):
        for key in self.items.keys():
            for item in self.items[key]:
                self.controleur.get_entitee(item).desactive()
        self.controleur = None
        
    def ramasse_item(self,ID_item):
        """
        Fonction qui gère le ramassage d'un item
        Entrée:
            -l'item à ramasser
        """
        item = self.controleur.get_entitee(ID_item)
        item.position = None
        self.items[item.get_classe()].append(ID_item)

    def utilise_item(self,agissant):
        """
        Fonction qui utilise l'item actuellement sélectionné dans l'inventaire
        En sortie : Rien
        """
        ID_item = self.get_item_courant()
        item = self.controleur.get_entitee(ID_item)
        if isinstance(item,consommable):
            item.utilise(agissant)

    def get_items_visibles(self):
        items_visibles = []
        if self.arme != None:
            items_visibles.append(self.arme)
        if self.bouclier != None:
            items_visibles.append(self.bouclier)
        if self.armure != None:
            items_visibles.append(self.armure)
        if self.haume != None:
            items_visibles.append(self.haume)
        return items_visibles

    def get_arme(self):
        return self.arme

    def set_arme(self):
        ID_item = self.get_item_courant()
        item = self.controleur.get_entitee(ID_item)
        if isinstance(item,Arme):
            self.arme = ID_item

    def get_bouclier(self):
        return self.bouclier

    def set_bouclier(self):
        ID_item = self.get_item_courant()
        item = self.controleur.get_entitee(ID_item)
        if isinstance(item,Bouclier):
            self.bouclier = ID_item

    def get_armure(self):
        return self.armure

    def set_armure(self):
        ID_item = self.get_item_courant()
        item = self.controleur.get_entitee(ID_item)
        if isinstance(item,Armure):
            self.armure = ID_item

    def get_haume(self):
        return self.haume

    def set_haume(self):
        ID_item = self.get_item_courant()
        item = self.controleur.get_entitee(ID_item)
        if isinstance(item,Haume):
            self.haume = ID_item

    def get_anneau(self):
        return self.anneau

    def get_clees(self):
        clees = []
        for ID_cle in self.items[Cle]:
            cle = self.controleur.get_entitee(ID_cle)
            for code in cle.codes:
                clees.append(code)
        return clees

    def get_item_courant(self):
        cat = self.items[self.kiiz[self.cat_courante]]
        return cat[self.item_courant]

    def nettoie_item(self): #Méthode appelée à chaque fin de tour pour supprimer les items retirés ou utilisés.
        for cat in range(10): #On parcourt les catégories
            items = self.items[self.kiiz[cat]]
            for nb_item in range(len(items)): #On parcourt les items
                ID_item = items[nb_item]
                item = self.controleur.get_entitee(ID_item)
                if item.position != None or item.etat == "brisé": #S'il a été lancé ou n'est plus en état
                    items.remove(ID_item)

                    if cat == self.cat_courante :
                        if nb_item < self.item_courant or nb_item == len(items)-1 == self.item_courant :
                            self.item_courant -= 1 #On gère d'éventuels problèmes de selection

                    if self.arme == ID_item :
                        self.arme = None
                    elif self.bouclier == ID_item :
                        self.bouclier = None
                    elif self.armure == ID_item :
                        self.armure = None
                    elif self.haume == ID_item :
                        self.haume = None
                    else :
                        for doigt in range(len(self.anneau)):
                            if self.anneau[doigt] == ID_item :
                                self.anneau[doigt] = None #Quel genre d'imbécile briserait ou lancerait son équippement ? Enfin...

        if 0 == len(self.items[Potion]) == len(self.items[Parchemin]) == len(self.items[Cle]) == len(self.items[Arme]) == len(self.items[Bouclier]) == len(self.items[Armure]) == len(self.items[Haume]) == len(self.items[Anneau]) == len(self.items[Cadavre]) == len(self.items[Oeuf]) : #Sérieusement, l'inventaire est vide ?!
            self.cat_courante = 0
            self.item_courant = 0
        else :
            while len(self.items[self.kiiz[self.cat_courante]]) == 0: #On a au moins une catégorie non vide.
                self.cat_courante = (self.cat_courante + 1) % 10
            if self.item_courant == -1 : #Ce devrait être le cas si on est passé dans la boucle précédente, et ce n'est pas très souhaitable...
                self.item_courant = 0

    def deplace_toi(self,direction):
        if direction == DROITE:
            self.item_courant += 1
            if self.item_courant >= len(self.items[self.kiiz[self.cat_courante]]):
                self.item_courant = 0
                self.cat_courante += 1
                if self.cat_courante >= 10:
                    self.cat_courante = 0

        elif direction == GAUCHE:
            self.item_courant -= 1
            if self.item_courant < 0:
                self.cat_courante -= 1
                if self.cat_courante < 0:
                    self.cat_courante = 9
                self.item_courant = len(self.items[self.kiiz[self.cat_courante]])-1

    def drop_all(self,position):
        items = []
        for cat_item in [Potion,Parchemin,Cle,Arme,Bouclier,Armure,Haume,Anneau] : #On sépare les 'vrais' items des faux.
            items += self.items[cat_item]
        for ID_item in items :
            item = self.controleur.get_entitee(ID_item)
            item.position = position

    def debut_tour(self):
        items = []
        for cat_item in [Potion,Parchemin,Cle,Arme,Bouclier,Armure,Haume,Anneau] : #On sépare les 'vrais' items des faux.
            items += self.items[cat_item]
        for ID_item in items :
            item = self.controleur.get_entitee(ID_item)
            item.debut_tour()
        #On ne manipule pas les cadavres
        for ID_oeuf in self.items[Oeuf]: #Mais les oeufs incubent !
            oeuf = self.controleur.get_entitee(ID_oeuf)
            hatch = trouve_skill(oeuf.classe_principale,Hatching)
            if hatch != None:
                if hatch.utilise(): #Et peuvent même éclore !
                    self.controleur.fait_eclore(oeuf,self.possesseur)

    def fin_tour(self):
        items = []
        for item in [Potion,Parchemin,Cle,Arme,Bouclier,Armure,Haume,Anneau] : #On sépare les 'vrais' items des faux.
            items += self.items[item]
        for ID_item in items :
            item = self.controleur.get_entitee(ID_item)
            item.fin_tour() #Moins de choses à faire à la fin du tour.
        self.nettoie_item()

class Esprit :
    """La classe des esprits, qui manipulent les agisants."""
    def __init__(self,nom): #On identifie les esprits par des noms (en fait on s'en fout, vu qu'on ne fait pas d'opérations dessus on pourrait avoir des labs, des entitees et des esprits nommés avec des str, des int, des float, des bool, etc.)
        self.corps = {}
        self.vue = {}
        self.ennemis = {}
        self.oubli = 1
        self.nom = nom
        self.controleur = None

    def ajoute_corp(self,corp):
        if not corp in self.corps:
            self.corps[corp] = "incapacite"
            self.controleur.get_entitee(corp).rejoint(self.nom)

    def ajoute_corps(self,corps):
        for corp in corps:
            self.ajoute_corp(corp)

    def retire_corp(self,corp):
        if corp in self.corps:
            self.corps.pop(corp)

    def retire_corps(self,corps):
        for corp in corps:
            self.retire_corp(corp)

    def get_corps(self):
        corps = []
        for corp in self.corps.keys():
            corps.append(corp)
        return corps

    def ajoute_vue(self,vue,niveau):
        self.vue[niveau] = vue

    def maj_vue(self,vue,niveau):
        for i in range(len(vue)):
            for j in range(len(vue[0])):
                case = vue[i][j]
                if case[1] > 0: #Si la clarté est positive
                    self.vue[niveau][i][j] = case #On remplace par la dernière version de la vision

    def trouve_agissants(self,vue):
        agissants = []
        for i in range(len(vue)):
            for j in range(len(vue[0])):
                case = vue[i][j]
                agissants += case[7]
        return agissants

    def oublie_agissants(self,agissants):
        for vue in self.vue.values():
            for i in range(len(vue)):
                for j in range(len(vue[0])):
                    case = vue[i][j]
                    for ID in agissants:
                        if ID in case[7]:
                            case[7].remove(ID)

    def ordonne_bourrin(self,agissant):
        #Il faudra identifier les comportements possibles des agissants : attaque bourrine, attaque à distance, support (renforcement), soin, fuite, recherche et autres (réanimation pour les nécromantiens par exemple)
        #Pour l'instant juste des bourrins.
        position = agissant.get_position()
        niveau = position[0]
        labyrinthe = self.vue[niveau] #On récupère le labyrinthe
        case = labyrinthe[position[1]][position[2]]
        directions = []
        for i in range(4):
            if case[6][i]:
                directions.append(i) #On détermine les directions accessibles
        cases = []
        for direction in directions:
            if direction == 0:
                cases.append(labyrinthe[position[1]][position[2]-1])
            elif direction == 1:
                cases.append(labyrinthe[position[1]+1][position[2]])
            elif direction == 2:
                cases.append(labyrinthe[position[1]][position[2]+1])
            else:
                cases.append(labyrinthe[position[1]-1][position[2]])
        dir_choix = 2
        num_choix = 0
        distance = case[3]

        for i in range(len(cases)):
            if cases[i][3] > distance or (cases[i][3] == distance and cases[i][4] > cases[num_choix][4]):
                distance = cases[i][3] #Modifier pour départager les égalités avec la distance avec obstacles
                dir_choix = directions[i]
                num_choix = i

        if distance == 0 : #Pas d'accès direct à une cible
            cases_indirectes = []
            dirs_indirectes = []

            for i in range(len(directions)):
                entitees = cases[i][7]
                libre = True
                for ID_entitee in entitees: #Si l'accès direct est coupé, il y a probablement des agissants à proximité
                    if not issubclass(agissant.controleur.get_entitee(ID_entitee).get_classe(),Item): #Un agissant !
                        libre = False
                if libre:
                    cases_indirectes.append(cases[i])
                    dirs_indirectes.append(directions[i])

            if len(cases_indirectes) == 0:
                agissant.skill_courant = None

            else:
                distance = case[4]
                meilleur_choix = False
                agissant.skill_courant = None #Dans l'éventualité où on est déjà sur la meilleure case

                for i in range(len(cases_indirectes)):
                    if cases_indirectes[i][4] > distance:
                        meilleur_choix = True
                        distance = cases_indirectes[i][4] #On prend le chemin avec des obstacles
                        dir_choix = dirs_indirectes[i]

                if meilleur_choix:
                    agissant.skill_courant = Skill_deplacement
                    agissant.dir_regard = dir_choix

                if distance == 0: #Pas d'accès du tout !
                    if len(dirs_indirectes)>1: #On peut se permettre de choisir
                        if agissant.dir_regard != None: #L'agissant regarde quelque part
                            dir_back = [HAUT,DROITE,BAS,GAUCHE][agissant.dir_regard-2]
                            if dir_back in dirs_indirectes: #On ne veut pas y retourner
                                dirs_indirectes.remove(dir_back)
                    agissant.skill_courant = Skill_deplacement #On cherche (au hasard en l'occurence)
                    agissant.dir_regard = dirs_indirectes[random.randint(0,len(dirs_indirectes)-1)] #On prend une direction random
                    # ! Modifier pour avoir différents comportements !

        else : #Accès direct à une cible !
            agissant.dir_regard = dir_choix #On y va, sans se poser plus de questions !
            agissant.skill_courant = Skill_deplacement
            entitees = cases[num_choix][7]
            for ID_entitee in entitees: #Si l'accès direct passe par une case occupé, c'est que la cible y est !
                if not issubclass(agissant.controleur.get_entitee(ID_entitee).get_classe(),Item): #Il ne devrait pas y en avoir deux...
                    agissant.skill_courant = Skill_stomp

    def ordonne_fuite(self,agissant):
        #Il faudra identifier les comportements possibles des agissants : attaque bourrine, attaque à distance, support (renforcement), soin, fuite, recherche et autres (réanimation pour les nécromantiens par exemple)
        position = agissant.get_position()
        niveau = position[0]
        labyrinthe = self.vue[niveau] #On récupère le labyrinthe
        case = labyrinthe[position[1]][position[2]]
        directions = []
        cases = []
        for i in range(4):
            if i == 0 and case[6][i]:
                case_possible = labyrinthe[position[1]][position[2]-1]
                entitees = case_possible[7]
                libre = True
                for ID_entitee in entitees: 
                    if not issubclass(agissant.controleur.get_entitee(ID_entitee).get_classe(),Item): #On veut s'enfuir, pas foncer dans quelqu'un !
                        libre = False
                if libre :
                    cases.append(case_possible)
                    directions.append(i)
            elif i == 1 and case[6][i]:
                case_possible = labyrinthe[position[1]+1][position[2]]
                entitees = case_possible[7]
                libre = True
                for ID_entitee in entitees: 
                    if not issubclass(agissant.controleur.get_entitee(ID_entitee).get_classe(),Item): #On veut s'enfuir, pas foncer dans quelqu'un !
                        libre = False
                if libre :
                    cases.append(case_possible)
                    directions.append(i)
            elif i == 2 and case[6][i]:
                case_possible = labyrinthe[position[1]][position[2]+1]
                entitees = case_possible[7]
                libre = True
                for ID_entitee in entitees: 
                    if not issubclass(agissant.controleur.get_entitee(ID_entitee).get_classe(),Item): #On veut s'enfuir, pas foncer dans quelqu'un !
                        libre = False
                if libre :
                    cases.append(case_possible)
                    directions.append(i)
            elif i == 3 and case[6][i]:
                case_possible = labyrinthe[position[1]-1][position[2]]
                entitees = case_possible[7]
                libre = True
                for ID_entitee in entitees: 
                    if not issubclass(agissant.controleur.get_entitee(ID_entitee).get_classe(),Item): #On veut s'enfuir, pas foncer dans quelqu'un !
                        libre = False
                if libre :
                    cases.append(case_possible)
                    directions.append(i)

        if len(cases) == 0: #On n'a nulle part où aller ! Aaaaaaaaaaaaaaaaaaaaaaaaaaaaah !
            agissant.skill_courant = None

        else:

            dir_choix = 2
            num_choix = 0
            distance = case[3]

            if distance == 0 : #On n'est pas accessible directement, ouf !

                distance = case[4]

                if distance == 0: #On n'est pas accessible du tout ! On va pouvoir souffler un peu.
                    #if isinstance(agissant,Soigneur): #On peut se soigner soi-même !
                    #    agissant.skill_courant = Skill_magie
                    #    agissant.magie_courante = "Soin"
                    #else:
                    if len(directions)>1: #On peut se permettre de choisir
                        if agissant.dir_regard != None: #L'agissant regarde quelque part
                            dir_back = [HAUT,DROITE,BAS,GAUCHE][agissant.dir_regard-2]
                            if dir_back in directions: #On ne veut pas y retourner
                                directions.remove(dir_back)
                    agissant.skill_courant = Skill_deplacement #On cherche (au hasard en l'occurence)
                    agissant.dir_regard = directions[random.randint(0,len(directions)-1)] #On prend une direction random
                    # ! Modifier pour avoir différents comportements !

                else : #On est accessible indirectement ! Aaah !
                    meilleur_choix = False
                    agissant.skill_courant = None #Dans l'éventualité où on est déjà sur la meilleure case

                    for i in range(len(cases)):
                        if cases[i][4] < distance:
                            meilleur_choix = True
                            distance = cases[i][4] #On s'éloigne quand même
                            dir_choix = directions[i]

                    if meilleur_choix:
                        agissant.skill_courant = Skill_deplacement
                        agissant.dir_regard = dir_choix 

            else : #On est accessible directement ! Aaaaaaaah !
                for i in range(len(cases)):
                    if cases[i][3] < distance or (cases[i][3] == distance and cases[i][4] < cases[num_choix][4]): #On cherche à s'éloigner
                        distance = cases[i][3]
                        dir_choix = directions[i]
                        num_choix = i
                    
                agissant.dir_regard = dir_choix #On s'en va, sans se poser plus de questions !
                agissant.skill_courant = Skill_deplacement

    def ordonne_soin(self,agissant,fuyards,bourrins):
        #On va considérer qu'on peut soigner à n'importe quelle distance pour l'instant
        #Mais pas d'un étage à l'autre quand même !
        PV_mins = 0
        cible = None
        for ID_fuyard in fuyards :
            fuyard = self.controleur.get_entitee(ID_fuyard)
            if fuyard.get_position()[0] == agissant.get_position()[0] and (cible == None or fuyard.pv <= PV_mins) :
                cible = ID_fuyard
                PV_mins = fuyard.pv
        if cible == None : #On soigne les bourrins alors
            for ID_bourrin in bourrins :
                bourrin = self.controleur.get_entitee(ID_bourrin)
                if bourrin.get_position()[0] == agissant.get_position()[0] and (cible == None or bourrin.pv <= PV_mins) and bourrin.pv < bourrin.pv_max :
                    cible = ID_bourrin
                    PV_mins = bourrin.pv
        if cible != None:
            agissant.skill_courant = Skill_magie
            agissant.magie_courante = "Soin"
            agissant.cible_magie = cible
        else:
            self.ordonne_cherche(agissant)

    def ordonne_soutien(self,agissant,bourrins):
        #On va considérer qu'on peut soutenir à n'importe quelle distance pour l'instant
        #Mais pas d'un étage à l'autre quand même !
        importance = 0
        cible = None
        for ID_bourrin in bourrins :
            bourrin = self.controleur.get_entitee(ID_bourrin)
            pos = bourrin.get_position()
            distance = self.vue[pos[0]][pos[1]][pos[2]][3]
            if bourrin.get_position()[0] == agissant.get_position()[0] and distance > importance :
                cible = ID_bourrin
                importance = distance
##        if cible != None:
##            agissant.skill_courant = Skill_magie
##            agissant.magie_courante = Magie_support
##            agissant.cible_magie = cible
##        else:
##            self.ordonne_cherche(agissant)

    def ordonne_cherche(self,agissant):
        position = agissant.get_position()
        niveau = position[0]
        labyrinthe = self.vue[niveau] #On récupère le labyrinthe
        case = labyrinthe[position[1]][position[2]]
        directions = []
        cases = []
        for i in range(4):
            if i == 0 and case[6][i]:
                case_possible = labyrinthe[position[1]][position[2]-1]
                entitees = case_possible[7]
                libre = True
                for ID_entitee in entitees: 
                    if not issubclass(agissant.controleur.get_entitee(ID_entitee).get_classe(),Item):
                        libre = False
                if libre :
                    cases.append(case_possible)
                    directions.append(i)
            elif i == 1 and case[6][i]:
                case_possible = labyrinthe[position[1]+1][position[2]]
                entitees = case_possible[7]
                libre = True
                for ID_entitee in entitees: 
                    if not issubclass(agissant.controleur.get_entitee(ID_entitee).get_classe(),Item):
                        libre = False
                if libre :
                    cases.append(case_possible)
                    directions.append(i)
            elif i == 2 and case[6][i]:
                case_possible = labyrinthe[position[1]][position[2]+1]
                entitees = case_possible[7]
                libre = True
                for ID_entitee in entitees: 
                    if not issubclass(agissant.controleur.get_entitee(ID_entitee).get_classe(),Item):
                        libre = False
                if libre :
                    cases.append(case_possible)
                    directions.append(i)
            elif i == 3 and case[6][i]:
                case_possible = labyrinthe[position[1]-1][position[2]]
                entitees = case_possible[7]
                libre = True
                for ID_entitee in entitees: 
                    if not issubclass(agissant.controleur.get_entitee(ID_entitee).get_classe(),Item):
                        libre = False
                if libre :
                    cases.append(case_possible)
                    directions.append(i)

        if len(cases) == 0: #On n'a nulle part où aller
            agissant.skill_courant = None

        else:

            if len(directions)>1: #On peut se permettre de choisir
                if agissant.dir_regard != None: #L'agissant regarde quelque part
                    dir_back = [HAUT,DROITE,BAS,GAUCHE][agissant.dir_regard-2]
                    if dir_back in directions: #On ne veut pas y retourner
                        directions.remove(dir_back)
            agissant.skill_courant = Skill_deplacement #On cherche (au hasard en l'occurence)
            agissant.dir_regard = directions[random.randint(0,len(directions)-1)] #On prend une direction random
            # ! Modifier pour avoir différents comportements !

    def refait_vue(self):
        vues = []
        for corp in self.corps.keys(): #On récupère les vues
            if self.corps[corp] != "incapacite":
                agissant = self.controleur.get_entitee(corp)
                vues.append(agissant.vue)
        agissants_vus = []
        for vue in vues: #On identifie les agissants perçus
            agissants_vus += self.trouve_agissants(vue)
        self.oublie_agissants(agissants_vus) #Puisqu'on les a vus, on n'a plus besoin de garder en mémoire leur position précédente
        for vue in vues :
            niveau = vue[0][0][0][0] #La première coordonée de la position (première information) de la première case de la première colonne
            if niveau in self.vue.keys(): 
                self.maj_vue(vue,niveau)
            else:
                self.ajoute_vue(vue,niveau)

    def get_offenses(self):
        for corp in self.corps.keys(): #On vérifie si quelqu'un nous a offensé
            agissant = self.controleur.get_entitee(corp)
            offenses,etat = agissant.get_offenses()
            self.corps[corp] = etat
            for offense in offenses:
                ID_offenseur = offense[0]
                gravite = offense[1]
                if ID_offenseur in self.ennemis:
                    self.ennemis[ID_offenseur] += gravite
                else:
                    self.ennemis[ID_offenseur] = gravite

    def calcule_trajets(self):
        for ID_ennemi in self.ennemis.keys():
            ennemi = self.controleur.get_entitee(ID_ennemi)
            if ennemi.etat == "vivant":
                self.resoud(ennemi.get_position(),self.ennemis[ID_ennemi])
                self.resoud(ennemi.get_position(),self.ennemis[ID_ennemi],4,True)

    def resoud(self,position,portee,indice=3,dead_ends=False):

        #la queue est une liste de positions
        queue=[position]

        matrice_cases = self.vue[position[0]]

        matrice_cases[position[1]][position[2]][indice] = portee

        while len(queue)!=0 :

            position = queue[0]

            clarte = matrice_cases[position[1]][position[2]][indice]/2
            #enlever position dans queue
            queue.pop(0)

            #trouver les positions explorables
            positions_voisins=self.voisins_case(position)

            pos_explorables = self.positions_utilisables(positions_voisins,position,dead_ends)

            for pos in pos_explorables:
                if clarte > matrice_cases[pos[1]][pos[2]][indice] :
                    #on marque la case comme visitée
                    matrice_cases[pos[1]][pos[2]][indice] = clarte
                    
                    #on ajoute toutes les directions explorables
                    queue.append(pos)

        return matrice_cases

    def voisins_case(self,position):
        positions_voisins=[]
        largeur = len(self.vue[position[0]])
        hauteur = len(self.vue[position[0]][0])
        #on élimine les voisins aux extrémitées
        if position[2]-1>=0:
            positions_voisins.append((position[0],position[1],position[2]-1))
        else:
            positions_voisins.append(None)
            
        if position[1]+1<largeur:
            positions_voisins.append((position[0],position[1]+1,position[2]))
        else:
            positions_voisins.append(None)
            
        if position[2]+1<hauteur:
            positions_voisins.append((position[0],position[1],position[2]+1))
        else:
            positions_voisins.append(None)
            
        if position[1]-1>=0:
            positions_voisins.append((position[0],position[1]-1,position[2]))
        else:
            positions_voisins.append(None)

        return positions_voisins

    def positions_utilisables(self,positions_voisins,position,dead_ends):
        pos_utilisables=[]
        cardinaux = [HAUT,DROITE,BAS,GAUCHE]

        for direction in cardinaux:
            if positions_voisins[direction]!=None:
                voisin = positions_voisins[direction]

                #on vérifie si on peut passer
                case = self.vue[position[0]][position[1]][position[2]]
                if case[6][direction]:
                    if not(dead_ends and case[7]!=[]):
                        pos_utilisables.append(voisin)

        return pos_utilisables

    def decide(self):
        for corp in self.corps.keys():
            if self.corps[corp] != "incapacite":
                agissant = self.controleur.get_entitee(corp)
                if agissant.latence <= 0 and not isinstance(agissant,Joueur): #Le joueur décide pour lui-même
                    self.ordonne_bourrin(agissant) #Il faudra varier les stratégies !

    def oublie(self):
        for lab in self.vue.values():
            for i in range(len(lab)):
                for j in range(len(lab)):
                    case = lab[i][j]
                    if case[2] > 0:
                        case[2] -= 1
                    if case[2] <= 0:
                        case[1] = 0
                        case[5] = 0
                        case[6] = [False,False,False,False]
                        case[7] = []
                    case[3] = 0
                    case[4] = 0

    #Découvront le déroulé d'un tour avec esprit-sensei :
    def debut_tour(self):
        #On va faire plein de choses pendant ce tour (est-ce vraiment nécessaire de prendre des décisions si aucun des corps ne va jouer à ce tour ?
        self.get_offenses() #On s'insurge à grands cris (s'il y a lieu)
        self.refait_vue() #On prend connaissance de son environnement
        #Il faudra éventuellement définir une stratégie
        self.calcule_trajets() #On dresse les plans de bataille (s'il y a lieu)
        self.decide() #On donne les ordres

    #Tout le monde agit, nos bon-à-rien d'agissants se font massacrer à cause de leurs capacités médiocres ou remportent la victoire grâce à nos ordres brillants

    def fin_tour(self):
        #Le tour est fini, on réfléchira pendant le prochain. Comment ça, c'est mauvais pour la mémoire ?
        self.oublie()

class Esprit_type(Esprit):
    """Un esprit caricatural, pour les besoins de mes expériences."""
    def __init__(self,nom,niveau,controleur,position):
        # Tout le monde spawn au même endroit, changer ça !
        self.nom = nom
        self.controleur = controleur
        self.oubli = niveau
        self.ennemis = {}
        self.vue = {}
        self.corps = {}
        if niveau == 1:
            corps = [Tank(position,1),Dps(position,1),Dps(position,1)]
        if niveau == 2:
            corps = [Tank(position,2),Tank(position,1),Dps(position,2),Dps(position,2),Soigneur(position,1)]
        controleur.ajoute_entitees(corps)
        IDs = [corp.ID for corp in corps]
        self.ajoute_corps(IDs)
        i = 0
        random.shuffle(corps)
        for corp in corps:
            corp.position = (position[0],position[1],position[2]+i)
            i+=1

    def antagonise(self,nom_esprit):
        for corp in self.controleur.get_esprit(nom_esprit).get_corps():
            if not corp in self.ennemis.keys():
                self.ennemis[corp] = 0.1

    def decide(self):
        bourrins = []
        fuyards = []
        soigneurs = []
        soutiens = []
        for corp in self.corps.keys():
            if self.corps[corp] == "attaque":
                bourrins.append(corp)
            elif self.corps[corp] == "fuite":
                fuyards.append(corp)
            elif self.corps[corp] == "soin":
                soigneurs.append(corp)
            elif self.corps[corp] == "soutien":
                soutiens.append(corp)
        if bourrins == fuyards == soigneurs == [] and soutiens != []:
            bourrins.append(soutiens[0])
            soutiens.pop(0)
        elif bourrins == fuyards == []:
            bourrins = soigneurs
            soigneurs = []
        elif soigneurs == []:
            bourrins += fuyards
            fuyards = []
        for corp in bourrins:
            agissant = self.controleur.get_entitee(corp)
            if agissant.latence <= 0 :
                self.ordonne_bourrin(agissant)
        for corp in fuyards:
            agissant = self.controleur.get_entitee(corp)
            if agissant.latence <= 0 :
                self.ordonne_fuite(agissant)
        for corp in soigneurs:
            agissant = self.controleur.get_entitee(corp)
            if agissant.latence <= 0 :
                self.ordonne_soin(agissant,fuyards,bourrins)
        for corp in soutiens:
            agissant = self.controleur.get_entitee(corp)
            if agissant.latence <= 0 :
                self.ordonne_soutien(agissant,bourrins)

class Esprit_sans_scrupule(Esprit_type):
    """Un esprit qui s'en prend principalement aux soigneurs et aux soutiens."""

    def get_offenses(self):
        for corp in self.corps.keys(): #On vérifie si quelqu'un nous a offensé
            agissant = self.controleur.get_entitee(corp)
            offenses,etat = agissant.get_offenses()
            self.corps[corp] = etat
            for offense in offenses:
                ID_offenseur = offense[0]
                gravite = offense[1]
                if ID_offenseur in self.ennemis:
                    self.ennemis[ID_offenseur] += gravite
                else:
                    self.ennemis[ID_offenseur] = gravite
                offenseur = self.controleur.get_entitee(ID_offenseur)
                esprit_offenseur = self.controleur.get_esprit(offenseur.esprit)
                corps_ennemis = esprit_offenseur.corps
                for ID in corps_ennemis.keys():
                    if corps_ennemis[ID] == "soin":
                        if ID in self.ennemis:
                            self.ennemis[ID] += gravite
                        else:
                            self.ennemis[ID] = gravite
                    elif corps_ennemis[ID] == "soutien":
                        if ID in self.ennemis:
                            self.ennemis[ID] += gravite/2
                        else:
                            self.ennemis[ID] = gravite/2

class Esprit_bourrin(Esprit_type):
    """Un esprit sans soigneurs ni soutiens."""
    def __init__(self,nom,niveau,controleur,position):
        # Tout le monde spawn au même endroit, changer ça !
        self.nom = nom
        self.controleur = controleur
        self.oubli = niveau
        self.ennemis = {}
        self.vue = {}
        self.corps = {}
        if niveau == 1:
            corps = [Dps(position,1),Dps(position,1),Dps(position,1)]
        if niveau == 2:
            corps = [Dps(position,2),Dps(position,2),Dps(position,2),Dps(position,1),Dps(position,1)]
        controleur.ajoute_entitees(corps)
        IDs = [corp.ID for corp in corps]
        self.ajoute_corps(IDs)
        i = 0
        random.shuffle(corps)
        for corp in corps:
            corp.position = (position[0],position[1],position[2]+i)
            i+=1

class Esprit_defensif(Esprit_type):
    """Un esprit sans soigneurs ni soutiens."""
    def __init__(self,nom,niveau,controleur,position):
        # Tout le monde spawn au même endroit, changer ça !
        self.nom = nom
        self.controleur = controleur
        self.oubli = niveau
        self.ennemis = {}
        self.vue = {}
        self.corps = {}
        if niveau == 1:
            corps = [Tank(position,1),Tank(position,1),Dps(position,1)]
        if niveau == 2:
            corps = [Tank(position,2),Tank(position,2),Dps(position,2),Tank(position,1),Dps(position,1)]
        controleur.ajoute_entitees(corps)
        IDs = [corp.ID for corp in corps]
        self.ajoute_corps(IDs)
        i = 0
        random.shuffle(corps)
        for corp in corps:
            corp.position = (position[0],position[1],position[2]+i)
            i+=1

class Magie_soin :
    """La magie de soin. Renvoie un sort de soin plus ou moins puissant."""
    def __init__(self):
        self.nom = "Soin"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Sort_de_soin(0.1,50,3,30,10000)
        elif niveau == 2:
            return Sort_de_soin(0.11,49,3,35,10000)
        elif niveau == 3:
            return Sort_de_soin(0.12,48,3,40,10000)
        elif niveau == 4:
            return Sort_de_soin(0.13,47,3,45,10000)
        elif niveau == 5:
            return Sort_de_soin(0.14,46,3,50,10000)
        elif niveau == 6:
            return Sort_de_soin(0.15,45,3,55,10000)
        elif niveau == 7:
            return Sort_de_soin(0.16,44,3,60,10000)
        elif niveau == 8:
            return Sort_de_soin(0.17,43,3,65,10000)
        elif niveau == 9:
            return Sort_de_soin(0.18,42,3,70,10000)
        elif niveau == 10:
            return Sort_de_soin(0.19,41,3,75,10000)

class Magie_soin_superieure :
    """La magie de soin de haut niveau. Renvoie un sort de soin plus ou moins puissant."""
    def __init__(self):
        self.nom = "Soin_sup"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Sort_de_soin(0.2,50,6,50,10000)
        elif niveau == 2:
            return Sort_de_soin(0.2,50,6,60,10000)
        elif niveau == 3:
            return Sort_de_soin(0.2,50,6,70,10000)
        elif niveau == 4:
            return Sort_de_soin(0.2,50,6,80,10000)
        elif niveau == 5:
            return Sort_de_soin(0.2,40,6,80,10000)
        elif niveau == 6:
            return Sort_de_soin(0.2,40,6,90,10000)
        elif niveau == 7:
            return Sort_de_soin(0.2,40,6,100,10000)
        elif niveau == 8:
            return Sort_de_soin(0.2,30,6,100,10000)
        elif niveau == 9:
            return Sort_de_soin(0.2,30,6,150,10000)
        elif niveau == 10:
            return Sort_de_soin(0.2,20,6,150,10000)

class Magie_zone_soin :
    """La magie de zone de soin. Renvoie un sort de soin de zone plus ou moins puissant."""
    def __init__(self):
        self.nom = "Soin_zone"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Soin_de_zone(0.1,100,6,30,5,10000)
        elif niveau == 2:
            return Soin_de_zone(0.2,100,6,30,5,10000)
        elif niveau == 3:
            return Soin_de_zone(0.2,100,5,30,5,10000)
        elif niveau == 4:
            return Soin_de_zone(0.3,90,5,30,5,10000)
        elif niveau == 5:
            return Soin_de_zone(0.3,90,4,40,5,10000)
        elif niveau == 6:
            return Soin_de_zone(0.4,90,4,40,5,10000)
        elif niveau == 7:
            return Soin_de_zone(0.4,80,3,40,5,10000)
        elif niveau == 8:
            return Soin_de_zone(0.5,80,3,50,5,10000)
        elif niveau == 9:
            return Soin_de_zone(0.5,80,2,50,5,10000)
        elif niveau == 10:
            return Soin_de_zone(0.5,70,1,50,5,10000)

class Magie_auto_soin :
    """La magie d'auto soin. Renvoie un sort d'auto soin plus ou moins puissant."""
    def __init__(self):
        self.nom = "Soin_perso"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Auto_soin(0.1,50,3,40)
        elif niveau == 2:
            return Auto_soin(0.11,49,3,45)
        elif niveau == 3:
            return Auto_soin(0.12,48,3,50)
        elif niveau == 4:
            return Auto_soin(0.13,47,3,55)
        elif niveau == 5:
            return Auto_soin(0.14,46,3,60)
        elif niveau == 6:
            return Auto_soin(0.15,45,3,65)
        elif niveau == 7:
            return Auto_soin(0.16,44,3,70)
        elif niveau == 8:
            return Auto_soin(0.17,43,3,75)
        elif niveau == 9:
            return Auto_soin(0.18,42,3,80)
        elif niveau == 10:
            return Auto_soin(0.19,41,3,85)

class Magie_resurection :
    """La magie de résurection. Renvoie un sort de résurection plus ou moins puissant."""
    def __init__(self):
        self.nom = "Resurection"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Resurection(0.2,500,20,1,10000)
        elif niveau == 2:
            return Resurection(0.21,500,20,1,10000)
        elif niveau == 3:
            return Resurection(0.22,500,20,1,10000)
        elif niveau == 4:
            return Resurection(0.23,500,20,2,10000)
        elif niveau == 5:
            return Resurection(0.24,500,19,2,10000)
        elif niveau == 6:
            return Resurection(0.25,500,19,3,10000)
        elif niveau == 7:
            return Resurection(0.26,500,19,5,10000)
        elif niveau == 8:
            return Resurection(0.27,500,17,6,10000)
        elif niveau == 9:
            return Resurection(0.28,500,17,8,10000)
        elif niveau == 10:
            return Resurection(0.29,500,15,8,10000)

class Magie_zone_reanimation :
    """La magie de réanimation de zone. Renvoie un sort de réanimation de zone plus ou moins puissant."""
    def __init__(self):
        self.nom = "Reanimation"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Reanimation_de_zone(0.1,200,20,0.1,1,5,10,10000)
        elif niveau == 2:
            return Reanimation_de_zone(0.1,200,20,0.1,2,5,10,10000)
        elif niveau == 3:
            return Reanimation_de_zone(0.1,200,20,0.1,3,5,10,10000)
        elif niveau == 4:
            return Reanimation_de_zone(0.1,200,20,0.1,4,5,10,10000)
        elif niveau == 5:
            return Reanimation_de_zone(0.1,200,20,0.1,5,6,10,10000)
        elif niveau == 6:
            return Reanimation_de_zone(0.1,200,20,0.1,6,7,9,10000)
        elif niveau == 7:
            return Reanimation_de_zone(0.1,200,20,0.2,7,8,8,10000)
        elif niveau == 8:
            return Reanimation_de_zone(0.1,200,20,0.3,8,10,7,10000)
        elif niveau == 9:
            return Reanimation_de_zone(0.1,500,20,0.4,9,12,6,10000)
        elif niveau == 10:
            return Reanimation_de_zone(0.1,500,20,0.5,10,15,5,10000)

class Magie_boule_de_feu :
    """La magie de boule de feu. Renvoie un sort de création de boule de feu plus ou moins puissant."""
    def __init__(self):
        self.nom = "Boule_de_feu"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Invocation_projectile(0.1,30,5,10000,Magie_explosive(None,0.5,[],[Charge(2,10)]))
        elif niveau == 2:
            return Invocation_projectile(0.1,29,5,10000,Magie_explosive(None,0.5,[],[Charge(3,10)]))
        elif niveau == 3:
            return Invocation_projectile(0.1,28,5,10000,Magie_explosive(None,0.5,[],[Charge(4,10)]))
        elif niveau == 4:
            return Invocation_projectile(0.1,27,5,10000,Magie_explosive(None,0.5,[],[Charge(4,15)]))
        elif niveau == 5:
            return Invocation_projectile(0.1,26,5,10000,Magie_explosive(None,0.5,[],[Charge(4,20)]))
        elif niveau == 6:
            return Invocation_projectile(0.1,25,5,10000,Magie_explosive(None,0.5,[],[Charge(5,20)]))
        elif niveau == 7:
            return Invocation_projectile(0.1,23,5,10000,Magie_explosive(None,0.5,[],[Charge(6,25)]))
        elif niveau == 8:
            return Invocation_projectile(0.1,21,5,10000,Magie_explosive(None,0.5,[],[Charge(7,25)]))
        elif niveau == 9:
            return Invocation_projectile(0.1,18,5,10000,Magie_explosive(None,0.5,[],[Charge(8,30)]))
        elif niveau == 10:
            return Invocation_projectile(0.1,15,5,10000,Magie_explosive(None,0.5,[],[Charge(10,40)]))

class Magie_fleche_de_glace :
    """La magie de fleche de glace. Renvoie un sort de création de fleche de glace plus ou moins puissant."""
    def __init__(self):
        self.nom = "Fleche_de_glace"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Invocation_projectile(0.1,30,5,10000,Fleche_magique(None,0.5,[Choc(20,GLACE)]))
        elif niveau == 2:
            return Invocation_projectile(0.1,29,5,10000,Fleche_magique(None,0.5,[Choc(20,GLACE)]))
        elif niveau == 3:
            return Invocation_projectile(0.1,28,5,10000,Fleche_magique(None,0.5,[Choc(20,GLACE)]))
        elif niveau == 4:
            return Invocation_projectile(0.1,27,5,10000,Fleche_magique(None,0.5,[Choc(30,GLACE)]))
        elif niveau == 5:
            return Invocation_projectile(0.1,26,5,10000,Fleche_magique(None,0.5,[Choc(30,GLACE)]))
        elif niveau == 6:
            return Invocation_projectile(0.1,25,5,10000,Fleche_magique(None,0.5,[Choc(40,GLACE)]))
        elif niveau == 7:
            return Invocation_projectile(0.1,23,5,10000,Fleche_magique(None,0.5,[Choc(50,GLACE)]))
        elif niveau == 8:
            return Invocation_projectile(0.1,21,5,10000,Fleche_magique(None,0.5,[Choc(70,GLACE)]))
        elif niveau == 9:
            return Invocation_projectile(0.1,18,5,10000,Fleche_magique(None,0.5,[Choc(80,GLACE)]))
        elif niveau == 10:
            return Invocation_projectile(0.1,15,5,10000,Fleche_magique(None,0.5,[Choc(100,GLACE)]))

class Magie_rocher :
    """La magie de rocher. Renvoie un sort de création de rocher plus ou moins puissant."""
    def __init__(self):
        self.nom = "Rocher"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Invocation_projectile(0.1,30,5,10000,Projectile_magique(None,0.5,[Choc(30)]))
        elif niveau == 2:
            return Invocation_projectile(0.1,29,5,10000,Projectile_magique(None,0.5,[Choc(30)]))
        elif niveau == 3:
            return Invocation_projectile(0.1,28,5,10000,Projectile_magique(None,0.5,[Choc(40)]))
        elif niveau == 4:
            return Invocation_projectile(0.1,27,5,10000,Projectile_magique(None,0.5,[Choc(50)]))
        elif niveau == 5:
            return Invocation_projectile(0.1,26,5,10000,Projectile_magique(None,0.5,[Choc(70)]))
        elif niveau == 6:
            return Invocation_projectile(0.1,25,5,10000,Projectile_magique(None,0.5,[Choc(90)]))
        elif niveau == 7:
            return Invocation_projectile(0.1,23,5,10000,Projectile_magique(None,0.5,[Choc(110)]))
        elif niveau == 8:
            return Invocation_projectile(0.1,21,5,10000,Projectile_magique(None,0.5,[Choc(130)]))
        elif niveau == 9:
            return Invocation_projectile(0.1,18,5,10000,Projectile_magique(None,1,[Choc(150)]))
        elif niveau == 10:
            return Invocation_projectile(0.1,15,5,10000,Projectile_magique(None,1,[Choc(190)]))

class Magie_ombre_furtive :
    """La magie d'ombre. Renvoie un sort de création d'ombre furtive plus ou moins puissant."""
    def __init__(self):
        self.nom = "Ombre"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Ombre_furtive(0.1,30,5,10000,Perce_armure_magique(None,2,[Choc(15,OMBRE)]),3,10000)
        elif niveau == 2:
            return Ombre_furtive(0.1,29,5,10000,Perce_armure(None,0.5,[Choc(15,OMBRE)]),3,10000)
        elif niveau == 3:
            return Ombre_furtive(0.1,28,5,10000,Perce_armure(None,0.5,[Choc(20,OMBRE)]),4,10000)
        elif niveau == 4:
            return Ombre_furtive(0.1,27,5,10000,Perce_armure(None,0.5,[Choc(20,OMBRE)]),4,10000)
        elif niveau == 5:
            return Ombre_furtive(0.1,26,5,10000,Perce_armure(None,0.5,[Choc(20,OMBRE)]),5,10000)
        elif niveau == 6:
            return Ombre_furtive(0.1,25,5,10000,Perce_armure(None,0.5,[Choc(25,OMBRE)]),6,10000)
        elif niveau == 7:
            return Ombre_furtive(0.1,23,5,10000,Perce_armure(None,0.5,[Choc(25,OMBRE)]),7,10000)
        elif niveau == 8:
            return Ombre_furtive(0.1,21,5,10000,Perce_armure(None,0.5,[Choc(30,OMBRE)]),8,10000)
        elif niveau == 9:
            return Ombre_furtive(0.1,18,5,10000,Perce_armure(None,0.5,[Choc(40,OMBRE)]),9,10000)
        elif niveau == 10:
            return Ombre_furtive(0.1,15,5,10000,Perce_armure(None,0.5,[Choc(50,OMBRE)]),10,10000)

class Magie_jet_de_mana :
    """La magie de jet de mana. Renvoie un sort de création de jet de mana plus ou moins puissant."""
    def __init__(self):
        self.nom = "Jet_de_mana"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Invocation_projectile(0.1,20,3,10000,Projectile_magique(None,0.5,[Choc(20)]))
        elif niveau == 2:
            return Invocation_projectile(0.1,20,3,10000,Projectile_magique(None,0.5,[Choc(20)]))
        elif niveau == 3:
            return Invocation_projectile(0.1,20,3,10000,Projectile_magique(None,0.5,[Choc(20)]))
        elif niveau == 4:
            return Invocation_projectile(0.1,20,3,10000,Projectile_magique(None,0.5,[Choc(20)]))
        elif niveau == 5:
            return Invocation_projectile(0.1,20,3,10000,Projectile_magique(None,0.5,[Choc(30)]))
        elif niveau == 6:
            return Invocation_projectile(0.1,20,3,10000,Projectile_magique(None,0.5,[Choc(30)]))
        elif niveau == 7:
            return Invocation_projectile(0.1,20,3,10000,Projectile_magique(None,0.5,[Choc(30)]))
        elif niveau == 8:
            return Invocation_projectile(0.1,20,3,10000,Projectile_magique(None,0.5,[Choc(40)]))
        elif niveau == 9:
            return Invocation_projectile(0.1,20,3,10000,Projectile_magique(None,0.5,[Choc(40)]))
        elif niveau == 10:
            return Invocation_projectile(0.1,20,3,10000,Projectile_magique(None,0.5,[Choc(50)]))

class Magie_eclair_noir :
    """La magie d'éclair noir. Renvoie un sort de création d'éclair noir plus ou moins puissant."""
    def __init__(self):
        self.nom = "Eclair_noir"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Invocation_projectile(0.1,150,10,10000,Magie_explosive_percante(None,0.2,[Choc(50)],[Charge(3,50)]))
        elif niveau == 2:
            return Invocation_projectile(0.1,150,10,10000,Magie_explosive_percante(None,0.2,[Choc(50)],[Charge(3,50)]))
        elif niveau == 3:
            return Invocation_projectile(0.1,150,10,10000,Magie_explosive_percante(None,0.2,[Choc(50)],[Charge(3,50)]))
        elif niveau == 4:
            return Invocation_projectile(0.1,150,10,10000,Magie_explosive_percante(None,0.2,[Choc(50)],[Charge(4,50)]))
        elif niveau == 5:
            return Invocation_projectile(0.1,150,10,10000,Magie_explosive_percante(None,0.2,[Choc(70)],[Charge(4,50)]))
        elif niveau == 6:
            return Invocation_projectile(0.1,140,8,10000,Magie_explosive_percante(None,0.25,[Choc(70)],[Charge(5,60)]))
        elif niveau == 7:
            return Invocation_projectile(0.1,130,8,10000,Magie_explosive_percante(None,0.25,[Choc(70)],[Charge(5,70)]))
        elif niveau == 8:
            return Invocation_projectile(0.1,120,7,10000,Magie_explosive_percante(None,0.25,[Choc(90)],[Charge(6,70)]))
        elif niveau == 9:
            return Invocation_projectile(0.1,110,6,10000,Magie_explosive_percante(None,0.34,[Choc(90)],[Charge(6,75)]))
        elif niveau == 10:
            return Invocation_projectile(0.1,100,5,10000,Magie_explosive_percante(None,0.34,[Choc(100)],[Charge(7,75)]))

class Magie_enchantement_faiblesse :
    """La magie d'enchantement de faiblesse. Renvoie un sort de création d'enchantement de faiblesse plus ou moins puissant."""
    def __init__(self):
        self.nom = "Faiblesse"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Enchante_agissant(0.1,200,10,10000,Enchantement_force(50,-20))
        elif niveau == 2:
            return Enchante_agissant(0.1,180,10,10000,Enchantement_force(100,-20))
        elif niveau == 3:
            return Enchante_agissant(0.1,160,10,10000,Enchantement_force(150,-20))
        elif niveau == 4:
            return Enchante_agissant(0.1,150,10,10000,Enchantement_force(200,-20))
        elif niveau == 5:
            return Enchante_agissant(0.1,140,10,10000,Enchantement_force(250,-50))
        elif niveau == 6:
            return Enchante_agissant(0.1,130,10,10000,Enchantement_force(300,-50))
        elif niveau == 7:
            return Enchante_agissant(0.1,118,10,10000,Enchantement_force(350,-50))
        elif niveau == 8:
            return Enchante_agissant(0.1,109,10,10000,Enchantement_force(400,-80))
        elif niveau == 9:
            return Enchante_agissant(0.1,103,10,10000,Enchantement_force(450,-80))
        elif niveau == 10:
            return Enchante_agissant(0.1,100,10,10000,Enchantement_force(500,-100))

class Magie_enchantement_cecite :
    """La magie d'enchantement de cécité. Renvoie un sort de création d'enchantement de cécité plus ou moins puissant."""
    def __init__(self):
        self.nom = "Cecite"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Enchante_agissant(0.1,200,10,10000,Enchantement_vision(50,-2))
        elif niveau == 2:
            return Enchante_agissant(0.1,180,10,10000,Enchantement_vision(100,-2))
        elif niveau == 3:
            return Enchante_agissant(0.1,160,10,10000,Enchantement_vision(150,-2))
        elif niveau == 4:
            return Enchante_agissant(0.1,150,10,10000,Enchantement_vision(200,-2))
        elif niveau == 5:
            return Enchante_agissant(0.1,140,10,10000,Enchantement_vision(250,-5))
        elif niveau == 6:
            return Enchante_agissant(0.1,130,10,10000,Enchantement_vision(300,-5))
        elif niveau == 7:
            return Enchante_agissant(0.1,118,10,10000,Enchantement_vision(350,-5))
        elif niveau == 8:
            return Enchante_agissant(0.1,109,10,10000,Enchantement_vision(400,-8))
        elif niveau == 9:
            return Enchante_agissant(0.1,103,10,10000,Enchantement_vision(450,-8))
        elif niveau == 10:
            return Enchante_agissant(0.1,100,10,10000,Enchantement_vision(500,-10))

class Magie_enchantement_perte_de_pv :
    """La magie d'enchantement de perte de pv. Renvoie un sort de création d'enchantement de perte de pv plus ou moins puissant."""
    def __init__(self):
        self.nom = "Perte_de_pv"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Enchante_agissant(0.1,200,10,10000,Enchantement_pv(50,-10))
        elif niveau == 2:
            return Enchante_agissant(0.1,180,10,10000,Enchantement_pv(100,-10))
        elif niveau == 3:
            return Enchante_agissant(0.1,160,10,10000,Enchantement_pv(150,-10))
        elif niveau == 4:
            return Enchante_agissant(0.1,150,10,10000,Enchantement_pv(200,-10))
        elif niveau == 5:
            return Enchante_agissant(0.1,140,10,10000,Enchantement_pv(250,-25))
        elif niveau == 6:
            return Enchante_agissant(0.1,130,10,10000,Enchantement_pv(300,-25))
        elif niveau == 7:
            return Enchante_agissant(0.1,118,10,10000,Enchantement_pv(350,-25))
        elif niveau == 8:
            return Enchante_agissant(0.1,109,10,10000,Enchantement_pv(400,-40))
        elif niveau == 9:
            return Enchante_agissant(0.1,103,10,10000,Enchantement_pv(450,-40))
        elif niveau == 10:
            return Enchante_agissant(0.1,100,10,10000,Enchantement_pv(500,-50))

class Magie_enchantement_perte_de_pm :
    """La magie d'enchantement de perte de pm. Renvoie un sort de création d'enchantement de perte de pm plus ou moins puissant."""
    def __init__(self):
        self.nom = "Perte_de_pm"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Enchante_agissant(0.1,200,10,10000,Enchantement_pm(50,-10))
        elif niveau == 2:
            return Enchante_agissant(0.1,180,10,10000,Enchantement_pm(100,-10))
        elif niveau == 3:
            return Enchante_agissant(0.1,160,10,10000,Enchantement_pm(150,-10))
        elif niveau == 4:
            return Enchante_agissant(0.1,150,10,10000,Enchantement_pm(200,-10))
        elif niveau == 5:
            return Enchante_agissant(0.1,140,10,10000,Enchantement_pm(250,-25))
        elif niveau == 6:
            return Enchante_agissant(0.1,130,10,10000,Enchantement_pm(300,-25))
        elif niveau == 7:
            return Enchante_agissant(0.1,118,10,10000,Enchantement_pm(350,-25))
        elif niveau == 8:
            return Enchante_agissant(0.1,109,10,10000,Enchantement_pm(400,-40))
        elif niveau == 9:
            return Enchante_agissant(0.1,103,10,10000,Enchantement_pm(450,-40))
        elif niveau == 10:
            return Enchante_agissant(0.1,100,10,10000,Enchantement_pm(500,-50))

class Magie_enchantement_confusion :
    """La magie d'enchantement de confusion. Renvoie un sort de création d'enchantement de confusion plus ou moins puissant."""
    def __init__(self):
        self.nom = "Confusion"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Enchante_agissant(0.1,200,10,10000,Enchantement_confusion(50,0.05))
        elif niveau == 2:
            return Enchante_agissant(0.1,180,10,10000,Enchantement_confusion(100,0.1))
        elif niveau == 3:
            return Enchante_agissant(0.1,160,10,10000,Enchantement_confusion(150,0.15))
        elif niveau == 4:
            return Enchante_agissant(0.1,150,10,10000,Enchantement_confusion(200,0.2))
        elif niveau == 5:
            return Enchante_agissant(0.1,140,10,10000,Enchantement_confusion(250,0.25))
        elif niveau == 6:
            return Enchante_agissant(0.1,130,10,10000,Enchantement_confusion(300,0.3))
        elif niveau == 7:
            return Enchante_agissant(0.1,118,10,10000,Enchantement_confusion(350,0.35))
        elif niveau == 8:
            return Enchante_agissant(0.1,109,10,10000,Enchantement_confusion(400,0.4))
        elif niveau == 9:
            return Enchante_agissant(0.1,103,10,10000,Enchantement_confusion(450,0.45))
        elif niveau == 10:
            return Enchante_agissant(0.1,100,10,10000,Enchantement_confusion(500,0.5))

class Magie_enchantement_poches_trouees :
    """La magie d'enchantement de poches trouées. Renvoie un sort de création d'enchantement de poches trouées plus ou moins puissant."""
    def __init__(self):
        self.nom = "Poches_trouees"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Enchante_agissant(0.1,200,10,10000,Enchantement_poches_trouees(50,0.005))
        elif niveau == 2:
            return Enchante_agissant(0.1,180,10,10000,Enchantement_poches_trouees(100,0.01))
        elif niveau == 3:
            return Enchante_agissant(0.1,160,10,10000,Enchantement_poches_trouees(150,0.015))
        elif niveau == 4:
            return Enchante_agissant(0.1,150,10,10000,Enchantement_poches_trouees(200,0.02))
        elif niveau == 5:
            return Enchante_agissant(0.1,140,10,10000,Enchantement_poches_trouees(250,0.025))
        elif niveau == 6:
            return Enchante_agissant(0.1,130,10,10000,Enchantement_poches_trouees(300,0.03))
        elif niveau == 7:
            return Enchante_agissant(0.1,118,10,10000,Enchantement_poches_trouees(350,0.035))
        elif niveau == 8:
            return Enchante_agissant(0.1,109,10,10000,Enchantement_poches_trouees(400,0.04))
        elif niveau == 9:
            return Enchante_agissant(0.1,103,10,10000,Enchantement_poches_trouees(450,0.045))
        elif niveau == 10:
            return Enchante_agissant(0.1,100,10,10000,Enchantement_poches_trouees(500,0.05))

class Magie_enchantement_force :
    """La magie d'enchantement de force. Renvoie un sort de création d'enchantement de force plus ou moins puissant."""
    def __init__(self):
        self.nom = "Force"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Enchante_agissant(0.1,200,10,10000,Enchantement_force(50,20))
        elif niveau == 2:
            return Enchante_agissant(0.1,180,10,10000,Enchantement_force(100,20))
        elif niveau == 3:
            return Enchante_agissant(0.1,160,10,10000,Enchantement_force(150,20))
        elif niveau == 4:
            return Enchante_agissant(0.1,150,10,10000,Enchantement_force(200,20))
        elif niveau == 5:
            return Enchante_agissant(0.1,140,10,10000,Enchantement_force(250,50))
        elif niveau == 6:
            return Enchante_agissant(0.1,130,10,10000,Enchantement_force(300,50))
        elif niveau == 7:
            return Enchante_agissant(0.1,118,10,10000,Enchantement_force(350,50))
        elif niveau == 8:
            return Enchante_agissant(0.1,109,10,10000,Enchantement_force(400,80))
        elif niveau == 9:
            return Enchante_agissant(0.1,103,10,10000,Enchantement_force(450,80))
        elif niveau == 10:
            return Enchante_agissant(0.1,100,10,10000,Enchantement_force(500,100))

class Magie_enchantement_vision :
    """La magie d'enchantement de vision. Renvoie un sort de création d'enchantement de vision plus ou moins puissant."""
    def __init__(self):
        self.nom = "Vision"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Enchante_agissant(0.1,200,10,10000,Enchantement_vision(50,2))
        elif niveau == 2:
            return Enchante_agissant(0.1,180,10,10000,Enchantement_vision(100,2))
        elif niveau == 3:
            return Enchante_agissant(0.1,160,10,10000,Enchantement_vision(150,2))
        elif niveau == 4:
            return Enchante_agissant(0.1,150,10,10000,Enchantement_vision(200,2))
        elif niveau == 5:
            return Enchante_agissant(0.1,140,10,10000,Enchantement_vision(250,5))
        elif niveau == 6:
            return Enchante_agissant(0.1,130,10,10000,Enchantement_vision(300,5))
        elif niveau == 7:
            return Enchante_agissant(0.1,118,10,10000,Enchantement_vision(350,5))
        elif niveau == 8:
            return Enchante_agissant(0.1,109,10,10000,Enchantement_vision(400,8))
        elif niveau == 9:
            return Enchante_agissant(0.1,103,10,10000,Enchantement_vision(450,8))
        elif niveau == 10:
            return Enchante_agissant(0.1,100,10,10000,Enchantement_vision(500,10))

class Magie_enchantement_celerite :
    """La magie d'enchantement de célérité. Renvoie un sort de création d'enchantement de célérité plus ou moins puissant."""
    def __init__(self):
        self.nom = "Celerite"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Enchante_agissant(0.1,200,10,10000,Enchantement_vitesse(50,-1))
        elif niveau == 2:
            return Enchante_agissant(0.1,180,10,10000,Enchantement_vitesse(100,-1))
        elif niveau == 3:
            return Enchante_agissant(0.1,160,10,10000,Enchantement_vitesse(150,-1))
        elif niveau == 4:
            return Enchante_agissant(0.1,150,10,10000,Enchantement_vitesse(200,-1))
        elif niveau == 5:
            return Enchante_agissant(0.1,140,10,10000,Enchantement_vitesse(250,-2.5))
        elif niveau == 6:
            return Enchante_agissant(0.1,130,10,10000,Enchantement_vitesse(300,-2.5))
        elif niveau == 7:
            return Enchante_agissant(0.1,118,10,10000,Enchantement_vitesse(350,-2.5))
        elif niveau == 8:
            return Enchante_agissant(0.1,109,10,10000,Enchantement_vitesse(400,-4))
        elif niveau == 9:
            return Enchante_agissant(0.1,103,10,10000,Enchantement_vitesse(450,-4))
        elif niveau == 10:
            return Enchante_agissant(0.1,100,10,10000,Enchantement_vitesse(500,-5))

class Magie_enchantement_vitalité :
    """La magie d'enchantement de vitalité. Renvoie un sort de création d'enchantement de vitalité plus ou moins puissant."""
    def __init__(self):
        self.nom = "Vitalite"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Enchante_agissant(0.1,200,10,10000,Enchantement_pv(50,10))
        elif niveau == 2:
            return Enchante_agissant(0.1,180,10,10000,Enchantement_pv(100,10))
        elif niveau == 3:
            return Enchante_agissant(0.1,160,10,10000,Enchantement_pv(150,10))
        elif niveau == 4:
            return Enchante_agissant(0.1,150,10,10000,Enchantement_pv(200,10))
        elif niveau == 5:
            return Enchante_agissant(0.1,140,10,10000,Enchantement_pv(250,25))
        elif niveau == 6:
            return Enchante_agissant(0.1,130,10,10000,Enchantement_pv(300,25))
        elif niveau == 7:
            return Enchante_agissant(0.1,118,10,10000,Enchantement_pv(350,25))
        elif niveau == 8:
            return Enchante_agissant(0.1,109,10,10000,Enchantement_pv(400,40))
        elif niveau == 9:
            return Enchante_agissant(0.1,103,10,10000,Enchantement_pv(450,40))
        elif niveau == 10:
            return Enchante_agissant(0.1,100,10,10000,Enchantement_pv(500,50))

class Magie_enchantement_absorption :
    """La magie d'enchantement d'absorption. Renvoie un sort de création d'enchantement d'absorption plus ou moins puissant."""
    def __init__(self):
        self.nom = "Absorption"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Enchante_agissant(0.1,200,10,10000,Enchantement_pm(50,10))
        elif niveau == 2:
            return Enchante_agissant(0.1,180,10,10000,Enchantement_pm(100,10))
        elif niveau == 3:
            return Enchante_agissant(0.1,160,10,10000,Enchantement_pm(150,10))
        elif niveau == 4:
            return Enchante_agissant(0.1,150,10,10000,Enchantement_pm(200,10))
        elif niveau == 5:
            return Enchante_agissant(0.1,140,10,10000,Enchantement_pm(250,25))
        elif niveau == 6:
            return Enchante_agissant(0.1,130,10,10000,Enchantement_pm(300,25))
        elif niveau == 7:
            return Enchante_agissant(0.1,118,10,10000,Enchantement_pm(350,25))
        elif niveau == 8:
            return Enchante_agissant(0.1,109,10,10000,Enchantement_pm(400,40))
        elif niveau == 9:
            return Enchante_agissant(0.1,103,10,10000,Enchantement_pm(450,40))
        elif niveau == 10:
            return Enchante_agissant(0.1,100,10,10000,Enchantement_pm(500,50))

class Magie_enchantement_immunite :
    """La magie d'enchantement d'immunité. Renvoie un sort de création d'enchantement d'immunité plus ou moins puissant."""
    def __init__(self):
        self.nom = "Immunite"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Enchante_agissant(0.1,200,10,10000,Enchantement_immunite(50,10))
        elif niveau == 2:
            return Enchante_agissant(0.1,180,10,10000,Enchantement_immunite(100,8))
        elif niveau == 3:
            return Enchante_agissant(0.1,160,10,10000,Enchantement_immunite(150,6))
        elif niveau == 4:
            return Enchante_agissant(0.1,150,10,10000,Enchantement_immunite(200,4))
        elif niveau == 5:
            return Enchante_agissant(0.1,140,10,10000,Enchantement_immunite(250,2))
        elif niveau == 6:
            return Enchante_agissant(0.1,130,10,10000,Enchantement_immunite(300,0))
        elif niveau == 7:
            return Enchante_agissant(0.1,118,10,10000,Enchantement_immunite(350,0))
        elif niveau == 8:
            return Enchante_agissant(0.1,109,10,10000,Enchantement_immunite(400,-40))
        elif niveau == 9:
            return Enchante_agissant(0.1,103,10,10000,Enchantement_immunite(450,-70))
        elif niveau == 10:
            return Enchante_agissant(0.1,100,10,10000,Enchantement_immunite(500,-10))

class Magie_enchantement_flamme :
    """La magie d'enchantement de flamme. Renvoie un sort de création d'enchantement de flamme plus ou moins puissant."""
    def __init__(self):
        self.nom = "Flamme"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Enchante_agissant(0.1,200,10,10000,Enchantement_flamme(50,0.1))
        elif niveau == 2:
            return Enchante_agissant(0.1,180,10,10000,Enchantement_flamme(100,0.2))
        elif niveau == 3:
            return Enchante_agissant(0.1,160,10,10000,Enchantement_flamme(150,0.3))
        elif niveau == 4:
            return Enchante_agissant(0.1,150,10,10000,Enchantement_flamme(200,0.4))
        elif niveau == 5:
            return Enchante_agissant(0.1,140,10,10000,Enchantement_flamme(250,0.5))
        elif niveau == 6:
            return Enchante_agissant(0.1,130,10,10000,Enchantement_flamme(300,0.6))
        elif niveau == 7:
            return Enchante_agissant(0.1,118,10,10000,Enchantement_flamme(350,0.7))
        elif niveau == 8:
            return Enchante_agissant(0.1,109,10,10000,Enchantement_flamme(400,0.8))
        elif niveau == 9:
            return Enchante_agissant(0.1,103,10,10000,Enchantement_flamme(450,0.9))
        elif niveau == 10:
            return Enchante_agissant(0.1,100,10,10000,Enchantement_flamme(500,1))

class Magie_enchantement_neige :
    """La magie d'enchantement de flamme. Renvoie un sort de création d'enchantement de neige plus ou moins puissant."""
    def __init__(self):
        self.nom = "Neige"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Enchante_agissant(0.1,200,10,10000,Enchantement_neige(50,0.1))
        elif niveau == 2:
            return Enchante_agissant(0.1,180,10,10000,Enchantement_neige(100,0.2))
        elif niveau == 3:
            return Enchante_agissant(0.1,160,10,10000,Enchantement_neige(150,0.3))
        elif niveau == 4:
            return Enchante_agissant(0.1,150,10,10000,Enchantement_neige(200,0.4))
        elif niveau == 5:
            return Enchante_agissant(0.1,140,10,10000,Enchantement_neige(250,0.5))
        elif niveau == 6:
            return Enchante_agissant(0.1,130,10,10000,Enchantement_neige(300,0.6))
        elif niveau == 7:
            return Enchante_agissant(0.1,118,10,10000,Enchantement_neige(350,0.7))
        elif niveau == 8:
            return Enchante_agissant(0.1,109,10,10000,Enchantement_neige(400,0.8))
        elif niveau == 9:
            return Enchante_agissant(0.1,103,10,10000,Enchantement_neige(450,0.9))
        elif niveau == 10:
            return Enchante_agissant(0.1,100,10,10000,Enchantement_neige(500,1))

class Magie_enchantement_sable :
    """La magie d'enchantement de flamme. Renvoie un sort de création d'enchantement de sable plus ou moins puissant."""
    def __init__(self):
        self.nom = "Sable"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Enchante_agissant(0.1,200,10,10000,Enchantement_sable(50,0.1))
        elif niveau == 2:
            return Enchante_agissant(0.1,180,10,10000,Enchantement_sable(100,0.2))
        elif niveau == 3:
            return Enchante_agissant(0.1,160,10,10000,Enchantement_sable(150,0.3))
        elif niveau == 4:
            return Enchante_agissant(0.1,150,10,10000,Enchantement_sable(200,0.4))
        elif niveau == 5:
            return Enchante_agissant(0.1,140,10,10000,Enchantement_sable(250,0.5))
        elif niveau == 6:
            return Enchante_agissant(0.1,130,10,10000,Enchantement_sable(300,0.6))
        elif niveau == 7:
            return Enchante_agissant(0.1,118,10,10000,Enchantement_sable(350,0.7))
        elif niveau == 8:
            return Enchante_agissant(0.1,109,10,10000,Enchantement_sable(400,0.8))
        elif niveau == 9:
            return Enchante_agissant(0.1,103,10,10000,Enchantement_sable(450,0.9))
        elif niveau == 10:
            return Enchante_agissant(0.1,100,10,10000,Enchantement_sable(500,1))

class Magie_enchantement_tenebre :
    """La magie d'enchantement de flamme. Renvoie un sort de création d'enchantement de tenebre plus ou moins puissant."""
    def __init__(self):
        self.nom = "Tenebre"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Enchante_agissant(0.1,200,10,10000,Enchantement_tenebre(50,0.1))
        elif niveau == 2:
            return Enchante_agissant(0.1,180,10,10000,Enchantement_tenebre(100,0.2))
        elif niveau == 3:
            return Enchante_agissant(0.1,160,10,10000,Enchantement_tenebre(150,0.3))
        elif niveau == 4:
            return Enchante_agissant(0.1,150,10,10000,Enchantement_tenebre(200,0.4))
        elif niveau == 5:
            return Enchante_agissant(0.1,140,10,10000,Enchantement_tenebre(250,0.5))
        elif niveau == 6:
            return Enchante_agissant(0.1,130,10,10000,Enchantement_tenebre(300,0.6))
        elif niveau == 7:
            return Enchante_agissant(0.1,118,10,10000,Enchantement_tenebre(350,0.7))
        elif niveau == 8:
            return Enchante_agissant(0.1,109,10,10000,Enchantement_tenebre(400,0.8))
        elif niveau == 9:
            return Enchante_agissant(0.1,103,10,10000,Enchantement_tenebre(450,0.9))
        elif niveau == 10:
            return Enchante_agissant(0.1,100,10,10000,Enchantement_tenebre(500,1))

class Magie_enchantement_rouille :
    """La magie d'enchantement de rouille. Renvoie un sort de création d'enchantement de rouille plus ou moins puissant."""
    def __init__(self):
        self.nom = "Rouille"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Enchante_item(0.1,200,10,10000,Enchantement_arme(50,-0.05,-1))
        elif niveau == 2:
            return Enchante_item(0.1,180,10,10000,Enchantement_arme(100,-0.1,-1))
        elif niveau == 3:
            return Enchante_item(0.1,160,10,10000,Enchantement_arme(150,-0.15,-1))
        elif niveau == 4:
            return Enchante_item(0.1,150,10,10000,Enchantement_arme(200,-0.2,-1))
        elif niveau == 5:
            return Enchante_item(0.1,140,10,10000,Enchantement_arme(250,-0.25,-2))
        elif niveau == 6:
            return Enchante_item(0.1,130,10,10000,Enchantement_arme(300,-0.3,-2))
        elif niveau == 7:
            return Enchante_item(0.1,118,10,10000,Enchantement_arme(350,-0.35,-2))
        elif niveau == 8:
            return Enchante_item(0.1,109,10,10000,Enchantement_arme(400,-0.4,-3))
        elif niveau == 9:
            return Enchante_item(0.1,103,10,10000,Enchantement_arme(450,-0.45,-3))
        elif niveau == 10:
            return Enchante_item(0.1,100,10,10000,Enchantement_arme(500,-0.5,-4))

class Magie_enchantement_renforcement :
    """La magie d'enchantement de renforcement. Renvoie un sort de création d'enchantement de renforcement plus ou moins puissant."""
    def __init__(self):
        self.nom = "Renforcement"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Enchante_item(0.1,200,10,10000,Enchantement_arme(50,0.05,1))
        elif niveau == 2:
            return Enchante_item(0.1,180,10,10000,Enchantement_arme(100,0.1,1))
        elif niveau == 3:
            return Enchante_item(0.1,160,10,10000,Enchantement_arme(150,0.15,1))
        elif niveau == 4:
            return Enchante_item(0.1,150,10,10000,Enchantement_arme(200,0.2,1))
        elif niveau == 5:
            return Enchante_item(0.1,140,10,10000,Enchantement_arme(250,0.25,2))
        elif niveau == 6:
            return Enchante_item(0.1,130,10,10000,Enchantement_arme(300,0.3,2))
        elif niveau == 7:
            return Enchante_item(0.1,118,10,10000,Enchantement_arme(350,0.35,2))
        elif niveau == 8:
            return Enchante_item(0.1,109,10,10000,Enchantement_arme(400,0.4,3))
        elif niveau == 9:
            return Enchante_item(0.1,103,10,10000,Enchantement_arme(450,0.45,3))
        elif niveau == 10:
            return Enchante_item(0.1,100,10,10000,Enchantement_arme(500,0.5,4))

class Magie_enchantement_bombe :
    """La magie d'enchantement de bombe. Renvoie un sort de création d'enchantement de bombe plus ou moins puissant."""
    def __init__(self):
        self.nom = "Bombe"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Enchante_item(0.1,200,10,10000,Enchantement_bombe(50,Charge(2,5)))
        elif niveau == 2:
            return Enchante_item(0.1,180,10,10000,Enchantement_bombe(100,Charge(2,6)))
        elif niveau == 3:
            return Enchante_item(0.1,160,10,10000,Enchantement_bombe(150,Charge(3,6)))
        elif niveau == 4:
            return Enchante_item(0.1,150,10,10000,Enchantement_bombe(200,Charge(4,7)))
        elif niveau == 5:
            return Enchante_item(0.1,140,10,10000,Enchantement_bombe(250,Charge(5,7)))
        elif niveau == 6:
            return Enchante_item(0.1,130,10,10000,Enchantement_bombe(300,Charge(5,8)))
        elif niveau == 7:
            return Enchante_item(0.1,118,10,10000,Enchantement_bombe(350,Charge(6,8)))
        elif niveau == 8:
            return Enchante_item(0.1,109,10,10000,Enchantement_bombe(400,Charge(7,9)))
        elif niveau == 9:
            return Enchante_item(0.1,103,10,10000,Enchantement_bombe(450,Charge(8,9)))
        elif niveau == 10:
            return Enchante_item(0.1,100,10,10000,Enchantement_bombe(500,Charge(8,10)))

class Magie_reserve :
    """La magie de réserve de mana. Renvoie un sort de création de réserve de mana plus ou moins puissant."""
    def __init__(self):
        self.nom = "Reserve"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Economie(0.1,0,3,10000,0.5,Reserve_mana())
        elif niveau == 2:
            return Economie(0.1,0,3,10000,0.55,Reserve_mana())
        elif niveau == 3:
            return Economie(0.1,0,3,10000,0.6,Reserve_mana())
        elif niveau == 4:
            return Economie(0.1,0,3,10000,0.65,Reserve_mana())
        elif niveau == 5:
            return Economie(0.1,0,3,10000,0.7,Reserve_mana())
        elif niveau == 6:
            return Economie(0.1,0,3,10000,0.75,Reserve_mana())
        elif niveau == 7:
            return Economie(0.1,0,3,10000,0.8,Reserve_mana())
        elif niveau == 8:
            return Economie(0.1,0,3,10000,0.85,Reserve_mana())
        elif niveau == 9:
            return Economie(0.1,0,3,10000,0.9,Reserve_mana())
        elif niveau == 10:
            return Economie(0.1,0,3,10000,0.95,Reserve_mana())

class Magie_investissement :
    """La magie d'investissement de mana. Renvoie un sort de création d'investissement de mana plus ou moins puissant."""
    def __init__(self):
        self.nom = "Investissement"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Economie(0.1,0,3,10000,1.25,Investissement_mana(50))
        elif niveau == 2:
            return Economie(0.1,0,3,10000,1.35,Investissement_mana(50))
        elif niveau == 3:
            return Economie(0.1,0,3,10000,1.5,Investissement_mana(50))
        elif niveau == 4:
            return Economie(0.1,0,3,10000,1.7,Investissement_mana(50))
        elif niveau == 5:
            return Economie(0.1,0,3,10000,1.75,Investissement_mana(40))
        elif niveau == 6:
            return Economie(0.1,0,3,10000,1.8,Investissement_mana(34))
        elif niveau == 7:
            return Economie(0.1,0,3,10000,1.85,Investissement_mana(30))
        elif niveau == 8:
            return Economie(0.1,0,3,10000,1.9,Investissement_mana(26))
        elif niveau == 9:
            return Economie(0.1,0,3,10000,1.95,Investissement_mana(22))
        elif niveau == 10:
            return Economie(0.1,0,3,10000,2,Investissement_mana(20))

class Magie_explosion_de_mana :
    """La magie d'explosion de mana. Renvoie un sort d'explosion de mana plus ou moins puissant."""
    def __init__(self):
        self.nom = "Explosion_de_mana"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Explosion_de_mana(0.1,0,3,10000,Attaque(0,0.8,TERRE,3))
        elif niveau == 2:
            return Explosion_de_mana(0.1,0,3,10000,Attaque(0,0.9,TERRE,3))
        elif niveau == 3:
            return Explosion_de_mana(0.1,0,3,10000,Attaque(0,0.9,TERRE,4))
        elif niveau == 4:
            return Explosion_de_mana(0.1,0,3,10000,Attaque(0,1,TERRE,4))
        elif niveau == 5:
            return Explosion_de_mana(0.1,0,3,10000,Attaque(0,1.1,TERRE,4))
        elif niveau == 6:
            return Explosion_de_mana(0.1,0,3,10000,Attaque(0,1.2,TERRE,5))
        elif niveau == 7:
            return Explosion_de_mana(0.1,0,3,10000,Attaque(0,1.3,TERRE,5))
        elif niveau == 8:
            return Explosion_de_mana(0.1,0,3,10000,Attaque(0,1.5,TERRE,5))
        elif niveau == 9:
            return Explosion_de_mana(0.1,0,3,10000,Attaque(0,2,TERRE,6))
        elif niveau == 10:
            return Explosion_de_mana(0.1,0,3,10000,Attaque(0,3,TERRE,6))

class Magie_laser :
    """La magie de laser. Renvoie un sort de création de laser plus ou moins puissant."""
    def __init__(self):
        self.nom = "Laser"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Attaque_magique_dirigee(0.1,20,5,10000,Attaque(0,10,TERRE,5,"R__T___"))
        elif niveau == 2:
            return Attaque_magique_dirigee(0.1,18,4,10000,Attaque(0,20,TERRE,6,"R__T___"))
        elif niveau == 3:
            return Attaque_magique_dirigee(0.1,16,4,10000,Attaque(0,30,TERRE,6,"R__T___"))
        elif niveau == 4:
            return Attaque_magique_dirigee(0.1,15,3,10000,Attaque(0,40,TERRE,7,"R__T___"))
        elif niveau == 5:
            return Attaque_magique_dirigee(0.1,14,3,10000,Attaque(0,50,TERRE,7,"R__T___"))
        elif niveau == 6:
            return Attaque_magique_dirigee(0.1,13,3,10000,Attaque(0,60,TERRE,8,"R__T___"))
        elif niveau == 7:
            return Attaque_magique_dirigee(0.1,11,2,10000,Attaque(0,70,TERRE,8,"R__T___"))
        elif niveau == 8:
            return Attaque_magique_dirigee(0.1,10,2,10000,Attaque(0,80,TERRE,9,"R__T___"))
        elif niveau == 9:
            return Attaque_magique_dirigee(0.1,10,2,10000,Attaque(0,90,TERRE,9,"R__T___"))
        elif niveau == 10:
            return Attaque_magique_dirigee(0.1,10,2,10000,Attaque(0,100,TERRE,10,"R__T___"))

class Magie_brasier :
    """La magie de brasier. Renvoie un sort de création de brasier plus ou moins puissant."""
    def __init__(self):
        self.nom = "Brasier"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Attaque_magique(0.1,20,10,Attaque(0,10,FEU,5))
        elif niveau == 2:
            return Attaque_magique(0.1,18,9,Attaque(0,20,FEU,6))
        elif niveau == 3:
            return Attaque_magique(0.1,16,9,Attaque(0,30,FEU,6))
        elif niveau == 4:
            return Attaque_magique(0.1,15,8,Attaque(0,40,FEU,7))
        elif niveau == 5:
            return Attaque_magique(0.1,14,8,Attaque(0,50,FEU,7))
        elif niveau == 6:
            return Attaque_magique(0.1,13,8,Attaque(0,60,FEU,8))
        elif niveau == 7:
            return Attaque_magique(0.1,11,7,Attaque(0,70,FEU,8))
        elif niveau == 8:
            return Attaque_magique(0.1,10,7,Attaque(0,80,FEU,9))
        elif niveau == 9:
            return Attaque_magique(0.1,10,7,Attaque(0,90,FEU,9))
        elif niveau == 10:
            return Attaque_magique(0.1,10,7,Attaque(0,100,FEU,10))

class Magie_avalanche :
    """La magie d'avalanche. Renvoie un sort de création d'avalanche plus ou moins puissant."""
    def __init__(self):
        self.nom = "Avalanche"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Attaque_magique_dirigee(0.1,20,10,10000,Attaque(0,20,TERRE,5,"S__S_Pb"))
        elif niveau == 2:
            return Attaque_magique_dirigee(0.1,18,9,10000,Attaque(0,40,TERRE,6,"S__S_Pb"))
        elif niveau == 3:
            return Attaque_magique_dirigee(0.1,16,9,10000,Attaque(0,60,TERRE,6,"S__S_Pb"))
        elif niveau == 4:
            return Attaque_magique_dirigee(0.1,15,8,10000,Attaque(0,80,TERRE,7,"S__S_Pb"))
        elif niveau == 5:
            return Attaque_magique_dirigee(0.1,14,8,10000,Attaque(0,100,TERRE,7,"S__S_Pb"))
        elif niveau == 6:
            return Attaque_magique_dirigee(0.1,13,8,10000,Attaque(0,120,TERRE,8,"S__S_Pb"))
        elif niveau == 7:
            return Attaque_magique_dirigee(0.1,11,7,10000,Attaque(0,140,TERRE,8,"S__S_Pb"))
        elif niveau == 8:
            return Attaque_magique_dirigee(0.1,10,7,10000,Attaque(0,160,TERRE,9,"S__S_Pb"))
        elif niveau == 9:
            return Attaque_magique_dirigee(0.1,10,7,10000,Attaque(0,180,TERRE,9,"S__S_Pb"))
        elif niveau == 10:
            return Attaque_magique_dirigee(0.1,10,7,10000,Attaque(0,200,TERRE,10,"S__S_Pb"))

class Magie_dopage :
    """La magie de dopage. Renvoie un sort de création de dopage plus ou moins puissant."""
    def __init__(self):
        self.nom = "Dopage"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Creation_effet(0.1,50,1,Dopage(1.5))
        elif niveau == 2:
            return Creation_effet(0.1,48,1,Dopage(1.6))
        elif niveau == 3:
            return Creation_effet(0.1,46,1,Dopage(1.7))
        elif niveau == 4:
            return Creation_effet(0.1,45,1,Dopage(1.9))
        elif niveau == 5:
            return Creation_effet(0.1,44,1,Dopage(2.1))
        elif niveau == 6:
            return Creation_effet(0.1,43,1,Dopage(2.4))
        elif niveau == 7:
            return Creation_effet(0.1,41,1,Dopage(2.7))
        elif niveau == 8:
            return Creation_effet(0.1,40,1,Dopage(3.1))
        elif niveau == 9:
            return Creation_effet(0.1,40,1,Dopage(3.5))
        elif niveau == 10:
            return Creation_effet(0.1,40,1,Dopage(4))

class Magie_blizzard :
    """La magie de blizzard. Renvoie un sort de création de blizzard plus ou moins puissant."""
    def __init__(self):
        self.nom = "Blizzard"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Creation_effet(0.1,20,5,Debut_blizzard(5,0.1,7))
        elif niveau == 2:
            return Creation_effet(0.1,20,5,Debut_blizzard(5,0.15,7))
        elif niveau == 3:
            return Creation_effet(0.1,20,5,Debut_blizzard(5,0.2,7))
        elif niveau == 4:
            return Creation_effet(0.1,20,5,Debut_blizzard(5,0.25,7))
        elif niveau == 5:
            return Creation_effet(0.1,20,4,Debut_blizzard(5,0.3,8))
        elif niveau == 6:
            return Creation_effet(0.1,20,4,Debut_blizzard(6,0.3,8))
        elif niveau == 7:
            return Creation_effet(0.1,20,4,Debut_blizzard(6,0.35,8))
        elif niveau == 8:
            return Creation_effet(0.1,20,3,Debut_blizzard(6,0.4,9))
        elif niveau == 9:
            return Creation_effet(0.1,20,3,Debut_blizzard(6,0.45,9))
        elif niveau == 10:
            return Creation_effet(0.1,20,2,Debut_blizzard(6,0.5,10))

class Magie_obscurite :
    """La magie d'obscurite. Renvoie un sort de création d'obscurite plus ou moins puissant."""
    def __init__(self):
        self.nom = "Obscurite"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Creation_effet(0.1,20,5,Debut_obscurite(5,0.5,7))
        elif niveau == 2:
            return Creation_effet(0.1,20,5,Debut_obscurite(5,0.6,7))
        elif niveau == 3:
            return Creation_effet(0.1,20,5,Debut_obscurite(5,0.7,7))
        elif niveau == 4:
            return Creation_effet(0.1,20,5,Debut_obscurite(5,0.8,7))
        elif niveau == 5:
            return Creation_effet(0.1,20,4,Debut_obscurite(5,0.9,8))
        elif niveau == 6:
            return Creation_effet(0.1,20,4,Debut_obscurite(6,1,8))
        elif niveau == 7:
            return Creation_effet(0.1,20,4,Debut_obscurite(6,1.2,8))
        elif niveau == 8:
            return Creation_effet(0.1,20,3,Debut_obscurite(6,1.4,9))
        elif niveau == 9:
            return Creation_effet(0.1,20,3,Debut_obscurite(6,1.7,9))
        elif niveau == 10:
            return Creation_effet(0.1,20,2,Debut_obscurite(6,2,10))

class Magie_instakill :
    """La magie d'instakill. Renvoie un sort de création d'instakill plus ou moins puissant."""
    def __init__(self):
        self.nom = "Instakill"

    def donne_magie(self,niveau):
        if niveau == 1:
            return Creation_effet(0.1,200,10,Instakill(5))
        elif niveau == 2:
            return Creation_effet(0.1,200,10,Instakill(4))
        elif niveau == 3:
            return Creation_effet(0.1,200,10,Instakill(3))
        elif niveau == 4:
            return Creation_effet(0.1,200,10,Instakill(2))
        elif niveau == 5:
            return Creation_effet(0.1,200,10,Instakill(1))
        elif niveau == 6:
            return Creation_effet(0.1,200,10,Instakill(0))
        elif niveau == 7:
            return Creation_effet(0.1,200,10,Instakill(-1))
        elif niveau == 8:
            return Creation_effet(0.1,200,10,Instakill(-2))
        elif niveau == 9:
            return Creation_effet(0.1,200,10,Instakill(-3))
        elif niveau == 10:
            return Creation_effet(0.1,200,10,Instakill(-4))

class Effet :
    """Les effets regroupent des choses qui arrivent à des éléments du système. Ils peuvent cibler une case, un mur, un agissant, un étage, etc. et sont souvent limités dans le temps ou par d'autres conditions. Ils sont évalués par le controleur dans différentes circonstances."""
    def __init__(self):
        print("a surdéfinir")

    def action(self):
        """La fonction qui exécute l'action de l'effet. En général, renvoie des valeurs que le controleur traitera."""
        print("a surdéfinir")

    def execute(self):
        """La fonction qui est appelée par le controleur. Détermine, d'après les informations transmises par le controleur, si l'action doit être effectuée ou pas. Vérifie si l'effet doit encore exister ou non."""
        print("a surdéfinir")

    def get_image(self):
        return Effet_vue()

#On distingue les effets par circonstances d'appel.
class On_tick(Effet) :
    """La classe des effets appelés à chaque tour."""
    pass

class On_debut_tour(On_tick):
    """La classe des effets appelés au début du tour."""
    pass

class On_post_decision(On_tick):
    """La classe des effets appelés après la phase de décision."""
    pass

class On_post_action(On_tick):
    """La classe des effets appelés après la phase d'action."""
    pass

class On_pre_attack(On_tick):
    """La classe des effets appelés avant les attaques."""
    pass

class On_fin_tour(On_tick):
    """La classe des effets appelés à la fin du tour."""
    pass

class Evenement(On_tick) :
    """La classe des effets limités par le temps, appelés une seule fois par tour."""
    def __init__(self,temps_restant):
        self.affiche = False
        self.temps_restant=temps_restant
        self.phase = "démarrage"

    def action(self):
        """La fonction qui exécute l'action de l'évènement. En général, renvoie des valeurs que le controleur traitera ?"""
        print("a surdéfinir")
    def execute(self):
        """La fonction qui est appelée par le controleur. Détermine, d'après les informations transmises par le controleur, si l'action doit être effectuée ou pas. Vérifie si l'évènement est terminé ou non."""
        self.temps_restant-=1
        #on exécute l'évènement
        self.action()
        return (self.temps_restant<=0)

class Protection_general(Evenement,On_post_action):
    """Le joueur qui a utilisé un bouclier 'protège' une zone autour de lui. C'est à dire qu'à chaque tour, d'après sa position, sa direction et les murs, certaines cases reçoivent une protection jusqu'à la fin du tour."""
    def __init__(self,temps_restant,bouclier):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.bouclier = bouclier #Techniquement c'est le bouclier qui intercepte.

    def action(self,agissant):
        cases = get_cases_voisines(agissant.get_position(),0) #Seule la case de l'agissant est protégée par cette version de la protection.
        for case in cases :
            case.effets.append(Protection_particulier(1,bouclier,[agissant.dir_regard]))

    def execute(self,agissant):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.phase = "terminé"
        else :
            self.action(agissant)

class Investissement_mana(Evenement,On_debut_tour):
    """Le joueur met du mana de côté, et en a plus après !"""
    def __init__(self,temps_restant):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.mana = 0

    def action(self,managissant):
        if self.phase == "démarrage" :
            self.mana += managissant
        elif self.phase == "terminé":
            managissant.mana += self.mana

    def execute(self,managissant):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.action(managissant)
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.phase = "terminé"
            self.action(managissant)

class Obscurite(Evenement,On_debut_tour):
    """Evenement d'obscurité."""
    def __init__(self,gain_opacite,temps_restant):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_opacite = gain_opacite

    def action(self,case): #La case affectée devient plus impénétrable à la lumière
        if self.phase == "démarrage" :
            case.opacite += gain_opacite
        elif self.phase == "terminé":
            case.opacite -= gain_opacite

    def execute(self,case):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.action(case)
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.phase = "terminé"
            self.action(case)

class Protection_particulier(Evenement,On_post_action):
    """La case protégée par le bouclier est 'entourée' par ce dernier, c'est à dire que pour y rentrer par certains côtés, une attaque doit d'abord être affectée par le bouclier."""
    def __init__(self,temps_restant,bouclier,directions):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.bouclier = bouclier #Techniquement c'est le bouclier qui intercepte.
        self.directions = directions

    def action(self,position):
        occupants = get_voisins(position) #À passer en évènements
        if get_dir_opposee(attaque.direction) in self.directions:
            self.bouclier.intercepte(attaque)

    def execute(self,position):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.phase = "terminé"
        else :
            self.action(case)

class Blizzard(Evenement,On_post_action):
    """Evenement de blizzard."""
    def __init__(self,gain_latence,temps_restant):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_latence = gain_latence

    def action(self,position):
        if self.phase == "en cours":
            occupants = get_voisins(position)
            for occupant in occupant :
                agissant.latence += gain_latence

    def execute(self,position):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.phase = "terminé"
        else :
            self.action(case)

class Enchantement(Evenement) :
    """Des effets avec un temps très long ! Leur classe à part permet de les affecter différement."""
    def __init__(self,temps_restant):
        self.affiche = False
        self.temps_restant=temps_restant
        self.phase = "démarrage"

    def action(self):
        """La fonction qui exécute l'action de l'enchantement. En général, renvoie des valeurs que le controleur traitera ?"""
        print("a surdéfinir")

    def execute(self,agissant):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.action(agissant)
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.phase = "terminé"
            self.action(agissant)

class Enchantement_force(Enchantement,On_debut_tour):
    """Les enchantements qui affectent la force (en positif ou négatif)."""
    def __init__(self,temps_restant,gain_force):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_force = gain_force

    def action(self,agissant):
        if self.phase == "démarrage" and "enchantf" not in agissant.taux_force :
            agissant.taux_force["enchantf"] = gain_force
        elif self.phase == "terminé":
            agissant.taux_force.pop("enchantf")


class Enchantement_vision(Enchantement,On_debut_tour):
    """Les enchantements qui affectent le champ de vision (en positif ou négatif)."""
    def __init__(self,temps_restant,gain_vision):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_vision = gain_vision

    def action(self,agissant):
        skill = trouve_skill(agissant.classe_principale,Skill_vision)
        if self.phase == "démarrage" :
            skill.portee += gain_vision
        elif self.phase == "terminé":
            skill.portee -= gain_vision

class Enchantement_pv(Enchantement,On_debut_tour):
    """Les enchantements qui affectent la régénération des PV (en positif ou négatif)."""
    def __init__(self,temps_restant,gain_pv):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_pv = gain_pv

    def action(self,agissant):
        if self.phase == "démarrage" :
            agissant.regen_pv += gain_pv
        elif self.phase == "terminé":
            agissant.regen_pv -= gain_pv

class Enchantement_pm(Enchantement,On_debut_tour):
    """Les enchantements qui affectent la régénération des PM (en positif ou négatif)."""
    def __init__(self,temps_restant,gain_pm):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_pm = gain_pm

    def action(self,agissant):
        if self.phase == "démarrage" :
            agissant.regen_pm += gain_pm
        elif self.phase == "terminé":
            agissant.regen_pm -= gain_pm

class Enchantement_confusion(Enchantement,On_post_decision):
    """Les enchantements qui provoque des erreurs de direction."""
    def __init__(self,temps_restant,taux_erreur):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.taux_erreur = taux_erreur

    def action(self,agissant):
        if self.phase == "en cours":
            if random.random() < self.taux_erreur and dir_voulue != None and agissant.latence <= 0 :
                dir_voulue = agissant.dir_regard
                dir_possibles = [HAUT,BAS,GAUCHE,DROITE].remove(dir_voulue)
                agissant.dir_regard = dir_possible[random.randint(0,2)]

    def execute(self,agissant):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.phase = "terminé"
        else :
            self.action(agissant)

class Enchantement_poches_trouees(Enchantement,On_debut_tour):
    """Les enchantements qui fait droper des items involontairement."""
    def __init__(self,temps_restant,taux_drop):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.taux_drop = taux_drop

    def action(self,agissant):
        if self.phase == "en cours":
            if random.random() < self.taux_drop :
                agissant.drop_random()

    def execute(self,agissant):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.phase = "terminé"
        else :
            self.action(agissant)

class Enchantement_vitesse(Enchantement,On_debut_tour):
    """Les enchantements qui affectent la vitesse (en positif ou négatif)."""
    def __init__(self,temps_restant,gain_vitesse):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_vitesse = gain_vitesse

    def action(self,agissant):
        if self.phase == "démarrage" and "enchantv" not in agissant.taux_vitesse :
            agissant.taux_vitesse["enchantv"] = gain_vitesse
        elif self.phase == "terminé":
            agissant.taux_vitesse.pop("enchantv")

class Enchantement_immunite(Enchantement,On_debut_tour):
    """Enchantement qui confère une immunité aux maladies, à condition de disposer de suffisamment de priorité."""
    def __init__(self,temps_restant,superiorite):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.superiorite = superiorite

    def action(self,agissant):
        if self.phase == "en cours":
            for effet in agissant.effet :
                if issubclass(type(effet),Maladie):
                    if maladie.priorite + self.superiorite < agissant.superiorite :
                        effet.phase = "terminé"
                        effet.action(agissant)
                        agissant.effet.remove(effet)

    def execute(self,agissant):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.phase = "terminé"
        else :
            self.action(agissant)

class Enchantement_flamme(Enchantement,On_debut_tour):
    """Enchantement qui augmente l'affinité à l'élément feu."""
    def __init__(self,temps_restant,gain_aff):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_aff = gain_aff

    def action(self,agissant):
        if self.phase == "démarrage" and "enchantf" not in agissant.taux_aff_f :
            agissant.taux_aff_f["enchantf"] = gain_aff
        elif self.phase == "terminé":
            agissant.taux_aff_f.pop("enchantf")

class Enchantement_neige(Enchantement,On_debut_tour):
    """Enchantement qui augmente l'affinité à l'élément glace."""
    def __init__(self,temps_restant,gain_aff):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_aff = gain_aff

    def action(self,agissant):
        if self.phase == "démarrage" and "enchantf" not in agissant.taux_aff_g :
            agissant.taux_aff_g["enchantn"] = gain_aff
        elif self.phase == "terminé":
            agissant.taux_aff_g.pop("enchantn")

class Enchantement_sable(Enchantement,On_debut_tour):
    """Enchantement qui augmente l'affinité à l'élément terre."""
    def __init__(self,temps_restant,gain_aff):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_aff = gain_aff

    def action(self,agissant):
        if self.phase == "démarrage" and "enchants" not in agissant.taux_aff_t :
            agissant.taux_aff_t["enchants"] = gain_aff
        elif self.phase == "terminé":
            agissant.taux_aff_t.pop("enchants")

class Enchantement_tenebre(Enchantement,On_debut_tour):
    """Enchantement qui augmente l'affinité à l'élément ombre."""
    def __init__(self,temps_restant,gain_aff):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_aff = gain_aff

    def action(self,agissant):
        if self.phase == "démarrage" and "enchantt" not in agissant.taux_aff_o :
            agissant.taux_aff_o["enchantt"] = gain_aff
        elif self.phase == "terminé":
            agissant.taux_aff_o.pop("enchantt")

class Enchantement_arme(Enchantement,On_debut_tour):
    """Enchantement qui modifie les statistiques d'une arme (en positif ou négatif)."""
    def __init__(self,temps_restant,gain_force,gain_portee):
        self.temps_restant = temps_restant
        self.affiche = False
        self.phase = "démarrage"
        self.gain_force = gain_force
        self.gain_portee = gain_portee

    def action(self,arme):
        if self.phase == "démarrage" and "enchantf" not in arme.taux_force :
            arme.taux_force["enchantf"] = gain_force
        elif self.phase == "terminé":
            arme.taux_force.pop("enchantf")
        if self.phase == "démarrage" and "enchantp" not in arme.taux_portee :
            arme.taux_portee["enchantp"] = gain_portee
        elif self.phase == "terminé":
            arme.taux_portee.pop("enchantp")

class Enchantement_bombe(Enchantement,On_debut_tour):
    """Enchantement qui confère des propriétés explosives à un item."""
    def __init__(self,temps_restant,effet):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.charge = effet

    def action(self,item):
        if self.phase == "démarrage" :
            item.effets = self.effet
        elif self.phase == "terminé":
            item.effets.remove(self.effet)

class Maladie(On_post_decision,On_tick):
    """L'effet de maladie. Applique un déboost à l'agissant. Peut se transmettre aux voisins. Il existe différentes maladies."""
    def __init__(self,contagiosite,distance,persistence,virulence):
        self.affiche = False
        self.phase = "démarrage"
        self.contagiosite = contagiosite
        self.distance = distance
        self.persistence = persistence
        self.immunite = 0

    def action(self,malade):
        print("À surdéfinir !")

    def contagion(self,malade): #Méthode propre aux maladies
        voisins = get_voisins(malade,distance)
        for voisin in voisins :
            if random.random() < contagiosite and (type(self) != type(effet) for effet in voisin.effets): #On ne tombe pas deux fois malade de la même maladie
                voisin.effets.append(type(self)(self.contagiosite,self.distance,self.persistence,self.virulence)) #Nid à problèmes très potentiel !

    def execute(self,malade):
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.immunite <= self.persistence :
            self.phase = "terminé"
        else :
            self.action(malade)

class Tirnogose(Maladie):
    """Maladie qui cause une perte progressive de PV. Peut se transmettre aux voisins."""
    def __init__(self,contagiosite,distance,persistence,virulence):
        self.affiche = False
        self.phase = "démarrage"
        self.contagiosite = contagiosite
        self.distance = distance
        self.persistence = persistence
        self.immunite = 0
        self.virulence = virulence

    def action(self,malade):
        if self.phase == "en cours" :
            malade.pv -= self.virulence
            self.immunite += 1

class Fibaluse(Maladie):
    """Maladie qui réduit les statistiques. Peut se transmettre aux voisins."""
    def __init__(self,contagiosite,distance,persistence,virulence):
        self.affiche = False
        self.phase = "démarrage"
        self.contagiosite = contagiosite
        self.distance = distance
        self.persistence = persistence
        self.immunite = 0
        self.virulence = virulence

    def action(self,malade):
        if self.phase == "démarrage" and "maladf" not in malade.taux_stats :
            arme.taux_stats["maladf"] = virulence
        elif self.phase == "en cours" :
            self.immunite += 1
        elif self.phase == "terminé" :
            arme.taux_stats.pop("maladf")

    def execute(self,malade):
        if self.phase == "démarrage" :
            self.action(malade)
            self.phase = "en cours"
        elif self.persistence <= self.immunite :
            self.phase = "terminé"
            self.action(malade)
        else :
            self.action(malade)

class Ibsutiomialgie(Maladie):
    """Maladie qui peut causer une mort subite. Peut se transmettre aux voisins."""
    def __init__(self,contagiosite,distance,persistence,virulence):
        self.affiche = False
        self.phase = "démarrage"
        self.contagiosite = contagiosite
        self.distance = distance
        self.persistence = persistence
        self.immunite = 0
        self.virulence = virulence

    def action(self,malade):
        if self.phase == "démarrage" and random.random() < virulence :
            malade.pv = 0
        elif self.phase == "en cours" :
            self.immunite += 1

class Poison(On_debut_tour,On_tick):
    """La classe des effets d'empoisonnement."""
    def __init__(self,responsable,degats_max,progression):
        self.affiche = False
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = 0
        self.progression = progression
        self.degats_max = degats_max

    def action(self,victime):
        if self.phase == "en cours" :
            victime.pv -= self.degats
            if self.degats < self.degats_max:
                self.degats += self.progression

    def execute(self,victime):
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif victime.etat == "mort" :
            self.phase = "terminé"
        else :
            self.action(victime)

class Time_limited(Effet):
    """Classe des effets limités par le temps, qu'on ne peut pas considérer comme des événements car leur appel est irrégulier."""
    def __init__(self,temps_restant):
        self.affiche = False
        self.phase = "démarrage"
        self.temps_restant = temps_restant

    def wait(self):
        self.temps_resant -= 1
        if self.temps_restant <= 0:
            self.phase = "terminé"

class On_need(Effet) :
    """Classe des effets appelés lors de circonstances particulières. Ils n'ont pas besoin d'être mis à jour, pris en compte ou quoique ce soit le reste du temps."""
    pass

class Reserve_mana(On_need):
    """Effet qui correspond à une réserve de mana pour le joueur qui peut piocher dedans lorsqu'il en a besoin, mais ce mana n'est pas compté dans le calcul de son mana max."""
    def __init__(self):
        self.affiche = False
        self.phase = "démarrage"
        self.mana = 0

    def action(self,mana):
        if self.phase == "démarrage" :
            self.mana += mana
        elif self.phase == "en cours":
            self.mana -= mana

    def execute(self,mana):
        if self.phase == "démarrage" :
            self.action(mana)
            self.phase = "en cours"
        elif self.phase == "en cours" :
            self.action(mana)
        if self.mana <= 0 :
            self.phase = "terminé"

class On_attack(Effet):
    """Classe des effets appelés lors d'une attaque."""
    pass

class One_shot(Effet):
    """Classe des effets qui n'ont à être appelés qu'une seule fois (lors de leur création)."""

    def execute(self,parametre): #La plupart des one_shot sont de cette forme...
        if self.phase == "démarrage" :
            self.action(parametre)
            self.phase = "terminé"

class Dopage(One_shot,On_attack):
    """Effet qui "dope" la prochaine attaque du joueur. Appelé par collision pour permettre de prendre en compte tout type d'attaque ?"""
    def __init__(self,taux_degats):
        self.affiche = False
        self.phase = "démarrage"
        self.taux_degats = taux_degats

    def action(self,attaque):
        if self.phase == "démarrage" :
            attaque.degats *= self.taux_degats

class Debut_blizzard(One_shot,On_post_action):
    """Effet qui crée un blizzard (rajoute l'effet blizzard sur les cases désignées)."""
    def __init__(self,portee,gain_latence,duree):
        self.affiche = False
        self.phase = "démarrage"
        self.portee = portee
        self.gain_latence = gain_latence
        self.duree = duree

    def action(self,agissant):
        cases = get_cases_voisines(agissant,portee) #On laisse le boulot compliqué au controleur
        for case in cases :
            case.effets.append(Blizzard(self.gain_latence,self.duree))

class Debut_obscurite(One_shot,On_post_action):
    """Effet qui crée un blizzard (rajoute l'effet blizzard sur les cases désignées)."""
    def __init__(self,portee,gain_opacite,duree):
        self.affiche = False
        self.phase = "démarrage"
        self.portee = portee
        self.gain_opacite = gain_opacite
        self.duree = duree

    def action(self,agissant):
        cases = get_cases_voisines(agissant.position,portee) #On laisse le boulot compliqué au controleur
        for case in cases :
            case.effets.append(Obscurite(self.gain_opacite,self.duree))

    def execute(self,agissant):
        if self.phase == "démarrage" :
            self.action(agissant)
            self.phase = "terminé"

class Instakill(One_shot,On_post_action):
    """L'effet d'instakill. S'il réussit, la victime voit ses PV descendre à 0. Sinon, rien.""" #Comment retirer aussi les PM, si la victime a la persévérance (essence magique) ?
    def __init__(self,superiorite):
        self.affiche = False
        self.phase = "démarrage"
        self.superiorite = superiorite

    def action(self,victime,coupable):
        if victime.priorite + superiorite < coupable.superiorite :
            victime.subit(victime.pv,coupable.ID)
        else :
            victime.insurge(coupable.ID,0.5)

    def execute(self,victime,coupable):
        if self.phase == "démarrage" :
            self.action(victime,coupable)
            self.phase = "terminé"

class En_sursis(One_shot,On_fin_tour):
    """L'effet de sursis d'un projectile perçant qui a jusqu'à la fin du tour pour tuer l'agissant sur sa case."""
    def __init__(self):
        self.phase = "démarrage"

    def action(self,item):
        if get_voisins(item.get_position(),0) != []:
            if isinstance(item,[Fragile,Evanescent]):
                item.etat = "brisé"
            else :
                item.arret()
        
class Attaque(One_shot):
    """L'effet d'attaque dans sa version générale. Pour chaque agissant dans la zone, crée une attaque (version particulière). Attachée au responsable."""
    def __init__(self,responsable=0,degats=0,element=TERRE,portee=1,propagation="C__S___",direction=None,autre=None,taux_autre=None):
        self.affiche = False
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = degats
        self.element = element
        self.portee = portee
        self.propagation = propagation
        self.direction = direction
        self.autre = autre
        self.taux_autre = taux_autre

    def action(self,controleur):
        position = controleur.get_entitee(self.responsable).get_position()
        victimes = controleur.get_touches(self.responsable,position,self.portee,self.propagation,self.direction)
        for victime in victimes :
            if self.autre == None :
                victime.effets.append(Attaque_particulier(self.responsable,self.degats,self.element,self.direction))
            elif self.autre == "piercing":
                victime.effets.append(Attaque_percante(self.responsable,self.degats,self.element,self.direction,taux_perce))

class Attaque_particulier(One_shot):
    """L'effet d'attaque dans sa version particulière. Créée par une attaque (version générale), chargé d'infligé les dégats, en passant d'abord les défenses de la case puis celles de l'agissant. Attachée à la victime."""
    def __init__(self,responsable,degats,element,direction = None):
        self.affiche = True
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = degats
        self.element = element
        self.direction = direction

    def action(self,victime):
        self.degats *= victime.get_aff(self.element) #Peut-être déplacer ça dans la fonction "subit"
        victime.subit(self.degats,self.responsable)

    def get_skin(self):
        return SKIN_BLESSURE

class Attaque_percante(Attaque_particulier): #Attention ! Perçant pour une attaque signifie qu'elle traverse les defenses. C'est totalement différend pour un item !
    """L'effet d'attaque dans sa version particulière. Créée par une attaque (version générale), chargé d'infligé les dégats, en passant d'abord les défenses de la case puis celles de l'agissant. Attachée à la victime. En prime, une partie de ses dégats ne sont pas bloquables."""
    def __init__(self,responsable,degats,element,direction = None,taux_perce = 0):
        self.affiche = True
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = degats * taux_perce
        self.degats_imbloquables = degats - self.degats #Ces dégats ne seront pas affectés par les bloquages.
        self.element = element
        self.direction = direction

    def action(self,victime):
        self.degats += self.degats_imbloquables
        self.degats *= victime.get_aff(self.element)
        victime.subit(self.degats,self.responsable)

    def get_skin(self):
        return SKIN_BLESSURE
    
class On_hit(Effet):
    """La classe des effets qui se déclenchent quand un projectile heurte un agissant ou un mur."""
    def __init__(self,portee,degats,element = TERRE):
        self.affiche = False
        self.portee = portee
        self.degats = degats
        self.element = element

    def action(self,lanceur,position,controleur):
        victimes = controleur.get_touches(lanceur,position,self.portee)
        for victime in victimes :
            victime.effets.append(Attaque_particulier(self.responsable,self.degats,self.element))

    def execute(self,lanceur = None,position = None):
        self.action(lanceur,position,controleur)

class On_step_in(Effet):
    """La classe des effets déclenchés lorsqu'on marche sur une case."""
    pass

class On_step_out(Effet):
    """La classe des effets déclenchés quand on quitte une case."""
    pass

class On_through(Effet):
    """La classe des effets déclenchés quand on traverse un mur."""
    pass

class Teleport(On_through):
    """L'effet de téléportation, qui modifie la position de l'agissant (il peut aussi s'agir d'un déplacement normal)."""
    def __init__(self,position,surnaturel = False):
        self.affiche = surnaturel
        self.position = position

    def action(self,entitee):
        if entitee.get_position()[0]!=self.position[0]: #On change de labyrinthe !
            entitee.controleur.move(self.position,entitee)
        else:
            entitee.set_position(self.position)

    def execute(self,entitee):
        self.action(entitee)

    def get_skin(self):
        return SKIN_PORTAIL

class On_try_through(Effet):
    """La classe des effets déclenchés quand on essaye de traverser un mur."""
    
class Mur_plein(On_try_through):
    """L'effet qui correspond à la présence d'un mur plein sur le passage de l'entitee."""
    def __init__(self,durete):
        self.affiche = True
        self.durete = durete #La priorite qu'il faut avoir pour briser ce mur.
        self.casse = False

    def action(self,mur,entitee):
        if not(isinstance(entitee,Fantome)): #Deux moyens de traverser un mur plein : être un fantome ;
            ecrasement = trouve_skill(entitee.classe_principale,Skill_ecrasement)   # ou l'écraser.
            if ecrasement != None :
                passage = ecrasement.utilise(self.durete,entitee.get_priorite())
                if passage :
                    self.casse = True
                    mur_oppose = mur.get_mur_oppose()
                    if mur_oppose != None:
                        for effet in mur_oppose.effets :
                            if isinstance(effet,Mur_plein):
                                effet.casse = True
                else :
                    mur.peut_passer = False
            else :
                mur.peut_passer = False

    def execute(self,mur,entitee):
        if not(self.casse) :
            self.action(mur,entitee)

    def get_skin(self):
        return SKIN_MUR

class Mur_impassable(On_try_through):
    """L'effet qui correspond à un mur absolument infranchissable."""
    def __init__(self):
        self.affiche = True

    def action(self,mur,entitee):
        mur.peut_passer = False

    def execute(self,mur,entitee):
        self.action(mur,entitee)

    def get_skin(self):
        return SKIN_MUR

class Porte(On_try_through):
    """L'effet qui correspond à la présence d'une porte sur le passage de l'entitée (une porte et un mur plein peuvent se cumuler, mais ce n'est pas conseillé)."""
    def __init__(self,durete,code,automatique = False):
        self.affiche = True
        self.durete = durete #La priorite qu'il faut avoir pour briser ce mur.
        self.code = code #Le code qui permet d'ouvrir la porte
        self.casse = False
        self.ferme = True
        self.auto = automatique

    def action(self,mur,entitee):
        if not(isinstance(entitee,Fantome)):          #Trois moyens de traverser une porte : être un fantome ;
            if not(isinstance(entitee,Agissant)) or not(self.code in entitee.get_clees()): # avoir la clée ;
                ecrasement = trouve_skill(entitee.classe_principale,Skill_ecrasement)      # ou tout détruire !
                if ecrasement != None :
                    passage = ecrasement.utilise(self.durete,entitee.get_priorite())
                    if passage :
                        self.casse = True
                        self.affiche = False
                        self.ferme = False #Si on détruit la porte, elle n'est plus fermée...
                        mur_oppose = mur.get_mur_oppose()
                        if mur_oppose != None:
                            for effet in mur_oppose.effets :
                                if isinstance(effet,Porte):
                                    effet.casse = True
                                    effet.affiche = False
                                    effet.ferme = False #On voudrait aussi ouvrir l'autre côté de la porte.
                    else :
                        mur.peut_passer = False
                else :
                    mur.peut_passer = False
            elif not(self.auto): #Si on a la clé et la porte n'est pas automatique, elle reste ouverte !
                self.ferme = False
                mur_oppose = mur.get_mur_oppose()
                if mur_oppose != None:
                    for effet in mur_oppose.effets :
                        if isinstance(effet,Porte):
                            effet.ferme = False #On voudrait aussi ouvrir l'autre côté de la porte.

    def execute(self,mur,entitee):
        if not(self.casse) and self.ferme :
            self.action(mur,entitee)

    def get_skin(self):
        if self.ferme:
            return SKIN_PORTE
        else:
            return SKIN_PORTE_OUVERTE

class Barriere(On_try_through):
    """L'effet qui correspond à la présence d'une barrière magique, qui bloque certaines entitées selon certains critères."""

    def execute(self,mur,entitee):
        self.action(mur,entitee)

    def get_skin(self):
        return SKIN_BARRIERE

class Barriere_classe(Barriere):
    """L'effet qui correspond à la présence d'une barrière qui bloque selon des conditions de classe."""
    def __init__(self,classe):
        self.affiche = True
        self.classe = classe

    def action(self,mur,entitee): #Pour interdire certains coins aux fantômes
        if isinstance(entitee,self.classe):
            mur.peut_passer = False

class Barriere_espece(Barriere):
    """L'effet qui correspond à la présence d'une barrière qui bloque selon des conditions d'espèce."""
    def __init__(self,espece):
        self.affiche = True
        self.espece = espece

    def action(self,mur,entitee):
        if isinstance(entitee,Agissant) and self.espece in entitee.get_especes():
            mur.peut_passer = False

class Barriere_tribale(Barriere):
    """L'effet qui correspond à la présence d'un barrière qui bloque selon l'appartenance à un esprit."""
    def __init__(self,esprit):
        self.affiche = True
        self.esprit = esprit

    def action(self,mur,entitee): #Pour les zones protégées où seul le joueur et son groupe peuvent aller par exemple.
        if isinstance(entitee,Agissant) and entitee.get_esprit() != self.esprit:
            mur.peut_passer = False

class Barriere_altitude(Barriere):
    """L'effet qui correspond à la présence d'un barrière qui bloque selon l'altitude de l'item."""
    def __init__(self,altitude):
        self.affiche = True
        self.altitude = altitude

    def action(self,mur,entitee): #Pour les zones protégées où seul le joueur et son groupe peuvent aller par exemple.
        if not(isinstance(entitee,Item)) or not(entitee.hauteur >= self.altitude):
            mur.peut_passer = False

class Porte_barriere(Barriere,Porte):
    """Lorsqu'une barrière peut être franchie avec une clée."""
    pass

class Porte_classe(Porte_barriere):
    """L'effet qui correspond à la présence d'une barrière qui bloque selon des conditions de classe, sauf si on a la clé de la porte."""
    def __init__(self,durete,code,classe,automatique = False):
        Porte.__init__(self,durete,code,automatique)
        self.classe = classe

    def action(self,mur,entitee): #Pour interdire certains coins aux fantômes
        if isinstance(entitee,self.classe):
            if not(isinstance(entitee,Agissant)) or not(self.code in entitee.get_clees()):
                mur.peut_passer = False
            elif not(self.auto): #Si on a la clé et la porte n'est pas automatique, elle reste ouverte !
                self.ferme = False

class Porte_espece(Porte_barriere):
    """L'effet qui correspond à la présence d'une barrière qui bloque selon des conditions d'espèce, sauf si on a la clé de la porte."""
    def __init__(self,durete,code,espece,automatique = False):
        Porte.__init__(self,durete,code,automatique)
        self.espece = espece

    def action(self,mur,entitee):
        if isinstance(entitee,Agissant) and self.espece in entitee.get_especes():
            if not(isinstance(entitee,Agissant)) or not(self.code in entitee.get_clees()):
                mur.peut_passer = False
            elif not(self.auto): #Si on a la clé et la porte n'est pas automatique, elle reste ouverte !
                self.ferme = False

class Porte_tribale(Porte_barriere):
    """L'effet qui correspond à la présence d'un barrière qui bloque selon l'appartenance à un esprit, sauf si on a la clé de la porte."""
    def __init__(self,durete,code,esprit,automatique = False):
        Porte.__init__(self,durete,code,automatique)
        self.esprit = esprit

    def action(self,mur,entitee): #Pour les zones protégées où seul le joueur et son groupe peuvent aller par exemple.
        if isinstance(entitee,Agissant) and entitee.get_esprit() != self.esprit:
            if not(isinstance(entitee,Agissant)) or not(self.code in entitee.get_clees()):
                mur.peut_passer = False
            elif not(self.auto): #Si on a la clé et la porte n'est pas automatique, elle reste ouverte !
                self.ferme = False

class Porte_altitude(Porte_barriere):
    """L'effet qui correspond à la présence d'un barrière qui bloque selon l'altitude de l'item."""
    def __init__(self,durete,code,altitude,automatique = False):
        Porte.__init__(self,durete,code,automatique)
        self.altitude = altitude

    def action(self,mur,entitee): #Pour les zones protégées où seul le joueur et son groupe peuvent aller par exemple.
        if not(isinstance(entitee,Item)) or not(entitee.hauteur >= self.altitude):
            if not(isinstance(entitee,Agissant)) or not(self.code in entitee.get_clees()):
                mur.peut_passer = False
            elif not(self.auto): #Si on a la clé et la porte n'est pas automatique, elle reste ouverte !
                self.ferme = False

class Sort :
    """La classe des sorts. Lancer un sort de magie coûte du mana. Les agissants capable d'utiliser de la magie disposent d'un skill qui regroupe toutes les magies.
       !!! Ne pas confondre Sort et Magie ! Le premier est le produit de la deuxième ! Une magie regroupe 10 sorts, soit les dix formes de la magie, du niveau 1 au niveau 10."""
    def __init__(self,gain_xp,cout_mp,latence): #Les caractéristiques partagées par tous les sorts
        self.gain_xp = gain_xp
        self.cout_mp = cout_mp
        self.latence = latence

    #Il n'y a pas de méthode commune à tous les sorts

class Magie_dirigee(Sort) :
    """La classe des magies qui nécessitent une direction."""
    def __init__(self,temps):
        self.temps_dir = temps
        self.direction = None
        self.direction_acquise = False

    def check_direction(self):
        self.direction_acquise = self.direction != None

class Magie_cout(Sort):
    """La classe des magies dont le coût peut varier."""
    def __init__(self,temps):
        self.temps_cout = temps
        self.cout_acquis = False

    def check_cout(self):
        self.cout_acquis = True

class Magie_cible(Sort) :
    """La classe des magies qui nécessitent une (ou plusieurs) cible(s)."""
    def __init__(self,temps):
        self.temps = temps
        self.cible = None
        self.cible_acquise = False

    def check_cibles(self):
        self.cible_acquise = self.cible != None

class Multi_cible(Magie_cible) :
    """La classe des magies qui nécessitent plusieurs cibles."""
    def __init__(self,temps):
        Magie_cible.__init__(self,temps)
        self.cible = []

    def __check_cibles(self):
        self.cible_acquise = self.cible != []

class Portee_limitee(Magie_cible) :
    """La classe des magies qui ciblent quelque chose dans la proximité du joueur avec une portée limitée (sinon elles peuvent viser tout ce qui est dans le champ de vision du joueur)."""
    def __init__(self,portee):
        self.portee = portee

class Cible_agissant(Magie_cible):
    """La classe des magies qui ciblent d'autres agissants."""
    def __init__(self):
        print("Cible_agissant ne doit pas être instanciée.")

class Cible_item(Magie_cible):
    """La classe des magies qui ciblent des items."""
    def __init__(self):
        print("Cible_item ne doit pas être instanciée.")

class Cible_item_inventaire(Magie_cible):
    """La classe des magies qui ciblent des items dans l'inventaire d'un agissant."""
    def __init__(self):
        print("Cible_item_inventaire ne doit pas être instanciée.")

class Cible_case(Magie_cible):
    """La classe des magies qui ciblent une case. (Si si, une case. Pour une explosion par exemple, vous n'avez pas envie d'être au centre ! Vraiment !)"""
    def __init__(self):
        print("Cible_case ne doit pas être instanciée.")

# Normalement on en a fini avec les magies ciblées

class Invocation(Sort):
    """La classe des magies qui créent une entitée (un agissant pour se battre à vos côtés, un projectile magique pour attaque les ennemis, un item à utiliser plus tard..."""
    def __init__(self,gain_xp,cout_mp,latence,entitee):
        Sort.__init__(self,gain_xp,cout_mp,latence)
        self.entitee = entitee

    def invoque(self):
        return self.entitee

class Invocation_projectile(Invocation,Magie_dirigee):
    """La classe des magies qui créent une entitée avec un attribut direction."""
    def __init__(self,gain_xp,cout_mp,latence,temps,entitee):
        Sort.__init__(self,gain_xp,cout_mp,latence)
        Magie_dirigee.__init__(self,temps)
        self.entitee = entitee

    def invoque(self):
        return self.entitee

class Creation_effet(Sort):
    """La classe des magies qui créent un effet (un effet sur le long terme, comme les enchantement, ou sur le court terme, comme un boost ou déboost passager)."""
    def __init__(self,gain_xp,cout_mp,latence,effet):
        Sort.__init__(self,gain_xp,cout_mp,latence)
        self.effet = effet

    def get_effet(self):
        return self.effet

class Enchante(Creation_effet):
    """La classe des magies qui créent des enchantements (des effets sur le très, très long terme)."""
    def __init__(self,gain_xp,cout_mp,latence,enchantement):
        Sort.__init__(self,gain_xp,cout_mp,latence)
        self.enchantement = enchantement

    def get_enchantement(self):
        return self.enchantement

class Enchante_item(Enchante,Cible_item):
    """La classe des magies qui enchantent un item."""
    def __init__(self,gain_xp,cout_mp,latence,temps,enchantement):
        Enchante.__init__(self,gain_xp,cout_mp,latence,enchantement)
        Magie_cible.__init__(self,temps)

class Enchante_cases(Enchante,Cible_case,Multi_cible):
    """La classe des magies qui enchantent des cases."""
    def __init__(self,gain_xp,cout_mp,latence,temps,enchantement):
        Enchante.__init__(self,gain_xp,cout_mp,latence,enchantement)
        Magie_cible.__init__(self,temps)

class Enchante_agissant(Enchante,Cible_agissant):
    """La classe des magies qui enchantent un agissant."""
    def __init__(self,gain_xp,cout_mp,latence,temps,enchantement):
        Enchante.__init__(self,gain_xp,cout_mp,latence,enchantement)
        Magie_cible.__init__(self,temps)

class Attaque_magique(Sort):
    """La classe des magies d'attaque (pas les projectiles, ni les effets qui infligent des dégats, ni les instakills, juste les dégats directs, représentés par un objet Attaque)."""
    def __init__(self,gain_xp,cout_mp,latence,attaque):
        Sort.__init__(self,gain_xp,cout_mp,latence)
        self.attaque = attaque

    def get_attaque(self):
        return self.attaque

class Attaque_magique_dirigee(Magie_dirigee):
    def __init__(self,gain_xp,cout_mp,latence,temps,attaque):
        Attaque_magique.__init__(self,gain_xp,cout_mp,latence,attaque)
        Magie_dirigee.__init__(self,temps)

# Maintenant on va créer les véritables sorts. On commence par les soins :

class Sort_de_soin(Cible_agissant):
    def __init__(self,gain_xp,cout_pm,latence,gain_pv,temps):
        Sort.__init__(self,gain_xp,cout_pm,latence)
        Magie_cible.__init__(self,temps)
        self.gain_pv = gain_pv

    #On laisse le controleur accéder lui-même aux attribus ?

class Soin_de_zone(Cible_case):
    def __init__(self,gain_xp,cout_pm,latence,gain_pv,portee,temps):
        Sort.__init__(self,gain_xp,cout_mp,latence)
        Magie_cible.__init__(self,temps)
        self.gain_pv = gain_pv
        self.portee = portee

class Auto_soin(Sort):
    def __init__(self,gain_xp,cout_pm,latence,gain_pv):
        Sort.__init__(self,gain_xp,cout_mp,latence)
        self.gain_pv = gain_pv

class Resurection(Cible_item,Portee_limitee): #Les cadavres sont considérés comme des items.
    def __init__(self,gain_xp,cout_pm,latence,portee_limite,temps):
        Sort.__init__(self,gain_xp,cout_mp,latence)
        Magie_cible.__init__(self,temps)
        Portee_limitee.__init__(self,portee_limite) #Ces sorts surpuissants ne peuvent pas être balancés n'importe où !

class Reanimation_de_zone(Cible_case,Portee_limitee): #Les cadavres sont considérés comme des items.
    def __init__(self,gain_xp,cout_pm,latence,taux_pv,portee,portee_limite,superiorite,temps): 
        Sort.__init__(self,gain_xp,cout_mp,latence)
        Magie_cible.__init__(self,temps)
        Portee_limitee.__init__(self,portee_limite) #Ces sorts surpuissants ne peuvent pas être balancés n'importe où !
        self.taux_pv = taux_pv
        self.portee = portee
        self.superiorite = superiorite

# C'est tout pour les soins et assimilés.
# On passe aux projectiles :

class Ombre_furtive(Cible_case,Invocation_projectile,Portee_limitee):
    def __init__(self,gain_xp,cout_mp,latence,projectile,portee_limite,temps):
        Magie_ciblee.__init__(self,temps)
        Invocation_projectile.__init__(self,gain_xp,cout_mp,latence,temps,entitee)
        Portee_limitee.__init__(self,portee_limite)

class Economie(Magie_cout,Effet): #Parce que ces deux sorts sont des sorts d'économiste
    def __init__(self,gain_xp,cout_mp,latence,temps,taux,effet):
        Effet.__init__(self,gain_xp,cout_mp,latence,effet)
        Magie_cout.__init__(self,temps)
        self.taux = taux

    def check_cout(self):
        self.effet.execute(self.cout_mp * self.taux)
        self.cout_acquis = True

class Explosion_de_mana(Magie_cout,Attaque_magique):
    def __init__(self,gain_xp,cout_mp,latence,temps,attaque):
        Attaque_magique.__init__(self,gain_xp,cout_mp,latence,attaque)
        Magie_cout.__init__(self,temps)

    def check_cout(self):
        self.attaque.degats *= self.cout_mp
        self.cout_acquis = True

# Les sorts de projectiles qui sont lancés depuis l'emplacement de l'agissant n'ont pas besoin de classe propre (la classe Invocation suffit).
# On les liste quand même pour rappel :
#    - La boule de feu (c'est un projectile explosif (crée une zone de dégats quand il touche un ennemi ou un mur), parmi les magies de feu, quand il cause des dégats, inflige un effet de feu (la cible perd de la vie lentement))
#    - La flèche de glace (c'est un projectile percant (poursuit son trajet si l'agissant meurt), parmi les magies de glace, quand il cause des dégats, inflige un effet de glace (la cible est ralentie))
#    - Le rocher (c'est un projectile simple (tout dans les dégats !), parmi les magies de terre)
# (La magie de projectile d'ombre n'est pas lancée depuis l'emplacement de l'agissant, d'où son absence dans la liste.)
#    - Le projectile magique (c'est un projectile simple)
#    - L'éclair noir (c'est un projectile perçant explosif (quand il touche un agissant ou un mur, il provoque une grande zone de dégats autour de lui, et si l'obstacle était un agissant et est mort suite aux dégats directs ou à l'explosion, l'éclair noir poursuit sa course)
#    - D'autres ?

# Les enchantements qui affectent le joueur n'ont pas besoin de classe propre (la classe Enchantement suffit). De même pour les autres enchantements.
# On les liste quand même pour rappel :
#    - Faiblesse (réduit la force d'un agissant)
#    - Cécité (réduit la portée de la vision d'un agissant) (particulièrement utile contre les éclaireurs d'une meute)
#    - Perte de pv (réduit progressivement les pv d'un agissant)
#    - Perte de pm (réduit progressivement les pm d'un agissant)
#    - Confusion (l'agissant a une certaine chance de ne pas regarder dans la bonne direction lors de ses actions (attaque ou déplacement par exemple)
#    - Poches trouées (l'agissant a une certaine chance de perdre l'un de ses items à chaque tour)
#    - Force (augmente la force d'un agissant)
#    - Vision (augmente la portée de la vision d'un agissant) (particulièrement utile pour un sniper, un observateur, ou un enchanteur)
#    - Célérité (augmente la vitesse d'un agissant)
#    - Vitalité (augmente la régénération des pv d'un agissant)
#    - Absorption (augmente la régénération des pm d'un agissant)
#    - Immunité (protège l'agissant contre les maladies et poisons)
#    - Flamme (augmente l'affinité au feu, parmi les magies de feu)
#    - Neige (augmente l'affinité à la glace, parmi les magies de glace)
#    - Sable (augmente l'affinité à la terre, parmi les magies de terre)
#    - Ténèbre (augmente l'affinité à l'ombre, parmi les magies d'ombre)
#    - Rouille (réduit les statistiques d'une arme)
#    - Renforcement (augmente les statistiques d'une arme)
#    - Bombe (confère des propriétés d'explosif à un item)
#    - D'autres ?

# Les attaques magiques lancées depuis la position du joueur n'ont pas besoin de classe propre (la classe Attaque_magique suffit).
# On les liste quand même pour rappel :
#    - Laser (attaque rectiligne de très grande portée)
#    - Brasier (attaque de zone centrée sur l'agissant, parmi les magies de feu, inflige un effet de feu (la cible perd de la vie lentement))
#    - Avalanche (attaque semi-circulaire de grande portee, parmi les magies de terre)
#    - D'autres ?

# Les effets qui ciblent le joueur ou sont lancés à l'emplacement du joueur n'ont pas besoin de classe propre (la classe Effet suffit).
# On les liste quand même pour rappel :
#    - Dopage (augmente la force du joueur lors de la prochaine attaque)
#    - Réserve (crée une réserve de pm (indépendante des pm de l'agissant, donc potentiellement au delà des pm max) (contenant moins de pm que le sort n'en a coûté, mais permettant de dépenser plus de pm d'un coup par la suite))
#    - Investissement (donne des pm longtemps après le lancement du sort (plus de pm que le coût, si les pm dépassent les pm max l'agissant arrêtera de régénérer ses pm))
#    - Blizzard (crée une zone de ralentissement centrée sur l'agissant, parmi les magies de glace, inflige un effet de glace (la cible est ralentie))
#    - Obscurité (crée une zone où le champ de vision est réduit)
#    - D'autres ?

class Affichage:
    def __init__(self,screen):
        print("Initialisation de l'affichage")
        self.screen = screen
        self.hauteur_ecran = 0
        self.largeur_ecran = 0
        self.hauteur_exploitable = 0
        self.largeur_exploitable = 0
        self.marge_gauche = 0
        self.marge_haut = 0
        self.largeur_rectangles = 0
        self.position_debut_x_rectangle_1 = 0
        self.position_fin_x_rectangle_1 = 0
        self.position_debut_x_carre = 0
        self.position_fin_x_carre = 0
        self.position_debut_x_rectangle_2 = 0
        self.position_fin_x_rectangle_2 = 0
        self.position_debut_y_titre = 0
        self.position_debut_y_rectangles_et_carre = 0
        self.position_fin_y_rectangles_et_carre = 0
        self.messages = [["Affichage initialisé avec succès",20,0]]
        self.recalcule_zones()
        self.dessine_zones()

    def recalcule_zones(self):
        self.hauteur_ecran = self.screen.get_height() #Pour comparaison, l'écran de mon ASUS contient du (1350,690)
        self.largeur_ecran = self.screen.get_width()
        while self.hauteur_ecran < 690 or self.largeur_ecran < 1350:
            print("Ecran trop petit, veuilez redimensionner.")
            res = True
            while res:
                for event in pygame.event.get():
                    if event.type == pygame.VIDEORESIZE:
                        res = False
                        e = event
            self.hauteur_ecran = e.h
            self.largeur_ecran = e.w
        pygame.display.set_mode((self.largeur_ecran,self.hauteur_ecran),pygame.RESIZABLE)
        self.hauteur_exploitable = ((self.hauteur_ecran - 30)//20)*20
        self.largeur_exploitable = ((self.largeur_ecran - 30)//20)*20

        if self.hauteur_exploitable * 2 > self.largeur_exploitable :
            self.hauteur_exploitable = self.largeur_exploitable / 2
        elif self.hauteur_exploitable * 2 < self.largeur_exploitable :
            self.largeur_exploitable = self.hauteur_exploitable * 2
        else :
            print("Dimensions parfaites !")
        self.marge_gauche = ((self.largeur_ecran - self.largeur_exploitable) // 2) - 10
        self.marge_haut = ((self.hauteur_ecran - self.hauteur_exploitable) // 2) + -10
        self.largeur_rectangles = (self.largeur_exploitable) / 4

        self.position_debut_x_rectangle_1 = self.marge_gauche
        self.position_fin_x_rectangle_1 = self.position_debut_x_rectangle_1 + self.largeur_rectangles
        self.position_debut_x_carre = self.position_fin_x_rectangle_1 + 10
        self.position_fin_x_carre = self.position_debut_x_carre + self.hauteur_exploitable
        self.position_debut_x_rectangle_2 = self.position_fin_x_carre + 10
        self.position_fin_x_rectangle_2 = self.position_debut_x_rectangle_2 + self.largeur_rectangles

        self.position_debut_y_titre = self.marge_haut
        self.position_debut_y_rectangles_et_carre = self.marge_haut + 20
        self.position_fin_y_rectangles_et_carre = self.position_debut_y_rectangles_et_carre + self.hauteur_exploitable

    def dessine_zones(self):
        police=pygame.font.SysFont(None, 20)
        titre=police.render("Ceci est un test !",True,(255,255,255))
        self.screen.blit(titre,(self.position_debut_x_rectangle_1,self.position_debut_y_titre))
        pygame.draw.rect(self.screen,(255,255,255),(self.position_debut_x_rectangle_1,self.position_debut_y_rectangles_et_carre,self.largeur_rectangles,self.hauteur_exploitable))
        pygame.draw.rect(self.screen,(255,255,255),(self.position_debut_x_carre,self.position_debut_y_rectangles_et_carre,self.hauteur_exploitable,self.hauteur_exploitable))
        pygame.draw.rect(self.screen,(255,255,255),(self.position_debut_x_rectangle_2,self.position_debut_y_rectangles_et_carre,self.largeur_rectangles,self.hauteur_exploitable))

    def dessine(self,joueur):
        self.dessine_zones()

        self.dessine_lab(joueur)
        self.dessine_droite(joueur)

    def dessine_gauche(self,pv,pm,inventaire,joueur): #La fonction qui dessine le rectangle de gauche. Elle affiche principalement les informations du joueur, comme les pv, les pm, l'inventaire, etc.
        pass

    def dessine_droite(self,joueur): #La fonction qui dessine le rectangle de droite. Elle affiche le joueur, son interlocuteur ou son ennemi, sur fond de labyrinthe. Elle fait appel a des graphiques presque déjà complets (une couche pour le labyrinthe, une autre pour l'agissant, une troisième pour les équippements de l'agissant, une quatrième pour une expression du visage.

        marge_haut = self.position_debut_y_rectangles_et_carre + 2

        skill = trouve_skill(joueur.classe_principale,Skill_observation)

        observation = 0

        for message in self.messages:
            if skill != None:
                observation = skill.utilise() #On le réactive à chaque fois qu'on observe quelque chose !
            message[1]-=1
            if message[2]<=observation:
                police=pygame.font.SysFont(None, 20)
                texte = police.render(message[0],True,(0,0,0))
                self.screen.blit(texte,(self.position_debut_x_rectangle_2+2,marge_haut))
                marge_haut += 20
            if message[1] == 0:
                self.messages.remove(message)
            

    def dessine_lab(self,joueur): #La fonction qui dessine le carré au centre. Elle affiche le labyrinthe vu par le joueur, ses occupants, et tout ce que le joueur est capable de percevoir.
        vue = joueur.vue
        position = joueur.get_position()
        visible_x = [len(vue)-1,0]
        visible_y = [len(vue[0])-1,0]
        for i in range(len(vue)):
            for j in range(len(vue[0])):
                if vue[i][j][1] > 0:
                    if i < visible_x[0]:
                        visible_x[0] = i
                    if i > visible_x[1]:
                        visible_x[1] = i
                    if j < visible_y[0]:
                        visible_y[0] = j
                    if j > visible_y[1]:
                        visible_y[1] = j
        distance = max(position[1]-visible_x[0],visible_x[1]-position[1],position[2]-visible_y[0],visible_y[1]-position[2]) #On cherche à déterminer le carré qui comprend toutes les cases utiles de la vue
        vue_x = position[1] - distance
        vue_y = position[2] - distance
        nb_cases = distance*2 + 1
        taille_case = self.hauteur_exploitable // nb_cases
        hauteur_exploitee = taille_case * nb_cases
        marge = (self.hauteur_exploitable - hauteur_exploitee) // 2
        marge_haut = marge + self.position_debut_y_rectangles_et_carre
        for j in range(nb_cases):
            marge_gauche = marge + self.position_debut_x_carre
            for i in range(nb_cases):
                if 0 <= vue_x + i < len(vue) and 0 <= vue_y + j < len(vue):
                    self.affiche(joueur,vue[vue_x + i][vue_y + j],(marge_gauche,marge_haut),taille_case)
                else:
                    SKIN_BROUILLARD.dessine_toi(self.screen,(marge_gauche,marge_haut),taille_case)
                marge_gauche += taille_case
            marge_haut += taille_case
    
    def print_tailles(self):
        print("hauteur ecran : ",self.hauteur_ecran)
        print("largeur ecran : " , self.largeur_ecran)
        print("hauteur exploitable : " , self.hauteur_exploitable)
        print("largeur exploitable : " , self.largeur_exploitable)
        print("marge gauche : " , self.marge_gauche)
        print("marge haut : " , self.marge_haut)
        print("largeur rectangles : " , self.largeur_rectangles)
        print("position debut x rectangle 1 : " , self.position_debut_x_rectangle_1)
        print("position fin x rectangle 1 : " , self.position_fin_x_rectangle_1)
        print("position debut x carre : " , self.position_debut_x_carre)
        print("position fin x carre : " , self.position_fin_x_carre)
        print("position debut x rectangle 2 : " , self.position_debut_x_rectangle_2)
        print("position fin x rectangle 2 : " , self.position_fin_x_rectangle_2)
        print("position debut y titre : " , self.position_debut_y_titre)
        print("position debut y rectangles et carre : " , self.position_debut_y_rectangles_et_carre)
        print("position fin y rectangles et carre : " , self.position_fin_y_rectangles_et_carre)
    
    def message(self,texte="Ceci est le message par défaut. Avez-vous oublié de préciser ce que vous vouliez dire ?",temps = 20,secret=0):
        self.messages.append([texte,temps,secret])


    def affiche(self,joueur,vue,position,taille):
        self.affichables=[]
        if vue[1]==0:
            SKIN_BROUILLARD.dessine_toi(self.screen,position,taille)
        else:
            if vue[5]==0: #On teste le code de la case pour déterminer son image
                SKIN_CASE.dessine_toi(self.screen,position,taille) #La case en premier, donc en bas
            for i in range(4):
                case = joueur.controleur.get_case(vue[0])
                mur = case.get_mur_dir(i)
                for effet in mur.effets:
                    if effet.affiche:
                        effet.get_skin().dessine_toi(self.screen,position,taille,i)
            entitees = vue[7]
            agissant = None
            for ID_entitee in entitees : #Puis les items au sol
                entitee = joueur.controleur.get_entitee(ID_entitee)
                if issubclass(entitee.get_classe(),Item):
                    entitee.get_skin().dessine_toi(self.screen,position,taille,entitee.get_direction()) #La direction est surtout utile pour les projectiles, sinon ils devraient tous être dans le même sens.
                else:
                    agissant = entitee
            if agissant != None: #Enfin l'agissant (s'il y en a un)
                direction = agissant.get_direction()
                arme = agissant.inventaire.arme
                if arme != None:
                    arme.get_skin().dessine_toi(self.screen,position,taille,direction)
                agissant.get_skin().dessine_toi(self.screen,position,taille,direction)
                armure = agissant.inventaire.armure
                if armure != None:
                    armure.get_skin().dessine_toi(self.screen,position,taille,direction)
                bouclier = agissant.inventaire.bouclier
                if bouclier != None:
                    bouclier.get_skin().dessine_toi(self.screen,position,taille,direction)
                haume = agissant.inventaire.haume
                if haume != None:
                    haume.get_skin().dessine_toi(self.screen,position,taille,direction)
                for effet in agissant.effets:
                    if effet.affiche:
                        effet.get_skin().dessine_toi(self.screen,position,taille,direction)
            #Rajouter des conditions d'observation
