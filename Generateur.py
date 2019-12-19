import Cases
import random
from Constantes import *
from Teleporteurs import *

#constantes
HAUT=0
DROITE=1
BAS=2
GAUCHE=3

MUR_VIDE=0
MUR_PLEIN=1

class Generateur:
    def __init__(self,matrice_cases,largeur,hauteur,poids,paterns,cases_speciales,modeGeneration="Profondeur"):
        self.largeur = largeur
        self.hauteur = hauteur
        self.matrice_cases = matrice_cases
        self.modeGeneration = modeGeneration
        self.poids = poids
        self.paterns = paterns
        self.cases_speciales = cases_speciales
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
        matrice=None
        
        self.pre_gene_paterns()
        self.pre_gene_speciales()
        if self.modeGeneration=="Profondeur":
            matrice= self.generation_en_profondeur()
            #on casse les murs conformément aux paramètres
            self.casser_X_murs(proba,nbMurs,pourcentage)
        else:
            print("mode de génération choisi incompatible")

        self.post_gene_paterns()
        
        return matrice
    def pre_gene_speciales(self):
        """
        Fonction qui pregenere les cases spéciales
        Format d'une case spéciale: [coordonnées, objet]
        """
        if self.cases_speciales != None:
            for case in self.cases_speciales:
                self.matrice_cases[case[0][0]][case[0][1]] = case[1]
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
        depart_x=1
        depart_y=1

        #position dans la matrice
        position_x=depart_x
        position_y=depart_y
        #le stack est une liste de positions
        stack=[[depart_x,depart_y]]
    

        while len(stack)!=0 :
            
            #on récupère les coords de la ou l'on es cad la dernière case dans le stack
            position_x=stack[len(stack)-1][0]
            position_y=stack[len(stack)-1][1]
            
            voisins = self.voisins_case(position_x,position_y)
            
            murs_generables = self.murs_utilisables(voisins)

            #On ne fait pas passer un chemin par un téléporteur
            if len(murs_generables)>0 and not(issubclass(type(self.matrice_cases[position_x][position_y]),Teleporteur_local)): 
                
                #randrange est exclusif
                num_mur=self.randomPoids(murs_generables)
                
                #direction du mur à casser
                direction_mur=murs_generables[num_mur]

                
                self.casser_mur(direction_mur,position_x,position_y)

                new_x,new_y = self.nouvelles_coords(position_x,position_y,direction_mur)
                #on ajoute les nouvelles coordonnées de la case au stack
                stack.append([new_x,new_y])
            else:
                #on revient encore en arrière
                stack.pop()
                #print(position_x,position_y,len(stack))

                
        return self.matrice_cases

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
        
    def nouvelles_coords(self,x,y,direction):
        """
        Fonction qui calcul les nouvelles coordonnées du générateur
        Entrées:
            les coordonnées du générateur
            la direction ou le générateur va
        Sorties:
            les nouvelles coordonnées du générateur
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
    def murs_utilisables(self,voisins):
        """
        Fonction qui prend en entrées:
            les voisins de la case
        et qui renvoie les directions ou les murs sont cassables
        """
        murs_utilisables=[]

        for i in range(0,len(voisins)):
            if voisins[i]!=None and voisins[i].nb_murs_pleins()==4 and voisins[i].get_murs()[self.direction_opposee(i)].get_etat()!=INTOUCHABLE:
                murs_utilisables.append(i)
        return murs_utilisables
        
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
            if murs[i].get_etat()==INTOUCHABLE:
                directions_interdites.append(i)
            
        return directions_interdites

    def casser_mur_random_case(self,position_case):
        """
        Fonction qui prend en entrée la position de la case dont on veut casser un mur
        et qui renvoie un booléen indiquant si l'on as pu casser un mur
        """
        casser = False

        murs=self.directions_utilisables(self.voisins_case(position_case[0],position_case[1]))
        if len(murs)!=0:
            mur_a_casser=random.randrange(0,len(murs))
            self.casser_mur(murs[mur_a_casser],position_case[0],position_case[1])
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
                murs=self.directions_utilisables(self.voisins_case(x,y))
                if HAUT in murs and random.random() <= proba :
                    self.casser_mur(HAUT,x,y)
                if GAUCHE in murs and random.random() <= proba :
                    self.casser_mur(GAUCHE,x,y)
                    
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
        
        return int((murs_pleins-self.hauteur*2-self.largeur*2)/2)
    
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
                #on vérifie qu'on peut aussi casser le mur d'en face
                if voisins[direction].mur_plein(direction_inverse) and voisins[direction].get_murs()[direction_inverse].get_etat()!=INTOUCHABLE:
                    murs_utilisables.append(direction)
        return murs_utilisables





