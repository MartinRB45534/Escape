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
    def __init__(self,matrice_cases,largeur,hauteur,arrivee_x,arrivee_y,depart_x=0,depart_y=0,modeResolution="Profondeur"):
        self.largeur = largeur
        self.hauteur = hauteur
        self.arrivee_x = arrivee_x
        self.arrivee_y = arrivee_y

        self.depart_x=depart_x
        self.depart_y=depart_y
        
        self.matrice_cases = matrice_cases
        self.modeResolution = modeResolution
        self.cases_visitees=[[False for i in range(hauteur)]for i in range(largeur)]
    def resolution(self,get_chemin=False,afficher_chemin=True,afficher_seed=False,getMatrice=False):
        """
        Fonction qui résoud la matrice
        Entrée:
            Un booléen indiquant si l'on veut le chemin ou pas
            Un booléen indiquant si l'on veut afficher le chemin ou pas
            Un booléen indiquant si l'on veut afficher la seed ou non
            Un booléen indiquant si l'on veut obtenir la matrice indiquant ou est passé le résolveur
        Sorties:
            un booléen indiquant si la matrice est résolvable
            OU
            le chemin par lequel l'algo est arrivé
        """
        if self.modeResolution=="Profondeur":
            return self.resolution_en_profondeur(get_chemin,afficher_chemin,afficher_seed,getMatrice)
        elif self.modeResolution=="Largeur":
            return self.resolution_en_largeur(get_chemin,afficher_chemin)
        else:
            print("mode de résolution choisi incompatible")
    def resolution_en_profondeur(self,get_chemin,afficher_chemin,afficher_seed,getMatrice):
        """
        Fonction qui résoud la matrice avec la méthode du parcours en profondeur
        Entrées:
            Un booléen indiquant si l'on veut le chemin ou pas 
            Un booléen indiquant si l'on veut afficher le chemin ou pas
            Un booléen indiquant si l'on veut afficher la seed ou non
            Un booléen indiquant si l'on veut obtenir la matrice indiquant ou est passé le résolveur
        Sorties:
            un booléen indiquant si la matrice est résolvable
            OU
            le chemin par lequel l'algo est arrivé
        """
        rdm=random.randrange (1,10**18,1)

        #on définit la seed de notre solutionneur
        #cela permet d'avoir le meme résultat
        if afficher_seed:
            print("seed",rdm)
        #random.seed(498965033146031877)
        random.seed(rdm)
        depart_x=self.depart_x
        depart_y=self.depart_y

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

        solution=None
        
        while len(stack)!=0 and (position_x!=self.arrivee_x or position_y!=self.arrivee_y):
            #on récupère les coords de la ou l'on est cad la dernière case dans le stack
            position_x=stack[len(stack)-1][0]
            position_y=stack[len(stack)-1][1]
            #print(position_x,position_y)
            #on récupère les positions utilisables
            if afficher_chemin:
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
                if afficher_chemin:
                    self.matrice_cases[position_x][position_y].set_Couleur((255,0,0))
                #on revient encore en arrière
                stack.pop()
                #print(position_x,position_y,len(stack))

        solution=False
        
        if getMatrice:
            solution=self.cases_visitees
        elif position_x==self.arrivee_x and position_y == self.arrivee_y:
            if get_chemin:
                solution=stack
            else:
                solution=True

        
        return solution

    def resolution_en_largeur(self,get_chemin,afficher_chemin):
        """
        Fonction qui résoud la matrice avec la méthode du parcours en largeur
        Entrées:
            Un booléen indiquant si l'on veut le chemin ou pas 
            Un booléen indiquant si l'on veut afficher le chemin ou pas
            Un booléen indiquant si l'on veut afficher la seed ou non
        Sorties:
            un booléen indiquant si la matrice est résolvable
            OU
            le chemin par lequel l'algo est arrivé
        """
        depart_x=self.depart_x
        depart_y=self.depart_y

        #position dans la matrice
        position_x=depart_x
        position_y=depart_y
        #la queue est une liste de positions
        queue=[[depart_x,depart_y]]
        chemins=[Chemin([],0,depart_x,depart_y)]


        chemin_courant=chemins[0]

        self.cases_visitees[depart_x][depart_y]=True

        #schéma boucle
        #traiter elt
            #enlever position dans queue
            #ajouter les positions explorables à la queue
        #obtenir elt suivant
            #récuperer premier elt queue
        
        while len(queue)!=0 and (position_x!=self.arrivee_x or position_y!=self.arrivee_y):

            #enlever position dans queue
            queue.pop(0)
            chemins.pop(0)
            
            #on affiche le chemin
            if afficher_chemin:
                self.matrice_cases[position_x][position_y].set_Couleur((255,0,0))
            #trouver les positions explorables
            voisins,positions_voisins=self.voisins_case(position_x,position_y)

            directions_explorables = self.directions_utilisables(voisins,positions_voisins,position_x,position_y)

            for direction in directions_explorables:
                queue.append(positions_voisins[direction])
                new_chemin=Chemin(chemin_courant.getChemin(),chemin_courant.getPoids(),positions_voisins[direction][0],positions_voisins[direction][1])
                chemins.append(new_chemin)
                
                #on marque la case comme visitée
                self.cases_visitees[positions_voisins[direction][0]][positions_voisins[direction][1]]=True
            
            chemin_courant=chemins[0]
            #obtenir elt suivant
            position_x=queue[0][0]
            position_y=queue[0][1]

            #print(chemin_courant.getChemin())

                
        if afficher_chemin and len(chemins)>0:
            for i in chemins[0].getChemin():
                self.matrice_cases[i[0]][i[1]].set_Couleur((0,0,255))

        solution=None
        if get_chemin and (position_x==self.arrivee_x and position_y==self.arrivee_y):
            solution=chemins[0].getChemin()
        else:
            solution= (position_x==self.arrivee_x and position_y==self.arrivee_y)

            
        return solution
    def est_dans_chemin(self,position,chemin):
        """
        Fonction qui determine si la position est dans le chemin
        Entrées:
            -position
            -chemin
        Sorites:
            -un booléen indiquant si la position est dans le chemin
        """
        est_dedans=False
        for position_bis in chemin:
            if position_bis==position:
                est_dedans=True

        return est_dedans
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
            le chemin deja explorée
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

    def resolution_en_profondeur_distance_limitée(self,get_chemin,afficher_chemin,afficher_seed,getMatrice,distance_max):
        """
        Fonction qui affiche la matrice avec la méthode du parcours en profondeur en restant à une certaine distance du joueur
        Entrées:
            Un booléen indiquant si l'on veut le chemin ou pas 
            Un booléen indiquant si l'on veut afficher le chemin ou pas
            Un booléen indiquant si l'on veut afficher la seed ou non
            Un booléen indiquant si l'on veut obtenir la matrice indiquant ou est passé le résolveur
            la distance maximum d'affichage
        Sorties:
            un booléen indiquant si la matrice est résolvable
            OU
            le chemin par lequel l'algo est arrivé
        """
        rdm=random.randrange (1,10**18,1)

        #on définit la seed de notre solutionneur
        #cela permet d'avoir le meme résultat
        if afficher_seed:
            print("seed",rdm)
        #random.seed(498965033146031877)
        random.seed(rdm)
        depart_x=self.depart_x
        depart_y=self.depart_y

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

        solution=None
        
        while len(stack)!=0 and (position_x!=self.arrivee_x or position_y!=self.arrivee_y):
            #on récupère les coords de la ou l'on est cad la dernière case dans le stack
            position_x=stack[len(stack)-1][0]
            position_y=stack[len(stack)-1][1]
            #print(position_x,position_y)
            #on récupère les positions utilisables
            if afficher_chemin:
                self.matrice_cases[position_x][position_y].set_Couleur((0,0,255))
            
            voisins,positions_voisins = self.voisins_case(position_x,position_y)
            
            directions_explorables = self.directions_utilisables(voisins,positions_voisins,position_x,position_y)

            if len(directions_explorables)>0 and len(stack) < distance_max-1:
                
                #randrange est exclusif
                num_direction=random.randrange(0,len(directions_explorables))
                
                #direction ou l'on va
                direction=directions_explorables[num_direction]

                new_x,new_y = self.nouvelles_coords(position_x,position_y,direction)

                self.cases_visitees[new_x][new_y]=True
                
                #on ajoute les nouvelles coordonnées de la case au stack
                stack.append([new_x,new_y])
            else:
                if afficher_chemin:
                    self.matrice_cases[position_x][position_y].set_Couleur((255,0,0))
                #on revient encore en arrière
                stack.pop()
                #print(position_x,position_y,len(stack))

        if getMatrice:
            solution=self.cases_visitees
        elif position_x==self.arrivee_x and position_y == self.arrivee_y:
            if get_chemin:
                solution=stack
            else:
                solution=True
        else:
            solution=False
        
        return solution
    def resolution_en_largeur_distance_limitée(self,get_chemin,afficher_chemin,afficher_seed,getMatrice,distance_max):
        """
        Fonction qui affiche la matrice avec la méthode du parcours en largeur en restant à une certaine distance du joueur
        Entrées:
            Un booléen indiquant si l'on veut le chemin ou pas 
            Un booléen indiquant si l'on veut afficher le chemin ou pas
            Un booléen indiquant si l'on veut afficher la seed ou non
            Un booléen indiquant si l'on veut obtenir la matrice indiquant ou est passé le résolveur
            la distance maximum d'affichage
        Sorties:
            un booléen indiquant si la matrice est résolvable
            OU
            le chemin par lequel l'algo est arrivé
        """
        depart_x=self.depart_x
        depart_y=self.depart_y

        #position dans la matrice
        position_x=depart_x
        position_y=depart_y
        #la queue est une liste de positions
        queue=[[depart_x,depart_y]]
        chemins=[Chemin([],0,depart_x,depart_y)]


        chemin_courant=chemins[0]

        self.cases_visitees[depart_x][depart_y]=True

        while len(queue)!=0 and (position_x!=self.arrivee_x or position_y!=self.arrivee_y):
            chemin_courant=chemins[0]
            #obtenir elt suivant
            position_x=queue[0][0]
            position_y=queue[0][1]
            #enlever position dans queue
            queue.pop(0)
            chemins.pop(0)
            
            #on affiche le chemin
            if afficher_chemin:
                self.matrice_cases[position_x][position_y].set_Couleur((255,0,0))
            #trouver les positions explorables
            voisins,positions_voisins=self.voisins_case(position_x,position_y)

            directions_explorables = self.directions_utilisables(voisins,positions_voisins,position_x,position_y)

            for direction in directions_explorables:
                if chemin_courant.getPoids()<=distance_max:
                    queue.append(positions_voisins[direction])
                    new_chemin=Chemin(chemin_courant.getChemin(),chemin_courant.getPoids(),positions_voisins[direction][0],positions_voisins[direction][1])
                    chemins.append(new_chemin)
                    
                    #on marque la case comme visitée
                    self.cases_visitees[positions_voisins[direction][0]][positions_voisins[direction][1]]=True       
            #print(chemin_courant.getChemin())

        if afficher_chemin and len(chemins)>0:
            for i in chemins[0].getChemin():
                self.matrice_cases[i[0]][i[1]].set_Couleur((0,0,255))

        solution=None
        if getMatrice:
            solution=self.cases_visitees
        elif get_chemin and (position_x==self.arrivee_x and position_y==self.arrivee_y):
            solution=chemins[0].getChemin()
        else:
            solution= (position_x==self.arrivee_x and position_y==self.arrivee_y)

            
        return solution

class Chemin():
    def __init__(self,chemin_precedent,poids_precedent,position_x,position_y):
        #print("init chemin precedent: "+str(chemin_precedent)+" position suivante "+str(position_x)+" "+str(position_y))
        #if chemin_precedent!=None:
        self.chemin=chemin_precedent
        self.chemin.append([position_x,position_y])
        #print(self.chemin)
        #else:
        #    self.chemin=[[position_x,position_y]]
        self.poids=poids_precedent+1

    def getChemin(self):
        new_chemin=[self.chemin[i]for i in range(0,len(self.chemin))]
        return new_chemin
    def getPoids(self):
        return self.poids
