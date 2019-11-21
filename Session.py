from pygame import *
from Niveau import *

class Session ():
    def __init__(self,niveau,difficulté,mode_affichage,mode_minimap,nb_niv_max):
        self.niv_courant = Niveau(niveau,difficulté,mode_affichage,mode_minimap)
        #paramètres pour la réinitialisation
        self.difficulte=difficulté
        self.mode_affichage=mode_affichage
        self.mode_minimap=mode_minimap
        #paramètres pourle transfert de niveau
        self.nb_niv_courant=niveau
        self.nb_niv_max=nb_niv_max
    def reset_niveau(self):
        """
        Fonction qui recommence le niveau courant
        """
        self.niv_courant = Niveau(self.nb_niv_courant,self.difficulte,self.mode_affichage,self.mode_minimap)
    def transfert_niveau(self,joueur):
        """
        Fonction qui transfert les informations d'un niveau a un autre
        Entrées:
            -le niveau
        """
        self.niv_courant = Niveau(self.nb_niv_courant,self.difficulte,self.mode_affichage,self.mode_minimap,joueur)
    def run(self):
        """
        Fonction qui prend en charge la boucle principale de la session
        """
        pause = False
        while self.nb_niv_courant<=self.nb_niv_max and not pause:
            res,win,joueur = self.niv_courant.run()
            pause = (res==-1)
            if res != -1:
                pygame.time.wait(res)
                if win:
                    self.nb_niv_courant+=1
                    if self.nb_niv_courant>self.nb_niv_max:
                        self.nb_niv_courant=1
                    self.transfert_niveau(joueur)
                else:
                    self.reset_niveau()
        if self.nb_niv_courant>self.nb_niv_max:
            self.nb_niv_courant=1
        
