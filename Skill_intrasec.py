#Les skills sont la base des actions qui ont lieu dans le jeu (action voulues ou automatiques). Les skills intrasecs sont liés à une classe, et montent de niveau quand la classe monte de niveau.

class Skill_intrasec:
    """!!! Skill != skille !!! (Private joke)"""
    def __init__(self,cadeaux_evo=[[],[],[],[],[],[],[],[],[],[]]):
        """conditions_evo : les conditions d'évolution du skill au niveau supérieur ; si c'est un nombre, indique l'xp nécessaire à l'évolution, si c'est une chaine de caractère, indique la fonction capable d'évaluer la condition
           cadeux_evo : les récompenses d'évolution ; peuvent être des skills (?), des classes (?) ou de l'xp"""
        self.niveau=0 #Le niveau devrais passer à 1 lorsqu'on acquiert le skill
        self.cad_evo=cadeaux_evo
        self.xp_new=0 #Contabilise l'xp obtenue pendant le tour, pour la propagation
        self.propagation=0.5 #Certains skills ont un taux de propagation plus important (?)
        
    def gagne_xp(self):
        #On propage l'xp accumulé au cours du tour vers la classe mère
        res = self.xp_new*self.propagation
        self.xp_new=0
        return res

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1

class Skill_deplacement(Skill_intrasec):
    """Le skill utilisé pour se déplacer. Lorsqu'il augmente de niveau, la vitesse de déplacement augmente aussi. C'est un skill intrasec à la classe principale.
       Les pnjs le sélectionnent lorsqu'il choisissent de se déplacer, alors que le joueur le sélectionne lorsqu'il appuie sur les touches. Le joueur peut aussi s'en servir lorsqu'il explore la minimap ou l'inventaire.
       C'est un skill actif, qui s'actionne quand on le réclame."""
    def __init__(self): #Pour l'instant le skill est générique, identique pour tous
        Skill_intrasec.__init__(self)
        self.latence = 11 #Le temps qui s'écoule après une utilisation de ce skill, il passera à 10 quand le skill sera mis au niveau 1
        self.gain_xp = 0.1 #L'xp gagnée à chaque utilisation du skill, actuellement il faut se déplacer 100 fois pour monter d'un niveau de la classe principale (c'est peu !)

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.latence-=1 #La latence diminue à chaque niveau
            self.niveau+=1 #Le niveau augmente
            #Pas d'autre cadeau
        
    def utilise(self):
        """fonction qui utilise le skill"""
        self.xp_new+=self.gain_xp #On gagne de l'xp !
        return self.latence, self.niveau #On renvoie le temps que prendra l'action, pour savoir combien de temps l'agissant attendra, et le niveau, pour les calculs du controleur, des collisions, du labyrinthe, etc.

class Skill_vision(Skill_intrasec):
    """Le skill utilisé pour observer son environnement. Lorsqu'il augmente de niveau, on peut voir plus loin. C'est un skill intrasec à la classe principale. !!!Ne pas confondre avec observation, qui permet d'obtenir des informations sur ce que l'on voit.!!!
       C'est un skill semi-passif, qui s'actionne à chaque tour."""
    def __init__(self): #Pour l'instant le skill est générique, identique pour tous
        Skill_intrasec.__init__(self)
        self.portee = 5 #Avec combien veut-on commencer ? Peut-être un peu plus ?
        self.gain_xp = 0.01 #L'xp gagnée à chaque utilisation du skill, actuellement il faut juste attendre 1000 tours pour monter d'un niveau de la classe principale (c'est peu !)

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.portee+=1 #1, est-ce trop ? pas assez ? En tous cas la portée de la vision augmente à chaque niveau
            self.niveau+=1 #Le niveau augmente
            #Pas d'autre cadeau

    def utilise(self): #Le skill ne fait que donner des infos, il ne peut pas manipuler d'objet labyrinthe ou autres
        self.xp_new+=self.gain_xp #On gagne de l'xp !
        return self.portee #Pour l'instant la portée est la seule chose qu'on veut savoir

class Skill_ramasse(Skill_intrasec):
    """Le skill utilisé pour ramasser un item. Lorsqu'il augmente de niveau, on peut ramasser des objets plus puissants. C'est un skill intrasec à la classe principale (mais certains ne l'ont pas).
       C'est un skill actif, qui s'actionne quand on le réclame."""
    def __init__(self):
        Skill_intrasec.__init__(self)
        self.priorite = 0
        self.latence = 11
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.priorite+=1 #La priorite augmente à chaque niveau
            self.latence-=1 #La latence diminue à chaque niveau
            self.niveau+=1 #Le niveau augmente
            #Pas d'autre cadeau

    def utilise(self,priorite):
        return self.latence, self.priorite>priorite

