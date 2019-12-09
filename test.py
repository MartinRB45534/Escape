class Niveau:
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

            #si on détecte un mouvement on redessine l'écran
            #if move_j or move_m:
            self.redraw()
            self.traitement_evenements()
            self.check_missions()

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
        self.fin_niveau()
        return res,self.lab.as_gagner(self.joueur.getPosition()),self.joueur

    def fin_niveau(self):
        """
        Fonction qui gère la fin du niveau
        """
        #on met fin a tout les événements
        for evenement in self.evenements:
            evenement.temps_restant=0
            evenement.action()
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
        Fonction qui exécute la partie du code ou le jpueur demande à agir
        et qui renvoie rien
        """
                    


        #on récupère toutes les touches préssés sous forme de booléen
        keys=pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.affichage.affiche = MINIMAP
            self.joueur.vitesse = self.joueur.vitesse_autres
        elif keys[pygame.K_i]:
            self.affichage.affiche = INVENTAIRE
            self.joueur.vitesse = self.joueur.vitesse_autres
        elif keys[pygame.K_RETURN] and (self.affichage.affiche == INVENTAIRE or self.affichage.affiche == MINIMAP):
            self.affichage.affiche = LABYRINTHE
            self.joueur.vitesse = self.joueur.vitesse_lab

        if self.affichage.affiche == INVENTAIRE:
            if keys[pygame.K_RIGHT]:
                self.joueur.inventaire_vers_la_droite()
            elif keys[pygame.K_LEFT]:
                self.joueur.inventaire_vers_la_gauche()
            elif keys[pygame.K_SPACE]:
                self.joueur.utilise_inventaire()
            elif keys[pygame.K_EQUALS]:
                self.affichage.affiche = ITEM

        if self.affichage.affiche == ITEM:
            if keys[pygame.K_MINUS]:
                self.affichage.affiche = INVENTAIRE

        elif self.affichage.affiche == MINIMAP:
            if keys[pygame.K_UP]:
                self.joueur.minimap.va_vers_le_haut()
            elif keys[pygame.K_DOWN]:
                self.joueur.minimap.va_vers_le_bas()
            elif keys[pygame.K_RIGHT]:
                self.joueur.minimap.va_vers_la_droite()
            elif keys[pygame.K_LEFT]:
                self.joueur.minimap.va_vers_la_gauche()
            elif keys[pygame.K_EQUALS]:
                self.joueur.minimap.rezoom()
            elif keys[pygame.K_MINUS]:
                self.joueur.minimap.dezoom()

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
            elif keys[pygame.K_x]:
                self.joueur.tentative_interaction()

        elif self.affichage.affiche == DIALOGUE:
            self.joueur.vitesse = self.joueur.vitesse_autres
            if keys[pygame.K_RETURN]:
                self.affichage.pass_replique()
                self.joueur.vitesse = self.joueur.vitesse_lab


    def actions_entitees(self):
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
                    self.action_joueur()

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
                    passe,newcoord,tel=self.lab.peut_passer(agissant.getPosition(),direction_voulue,agissant.inventaire)
                else:
                    passe,newcoord,tel=self.lab.peut_passer(agissant.getPosition(),direction_voulue)
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
                            if tel != None:
                                if tel[0] == self.niveau:
                                    agissant.setPosition(tel[1])
                                else:
                                    self.greater_teleportation = True
                                    self.destination = tel
                                
        elif id_action==ATTAQUER:
            self.affichage.ajout_animation(agissant.getPosition(),0,3,agissant.getRadius()*(self.LARGEUR_CASE+self.LARGEUR_MUR))
            succes=self.collision.tentative_attaque(agissant,self.entitees)
        elif id_action==INTERAGIR:
            succes = self.collision.tentative_interaction(agissant,self.entitees)
        elif id_action==PARLER:
            succes = self.affichage.add_dialogue(action)
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
                    res.append(monstre((i,j),nb_meute,largeur_vue,hauteur_vue,pv,degats,vitesse,radius,couleur))
                    taille_meute += 1
                    if taille_meute == max_meute :
                        nb_meute += 1
                        taille_meute = 0
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

    def mission_bidon_tuto3(self):
        check = False
        if self.joueur.position == (5,1):
            check = True
        return check
