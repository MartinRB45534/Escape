class Replique ():
    def __init__(self,contenu,taille_ecriture):
        self.contenu=contenu
        self.taille_ecriture=taille_ecriture
        #compteur interne déterminant ou l'on en est dans la réplique
        self.position_replique=0
    def get_contenu(self,nb_chars):
        """
        Fonction qui renvoie la suite de la réplique
        Entrées:
            -le nombre de caractères que l'on veut
        Sorties:
            -les prochains charactères de la chaine
        """
        chaine = ""
        if self.position_replique < len(self.contenu):
            if not(self.position_replique+nb_chars < len(self.contenu)):
                nb_chars -= (self.position_replique+nb_chars-len(self.contenu))
            chaine=self.contenu[self.position_replique : self.position_replique+nb_chars]

            self.position_replique+=nb_chars
                
        return chaine
    def est_fini(self):
        """
        Fonction qui indique si la réplique est finie
        Entrées:
            -Rien
        Sorties:
            -un booléen indiquant si la réplique est finie
        """
        return (self.position_replique == len(self.contenu))
    