class Skill_boost_explosifs(Skill_intrasec):
    """Le skill d'amélioration des effets des explosifs (le spliter pour les trois effets ?). C'est un skill intrasec à la classe artificier.
       C'est un skill semi-passif (appelé à chaque utilisation d'un explosif)."""
    def __init__(self):
        Skill_intrasec.__init__(self)
        self.boost_degats_explosion = 0 #Les dégats infligés par le biais d'effets d'explosion sont boostés
        self.boost_portee_explosion = 0 #La portée des explosions (zone de dégats lorsqu'un explosif rencontre un obstacle) est boostée
        self.boost_portee_explosif = 0 #La portée des projectiles de type explosifs est boostée
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.boost_degats_explosion += 0.1 
            self.boost_portee_explosion += 0.1
            self.boost_portee_explosif += 0.1

    def utilise(self):
        self.xp_new+=self.gain_xp #On gagne de l'xp !
        return self.boost_degats_explosion,self.boost_portee_explosion,self.boost_portee_explosif

class Skill_boost_fleches(Skill_intrasec):
    """Le skill d'amélioration des effets des flèches (le spliter pour les trois effets ?). C'est un skill intrasec à la classe archer.
       C'est un skill semi-passif (appelé à chaque utilisation d'une flèche)."""
    def __init__(self):
        Skill_intrasec.__init__(self)
        self.boost_portee_fleche = 0 #La portée des projectiles de type flèche est boostée
        self.boost_vitesse_fleche = 0 #La vitesse des projectiles de type flèche est boostée
        self.boost_degats_fleche = 0 #Les dégats infligés par le biais de projectiles de type flèche sont boostés
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.boost_portee_fleche += 0.1 
            self.boost_vitesse_fleche += 0.1
            self.boost_degats_fleche += 0.1

    def utilise(self):
        self.xp_new+=self.gain_xp #On gagne de l'xp !
        return self.boost_portee_fleche,self.boost_vitesse_fleche,self.boost_degats_fleche

class Skill_boost_fleches_sniper(Skill_intrasec):
    """Le skill d'amélioration des effets des flèches (le spliter pour les trois effets ?). C'est un skill intrasec à la classe sniper.
       C'est un skill semi-passif (appelé à chaque utilisation d'une flèche)."""
    def __init__(self):
        Skill_intrasec.__init__(self)
        self.boost_portee_fleche = 0 #La portée des projectiles de type flèche est boostée
        self.boost_vitesse_fleche = 0 #La vitesse des projectiles de type flèche est boostée
        self.boost_degats_fleche = 0 #Les dégats infligés par le biais de projectiles de type flèche sont boostés
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.boost_portee_fleche += 0.2
            self.boost_vitesse_fleche += 0.2
            self.boost_degats_fleche += 0.2

    def utilise(self):
        self.xp_new+=self.gain_xp #On gagne de l'xp !
        return self.boost_portee_fleche,self.boost_vitesse_fleche,self.boost_degats_fleche

class Skill_boost_epee(Skill_intrasec):
    """Le skill d'amélioration des effets d'épées. C'est un skill intrasec à la classe Epéiste.
       C'est un skill semi-passif (appelé à chaque utilisation d'une épée)."""
    def __init__(self):
        Skill_intrasec.__init__(self)
        self.boost_degats = 0 #Le coefficient appliqué aux dégats de base pour calculer les dégats supplémentaires
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.boost_degats += 0.1 #On peut atteindre 100 % de dégats supplémentaires. Avec le skill de manipulation d'épée aussi au niveau 10, on aurait 200% de boost de dégats au total.

    def utilise(self):
        self.xp_new+=self.gain_xp #On gagne de l'xp !
        return self.boost_degats

