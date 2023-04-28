# Master-mind_12
projet master mind 

Biologie - Informatique 
TD 4

Lima-Pinto Jessica
Petit Nina
Kedir-Gegsa Firdos
Faradna Alissar

https://github.com/uvsq22200131/Master-mind_12-main.git

info supplémentaire : tout le monde n'a pas réussi à commit 


Répartition des tâches :
Nina -->    création fenêtre racine et boutons + accès à la fenetre de chaque mode, création du menu (a propos, préférences, timer), fonctions qui appliquent les préférences et timer, fonction pour sauvegarder la partie


Jessica -->  Création de toute les interphases graphiques, du mode 2 jouers, 1joueurs + interphases win et lost. Création des canvas et des grilles des grands cercles et petits cercles qui ce trouve dans les canvas , importation des images et modification via picsart (pour séparer chaque boutons), utilisation du module Pillow pour pouvoir afficher les images, png importer depuis : https://fr.pngtree.com/free-png-vectors/bouton

lien des boutons : https://fr.pngtree.com/freepng/stereo-macaron-button-material_4743390.html

lien confettis : https://fr.pngtree.com/freepng/birthday-cap-with-confetti-and-serpentine-explosion-celebration-vector_5574624.html

lien png qui s'aafiche dans la fenetre perdu :https://fr.pngtree.com/freepng/it-s-in-the-crying-cartoon-character-illustration-cant-grab-the-red-envelope-sad_3845898.html


Firdos --> Création du mode 1 joueurs et 2 joueurs qui inclue les fonction suivante : 
- creer_combinaison_secrete(code secret aléatoire) 
- get_couleur() et get_couleur2(insérer le code secret dans le mode 2 joueurs)
- comparer_combinaison(), comparer_combinaison2()
- comparer_combinaison2()
- supprimer()
- fonctionvalider1()
- fonctionvalider()
- fonctionvalider2()

Alisar --> essai code 2 joueur




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
création de toute les interphases graphique 

Etape 6 : 
code du jeu du mode 1 joueurs et 2 joueur




En plus :
- pouvoir sauvegarder la partie
- pouvoir revenir en arrière 
- proposer une aide fournissant un code compatible avec les informations obtenues aux essais précédents (sans utiliser le code secret!)

Pour aller plus loin :
- pouvoir modifier les principaux paramètres du jeux (nbr pions, nbr couleurs, nbr essais)
- programmer un mode sans joueur, dans lequel le code à chercher est choisi au hasard comme dans le mode à 1 joueur, puis une intelligence artificielle (IA) joue à la place du joueur qui décode
- créer un timer










