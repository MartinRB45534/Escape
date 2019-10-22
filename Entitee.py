class Entitee:
    def __init__(self,position):
        self.position=position
    def dessine_toi(self):
        """Fonction a surdéfinir dans la classe fille"""
        print("à surdéfinir")
    def setPosition(self,position):
        self.position=position
    def getPosition(self):
        return self.position
