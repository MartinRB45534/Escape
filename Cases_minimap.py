from Cases import *
from Mur_minimap import *

class Case_minimap(Case):
    def __init__(self,tailleCase,tailleMur,murs,mode_minimap,arrivee=False):
        self.decouvert=-1 #le temps depuis que le joueur a vu cette case
        self.arrivee=arrivee
        self.mode_minimap = mode_minimap
        if self.mode_minimap == voir_tout :
            self.non_vu = (100,100,100)
            self.vu = (200,200,200)
            self.voit = (255,255,255)
        elif self.mode_minimap == passage :
            self.non_vu = (0,0,0)
            self.vu = (150,150,150)
            self.voit = (255,255,255)
        elif self.mode_minimap == aveugle :
            self.non_vu = (0,0,0)
            self.vu = (0,0,0)
            self.voit = (255,255,255)
        else :
            print ("Valeur de mode_minimap incorrecte.")
        Case.__init__(self,tailleCase,tailleMur)
        self.couleur = self.non_vu
        for i in range(len(self.murs)):
            self.murs[i] = Mur_minimap(murs[i].get_etat(),1)
        
    def dessine_toi(self,screen,x,y):
        """
        Fonction qui dessine l'objet
        Entrées:
            l'écran, la surface sur laquelle on dessine(objet pygame)
            la position de la case
        """
        pygame.draw.rect(screen,self.couleur,(x,y,2,2))
        self.set_couleur()
        #on dessine les murs vides en premiers pour éviter les bugs graphiques

        for i in range(0,len(self.murs)):
            if self.murs[i].get_etat()==MUR_VIDE:
                self.murs[i].dessine_toi(screen,x,y,2,i,self.couleur)
        #on dessine les autres murs
        for i in range(0,len(self.murs)):
            if self.murs[i].get_etat()!=MUR_VIDE:
                self.murs[i].dessine_toi(screen,x,y,2,i)

    def affiche_toi(self,screen,x,y,zoom):
        """
        Fonction qui dessine l'objet
        Entrées:
            l'écran, la surface sur laquelle on dessine(objet pygame)
            la position de la case
        """
        tailleMur = 1 * zoom
        tailleCase = 5 * zoom
        pygame.draw.rect(screen,self.couleur,(x,y,tailleCase,tailleCase))
        
        self.set_couleur()
        for i in range(0,len(self.murs)):
            self.murs[i].tailleMur = tailleMur
        #on dessine les murs vides en premiers pour éviter les bugs graphiques
        for i in range(0,len(self.murs)):
            if self.murs[i].get_etat()==MUR_VIDE:
                self.murs[i].dessine_toi(screen,x,y,tailleCase,i,self.couleur)
        #on dessine les autres murs
        for i in range(0,len(self.murs)):
            if self.murs[i].get_etat()!=MUR_VIDE:
                self.murs[i].dessine_toi(screen,x,y,tailleCase,i)
        for i in range(0,len(self.murs)):
            self.murs[i].tailleMur = 1
    def set_couleur(self):
        if self.arrivee and (self.mode_minimap == voir_tout or (self.decouvert>0 and mode_affichage == passage) or self.decouvert == 0):
            self.couleur = ARRIVEE
        elif self.decouvert == 0:
            self.couleur = self.voit
            self.decouvert = 1
        elif self.decouvert > 0:
            self.couleur = self.vu
            self.decouvert += 1