class Skill_boost_lance(Skill_intrasec):
    """Le skill d'amélioration des effets de lance. C'est un skill intrasec à la classe Lancier.
       C'est un skill semi-passif (appelé à chaque utilisation d'une lance)."""
    def __init__(self):
        Skill_intrasec.__init__(self)
        self.boost_degats = 0 #Le coefficient appliqué aux dégats de base pour calculer les dégats supplémentaires
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.boost_degats += 0.1 #On peut atteindre 100 % de dégats supplémentaires. Avec le skill de manipulation de lance aussi au niveau 10, on aurait 200% de boost de dégats au total.

    def utilise(self):
        self.xp_new+=self.gain_xp #On gagne de l'xp !
        return self.boost_degats

class Skill_boost_bouclier(Skill_intrasec):
    """Le skill d'amélioration des effets de bouclier. C'est un skill intrasec à la classe Porteur de bouclier.
       C'est un skill semi-passif (appelé à chaque utilisation d'un bouclier)."""
    def __init__(self):
        Skill_intrasec.__init__(self)
        self.boost_defense = 1 #Le coefficient appliqué au taux de dégats non bloqués de base pour connaitre le taux réel de dégats non bloqués
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.boost_defense -= 0.1 #On peut bloquer 100 % des dégats grace à ce skill. Attention quand même aux effets qui ignorent les boucliers et aux attaques surprises.

    def utilise(self):
        self.xp_new+=self.gain_xp #On gagne de l'xp !
        return self.boost_defense

class Skill_boost_armes(Skill_intrasec):
    """Le skill d'amélioration des effets d'armes. C'est un skill intrasec à la classe Homme d'armes.
       C'est un skill semi-passif (appelé à chaque utilisation d'une arme)."""
    def __init__(self):
        Skill_intrasec.__init__(self)
        self.boost_degats = 0 #Le coefficient appliqué aux dégats de base pour calculer les dégats supplémentaires
        self.boost_defense = 1 #Le coefficient appliqué au taux de dégats non bloqués de base pour connaitre le taux réel de dégats non bloqués
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.boost_degats += 0.1 #On peut atteindre 100 % de dégats supplémentaires. Avec le skill de manipulation d'épée ou de lance aussi au niveau 10, on aurait 200% de boost de dégats au total. Avec la classe d'épéiste ou de lancier aussi au niveau 10, on arrive à 500% de boost de dégats au total.
            self.boost_defense -= 0.1 #On peut bloquer 100 % des dégats grace à la classe. Attention quand même aux effets qui ignorent les boucliers et aux attaques surprises.

    def utilise(self):
        self.xp_new+=self.gain_xp #On gagne de l'xp !
        return self.boost_degats,self.boost_defense

class Skill_boost_enchantements(Skill_intrasec):
    """Le skill d'amélioration des effets d'enchantements. C'est un skill intrasec à la classe Enchanteur.
       C'est un skill semi-passif (appelé à chaque utilisation d'un enchantement)."""
    def __init__(self):
        Skill_intrasec.__init__(self)
        self.reduc_mana = 0 #Le taux de mana nécessaire en moins pour lancer un enchantement
        self.boost_temps = 0 #La durée supplémentaire des enchantements
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.reduc_mana += 0.05
            self.boost_temps += 0.1

    def utilise(self):
        self.xp_new += self.gain_xp #On gagne de l'xp !
        return self.reduc_mana,self.boost_temps

class Skill_boost_soutien(Skill_intrasec):
    """Le skill d'amélioration des sorts de soutien. C'est un skill intrasec à la classe Soutien.
       C'est un skill semi-passif (appelé à chaque utilisation d'un sort de soutien)."""
    def __init__(self):
        Skill_intrasec.__init__(self)
        self.reduc_mana = 0 #Le taux de mana nécessaire en moins pour lancer un sort de soutien
        self.reduc_latence = 0 #Le taux de latence en moins après avoir lancé un sort de soutien
        self.gain_xp = 0.1
#Varier un peu plus les effets ?
    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.reduc_mana += 0.05
            self.reduc_latence += 0.05

    def utilise(self):
        self.xp_new += self.gain_xp #On gagne de l'xp !
        return self.reduc_mana,self.reduc_latence

class Skill_boost_ange(Skill_intrasec):
    """Le skill d'amélioration des sorts de soutien (hors débuffs). C'est un skill intrasec à la classe Ange.
       C'est un skill semi-passif (appelé à chaque utilisation d'un sort de soutien, hors débuffs)."""
    def __init__(self):
        Skill_intrasec.__init__(self)
        self.reduc_mana = 0 #Le taux de mana nécessaire en moins pour lancer un sort de soutien
        self.reduc_latence = 0 #Le taux de latence en moins après avoir lancé un sort de soutien
        self.gain_xp = 0.1
