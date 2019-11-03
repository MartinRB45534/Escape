import Cases
import random

#constantes
HAUT=0
DROITE=1
BAS=2
GAUCHE=3

MUR_VIDE=0
MUR_PLEIN=1

class Generateur:
    def __init__(self,matrice_cases,largeur,hauteur,poids,paterns,modeGeneration="Profondeur"):
        self.largeur = largeur
        self.hauteur = hauteur
        self.matrice_cases = matrice_cases
        self.modeGeneration = modeGeneration
        self.poids=poids
        self.paterns=paterns
    def generation(self):
        """
        Fonction qui permet de générer une matrice conformément au paramètres
        et au paterns
        Entrées:Rien
        Sorties:une matrice de cases générée
        """
        matrice=None
        
        self.pre_gene_paterns()
        if self.modeGeneration=="Profondeur":
            matrice= self.generation_en_profondeur()
        else:
            print("mode de génération choisi incompatible")

        self.post_gene_paterns()
        
        return matrice
    def pre_gene_paterns(self):
        """
        Fonction qui pregenere les paterns
        """
        if self.paterns != None:
            for patern in self.paterns :
                patern.pre_generation(self.matrice_cases)

    def post_gene_paterns(self):
        """
        Fonction qui postgenere les paterns
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
            #print(position_x,position_y)
            self.matrice_cases[position_x][position_y].set_Couleur((255,255,255))
            
            voisins = self.voisins_case(position_x,position_y)
            
            murs_generables = self.murs_utilisables(voisins)

            if len(murs_generables)>0:
                
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
    def murs_utilisables(self,voisins):
        """
        Fonction qui prend en entrées:
            les voisins de la case
        et qui renvoie les directions ou les murs sont cassables
        """
        murs_utilisables=[]

        for i in range(0,len(voisins)):
            if voisins[i]!=None and voisins[i].nb_murs_pleins()==4:
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
        

#gen = Generateur([],0,0)
#gen.generation()




