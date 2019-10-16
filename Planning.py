class Planning:
    
    def __init__(self):
        self.actions = []
        self.temps_restant = []

    def ajoute_action(self,action,temps):
        """fonction qui ajoute une action à la liste de choses à faire
           action est par exemple une méthode
           temps est en seconde, il est converti en milliseconde après"""
        self.actions += [action]
        self.temps_restant += [temps * 1000]

    def agit(self,temps_écoulé):
        """décompte et effectue les actions arrivées à terme"""
        nouvelles_actions = []
        nouveaux_temps = []
        for i in range(len(self.actions)):
            self.temps_restant[i]-=temps_écoulé
            if self.temps_restant[i] <= 0:
                self.actions[i]()
            else:
                nouvelles_actions += [self.actions[i]]
                nouveaux_temps += [self.temps_restant[i]]
        self.actions = nouvelles_actions
        self.temps_restant = nouveaux_temps
            
                
