# Master-mind_12
projet master mind 

Biologie - Informatique 
TD 4

Lima-Pinto Jessica
Petit Nina
Kedir-Gegsa Firdos
Faradna Alissar

https://github.com/uvsq22200131/Master-mind_12-main.git




Etape 1 :
création fenêtre racine
fenetre racine doit se fermer quand on clique sur un des deux boutons

Etape 2 :
création bouton "mode 1 joueur" et bouton "mode 2 joueurs"

Etape 3 :
création de la fonction pour accéder à l'interface graphique du mode choisi

Etape 4 : 
création d'un menu qui comprend :
- "a propos" = règles du jeu
- "préférences" = paramètres du jeu  --> création fonction pour appliquer les paramètres
- "ajouter un timer"   (idée bonus)

Etape 5 : 
création du plateau de jeu 

Etape 6 : 
code du jeu




En plus :
- pouvoir sauvegarder la partie
- pouvoir revenir en arrière 
- proposer une aide fournissant un code compatible avec les informations obtenues aux essais précédents (sans utiliser le code secret!)

Pour aller plus loin :
- pouvoir modifier les principaux paramètres du jeux (nbr pions, nbr couleurs, nbr essais)
- programmer un mode sans joueur, dans lequel le code à chercher est choisi au hasard comme dans le mode à 1 joueur, puis une intelligence artificielle (IA) joue à la place du joueur qui décode
- créer un timer




Répartition des tâches :
Nina -->    création fenêtre racine et boutons + accès à la fenetre de chaque mode, création du menu (a propos, préférences, timer), fonctions qui appliquent les préférences et timer, fonction pour sauvegarder la partie, fonction pour revenir en arrière
Jessica -->   création du plateau de jeu et des pions 
Firdos -->      début du code de jeu mode 1 joueur
Alisar -->      début code de jeu mode 2 joueur





Nina :
- création de la fenètre racine
- création de 2 boutons sur celle-ci pour accéder au mode 1 et 2 joueurs 
- création des fonction spermettant d'afficher le plateu de jeu lorsqu'on clique sur un des boutons des modes de jeu
- création du menu de jeu contenant les règles du jeu dans "à propos", les paramètres de jeu mofifiables selon nos envies dans "préférences", et enfin l'ajout d'un timer qui permettra de savoir en combien de temps le code secret a été trouver 
"préférence", "ajouter un timer" et "à propos" renvoient chacun à une fonction
pour la fonction préférénce ("preferencebouton1 (ou 2)) : Cette fonction permet de choisir le nombre de pions souhaité (= taille du code secret), le nombre de couleurs disponibles et le nombre d'essais possibles pour trouver le code secret. De plus, le bouton "appliquer" est crée qui renvoie à une fonction permettant d'appliquer tous ses paramètres : "appliquerparametres1 (ou 2)". 
La fonction "appliquerparamètres" renvoie à d'autres fonctions, selon les valeurs de paramètres choisis. 
Les valeurs des combobox ont du être appeler grace à .get, puis transformées en nombre entier grace à "int" afin d'être utilisables. 
les variables des préférences ont été définies plus tôt 
essai précédent : 
def appliquerparametres2 (master_mind) :
    if labelpreference4 == 3 :
        canvascs.delete(cercle4) 
    if labelpreference4 == 5 :
        cercle5 = canvascs.create_oval (210, 10, 240, 40)
    if labelpreference4 == 6 :
        cercle5 = canvascs.create_oval (210, 10, 240, 40)
        cercle6 = canvascs.create_oval (10, 10, 40, 40)
    if labelpreference4 == 7 :
        cercle5 = canvascs.create_oval (210, 10, 240, 40)
        cercle6 = canvascs.create_oval (10, 10, 40, 40)
        cercle7 = canvascs.create_oval (240, 10, 270, 40)
    if labelpreference4 == 8 :
        cercle5 = canvascs.create_oval (210, 10, 240, 40)
        cercle6 = canvascs.create_oval (10, 10, 40, 40)
        cercle7 = canvascs.create_oval (240, 10, 270, 40)
        cercle8 = canvascs.create_oval (280, 10, 300, 40)

- création du timer
- création du bouton permettant la sauvegarde de la partie 






A faire :
Ajouter docstring pour fonctions
demander à jessica pour que "choisir le code secret" passe au dessu du canva
voir pour espacer cercle 6, 7, 8