#Varier un peu plus les effets ?
    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.reduc_mana += 0.03
            self.reduc_latence += 0.09

    def utilise(self):
        self.xp_new += self.gain_xp #On gagne de l'xp !
        return self.reduc_mana,self.reduc_latence

class Skill_soin(Skill_intrasec):
    """Le skill équivalent au sort de soin supérieur. C'est un skill intrasec à la classe Ange.
       C'est un skill actif."""
    def __init__(self):
        Skill_intrasec.__init__(self)
        self.soin = 20 #La quantité de PV soignés par le skill
        self.portee = 0 #La portée du skill
        self.latence = 10
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.soin += 10
            self.portee += 1

    def utilise(self):
        self.xp_new += self.gain_xp #On gagne de l'xp !
        return self.latence,self.soin,self.portee

class Skill_regeneration_MP(Skill_intrasec):
    """Le skill équivalent au sort de régénration de MP. C'est un skill intrasec à la classe Ange.
       C'est un skill actif."""
    def __init__(self):
        Skill_intrasec.__init__(self)
        self.regen = 40 #La quantité de PM régénérés par le skill
        self.portee = 0 #La portée du skill
        self.latence = 10
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.regen += 5
            self.portee += 1

    def utilise(self):
        self.xp_new += self.gain_xp #On gagne de l'xp !
        return self.latence,self.regen,self.portee


class Skill_aura(Skill_intrasec): #Toutes les auras ne sont pas des skills intrasecs, mais par rapport aux méthodes c'est plus logique comme ça.
    """Offre un aura qui se matérialise autour de l'agissant. Les effets de l'aura diffèrent selon l'aura. Skill aura est une classe parente et ne doit pas être instanciée.
       Les auras sont des skills passifs, qui s'actionne à chaque tour."""
    def __init__(self,portee,effet):
        Skill_intrasec.__init__(self)
        self.portee = portee #La zone affectée par l'aura
        self.effet = effet #L'effet appliquée aux cases de la zone
        self.gain_xp = 0.1 #Il faut 100 tours pour augmenter le niveau d'un skill d'aura.

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.portee += 1 #On augmente la portée
            self.ameliore_effet() #On améliore l'effet. Chaque effet étant unique, l'amélioration aussi.
            self.niveau += 1

    def utilise(self):
        self.xp_new+=self.gain_xp
        return self.portee, self.effet

class Skill_aura_divine(Skill_aura):
    """Offre une aura divine qui soigne et boost les alliés et blesse les ennemis maléfique (élémentaux de l'ombre, nécromanciens, créatures réanimées, etc.). C'est un skill intrasec à la classe Ange.
       C'est un skill passif (appelé à chaque tour)."""
    def __init__(self):
        #effet = remplir cette ligne quand j'aurai créé les effets
        portee = 2
        Skill_aura.__init__(self,portee,effet)

    def ameliore_effet(self):
        #À remplir que j'aurai réfléchi aux effets
        pass

class Skill_boost_elementaliste(Skill_intrasec):
    """Un skill d'amélioration des effets de l'arbre élémental. Le boost est presque négligeable. C'est un skill intrasec à la classe Elémentaliste."""
    def __init__(self):
        Skill_intrasec.__init__(self)
        self.boost_portee_aura = 0 #Booster plutôt un caractère spécifique dans chaque aura ? Pour permettre de booster moins les auras. Une fois que j'aurais codé les effets.
        self.boost_affinites = 0 #On boost aussi les skills d'affinités.
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.boost_portee_aura += 1
            self.boost_affinites += 0.1 #Effet volontairement très faible.

    def utilise(self):
        self.xp_new+=self.gain_xp
        return self.boost_portee_aura,self.boost_affinites

class Skill_boost_elemental(Skill_intrasec):
    """Un skill d'amélioration de l'aura et de l'affinité élémentale. C'est un skill intrasec à la classe Elémental."""
    def __init__(self,element):
        Skill_intrasec.__init__(self)
        self.boost_portee_aura = 0 #Booster plutôt un caractère spécifique dans chaque aura ? Pour permettre de booster moins les auras. Une fois que j'aurais codé les effets. le paramètre element interviendra ici.
        self.boost_affinites = 0 #On boost aussi les skills d'affinités.
        self.element = element
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.boost_portee_aura += 1
            self.boost_affinites += 0.5 

    def utilise(self):
        self.xp_new+=self.gain_xp
        return self.boost_portee_aura,self.boost_affinites

