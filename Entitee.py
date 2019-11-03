class Entitee:
    def __init__(self,position):
        self.position=position
    def dessine_toi(self,screen,decalage,LARGEUR_CASE,LARGEUR_MUR,position_screen):
        """Fonction a surdéfinir dans la classe fille"""
        print("à surdéfinir")
    def setPosition(self,position):
        self.position=position
    def getPosition(self):
        return self.position
