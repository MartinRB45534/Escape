from Cases import *
from Resolveur import *

class Meute:
    def __init__(self,largeur_lab,hauteur_lab,id_meute,nb_monstres,vues_bases,positions_vues_bases):
        self.largeur_lab=largeur_lab
        self.hauteur_lab=hauteur_lab
        
        self.vue_globale=[[Case(0,0) for i in range(hauteur_lab)]for j in range(largeur_lab)]
        self.ini_vue_globale(vues_bases,positions_vues_bases)

        self.positions_precedentes=[[0,0] for i in range(0,nb_monstres)]
        self.id_meute=id_meute
        self.compteur=0
        

    def actualisation_vues(self,vues,positions_vues):
        """
        Fonction qui actualise la vue de chaque monstre avec la vue globale
        Entrées:
            -les différentes vues des monstres de la meute
            -les positions des vues des monstres de la meute
        Sorties:
            la vue globale de la meute
        """
        #on construit la vue de la meute
        self.actualisation_vue_globale(vues,positions_vues)

        return self.vue_globale

    def ini_vue_globale(self,vues_bases,positions_vues_bases):
        """
        Fonction qui initialise la vue globale
        Entrées:
            -les vues des monstres en l'instant 0
            -les positions des vues des monstres
        """
        for i in range(0,len(vues_bases)):
            self.copie_vue(vues_bases[i],positions_vues_bases[i])

    def copie_vue(self,vue,position_vue):
        """
        Fonction qui copie une vue dans la vue globale
        Entrées:
            -la position de la vue
            -la vue a copier
        """
        for x in range(0,len(vue)):
            for y in range(0,len(vue[0])):
                x_mat=x+position_vue[0]
                y_mat=y+position_vue[1]
                if (x_mat>=0 and x_mat<self.largeur_lab) and (y_mat>=0 and y_mat<self.hauteur_lab):
                    self.vue_globale[x_mat][y_mat]=vue[x][y]
    def actualisation_vue_globale(self,vues,positions_vues):
        """
        Fonction qui actualise la vue globale
        Entrées:
            -les différentes vues des monstres de la meute
            -les positions des vues des monstres de la meute
        Sorties:
            Rien
        """
        #self.vue_globale=[[Case(0,0) for i in range(self.hauteur_lab)]for j in range(self.largeur_lab)]

        for i in range(0,len(vues)):
            """if self.positions_precedentes[i]!=positions_vues[i]:
                print("position vue")
                print(positions_vues[i])
                print("coin bas droite")
                print(positions_vues[i][0]+len(vues[i]),positions_vues[i][1]+len(vues[i][0]))

                for y in range(0,len(vues[i][0])):
                    for x in range(0,len(vues[i])):
                        if vues[i][x][y]!=None:
                            print("  "+str(x+positions_vues[i][0])+" "+str(y+positions_vues[i][1]), end ='')
                    print()"""
            self.actualiser_vue(vues[i],positions_vues[i],self.positions_precedentes[i],positions_vues,vues)

        """ligne=False
        if self.compteur==20:
            print("vue globale")
            for y in range(0,len(self.vue_globale[0])):
                for x in range(0,len(self.vue_globale)):
                    if self.vue_globale[x][y].nb_murs_pleins()!=4:
                        print("  "+str(x)+" "+str(y), end ='')
                        ligne=True
                if ligne:
                    print()
                    ligne=False
            self.compteur=0
        else:
            self.compteur+=1"""
        self.positions_precedentes=positions_vues
            
    
    def actualiser_vue(self,vue,position_vue,position_anterieure,positions_vues,vues):
        """
        Fonction qui actualise une vue sur la vue globale
        Entrées:
            -la vue a copier
            -la position de la vue sur le labyrinthe
            -la position précédente de la vue
            -les positions des vues
            -les vues
        Sorties:
            Rien
        """
        if position_vue!=position_anterieure:
            largeurs_vues=[len(vues[i]) for i in range(0,len(vues))]
            hauteurs_vues=[len(vues[i][0]) for i in range(0,len(vues))]

            largeur_vue=len(vue)
            hauteur_vue=len(vue[0])
            
            if position_vue[0]<position_anterieure[0]:
                for y in range(0,hauteur_vue):
                    if self.coords_valides([position_vue[0],position_vue[1]+y]) and vue[0][y]!=None:
                        self.vue_globale[position_vue[0]][position_vue[1]+y]=vue[0][y]
                    self.clear_case([position_anterieure[0]+largeur_vue,position_vue[1]+y],positions_vues,largeurs_vues,hauteurs_vues)
                #print("ajout colonne gauche + del colonne droite")
                #print(position_vue[0],position_anterieure[0]+largeur_vue)
                
            elif position_vue[0]>position_anterieure[0]:
                for y in range(0,hauteur_vue):
                    if self.coords_valides([position_vue[0]+largeur_vue-1,position_vue[1]+y])and vue[largeur_vue-1][y]!=None:
                        self.vue_globale[position_vue[0]+largeur_vue-1][position_vue[1]+y]=vue[largeur_vue-1][y]
                    self.clear_case([position_anterieure[0],position_vue[1]+y],positions_vues,largeurs_vues,hauteurs_vues)
                #print("ajout colonne droite + del colonne gauche")
                #print(position_vue[0]+largeur_vue,position_anterieure[0])
                
            elif position_vue[1]<position_anterieure[1]:
                for x in range(0,largeur_vue):
                    if self.coords_valides([position_vue[0]+x,position_vue[1]])and vue[x][0]!=None:
                        self.vue_globale[position_vue[0]+x][position_vue[1]]=vue[x][0]
                    self.clear_case([position_vue[0]+x,position_anterieure[1]+hauteur_vue],positions_vues,largeurs_vues,hauteurs_vues)
                #print("ajout ligne gauche + del ligne droite")
                #print(position_vue[1],position_anterieure[1]+hauteur_vue)
            else:
                for x in range(0,largeur_vue):
                    if self.coords_valides([position_vue[0]+x,position_vue[1]+hauteur_vue-1])and vue[x][hauteur_vue-1]!=None:
                        self.vue_globale[position_vue[0]+x][position_vue[1]+hauteur_vue-1]=vue[x][hauteur_vue-1]
                    self.clear_case([position_vue[0]+x,position_anterieure[1]],positions_vues,largeurs_vues,hauteurs_vues)
                #print("ajout ligne droite + del ligne gauche")
                #print(position_vue[1]+hauteur_vue,position_anterieure[1])
                        
    def coords_valides(self,position_mat):
        """
        Fonction qui indique si les coords sont valides
        Entrées:
            -la position des coords dans la matrice
            -la largeur de la vue
            -la hauteur de la vue
        Sorties:
            -un booléen
        """
        valide_mat= (position_mat[0]>=0 and position_mat[0]<self.largeur_lab) and (position_mat[1]>=0 and position_mat[1]<self.hauteur_lab)

        return valide_mat
    def clear_case(self,position,positions_vues,largeurs,hauteurs):
        """
        Fonction qui efface la case si nécessaire
        Entrées:
            -la position de la case
            -les positions des vues
            -les largeurs des vues
            -les hauteurs des vues
        Sortie:
            Rien
        """
        if not(self.appartient_vue(position,positions_vues,largeurs,hauteurs)) and self.coords_valides(position):
            self.vue_globale[position[0]][position[1]]=Case(0,0)

    def appartient_vue(self,position,positions_vues,largeurs,hauteurs):
        """
        Fonction qui détermine si la position est dans une vue
        Entrées:
            -la position de la case
            -les positions des vues
            -les largeurs des vues
            -les hauteurs des vues
        Sortie:
            -booléen indiquant si la position appartient a une vue
        """
        appartient_a_une_vue=False
        i=0
        while i<len(positions_vues) and not(appartient_a_une_vue):
            appartient_a_une_vue=(position[0]>=positions_vues[i][0] and position[0]<=positions_vues[i][0]+largeurs[i])and (position[1]>=positions_vues[i][1] and position[1]<=positions_vues[i][1]+hauteurs[i])
            i+=1
        return appartient_a_une_vue

            
