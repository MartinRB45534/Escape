import Generateur
from Cases import *
from Constantes import *
from Resolveur import *
from Lumiere import *


class Labyrinthe:
    def __init__(self,largeur,hauteur,arrivee_x,arrivee_y,tailleCase=20,tailleMur=1,poids=[1,1,1,1],patterns=None):
        self.largeur = largeur
        self.hauteur = hauteur

        self.arrivee_x=arrivee_x
        self.arrivee_y=arrivee_y
        
        self.matrice_cases = [[Case(tailleCase,tailleMur) for i in range(hauteur)]for j in range(largeur)]

        #paramètre graphiques
        self.tailleCase = tailleCase
        self.tailleMur = tailleMur
        #poids servants à la génération du labyrinthe
        self.poids=poids

        self.patterns=patterns

    def generation(self):
        """
        Fonction qui génère la mzarice du labyrinthe
            Entrées:
                rien
            Sorties:
                rien
        """
        #ini du tableau de case (4 murs pleins)
        #génération en profondeur via l'objet generateur
        gene=Generateur.Generateur(self.matrice_cases,self.largeur,self.hauteur,self.poids,self.patterns)
        self.matrice_cases=gene.generation()
        #on change la couleur de la case d'arrivée
        self.matrice_cases[self.arrivee_x][self.arrivee_y].set_Couleur((30,144,255))

    def peut_passer(self,coord,sens):
        """
        Fonction qui valide et applique ou non le mouvement de l'entitée
        Entrées:
            -coordonnnées  actuelles de l'entitée
            -direction vers laquelle l'entitée veut se diriger
        Sorties:
            -un booléen qui indique si l'entitée est passé ou pas
            -les nouvelles coordonnées de l'entitée
        """
        newcoord = coord
        case = self.matrice_cases[coord[0]][coord[1]]
        passe = True
        if sens == GAUCHE and not case.mur_plein(GAUCHE):
            newcoord = (coord[0]-1,coord[1])
        elif sens == DROITE and not case.mur_plein(DROITE):
            newcoord = (coord[0]+1,coord[1])
        elif sens == BAS and not case.mur_plein(BAS):
            newcoord = (coord[0],coord[1]+1)
        elif sens == HAUT and not case.mur_plein(HAUT):
            newcoord = (coord[0],coord[1]-1)
        else :
            passe = False
        return passe, newcoord

    def as_gagner(self,coords):
        """
        Fonction qui indique si le joueur à gagner ou non
        Entrées:
            les coordonnées du joueur
        Sorties:
            un booléen qui indique si le joueur a gagné ou non
        """

        win=False

        if coords[0]==self.arrivee_x and coords[1]==self.arrivee_y:
            win=True
        
        return win
    
    def dessine_toi(self,screen,position_joueur,entitees,position_screen,largeur,hauteur,mode_affichage,LARGEUR_CASE,LARGEUR_MUR):

        """
        Fonction qui dessine le labyrinthe sur l'écran
        Entrées:
            l'écran, la surface sur laquelle on dessine(objet pygame)
            la position du joueur
            les entitées autres que le joueur a dessiner (ex les monstres)
            la position que l'on prend pour 0,0 sur l'écran (ex: un décalage de 20px sur la droite se traduit par (x+20,y))
            la largeur en cases
            la hauteur en cases
            le mode d'affichage
            la largueur des cases
            la largeur des murs
        Sorties:
            Rien
        """

        if mode_affichage == voir_tout :
            joueur_x = position_joueur[0]
            joueur_y = position_joueur[1]

            position_x=position_screen[0]
            position_y=position_screen[1]

            min_x=joueur_x-largeur//2
            max_x=joueur_x+largeur-largeur//2

            min_y=joueur_y-hauteur//2
            max_y=joueur_y+hauteur-hauteur//2


            for x in range(min_x,max_x):
                for y in range(min_y,max_y):

                    if not((x<0 or x>=self.largeur) or (y<0 or y>=self.hauteur)):
                        self.matrice_cases[x][y].dessine_toi(screen,position_x,position_y)
                    position_y+=self.tailleCase+self.tailleMur
                position_y=position_screen[1]
                position_x+=self.tailleCase+self.tailleMur
                
            self.affichage_entitees(entitees,mat_exploree,position_vue,screen,largeur,hauteur,LARGEUR_CASE,LARGEUR_MUR,position_screen)

        elif mode_affichage == parcours_en_profondeur :
            joueur_x = position_joueur[0]
            joueur_y = position_joueur[1]

            position_x=position_screen[0]
            position_y=position_screen[1]

            min_x=joueur_x-largeur//2
            max_x=joueur_x+largeur-largeur//2

            min_y=joueur_y-hauteur//2
            max_y=joueur_y+hauteur-hauteur//2

            vue, position_vue = self.construire_vue(position_joueur,largeur,hauteur)
            #on ne veut pas que le résolveur trouve de solution on veut juste qu'il explore la matrice
            resolveur = Resolveur(vue,largeur,hauteur,-1,-1,joueur_x-position_vue[0],joueur_y-position_vue[1],"Profondeur")

            mat_exploree=resolveur.resolution(False,False,False,True)
            
            for x in range(min_x,max_x):
                for y in range(min_y,max_y):
                    if not((x<0 or x>=self.largeur) or (y<0 or y>=self.hauteur)):
                        if mat_exploree[x-position_vue[0]][y-position_vue[1]]:
                            self.matrice_cases[x][y].dessine_toi(screen,position_x,position_y)
                    position_y+=self.tailleCase+self.tailleMur
                position_y=position_screen[1]
                position_x+=self.tailleCase+self.tailleMur

            self.affichage_entitees(entitees,mat_exploree,position_vue,screen,largeur,hauteur,LARGEUR_CASE,LARGEUR_MUR,position_screen)
        elif mode_affichage == distance_max :
            joueur_x = position_joueur[0]
            joueur_y = position_joueur[1]

            position_x=position_screen[0]
            position_y=position_screen[1]

            min_x=joueur_x-largeur//2
            max_x=joueur_x+largeur-largeur//2

            min_y=joueur_y-hauteur//2
            max_y=joueur_y+hauteur-hauteur//2

            vue, position_vue = self.construire_vue(position_joueur,largeur,hauteur)
            #on ne veut pas que le résolveur trouve de solution on veut juste qu'il explore la matrice
            resolveur = Resolveur(vue,largeur,hauteur,-1,-1,joueur_x-position_vue[0],joueur_y-position_vue[1])

            mat_exploree=resolveur.resolution_en_largeur_distance_limitée(False,False,False,True,11)
            
            for x in range(min_x,max_x):
                for y in range(min_y,max_y):
                    if not((x<0 or x>=self.largeur) or (y<0 or y>=self.hauteur)):
                        if mat_exploree[x-position_vue[0]][y-position_vue[1]]:
                            self.matrice_cases[x][y].dessine_toi(screen,position_x,position_y)
                    position_y+=self.tailleCase+self.tailleMur
                position_y=position_screen[1]
                position_x+=self.tailleCase+self.tailleMur
        
            self.affichage_entitees(entitees,mat_exploree,position_vue,screen,largeur,hauteur,LARGEUR_CASE,LARGEUR_MUR,position_screen)
        elif mode_affichage == aveugle :
            self.dessine_case(screen,position_joueur,position_screen,largeur,hauteur,position_joueur)

            lumiere_droite = Lumiere(position_joueur,DROITE,self)
            lumiere_gauche = Lumiere(position_joueur,GAUCHE,self)
            lumiere_haut = Lumiere(position_joueur,HAUT,self)
            lumiere_bas = Lumiere(position_joueur,BAS,self)

            lumiere_droite.avance(screen,position_joueur,position_screen,largeur,hauteur)
            lumiere_gauche.avance(screen,position_joueur,position_screen,largeur,hauteur)
            lumiere_haut.avance(screen,position_joueur,position_screen,largeur,hauteur)
            lumiere_bas.avance(screen,position_joueur,position_screen,largeur,hauteur)

    def dessine_case(self,screen,position_joueur,position_screen,largeur,hauteur,position):
        joueur_x = position_joueur[0]
        joueur_y = position_joueur[1]

        position_x  =position_screen[0]
        position_y = position_screen[1]

        x = position[0]
        y = position[1]

        self.matrice_cases[x][y].dessine_toi(screen,(x-joueur_x+largeur//2)*(self.tailleCase+self.tailleMur),(y-joueur_y+hauteur//2)*(self.tailleCase+self.tailleMur))

    def affichage_entitees(self,entitees,mat_exploree,position_vue,screen,largeur,hauteur,LARGEUR_CASE,LARGEUR_MUR,position_screen):
        """
        Fonction qui affiche les entitées
        Entrées:
            les entitées a afficher
            la matrice explorée
            la position de la vue
            l'écran sur lequel on dessine
            la largueur des cases
            la largeur des murs
            la position de l'écran dans la fenetre
        Sorties:
            Rien
        """
        if entitees!=None:
            for entitee in entitees:
                x=entitee.getPosition()[0]-position_vue[0]
                y=entitee.getPosition()[1]-position_vue[1]
                
                if not(x>len(mat_exploree)-1 or x<0 or y>len(mat_exploree[0])-1 or y<0):
                    if mat_exploree[x][y]:
                        entitee.dessine_toi(screen,[x,y],LARGEUR_CASE,LARGEUR_MUR,position_screen)
    def construire_vue(self,position,largeur,hauteur):
        """
        Fonction qui construit la vue disponible à un monstre ou au joueur
        Entrées:
            la position du monstre ou du joueur
            la largeur de la vue
            la hauteur de la vue
        Sortie:
            la vue correspondante
            les coordonnées de la vue dans le labyrinthe
        """

        vue=[]

        min_x=position[0]-largeur//2
        max_x=position[0]+largeur-largeur//2

        min_y=position[1]-hauteur//2
        max_y=position[1]+hauteur-hauteur//2


        for x in range(min_x,max_x):
            colonne=[]
            for y in range(min_y,max_y):
                if (x<0 or x>=self.largeur) or (y<0 or y>=self.hauteur):
                    colonne.append(None)
                else:
                    colonne.append(self.matrice_cases[x][y])
            vue.append(colonne)
        return vue,[min_x,min_y]
    def casser_X_murs(self,proba=None,nbMurs=None):
        """
        Fonction qui doit casser des murs sur la matrice
        on peut déterminer le nombre de murs avec un probabilité (proba*nb murs au total)
        ou selon un nombre défini en entrée
        """
        if proba!=None or nbMurs!=None:
            if proba!=None:
                nb_murs_a_casser=self.nb_murs_total()*proba
            elif nbMurs!=None:
                nb_murs_a_casser=nbMurs
            self.casser_murs(nb_murs_a_casser)
        else:
            print("mauvaise utilisation de la fonction on ne sait que faire")

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

        
    def casser_mur_random_case(self,position_case):
        """
        Fonction qui prend en entrée la position de la case dont on veut casser un mur
        et qui renvoie un booléen indiquant si l'on as pu casser un mur
        """
        casser = False

        murs=self.directions_utilisables(self.voisins_case(position_case[0],position_case[1]))
        if len(murs)!=0:
            mur_casser=random.randrange(0,len(murs))
            self.casser_mur(murs[mur_casser],position_case[0],position_case[1])
            casser = True
        #print(position_case,len(murs),len(self.voisins_case(position_case[0],position_case[1])))
        return casser

    def voisins_case(self,x,y):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
        et qui renvoie les voisins de la case
        """
        voisins=[]
        #on élimine les voisins aux extrémitées
        if y-1>=0:
            voisins.append(self.matrice_cases[x][y-1])
        else:
            voisins.append(None)
        if x+1<self.largeur:
            voisins.append(self.matrice_cases[x+1][y])
        else:
            voisins.append(None)
        if y+1<self.hauteur:
            voisins.append(self.matrice_cases[x][y+1])
        else:
            voisins.append(None)
        if x-1>=0:
            voisins.append(self.matrice_cases[x-1][y])
        else:
            voisins.append(None)
        return voisins
    
    def directions_utilisables(self,voisins):
        """
        Fonction qui prend en entrées:
            les voisins de la case
        et qui renvoie les directions ou les murs sont utilisables
        """
        murs_utilisables=[]

        for direction in range(0,len(voisins)):
            if voisins[direction]!=None:
                direction_inverse=self.direction_opposee(direction)
                if voisins[direction].mur_plein(direction_inverse):
                    murs_utilisables.append(direction)
        return murs_utilisables
    def direction_opposee(self,direction):
        """
        Fonction qui renvoie la direction opposée à celle en entrée
        """
        direction_opposee=0
        
        if direction == HAUT:
            direction_opposee=BAS
        elif direction == DROITE:
            direction_opposee=GAUCHE
        elif direction == BAS:
            direction_opposee=HAUT
        elif direction == GAUCHE:
            direction_opposee=DROITE

        return direction_opposee
    
    def casser_mur(self,direction,position_x,position_y):
        """
        Fonction qui casse un mur spécifique
        Entrées:
            la direction du mur
            la position de la case
        Sorites:Rien
        """
        #on casse les murs de la case et de la case d'en face
        self.matrice_cases[position_x][position_y].casser_mur(direction)
        
        if direction==HAUT:
            self.matrice_cases[position_x][position_y-1].casser_mur(BAS)
        elif direction==DROITE:
            self.matrice_cases[position_x+1][position_y].casser_mur(GAUCHE)
        elif direction==BAS:
            self.matrice_cases[position_x][position_y+1].casser_mur(HAUT)
        elif direction==GAUCHE:
            self.matrice_cases[position_x-1][position_y].casser_mur(DROITE)

    def nb_murs_total(self):
        """
        Fonction qui renvoie le nombres de murs pleins contenus dans le labyrinthe
        """
        murs_pleins=0
        for x in range(0,self.largeur):
            for y in range(0,self.hauteur):
                murs_pleins+=self.matrice_cases[x][y].nb_murs_pleins()

        return murs_pleins

    def resolution(self,arrivee_x,arrivee_y,depart_x=0,depart_y=0,mode="Profondeur"):
        """
        Fonction qui résoud le labyrinthe
        Entrées:
            coordonnées de l'arrivée
        Sorties:
            Rien
        """
        print(mode)
        resol = Resolveur(self.matrice_cases,self.largeur,self.hauteur,arrivee_x,arrivee_y,depart_x,depart_y,mode)
        solution=resol.resolution()

    def getMatrice_cases(self):
        new_mat = [[self.matrice_cases[j][i] for i in range(self.hauteur)]for j in range(self.largeur)]
        return new_mat

#lab = Labyrinthe(5,5)
#lab.dessine_toi(0,0,0)
