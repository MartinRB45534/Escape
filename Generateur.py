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
    def __init__(self,matrice_cases,largeur,hauteur,modeGeneration="Profondeur"):
        self.largeur = largeur
        self.hauteur = hauteur
        self.matrice_cases = matrice_cases
        self.modeGeneration = modeGeneration
    def generation(self):
        if self.modeGeneration=="Profondeur":
            return self.generation_en_profondeur()
        else:
            print("mode de génération choisi incompatible")
    def generation_en_profondeur(self):
        rdm=random.randrange (1,10**18,1)

        #on définit la seed de notre générateur
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
                num_mur=random.randrange(0,len(murs_generables))
                
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
        murs_utilisables=[]

        for i in range(0,len(voisins)):
            if voisins[i]!=None and voisins[i].nb_murs_pleins()==4:
                murs_utilisables.append(i)
        return murs_utilisables
        
    def voisins_case(self,x,y):
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


#gen = Generateur([],0,0)
#gen.generation()




