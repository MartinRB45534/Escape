import Generateur
from Cases import *
from Constantes import *
from Resolveur import *


class Labyrinthe:
    def __init__(self,largeur,hauteur,arrivee_x,arrivee_y,tailleCase=20,tailleMur=1):
        self.largeur = largeur
        self.hauteur = hauteur

        self.arrivee_x=arrivee_x
        self.arrivee_y=arrivee_y
        
        self.matrice_cases = [[Case(tailleCase,tailleMur) for i in range(hauteur)]for i in range(largeur)]

        #paramètre graphiques
        self.tailleCase = tailleCase
        self.tailleMur = tailleMur

    def generation(self):
        """
        Fonction qui génère la mztrice du labyrinthe
            Entrées:
                rien
            Sorties:
                rien
        """
        #ini du tableau de case (4 murs pleins)
        #génération en profondeur via l'objet generateur
        gene=Generateur.Generateur(self.matrice_cases,self.largeur,self.hauteur)
        self.matrice_cases=gene.generation()
        #on change la couleur de la case d'arrivée
        self.matrice_cases[self.arrivee_x][self.arrivee_y].set_Couleur((30,144,255))
    def peut_passer(self,coord,sens):
        """
        Fonction qui valide et applique ou non le mouvement du joueur
        Entrées:
            -coordonnnées  actuelles du joueur
            -direction vers laquelle le joueur veut se diriger
        Sorties:
            -un booléen qui indique si le joueur est passé ou pas
            -les nouvelles coordonnées du joueur
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
    
    def dessine_toi(self,screen,position_joueur,position_screen,largeur,hauteur):

        """
        Fonction qui dessine le labyrinthe sur l'écran
        Entrées:
            l'écran, la surface sur laquelle on dessine(objet pygame)
            la position du joueur
            la position que l'on prend pour 0,0 sur l'écran (ex: un décalage de 20px sur la droite se traduit par (x+20,y))
            la largeur en cases
            la hauteur en cases
        Sorties:
            Rien
        """

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

                if (x<0 or x>=self.largeur) or (y<0 or y>=self.hauteur):
                    pygame.draw.rect(screen,(0,0,0),(position_x,position_y,self.tailleCase+self.tailleMur,self.tailleCase+self.tailleMur))
                else:
                    self.matrice_cases[x][y].dessine_toi(screen,position_x,position_y)
                position_y+=self.tailleCase+self.tailleMur
            position_y=position_screen[1]
            position_x+=self.tailleCase+self.tailleMur
            
    def resolution(self,arrivee_x,arrivee_y):
        """
        Fonction qui résoud le labyrinthe
        Entrées:
            coordonnées de l'arrivée
        Sorties:
            Rien
        """
        resol = Resolveur(self.matrice_cases,self.largeur,self.hauteur,arrivee_x,arrivee_y)
        solution=resol.resolution()
        
#lab = Labyrinthe(5,5)
#lab.dessine_toi(0,0,0)
