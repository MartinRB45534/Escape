Work in progress !

Pour les garder les plus léger possible, on va demander aux esprits de ne pas manipuler d'objets (dans la mesure du raisonable).
Leurs informations seront de la forme :
[[[[(k,j,i),clarte,duree,distance,distance_bis,code,[etat_haut,etat_droite,etat_bas,etat_gauche],[ID_entitee,ID_entitee,ID_entitee]]]for i in range (largeur_lab)]for j in range (hauteur_lab)]for k in range (nombre_lab)]
avec :
   - (k,j,i) la position de la case
   - clarte sa clarté dans la vision des corps de l'esprit
   - distance pour indiquer le chemin vers les cibles
   - distance_bis pour le chemin en cas d'obstacles
   - code pour représenter numériquement l'état de la case (pas grand_chose à savoir pour la plupart des gens)
   - [etat_haut,etat_droite,etat_bas,etat_gauche] des booléens pour représenter l'état des murs
   - ID_entitee les ID des entitées vues