class Skill_boost_magicien(Skill_intrasec):
    """Un skill d'amélioration des magies (hors enchantement), particulièrement les magies d'attaque. C'est un skill intrasec à la classe Magicien
       C'est un skill semi-passif (appelé à chaque fois qu'une magie est lancée (excepté les enchantements)."""
    def __init__(self):
        Skill_intrasec.__init__(self)
        self.boost_portee_sort = 0 #La portée des sorts à distance est boostée
        self.boost_zone_sort = 0 #La portée de la zone d'effets des sorts de zone est boostée
        self.taux_cout_sort = 1 #Le taux du coût normal d'un sort que l'utilisateur devra vraiment payer
        self.taux_latence_sort = 1 #Le taux de la latence normal d'un sort que l'utilisateur devra vraiment attendre
        #Les sorts d'attaque disposent d'un second boost :
        self.boost_portee_attaque = 0 #La portée des sorts d'attaque à distance est boostée
        self.boost_zone_attaque = 0 #La portée de la zone d'effets des sorts d'attaque de zone est boostée
        self.taux_cout_attaque = 1 #Le taux du coût normal d'un sort d'attaque que l'utilisateur devra vraiment payer
        self.taux_latence_attaque = 1 #Le taux de la latence normal d'un sort d'attaque que l'utilisateur devra vraiment attendre

        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1

            self.boost_portee_sort += 0.1
            self.boost_zone_sort += 0.1
            self.taux_cout_sort -= 0.05
            self.taux_latence_sort -= 0.05

            self.boost_portee_attaque += 0.1
            self.boost_zone_attaque += 0.1
            self.taux_cout_attaque -= 0.05
            self.taux_latence_attaque -=0.05

    def utilise(self,latence,cout,zone,portee,attaque=False):
        self.xp_new += self.gain_xp
        latence *= self.taux_latence_sort
        cout *= self.taux_cout_sort
        portee += self.boost_portee_sort
        zone += self.boost_zone_sort
        if attaque:
            self.xp_new += self.gain_xp
            latence *= self.taux_latence_attaque
            cout *= self.taux_cout_attaque
            portee += self.boost_portee_attaque
            zone += self.boost_zone_attaque
        return latence, cout, zone, portee

class Skill_boost_necromancien(Skill_intrasec):
    """Un skill d'amélioration des magies d'ombre (seul caractéristique commune à tous les nécromanciens). C'est un skill intrasec à la classe Nécromancien.
       C'est un skill semi-passif (appelé à chaque fois qu'une magie d'ombre est utilisée)."""
    def __init__(self):
        Skill_intrasec.__init__(self)
        self.boost_portee_sort = 0 #La portée des sorts d'ombre à distance est boostée
        self.boost_zone_sort = 0 #La portée de la zone d'effets des sorts d'ombre de zone est boostée
        self.taux_cout_sort = 1 #Le taux du coût normal d'un sort d'ombre que l'utilisateur devra vraiment payer
        self.taux_latence_sort = 1 #Le taux de la latence normal d'un sort d'ombre que l'utilisateur devra vraiment attendre

        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1

            self.boost_portee_sort += 0.08
            self.boost_zone_sort += 0.08
            self.taux_cout_sort -= 0.03
            self.taux_latence_sort -= 0.03

    def utilise(self,latence,cout,zone,portee):
        self.xp_new += self.gain_xp
        latence *= self.taux_latence_sort
        cout *= self.taux_cout_sort
        portee += self.boost_portee_sort
        zone += self.boost_zone_sort
        return latence, cout, portee, zone

class Skill_reanimation(Skill_intrasec):
    """Un skill qui premet de ramener les morts à la vie. Ce skill une version plus faible (sur un cadavre à la fois) du sort de réanimation de zone. Contrairement au sort de résurection, la cible ne revient pas à son état d'origine : seule une partie de sa vie lui est rendue, il obtient l'espèce mort_vivant et peut être conveti à la cause du nécromancien. C'est un skill intrasec à la classe Nécromancien."""
    def __init__(self):
        Skill_intrasec.__init__(self)
        self.taux_vie_rendue = 0.25 #Le taux appliqué aux PV max du cadavre réanimé pour calculer ses PV après réanimation
        self.superiorite = 10 #La priorité que le nécromancien doit avoir de plus que sa cible pour en faire un serviteur
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.taux_vie_rendue += 0.05
            self.superiorite -= 1

    def utilise(self):
        self.xp_new += self.xp
        return self.taux_vie_rendue, self.superiorite

