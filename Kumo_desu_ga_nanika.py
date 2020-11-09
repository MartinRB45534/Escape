from Skill import *

#On commence par les skills de kumoko :
class Skanda(Skill,Skill_deplacement):
    """Le skill de déplacement de kumoko."""
    def __init__(self):
        Skill.__init__(self)
        self.latence = 5.5
        self.gain_xp = 0.1 

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.latence-=0.5 #La latence diminue à chaque niveau
            self.niveau+=1 #Le niveau augmente
            #Pas d'autre cadeau
        
    def utilise(self):
        """fonction qui utilise le skill"""
        self.xp_new+=self.gain_xp #On gagne de l'xp !
        return self.latence, self.niveau #On renvoie le temps que prendra l'action, pour savoir combien de temps l'agissant attendra, et le niveau, pour les calculs du controleur, des collisions, du labyrinthe, etc.

class Wisdom(Skill,Skill_vision):
    """Le skill de vision de kumoko.""" #À modifier pour ajouter les effets d'analyse
    def __init__(self):
        Skill.__init__(self)
        self.portee = 20
        self.gain_xp = 0.01

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.portee+=3
            self.niveau+=1

    def utilise(self):
        self.xp_new+=self.gain_xp
        return self.portee

class Height_of_Occultism(Skill):
    """Le skill de magie de kumoko""" #Kumoko peut lancer plusieurs magies en un tour si la somme de leurs latences est inférieure à 1
    def __init__(self,magies={}):
        Skill.__init__(self)
        self.magies=magies
        self.latence = 0
        self.gain_xp = 0

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            """fonction qui procède à l'évolution"""
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int):
                    self.xp.append(cadeau)
                elif isinstance(cadeau,magie):
                    self.ajoute(magie)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1

    def ajoute(self,magie):
        """Focntion qui ajoute une magie. Utilisée lors des montées de niveau ou par le joueur (le joueur peut choisir de nouvelles magies lors de l'évolution de sa classe principale)."""
        self.magies[magie.nom]=magie

    def utilise(self,nom):
        magie = self.magies[nom].donne_magie(self.niveau)
        self.gain_xp = magie.gain_xp + magie.cout_mp*0.1
        self.xp_new += self.gain_xp
        self.latence = magie.latence
        return self.latence, magie

class Divine_Thread_Weaving(Skill):
    """Le skill d'utilisation de toile de kumoko."""
    def __init__(self):
        Skill.__init__(self)
        self.degats = 100 #Les dégats qu'une rencontre avec la toile de kumoko infligent. Commencer à plus ?
        self.element = Terre #L'élément conféré à la toile de kumoko, qui servira pour les attaques. Kumoko peut en changer.
        self.colle = 10 #La priorité que l'action de mouvement doit dépasser pour échapper aux toiles collantes de kumoko.
        self.vitesse = 5 #Le nombre de cases qu'une toile éjectée par kumoko parcours en un tour.
        self.latence = 1 #Kumoko peut utiliser ce skill une fois par tour.
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            """fonction qui procède à l'évolution"""
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int):
                    self.xp.append(cadeau)
                elif isinstance(cadeau,magie):
                    self.ajoute(magie)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.degats += 100
            self.colle += 1
            self.vitesse += 2

    def confere(self,element):
        self.element = element

    def utilise(self,action):
        self.xp_new+=self.gain_xp
        if action == "attaque" :
            return latence, Morning_spider(self.degats,self.vitesse,self.element)
        elif action == "pose piege" :
            return latence, Thread_trap(self.colle)
        elif action == "lance piege" :
            return latence, Thread_bounds(self.colle,self.vitesse)
        else :
            print(action + " ? Qu'est-ce que c'est, ça se mange ?")

class Jinx_Evil_Eye(Skill):
    """Le skill de malédiction de kumoko."""
    def __init__(self):
        Skill.__init__(self)
        self.taux_absorbtion = 0 #Kumoko absorbe une partie des PV et PM restants de son adversaire.
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            """fonction qui procède à l'évolution"""
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int):
                    self.xp.append(cadeau)
                elif isinstance(cadeau,magie):
                    self.ajoute(magie)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.taux_absorption += 0.075 #Est-ce que c'est pas un peu beaucoup ? Kumoko est pas fait pour être vaincue en même temps...

    def utilise(self,nb_yeux):
        self.xp_new+=self.gain_xp*nb_yeux
        return self.taux_absorption

