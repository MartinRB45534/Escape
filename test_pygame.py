import pygame
from Niveau import *
from Constantes import *

difficulté = HARD
#mode affichage peut valoir voir_tout, parcours_en_profondeur ou aveugle. A gérer dans le menu ?
mode_affichage = parcours_en_profondeur

niv = Niveau(difficulté,mode_affichage)
niv.run()