class Skill_boost_maitre_de_la_mort(Skill_intrasec):
    """Un skill d'amélioration des magies d'ombre, de l'aura d'ombre, du sort de réanimation de masse, et du skill d'immortalité."""
    def __init__(self):
        Skill_intrasec.__init__(self)
        self.boost_portee_sort = 0 #La portée des sorts d'ombre à distance est boostée
        self.boost_zone_sort = 0 #La portée de la zone d'effets des sorts d'ombre de zone est boostée
        self.taux_cout_sort = 1 #Le taux du coût normal d'un sort d'ombre que l'utilisateur devra vraiment payer
        self.taux_latence_sort = 1 #Le taux de la latence normal d'un sort d'ombre que l'utilisateur devra vraiment attendre
        self.boost_portee_aura = 0 #Peut-être trouver autre chose que la portée à améliorer ?
        self.boost_portee_reanimation_de_masse = 0
        self.boost_priorite_reanimation = 0
        self.boost_coef_immortalite = 0 #On augmente le coef du skill immortalité qui indique quel portion de ses stats on garde quand on a - de 0 PV

        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1

            self.boost_portee_sort += 0.1
            self.boost_zone_sort += 0.1
            self.taux_cout_sort -= 0.05
            self.taux_latence_sort -= 0.05
            self.boost_portee_aura += 1
            self.boost_portee_reanimation_de_masse += 1
            self.boost_priorite_reanimation += 1
            self.boost_coef_immortalite += 0.05 #Quand l'immortalité et la classe mère de ce skill intrasec sont tous les deux au niveau 10, on garde 100% de ses stats peu importe les PV

    def utilise(self,latence,cout,zone,portee):
        self.xp_new += self.gain_xp
        latence *= self.taux_latence_sort
        cout *= self.taux_cout_sort
        portee += self.boost_portee_sort
        zone += self.boost_zone_sort
        return latence, cout, portee, zone, self.boost_portee_aura, self.boost_portee_reanimation_de_masse, self.boost_priorite_reanimation, self.boost_coef_immortalite #On peut appeler le skill plusieurs fois par tour, pour déclencher un gain d'xp à chaque fois.

class Skill_reanimation_renforcee(Skill_intrasec):
    """Un skill qui premet de ramener les morts à la vie. Ce skill une version plus faible (sur un cadavre à la fois) du sort de réanimation de zone. Contrairement au sort de résurection, la cible ne revient pas à son état d'origine : seule une partie de sa vie lui est rendue, il obtient l'espèce mort_vivant et peut être conveti à la cause du nécromancien. C'est un skill intrasec à la classe Maitre de la mort."""
    def __init__(self):
        Skill_intrasec.__init__(self)
        self.taux_vie_rendue = 0.75 #Le taux appliqué aux PV max du cadavre réanimé pour calculer ses PV après réanimation. On commence au taux maximum du skill de réanimation.
        self.superiorite = 0 #La priorité que le nécromancien doit avoir de plus que sa cible pour en faire un serviteur. On commence au taux maximum du skill de réanimation.
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.taux_vie_rendue += 0.025
            self.superiorite -= 1

    def utilise(self): #Ce skill remplace automatiquement (?) le skill de réanimation dans le skill clavier.
        self.xp_new += self.xp
        return self.taux_vie_rendue, self.superiorite

class Skill_boost_instakill(Skill_intrasec):
    """Un skill qui améliore les effets d'instakill. C'est un skill intrasec à la classe Assassin."""
    def __init__(self):
        Skill_intrasec.__init__(self)
        self.priorite_bonus = 0 #La priorite des effets d'instakill est boostée
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.priorite_bonus += 1

    def utilise(self):
        self.xp_new += self.gain_xp
        return self.priorite_bonus

class Skill_boost_vol(Skill_intrasec):
    """Un skill qui boost les performances des skills de vol. C'est un skill intrasec à la classe Voleur."""
    def __init__(self):
        Skill_intrasec.__init__(self)
        self.priorite_bonus = 0 #La priorite des skills de vol est boostée
        self.gain_xp = 0.1

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.priorite_bonus += 1

    def utilise(self):
        self.xp_new += self.gain_xp
        return self.priorite_bonus