class Inert_Evil_Eye(Skill):
    """Le skill de pétrification de kumoko."""
    def __init__(self):
        Skill.__init__(self)
        self.perte_vitesse = 0 #La pétrification se caractérise par une perte progressive de vitesse.
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            """fonction qui procède à l'évolution"""
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int):
                    self.xp.append(cadeau)
                elif isinstance(cadeau,magie):
                    self.ajoute(magie)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.perte_vitesse += 0.0025 #Est-ce que c'est pas un peu beaucoup ? Kumoko est pas fait pour être vaincue en même temps...

    def utilise(self,nb_yeux):
        self.xp_new+=self.gain_xp*nb_yeux
        return self.perte_vitesse

class Repellent_Evil_Eye(Skill):
    """Le skill de repoussement de kumoko."""
    def __init__(self):
        Skill.__init__(self)
        self.vitesse_repoussement = 0 #Le repoussement se traduit par une vitesse si kumoko repousse sur un côté (la cible se comporte comme un projectile ?)
        self.perte_vitesse = 0 #Si kumoko repousse vers le bas, l'ennemi est ralenti, mais les xp de déplacement sont augmentés. Par défaut, les huit yeux de kumoko sont équipés de cet Evil_Eye dirigé sur lui-même.
        self.boost_xp = 0
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            """fonction qui procède à l'évolution"""
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int):
                    self.xp.append(cadeau)
                elif isinstance(cadeau,magie):
                    self.ajoute(magie)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.vitesse_repoussement += 0.05 #Est-ce que c'est pas un peu beaucoup ? Kumoko est pas fait pour être vaincue en même temps...
            self.perte_vitesse += 0.05 #Est-ce que c'est pas un peu beaucoup ? Kumoko est pas fait pour être vaincue en même temps...
            self.boost_xp += 0.05

    def utilise(self,nb_yeux):
        self.xp_new+=self.gain_xp*nb_yeux
        return self.vitesse_repoussement,self.perte_vitesse,self.boost_xp

class Annihilating_Evil_Eye(Skill):
    """Le skill de one shot de kumoko."""
    def __init__(self):
        Skill.__init__(self)
        self.vitesse = 11 #Le nombre de tours qui s'écoulent entre le début de l'utilisation du skill et la mort. Si la cible sort de la vue de kumoko avant la fin du décompte, l'ennemi et l'oeil sont sauvés.
        self.gain_xp = 10 #On gagne un niveau à chaque mort (exempté de Pride, il faudrait si possible coder une montée de niveau conditionnelle).
        self.temps_restant = -1

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            """fonction qui procède à l'évolution"""
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int):
                    self.xp.append(cadeau)
                elif isinstance(cadeau,magie):
                    self.ajoute(magie)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.vitesse -= 1

    def utilise(self):
        if self.temps_restant == -1:
            self.temps_restant = self.vitesse
        self.temps_restant -= 1
        if self.temps_restant == 0:
            self.temps_restant = -1
            res = True
            self.xp_new += self.gain_xp
        else :
            res = False

        return res

    def perdu(self):
        """Quand la cible sort du champ de vision."""
        self.temps_restant = -1

class Evil_Eye(Skill):
    """Le skill qui controle les Evil_Eyes de kumoko."""
    def __init__(self):
        Skill.__init__(self)
        self.eyes = [["Libre",None]]*8

    def evo(self,nb_evo=1):
        self.niveau += 1

    def attribue(self,oeil,skill,cible):
        if self.eyes[oeil][0] != "Détruit" :
            self.eyes[oeil] = [skill,cible]

    def utilise(self):
        res = []
        for oeil in range(8):
            self.xp_new += self.gain_xp
            if not isinstance(str,self.eyes[oeil][0]):
                skill=self.eyes[oeil][0]
                cible=self.eyes[oeil][0]
                if isinstance(Annihilating_Evil_Eye,skill):
                    res_tmp = skill.utilise()
                    if res_tmp:
                        self.eyes[oeil] = ["Détruit",None]
                else :
                    res_tmp = skill.utilise()
                res += skill,res_tmp,cible
        return res

