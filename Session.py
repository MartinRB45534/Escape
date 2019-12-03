from pygame import *
from Niveau import *
from Constantes import *
import pickle


class Session ():
    def __init__(self,niveau,difficulte,mode_affichage,mode_minimap,nb_niv_max):
        try:
            fichier = open(sauvegarde,'rb')
            f = pickle.Unpickler(fichier)
            parametres = f.load()
            self.niv_courant = Niveau(parametres[0],parametres[1],parametres[2],parametres[3],parametres[4],parametres[5],parametres[6],parametres[7],parametres[8],parametres[9])
            #paramètres pour la réinitialisation
            self.difficulte=self.niv_courant.difficulte
            self.mode_affichage=self.niv_courant.mode_affichage
            self.mode_minimap=self.niv_courant.mode_minimap
            self.recupere = True
        except IOError:
            self.niv_courant = Niveau(niveau,difficulte,mode_affichage,mode_minimap)
            #paramètres pour la réinitialisation
            self.difficulte=difficulte
            self.mode_affichage=mode_affichage
            self.mode_minimap=mode_minimap
            self.recupere = False
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
            fichier = open(sauvegarde,'wb')
            f = pickle.Pickler(fichier)
            f.clear_memo()
            f.dump(self.niv_courant.sauve())
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

        
