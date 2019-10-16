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
            if entitees!=None:
                for entitee in entitees:
                    x=entitee.getPosition()[0]
                    y=entitee.getPosition()[1]
                    if (x>=min_x and x<=max_x) and (y>=min_y and y<=max_y):
                        entitee.dessine_toi(screen,[largeur//2+x-joueur_x,hauteur//2+y-joueur_y],LARGEUR_CASE,LARGEUR_MUR,position_screen)

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
            if entitees!=None:
                for entitee in entitees:
                    x=entitee.getPosition()[0]
                    y=entitee.getPosition()[1]
                    if (x>=min_x and x<=max_x) and (y>=min_y and y<=max_y):
                        entitee.dessine_toi(screen,[largeur//2+x-joueur_x,hauteur//2+y-joueur_y],LARGEUR_CASE,LARGEUR_MUR,position_screen)
                    
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