class Scythe(Skill):
    """Le skill d'attaque physique de kumoko."""
    def __init__(self):
        Skill.__init__(self)
        self.perce = 0.5 #La capacité de l'attaque à trancer les armures. Le coefficient placé devant le pourcentage de dégats bloqués.
        self.element = Terre #Kumoko peut associer l'élément de son choix à son attaque, selon les faiblesses de son adversaire.
        self.taux = 1 #La proportion de la stat d'attaque de kumoko qui sera traduite en dégats. Cette proportion est supérieure à 100%.
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.perce -= 0.05
            self.taux += 0.1
            self.niveau += 1

    def confere(self,element):
        self.element = element

    def utilise(self):
        self.xp_new += self.gain_xp
        return self.perce,self.element,self.taux

class Pride(Skill):
    """Le skill de boost d'amélioration de kumoko."""
    def __init__(self):
        Skill.__init__(self)
        self.taux_xp = 1 #Pride augmente la vitesse du gain d'xp.
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.taux_xp += 0.2
            self.niveau += 1

    def utilise(self):
        self.xp_new += self.gain_xp
        return self.taux_xp

class Sloth(Skill):
    """Le skill de déboost de zone de kumoko."""
    def __init__(self):
        Skill.__init__(self)
        self.taux = 1 #Les vitesses des ennemis de kumoko sont réduites.
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.taux -= 0.075
            self.niveau += 1

    def utilise(self):
        self.xp_new += self.gain_xp
        return self.taux

class Taboo(Skill):
    """Le skill piégé de kumoko."""
    def __init__(self):
        Skill.__init__(self)
        self.gain_xp = 0.01

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.niveau += 1

    def utilise(self):
        self.xp_new += self.gain_xp
        return self.taux #Le skill augmente de niveau au fur et à mesure. S'il est au niveau 10 entre les mains du joueur, ce dernier est "libéré" du monde factice du jeu et éjecté de la partie (c'est un piège contre les voleurs).

class Immortality(Skill):
    """Le skill d'immortalité de kumoko."""
    def __init__(self):
        Skill.__init__(self)
        self.coef = 0.80
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.coef+=0.02
            self.niveau+=1

    def utilise(self):
        self.xp_new+=self.gain_xp
        return self.coef

def Egg_Laying(Skill):
    """Le skill de ponte de kumoko."""
    def __init__(self):
        Skill.__init__(self)
        self.progeniture = []
        self.pontes = 0 #Le nombre d'oeufs qu'elle a pondus. Elle arrête de compter après 11.
        self.latence = 1
        self.gain_xp = 0.01

    def gagne_xp(self):
        for enfant in self.progeniture:
            self.xp_new += enfant.classe_principale.gagne_xp() #!!! Ne pas leur faire gagner l'xp deux fois !!! Kumoko récupère de l'xp de ses enfants.
        res = self.xp_new*self.propagation
        self.xp+=self.xp_new
        self.xp_new=0
        if self.next_evo=="xp":
            self.check_evo()
        return res

    def evo(self,nb_evo):
        for i in range(nb_evo):
            self.niveau += 1

    def utilise(self):
        if self.naissance < 11: #On est toujours dans les dix premiers oeufs.
            libre = True
            for enfant in self.progeniture :
                if enfant.etat == "oeuf" :
                    libre = False
                    return self.latence, None
        else :
            libre = True
        if libre :
            oeuf = Nightmare_vestige(self.position)
            oeuf.evo(self.niveau)
            return self.latence, oeuf #Les enfant de kumoko n'évoluent pas, mais ils ont le niveau qu'avait le skill Egg_Laying à leur naissance.

#Les skills des nightmare vestiges sont des version inférieures de ceux de kumoko :
class Hatching(Skill):
    """Le skill d'éclosion des oeufs."""
    def __init__(self):
        Skill.__init__(self)

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.niveau += 1

    def utilise(self):
        self.evo
        return self.niveau == 10 #Le controlleur l'active à chaque tour. Quand il atteint le niveau 10, le controleur le retire et fait éclore l'oeuf.

