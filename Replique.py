class Replique ():
    def __init__(self,contenu,taille_ecriture):
        self.contenu=contenu
        self.taille_ecriture=taille_ecriture
        #compteur interne déterminant ou l'on en est dans la réplique
        self.position_replique=0
    def get_contenu(self,nb_lignes):
        """
        Fonction qui renvoie la suite de la réplique
        Entrées:
            -le nombre de lignes que l'on veut
        Sorties:
            -les prochains lignes de la chaine
        """
        contenu = ""
        if self.position_replique < len(self.contenu):
            if not(self.position_replique + nb_lignes < len(self.contenu)):
                nb_lignes -= (self.position_replique + nb_lignes - len(self.contenu))
            contenu=self.contenu[self.position_replique : self.position_replique+nb_lignes]

            self.position_replique+=nb_lignes
                
        return contenu
    def est_fini(self):
        """
        Fonction qui indique si la réplique est finie
        Entrées:
            -Rien
        Sorties:
            -un booléen indiquant si la réplique est finie
        """
        return (self.position_replique == len(self.contenu))
    
