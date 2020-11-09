import pygame

def trouve_skill(classe,type_skill): #Vraiment une méthode propre au controleur ?
    trouve = None
    for skill in classe.skills:
        if isinstance(skill,type_skill) and skill.niveau > 0: #On ne devrait pas avoir de skill a 0 mais on ne sait jamais.
            trouve = skill
    for skill in classe.skills_intrasecs:
        if isinstance(skill,type_skill) and skill.niveau > 0: #On ne devrait pas avoir de skill a 0 mais on ne sait jamais.
            trouve = skill
    if trouve == None:
        for sous_classe in classe.sous_classes: #On récurse la recherche dans les sous-classes.
            trouve_bis = trouve_skill(sous_classe,type_skill)
            if trouve_bis != None:
                trouve = trouve_bis
    return trouve

#Constantes d'équilibrage :
global constantes_lab
constantes_lab = {0:0.1}

global ID_MAX
ID_MAX = 1 #L'ID de la dernière entitée crée.

#constantes
global HAUT
HAUT=0
global DROITE
DROITE=1
global BAS
BAS=2
global GAUCHE
GAUCHE=3


global MUR_VIDE
MUR_VIDE=0
global MUR_PLEIN
MUR_PLEIN=1
global INTOUCHABLE
INTOUCHABLE=2

global PORTE_FERMEE
PORTE_FERMEE=0
global PORTE_OUVERTE
PORTE_OUVERTE=1

global Potion

global FENETRE_X
FENETRE_X = 600
global FENETRE_Y
FENETRE_Y = 600

global malchance_forcee
malchance_forcee = False

global voir_tout
voir_tout = 0
global parcours_en_profondeur
parcours_en_profondeur = 1
global aveugle
aveugle = 2
global distance_max
distance_max = 3

global passage
passage = 1


global BEGINNER
BEGINNER = 0
global EASY
EASY = 1
global AVERAGE
AVERAGE = 2
global HARD
HARD = 3
global INSANE
INSANE = 4
global IMPOSSIBLE
IMPOSSIBLE = 5


global BOUGER
BOUGER = 0
global ATTAQUER
ATTAQUER = 1
global PARLER
PARLER = 2
global INTERAGIR
INTERAGIR = 3
global CONSULTER_MINIMAP
CONSULTER_MINIMAP = 4
global CONSULTER_INVENTAIRE
CONSULTER_INVENTAIRE = 5
global PRECISION
PRECISION = 6
global POSTCISION
POSTCISION = 7
global RETOUR
RETOUR = 8
global BOUGER_MINIMAP
BOUGER_MINIMAP = 9
global BOUGER_INVENTAIRE
BOUGER_INVENTAIRE = 10
global UTILISER
UTILISER = 11
global AIDER
AIDER = 12


global ARRIVEE
ARRIVEE=(30, 144, 255)

global LABYRINTHE
LABYRINTHE=0
global MINIMAP
MINIMAP=1
global INVENTAIRE_
INVENTAIRE_=2
global DIALOGUE
DIALOGUE=3
global ITEM
ITEM=4

global LIGHT
LIGHT = 0
global HEAVY
HEAVY = 1


global sauvegarde
sauvegarde = "save.p"

global TAILLE_FIXE
TAILLE_FIXE = False
global taille_fixe
taille_fixe = 10

global SCREEN

#À supprimer ?
global LAB
global JOUEUR
global AGISSANTS
global ITEMS

global BIENFAIT
BIENFAIT = 0
global DELIT
DELIT = 1
global CRIME
CRIME = 2

global MORT
MORT = 0
global VIVANT
VIVANT = 1

global TERRE
TERRE = 0
global FEU
FEU = 1
global GLACE
GLACE = 2
global OMBRE
OMBRE = 3

#Les positions possibles du curseur :
global RECTANGLE_G #Le rectangle gauche de l'affichage
RECTANGLE_G = 0
global CARRE #Le carré au centre de l'affichage, correspond à la vue du joueur, elle a son propre sous-curseur
CARRE = 1
global RECTANGLE_D #Le rectangle droit de l'affichage
RECTANGLE_D = 2

#Dans le rectangle gauche :
global INVENTAIRE #L'inventaire contient la liste des possessions du joueur, il a son propre sous-curseur
INVENTAIRE = 0
global SKILLS #Les skills tels que décrits par la classe principale du joueur, ils ont leur propre sous-curseur
SKILLS = 1
global STATS #Les stats du joueur
STATS = 2

#Dans les stats du joueur :
global VIE #Les informations sur la vie du joueur
VIE = 0
global MANA #Les informations sur le mana du joueur
MANA = 1
global PRIORITE #Les informations sur la priorite du joueur (visible à partir d'un certain niveau d'observation)
PRIORITE = 2
global IDENTIFIANT #Les informations sur la vie du joueur (visible à partir d'un certain niveau d'observation)
IDENTIFIANT = 3

#Dans les informations sur la vie du joueur :
global TITRE #Le titre devant la barre de vie
TITRE = 0
global BARRE #La barre de vie
BARRE = 1
global MIN #Le 0 de la barre de vie (visible à partir d'un certain niveau d'observation)
MIN = 2
global VAL #La valeur de la partie pleine de la barre de vie (visible à partir d'un certain niveau d'observation)
VAL = 3
global MAX #La valeur maximal que peut atteindre naturellement la barre de vie (visible à partir d'un certain niveau d'observation)
MAX = 4

#Les informations sur le mana du joueur sont indentiques aux informations sur la vie du joueur, mais si le joueur a des réserves de magies, un curseur indique la limite haute de quelle réserve est observée (0 pour la réserve naturelle) et quelle barre est observée (0 pour la réserve naturelle)
#Les informations sur la priorité et l'identifiant du joueur sont de la forme titre et val, uniquement.

#Dans le rectangle droit :
#Le rectangle droit peut contenir les informations d'un agissant séléctionné dans la vue (visible à partir d'un certain niveau d'observation, auquel cas le curseur est comme précédemment
#Le rectangle droit peut contenir les informations d'un item séléctionné dans un inventaire (celui du joueur ou d'un agissant observé dans la vue) :
global NOM #Les informations sur le nom de l'item
NOM = 0
#Dans le cas d'une potion, on observera aussi l'effet :
global EFFET #Les informations sur l'effet de la potion
EFFET = 1
#Dans le cas d'un parchemin, il y aura aussi une information sur le cout d'utilisation :
global COUT #Les informations sur le cout du parchemin
COUT = 2
#Dans le cas d'un 