class Lesser_Skanda(Skanda,Skill_intrasec):
    """Le skill de déplacement des nightmare vestiges."""
    def __init__(self):
        Skill.__init__(self)
        self.latence = 11
        self.gain_xp = 0.1 

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.latence-=1 #La latence diminue à chaque niveau
            self.niveau+=1 #Le niveau augmente
            #Pas d'autre cadeau
        
    def utilise(self):
        """fonction qui utilise le skill"""
        self.xp_new+=self.gain_xp #On gagne de l'xp !
        return self.latence, self.niveau #On renvoie le temps que prendra l'action, pour savoir combien de temps l'agissant attendra, et le niveau, pour les calculs du controleur, des collisions, du labyrinthe, etc.

class Lesser_Wisdom(Wisdom,Skill_intrasec):
    """Le skill de vision des nightmare vestiges.""" #À modifier pour ajouter les effets d'analyse
    def __init__(self):
        Skill.__init__(self)
        self.portee = 3
        self.gain_xp = 0.01

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.portee+=1
            self.niveau+=1

    def utilise(self):
        self.xp_new+=self.gain_xp
        return self.portee

class Lesser_Height_of_Occultism(Height_of_Occultism,Skill_intrasec):
    """Le skill de magie desnightmare vestiges.""" #Les nightmare vestiges peuvent lancer plusieurs magies en un tour si la somme de leurs latences est inférieure à 1
    def __init__(self,magies={}):
        Skill.__init__(self)
        self.magies=magies
        self.latence = 0
        self.gain_xp = 0

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            """fonction qui procède à l'évolution"""
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int):
                    self.xp.append(cadeau)
                elif isinstance(cadeau,magie):
                    self.ajoute(magie)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1

    def ajoute(self,magie):
        """Focntion qui ajoute une magie. Utilisée lors des montées de niveau ou par le joueur (le joueur peut choisir de nouvelles magies lors de l'évolution de sa classe principale)."""
        self.magies[magie.nom]=magie

    def utilise(self,nom):
        magie = self.magies[nom].donne_magie(self.niveau)
        self.gain_xp = magie.gain_xp + magie.cout*0.1
        self.xp_new+=self.gain_xp
        self.latence = magie.latence
        return self.latence, self.niveau, magie

class Lesser_Divine_Thread_Weaving(Divine_Thread_Weaving,Skill_intrasec):
    """Le skill d'utilisation de toile des nightmare vestiges."""
    def __init__(self):
        Skill.__init__(self)
        self.degats = 40 #Les dégats qu'une rencontre avec les toiles des nightmare vestiges infligent. Commencer à plus ?
        self.element = Terre #L'élément conféré à la toile des nightmare vestiges, qui servira pour les attaques. Terre ou ombre.
        self.colle = 6 #La priorité que l'action de mouvement doit dépasser pour échapper aux toiles collantes des nightmare vestiges.
        self.vitesse = 2 #Le nombre de cases qu'une toile éjectée par les nightmare vestiges parcours en un tour.
        self.latence = 2
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            """fonction qui procède à l'évolution"""
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int):
                    self.xp.append(cadeau)
                elif isinstance(cadeau,magie):
                    self.ajoute(magie)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.degats += 20
            self.colle += 1
            self.vitesse += 2

    def confere(self,element):
        self.element = element

    def utilise(self,action):
        self.xp_new+=self.gain_xp
        if action == "attaque" :
            return latence, Morning_spider(self.degats,self.vitesse,self.element)
        elif action == "pose piege" :
            return latence, Thread_trap(self.colle)
        elif action == "lance piege" :
            return latence, Thread_bounds(self.colle,self.vitesse)
        else :
            print(action + " ? Qu'est-ce que c'est, ça se mange ?")

class Lesser_Scythe(Scythe,Skill_intrasec):
    """Le skill d'attaque physique des nightmare vestiges."""
    def __init__(self):
        Skill.__init__(self)
        self.perce = 0.75 #La capacité de l'attaque à trancer les armures. Le coefficient placé devant le pourcentage de dégats bloqués.
        self.element = Terre #Les nightmare vestiges peuvent chosir l'ombre ou la terre comme élément.
        self.taux = 0.5 #La proportion de la stat d'attaque des nightmare vestiges qui sera traduite en dégats. Cette proportion est supérieure à 100%.
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.perce -= 0.025
            self.taux += 0.05
            self.niveau += 1

    def confere(self,element):
        self.element = element

    def utilise(self):
        self.xp_new += self.gain_xp
        return self.perce,self.element,self.taux
