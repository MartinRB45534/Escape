class Evenement:
    def __init__(self,temps_restant):
        self.temps_restant=temps_restant

    def action(self):
        """
        Fonction qui exécute l'action de l'événement
        Entrées:
            Rien
        Sorties:
            Rien
        """
        print("a surdéfinir")
    def execute(self):
        """
        Fonction qui exécute un tic de l'événement(1 frame = 1 tic)
        Entrées:
            Rien
        Sorties:
            un booléen indiquant si l'événement est fini
        """
        self.temps_restant-=1
        #on exécute l'évènement
        self.action()
        return (self.temps_restant<=0)