Nina :
- création de la fenètre racine
- création de 3 boutons sur celle-ci pour accéder au mode 1 et 2 joueurs et au mode préférence
- création des fonction spermettant d'afficher le plateu de jeu lorsqu'on clique sur un des boutons des modes de jeu
- création du menu de jeu contenant les règles du jeu dans "à propos", les paramètres de jeu mofifiables selon nos envies dans "préférences", et enfin l'ajout d'un timer qui permettra de savoir en combien de temps le code secret a été trouver 
"préférence", "ajouter un timer" et "à propos" renvoient chacun à une fonction
Le mode 1 et 2 joueurs ne contiennet que "à propos" et "ajouter un timer" dans le menu
pour la fonction préférénce ("preferencebouton1 (ou 2)) : Cette fonction permet de choisir le nombre de pions souhaité (= taille du code secret), le nombre de couleurs disponibles et le nombre d'essais possibles pour trouver le code secret. De plus, le bouton "appliquer" est crée qui renvoie à une fonction permettant d'appliquer tous ses paramètres : "appliquerparametres1 (ou 2)". 
La fonction "appliquerparamètres" renvoie à d'autres fonctions, selon les valeurs de paramètres choisis. 
Les valeurs des combobox ont du être appeler grace à .get, puis transformées en nombre entier grace à "int" afin d'être utilisables. 
les variables des préférences ont été définies plus tôt 
essai précédent : 
def appliquerparametres2 (master_mind) :
    if labelpreference4 == 3 :
        canvascs.delete(cercle4) 
    elif labelpreference4 == 5 :
        cercle5 = canvascs.create_oval (210, 10, 240, 40)
    elif labelpreference4 == 6 :
        cercle5 = canvascs.create_oval (210, 10, 240, 40)
        cercle6 = canvascs.create_oval (10, 10, 40, 40)
    elif labelpreference4 == 7 :
        cercle5 = canvascs.create_oval (210, 10, 240, 40)
        cercle6 = canvascs.create_oval (10, 10, 40, 40)
        cercle7 = canvascs.create_oval (240, 10, 270, 40)
    elif labelpreference4 == 8 :
        cercle5 = canvascs.create_oval (210, 10, 240, 40)
        cercle6 = canvascs.create_oval (10, 10, 40, 40)
        cercle7 = canvascs.create_oval (240, 10, 270, 40)
        cercle8 = canvascs.create_oval (280, 10, 300, 40)
    .... pareil pour les autres Combobox

- création du timer ---- plusieurs tentatives, mais pas concluantes 
- création du bouton permettant la sauvegarde de la partie ---- pas aboutit


Notre code : 
ajouter "cd Mastermind" dans le terminal pour appeller les boutons  
- création fenetre racine 
    * titre, taille, background...
    * ajout de labels 
    * ajout de trois boutons : 1 bouton pour chacun des modes 
  
- code du mode 1 joueur et 2 joueurs 
    * def cree_combinaison_secrete : pour le mode 1 joueur 
    * def get_couleur : mode 1 et 2 joueurs 
    * def get_couleur2 : code secret du mode 2 joueur
    * def comparer_combinaison
    * def fonction_valider : pour le mode 1 joueur 
    * def fonctionvalider2 : pour le mode 2 joueur

- création mode 1 joueur 
    * def bouton1fonction 
            ° création de la fenetre
            ° création du menu : "à propos" et "timer" (non fonctionnel)
            ° bontons validé/supprimer/quitter
            ° création ligne du bas/ du haut pour le plateau de jeu 
            ° création frame te boutons de couleurs (ouvrir les images, les redimmensionner...)
            ° mainloop
    * def aproposbouton_mode1
    * def sauvegarderjeu
    * def timer
    * création bouton1

- création mode 2 joueur 
    * def bouton2fonction 
            ° création de la fenetre
            ° création du menu : "à propos" et "timer" (non fonctionnel)
            ° bontons validé/supprimer/quitter
            ° création ligne du bas/ du haut pour le plateau de jeu 
            ° création frame te boutons de couleurs (ouvrir les images, les redimmensionner...)
            ° canva de la grille de jeu
            ° création des pions rouges et noirs
            ° appelle def code_secret   = fonction pour choisir le code secret
            ° mainloop
    * def code_secret
        ° création fenetre 
        ° labels et placement des labels
        ° bouton valider
        ° création canvas cercles (4)
        ° ouvrir + redimenssionner les images 
        ° mainloop
    * def aproposbouton_mode2
    * def sauvegarderjeu
    * def timer
    * bouton mode 2 joueur

- création du mode préférence 
    * variables paramètres 
    * def bouton3fonction (fonction{})
            ° création de la fenetre
            ° création du menu : "à propos" et "timer" (non fonctionnel), "préférences
            ° bontons validé/supprimer/quitter
            ° création ligne du bas/ du haut pour le plateau de jeu 
            ° création canva qui va révéler le code secret
            ° création frame te boutons de couleurs (ouvrir les images, les redimmensionner...)
            ° if fonction == {}
                    appliquer_parametres ()
              else : 
                    fonction ()
            ° mainloop
    * def timer 
    * def sauvegarder
    * def preferencebouton
        ° création fenetre pour choisir les préférences 
        ° création de 3 combobox : choix du nombre de pions = taille du code secret, choix du nombre de couleur à disposition, choix du nombre d'essai possible 
        ° création bouton appliquer qui appelle la fonction appliquerparametres
    * def appliquerparametres = renvoie à une fonction différente selon les paramètres qu'on choisi
        1- choix nombre de pions : if/else + master_mind.destroy()
                    récupération de la valeur choisie dans la combobox associée
                    Exemple : si le nombre de pions choisi est 3, cela renvoie à la fonction cercletrois
                    si le nombre de pions choisi est 4,cela rencoie à la fonction cerquatre (qui crée un quatrième cercle) qui elle même renvoie à la fonction cercletrois (ou les 3 premiers cercles on déjà été crées)
        2- choix couleur : if/else + master_mind.destroy()
                    récupération de la valeur choisie dans la combobox associée 
                    Exemple : si le nombre de couleur choisi est 4, cela renvoie à la fonction nbrcouleur4
                    si le nombre de couleur choisi est 5, cela renvoie à la fonction nbrcouleur5 (ou une quatrième couleur est ajouté) qui elle même renvoie à la fonction nbrcouleur4 sur laquelle les 4 premières couleur ont déjà été placés 
        3- choix du nombre d'essai : if/else 
                    récupération de la valeur choisie dans la combobox associée
                    Exemple : si le nombre d'essai choisi est 7, cela appelle la fonction ligne7
                    cette fonction ligne7 appelle esnsuite une fonction différente en fonction du nombre de pions choisi afin que le nombre de pions des essais soit le même que le nombre de pion du code secret
                    ligne7 appelle également les fonctions qui lui sont antérieurs (ligne1/2/3/4/5/6)
    * def cercletrois
        ° défintion de 3 cercles 
    * def cerclequatre/def cerclecinq/defcerclesix
        ° renvoient à la fonction précédente ; + 1 cercle pour chaqu fonction
    * def ligne1
        ° création de la grille 
        ° if/else : appelle une fonction différente en fonction du nombre de pions choisi
    * def ovalsligne1_pions3
    * def ovalsligne1_pions4
    * def ovalsligne1_pions5
    * def ovalsligne1_pions6
    * def ligne2/3/4/5/6/7/8/9/10 
        ° même fonctionnement que ligne1, mais chaque fonction appelle sa précédente
    * def nbrcouleur4
        ° création frame 
        ° ouvrir + redimenssionner les images 
        ° création 4 boutons de couleur 
    * def nbrcouleur5/6/7/8 
        ° chaque fonctiona appelle sa précédente 
        ° + 1 couleur à chaque fois
    * def aproposbouton
    * création bouton3
 Note : nous n'avons réussi à régler le problème des boutons. En effet, cela ne s'affichent pas malgré nos tentatives. Une fois ce problème réglé nous aurions relier ce mode à un code ressemblant au code de jeu du mode 1 joueur. 

* racine.mainloop()


Sources : 
cours 
fonction sauvegarder et recharger la partie : internet
