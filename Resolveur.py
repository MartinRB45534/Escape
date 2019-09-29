import Cases
import random

#constantes
HAUT=0
DROITE=1
BAS=2
GAUCHE=3

MUR_VIDE=0
MUR_PLEIN=1

class Resolveur:
    def __init__(self,matrice_cases,largeur,hauteur,arrivee_x,arrivee_y,modeResolution="Profondeur"):
        self.largeur = largeur
        self.hauteur = hauteur
        self.arrivee_x = arrivee_x
        self.arrivee_y = arrivee_y
        self.matrice_cases = matrice_cases
        self.modeResolution = modeResolution
        self.cases_visitees=[[False for i in range(hauteur)]for i in range(largeur)]
    def resolution(self):
        """
        Fonction qui résoud la matrice
        Entrée:Rien
        Sorties: un booléen indiquant si la matrice est résolvable
        """
        if self.modeResolution=="Profondeur":
            return self.resolution_en_profondeur()
        else:
            print("mode de résolution choisi incompatible")
    def resolution_en_profondeur(self):
        """
        Fonction qui résoud la matrice avec la méthode du parcours en profondeur
        Entrées:Rien
        Sorties:un booléen indiquant si la matrice est résolvable
        """
        rdm=random.randrange (1,10**18,1)

        #on définit la seed de notre solutionneur
        #cela permet d'avoir le meme résultat

        print("seed",rdm)
        #random.seed(498965033146031877)
        random.seed(rdm)
        depart_x=0
        depart_y=0

        #position dans la matrice
        position_x=depart_x
        position_y=depart_y
        #le stack est une liste de positions
        stack=[[depart_x,depart_y]]

        self.cases_visitees[depart_x][depart_y]=True
        
        #schéma boucle
        #récupérer les positions utilisables
                #si on as des positions utilisables

                #trouver la nouvelle position
                #aller à la nouvelle position
                #marquer la position

                #sinon revenir en arrière

        solution=False
        
        while len(stack)!=0 and (position_x!=self.arrivee_x or position_y!=self.arrivee_y):
            #on récupère les coords de la ou l'on es cad la dernière case dans le stack
            position_x=stack[len(stack)-1][0]
            position_y=stack[len(stack)-1][1]
            #print(position_x,position_y)
            #on récupère les positions utilisables
            self.matrice_cases[position_x][position_y].set_Couleur((0,0,255))
            
            voisins,positions_voisins = self.voisins_case(position_x,position_y)
            
            directions_explorables = self.directions_utilisables(voisins,positions_voisins,position_x,position_y)

            if len(directions_explorables)>0:
                
                #randrange est exclusif
                num_direction=random.randrange(0,len(directions_explorables))
                
                #direction ou l'on va
                direction=directions_explorables[num_direction]

                new_x,new_y = self.nouvelles_coords(position_x,position_y,direction)

                self.cases_visitees[new_x][new_y]=True
                
                #on ajoute les nouvelles coordonnées de la case au stack
                stack.append([new_x,new_y])
            else:
                self.matrice_cases[position_x][position_y].set_Couleur((255,0,0))
                #on revient encore en arrière
                stack.pop()
                #print(position_x,position_y,len(stack))

        if position_x==self.arrivee_x and position_y == self.arrivee_y:
            solution=True

        return solution
        
    def nouvelles_coords(self,x,y,direction):
        """
        Fonction qui calcul les nouvelles coordonnées du résolveur
        Entrées:
            les coordonnées du résolveur
            la direction ou le résolveur va
        Sorties:
            les nouvelles coordonnées résolveur
        """
        if direction == HAUT:
            y-=1
        elif direction == DROITE:
            x+=1
        elif direction == BAS:
            y+=1
        elif direction == GAUCHE:
            x-=1
        return x,y
    def directions_utilisables(self,voisins,positions_voisins,position_x,position_y):
        """
        Fonction qui prend en entrées:
            les voisins de la case
            les positions des voisins
            la position de la case
        et qui renvoie les directions ou l'on peut passer
        """
        directions_utilisables=[]

        for i in range(0,len(voisins)):
            if voisins[i]!=None:
                voisin_x=positions_voisins[i][0]
                voisin_y=positions_voisins[i][1]

                #on vérifie si la case n'as pas été explorée et si l'on peut passer
                if not(self.cases_visitees[voisin_x][voisin_y]) and not(self.matrice_cases[position_x][position_y].mur_plein(i)):
                    directions_utilisables.append(i)
        return directions_utilisables

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
    def voisins_case(self,x,y):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
        et qui renvoie les voisins de la case
        ainsi que leurs coordonnées
        """
        voisins=[]
        positions_voisins=[]
        #on élimine les voisins aux extrémitées
        if y-1>=0:
            voisins.append(self.matrice_cases[x][y-1])
            positions_voisins.append([x,y-1])
        else:
            voisins.append(None)
            positions_voisins.append(None)
            
        if x+1<self.largeur:
            voisins.append(self.matrice_cases[x+1][y])
            positions_voisins.append([x+1,y])
        else:
            voisins.append(None)
            positions_voisins.append(None)
            
        if y+1<self.hauteur:
            voisins.append(self.matrice_cases[x][y+1])
            positions_voisins.append([x,y+1])
        else:
            voisins.append(None)
            positions_voisins.append(None)
            
        if x-1>=0:
            voisins.append(self.matrice_cases[x-1][y])
            positions_voisins.append([x-1,y])
        else:
            voisins.append(None)
            positions_voisins.append(None)
            
        return voisins,positions_voisins
