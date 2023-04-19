
from tkinter import CENTER, RIGHT, Frame, Label, Menu, Tk, Toplevel, ttk, Canvas, Button
import tkinter
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
import random


# Paramètres fenetre racine
racine = Tk()    # création de la fenetre racine
racine.geometry("600x600")    # régler la taille de la fenetre
racine.title("Mastermind")     # nom fenetre
racine["bg"] = 'pink3'      # couleur arrière plan 
racine.resizable(height=False, width=False)   # = fenetre pas redimensionnable dans longeur et largeur, figer les dimenssions

label = Label(racine, text="Bienvenue", fg = ("black"), bg=("pink3"), font =("helvetica", "25"))
label.pack(side="top")

label1 = Label(racine, text="Choisissez un mode de jeu", fg = ("black"), bg=("pink3"), font =("helvetica", "25"))
label1.place(x='150', y='220')
M = Label(racine, text='sur le jeu Mastermind',bg=('pink3'),font='20')
M.place(x = 230, y=50)



# CREATION BOUTON 
nombrepions = ["3", "4", "5", "6", "7", "8"]
nombrecouleurs = ["4", "5", "6", "7", "8"]
nombreessai = ["6", "7", "8", "9", "10", "15", "20"]

combinaison_max=4
combinaison_secrete=[]
def creer_combinaison_secrete():
    combinaison_secrete=""
    for i in range(0,combinaison_max):
        couleurs=["rose","bleu","jaune","orange","turquoise", "violet","bleuciel","rouge"]
        index=random.randint(0,len(couleurs)-1)
        combinaison_secrete=combinaison_secrete+couleurs[index]#je ne comprends pas
    return combinaison_secrete
a=creer_combinaison_secrete()
combinaison=a
L=[]
#global cpt

def get_couleur(couleur, master_mind, image):
    if len(L)>=combinaison_max:
        Labelcouleur=Label(master_mind, text="tu as dépassé le nombre max")
        Labelcouleur.place(x=20, y=20)
    else:
        L.append(couleur)
        cpt=len(L)-1
        label_image = Label(master_mind, image=image)
        label_image.grid(row=0, column=cpt)
        cpt+=1
    print(L) 





longueur_combinaison=4
def comparer_combinaison(combinaison_entree, combinaison_secrete, master_mind):
    nb_couleurs_bien_placees=0
    nb_couleurs_mal_placees=0
    for i in range (longueur_combinaison):
        if combinaison_entree[i]==combinaison_secrete[i]:
            nb_couleurs_bien_placees+=1
        elif combinaison_entree[i] in combinaison_secrete:
            nb_couleurs_mal_placees+=1
            Labelperdue=Label(master_mind, text="recommence ce n'est pas sa")
            Labelperdue.place(x=50, y=20)
            nb_max_tentatives=0
            nb_max_tentatives+=1
    return (nb_couleurs_bien_placees, nb_couleurs_mal_placees)

# Fonction bouton 1
def bouton1fonction ():  
    """Création de la fonction permettant l'affichage du plateau de jeu lorsqu'on 
        clique sur le bouton du mode 1 joueur""" 
    master_mind=Toplevel(racine)
    master_mind.geometry("450x660")#taille de la fenetre
    master_mind.title("Master mind mode 1 joueurs")#titre de la fenetre 
    master_mind.resizable(height=False, width=False)   # On peut l'enlever nan ?????
    palette = Label(master_mind, text='palette de couleurs :') 
    c = Label(master_mind, text='trouver le code ')
    s = Label(master_mind,text='secret ;)')

    # Création Menu
    bouton1_menu = Menu(master_mind)               
    master_mind['menu'] = bouton1_menu
    main_cascade = Menu(bouton1_menu)
    bouton1_menu.add_cascade(label='Menu', menu = main_cascade)
    main_cascade.add_command(label='Préférences', command = preferencebouton1)
    main_cascade.add_separator()
    main_cascade.add_separator()
    main_cascade.add_command(label='À propos', command = aproposbouton1)
    main_cascade.add_separator()
    main_cascade.add_separator()
    main_cascade.add_command(label='Ajouter un timer', command = timerbouton1)

    #création du bouton validé, supprimer et quitter 
    bvalide = Button(master_mind,text = 'Validé', height=1, width=8, command=lambda:comparer_combinaison(L,combinaison,master_mind))
    bsupprimer = Button(master_mind,text = 'Supprimer',height=1, width=8)
    bquitter = Button(master_mind,text = 'Quitter',height=1, width=8,command=master_mind.destroy)
    bsauvegarder = Button(master_mind,text = 'Sauvegarder', height=1, width=8, command = sauvegarderjeu)
    
    #placement des boutons validé,supprimer,quitter et le label code
    bvalide.place(x = 175, y = 585)
    bsupprimer.place(x =50, y = 585)
    bquitter.place(x = 300, y = 585)
    bsauvegarder.place(x =175, y=620)
    c.place(x= 5, y=5)
    s.place(x=20, y=23)

    #création de la ligne du bas
    ligne1=Canvas(master_mind,width=400, height=30)#largeur et hauteur du canvas 
    a=(0, 30)
    b=(400,30)
    ligne1.create_line(a, b)
    ligne1.place(x = 20, y = 470)#placer le canvas

    

    

    #creation de la frame et des boutons de couleurs 
    frameb1 = Frame(master_mind, width=400, height=600, borderwidth=2)
    frameb1.place(x= 60, y=535)

    #ouvrir les images 
    img = Image.open('boutonrose.PNG')
    img1 = Image.open('boutonviolet.PNG')
    img2 = Image.open('boutonbleuf.PNG')
    img3 = Image.open('boutonbleuciel.PNG')
    img4 = Image.open('boutonturquoise.PNG')
    img5 = Image.open('boutonjeune.PNG')
    img6 = Image.open('boutonorange1.PNG')
    img7 = Image.open('boutonrouge.PNG')

    #redimentionner les images
    taille0= img.resize((35,35))
    a = ImageTk.PhotoImage(taille0)

    taille1 = img1.resize((35,35))
    b = ImageTk.PhotoImage(taille1)

    taille2 = img2.resize((35,35))
    c = ImageTk.PhotoImage(taille2)

    taille3 = img3.resize((35,35))
    d = ImageTk.PhotoImage(taille3)

    taille4 = img4.resize((35,35))
    e = ImageTk.PhotoImage(taille4)

    taille5 = img5.resize((35,35))
    f = ImageTk.PhotoImage(taille5)

    taille6 = img6.resize((35,35))
    g = ImageTk.PhotoImage(taille6)

    taille7 = img7.resize((35,35))
    h = ImageTk.PhotoImage(taille7)

    #boutons
    B0 = Button(frameb1, image=a, command=lambda: get_couleur("rose",master_mind,a))
    B1 = Button(frameb1, image=b, command=lambda: get_couleur("violet",master_mind,b))
    B2 = Button(frameb1, image=c, command=lambda: get_couleur("bleu", master_mind,c))
    B3 = Button(frameb1, image=d, command=lambda: get_couleur("bleuciel",master_mind,d))
    B4 = Button(frameb1, image=e,command=lambda: get_couleur("turquoise",master_mind,e))
    B5 = Button(frameb1, image=f,command=lambda: get_couleur("jaune",master_mind,f))
    B6 = Button(frameb1, image=g,command=lambda: get_couleur("orange",master_mind,g))
    B7 = Button(frameb1, image=h,command=lambda: get_couleur("rouge",master_mind,h))

    #affichage des boutons
    B0.grid()
    B1.grid(row =0, column=1)
    B2.grid(row =0,column=2)
    B3.grid(row =0,column=3)
    B4.grid(row =0,column=4)
    B5.grid(row =0,column=5)
    B6.grid(row =0,column=6)
    B7.grid(row =0,column=7)
    palette.place(x=170, y=509)

    

    master_mind.mainloop()


def preferencebouton1 () :
    """Création de la fonction permettant de choisir les préférences du jeu, c'est à dire :
    - la taille du code secret (nombre de pion)
    - le nombre de couleurs
    - le nombre d'essai afin de trouver le code secret"""
    preference = Toplevel(bouton1)
    preference.title ("Préferences")
    preference.geometry ("300x300")
    labelpreference1 = Label (preference, text = 'Choississez un nombre de pions', fg = ('black'), font = ('helvetica', '10'))
    labelpreference1.pack(side ='top')
    listeCombo1 = ttk.Combobox (preference, values = nombrepions)
    listeCombo1.pack()
    labelpreference2 = Label (preference, text = 'Choississez un nombre de couleurs', fg = ('black'), font = ('helvetica', '10'))
    labelpreference2.pack(side = 'top')
    listeCombo2 = ttk.Combobox (preference, values = nombrecouleurs)
    listeCombo2.pack()
    labelpreference3 = Label (preference, text = "Choississez un nombre d' esssai", fg = ('black'), font = ('helvetica', '10'))
    labelpreference3.pack(side = 'top')
    listeCombo3 = ttk.Combobox (preference, values = nombreessai)
    listeCombo3.pack()
    appliquer = tkinter.Button (preference, text="Appliquer", fg = ("black"), font =("helvetica", "10"), command = appliquerparametres1)
    appliquer.pack(side = "bottom")
    

def aproposbouton1 () : 
    """Création de la fonction permettant d'afficher les règles du jeu"""  
    showinfo ('À propos',
             message = "Bienvenue dans Mastermind.\n\n"
                     "Ce jeu consiste à trouver un code secret composé de plusieurs couleurs, sachant que "
                     "chaque couleur peut apparaître plusieurs fois.\n\n"
                     "Vous pouvez configurer le nombre de couleurs différentes, la taille du code secret "
                     "et le nombre de tentatives que vous pouvez effectuer dans le menu Préférences.")
    

def appliquerparametres1 () : 
    print ("boujour")


def timerbouton1 () :
    print ('Bonjour')     
    

def sauvegarderjeu () :
    print ("bonjour")


# Bouton mode 1 joueur 
bouton1 = tkinter.Button(racine, text = 'mode 1 joueur', bd = '5', command=bouton1fonction)
bouton1.pack(side = 'left', fill='x', expand = True)            # .pack = pour afficher le bouton       SAVOIR EXPLIQUER LE RESTE 




# Fonction bouton 2 
def bouton2fonction (fonction={}) :
    """Création de la fonction permettant l'affichage du plateau de jeu lorsqu'on 
    clique sur le bouton du mode 2 joueur"""  
    global master_mind
    master_mind=Toplevel(racine)
    master_mind.geometry("450x660")#taille de la fenetre
    master_mind.title("Master mind mode 2 joueurs")#titre de la fenetre 
    palette = Label(master_mind, text='palette de couleurs :')
    master_mind.resizable(height=False, width=False)
    c = Label(master_mind, text='trouver le code ')
    s = Label(master_mind,text='secret ;)') 
    
    # Création Menu
    bouton2_menu = Menu(master_mind)               
    master_mind['menu'] = bouton2_menu
    main_cascade = Menu(bouton2_menu)
    bouton2_menu.add_cascade(label='Menu', menu = main_cascade)
    main_cascade.add_command(label='Préférences', command = preferencebouton2)
    main_cascade.add_separator()
    main_cascade.add_separator()
    main_cascade.add_command(label='À propos', command = aproposbouton2)
    main_cascade.add_separator()
    main_cascade.add_separator()
    main_cascade.add_command(label='Ajouter un timer', command = timerbouton2)

    # label 1 à 10
    l1= Label(master_mind, text='1.')
    l2= Label(master_mind, text='2.')
    l3= Label(master_mind, text='3.')
    l4= Label(master_mind, text='4.')
    l5= Label(master_mind, text='5.')
    l6= Label(master_mind, text='6.')
    l7= Label(master_mind, text='7.')
    l8= Label(master_mind, text='8.')
    l9= Label(master_mind, text='9.')
    l10= Label(master_mind, text='10.')

    #création du bouton validé,supprimer et quitter
    bvalide = Button(master_mind,text = 'Validé', height=1, width=8)
    bsupprimer = Button(master_mind,text = 'Supprimer',height=1, width=8)
    bquitter = Button(master_mind,text = 'Quitter',height=1, width=8,command=master_mind.destroy)
    bsauvegarder = Button(master_mind,text= 'Sauvegarder', height=1, width=8, command = sauvegarderjeu)
    
    #placement des boutons validé,supprimer,quiter + label
    bvalide.place(x = 175, y = 585)
    bsupprimer.place(x =50, y = 585)
    bquitter.place(x = 300, y = 585)
    bsauvegarder.place(x =175, y=620)
    c.place(x= 5, y=5)
    s.place(x=20, y=23)

    #placement label 1 à 10
    l1.place(x = 35, y = 85)
    l2.place(x = 35, y = 125)
    l3.place(x = 35, y = 170)
    l4.place(x = 35, y = 210)
    l5.place(x = 35, y = 250)
    l6.place(x = 35, y = 292)
    l7.place(x = 35, y = 330)
    l8.place(x = 35, y = 370)
    l9.place(x = 35, y = 410)
    l10.place(x = 30, y = 447)
    
    
    #création du canvas qui va révéler le code secret  
    global canvascs
    canvascs = Canvas(master_mind,width = 300, height = 40)
    canvascs.place(x = 70, y= 8)

    if fonction == {}:                         #fonction prend en paramètre un élément
        cerclequatre()                          # si le paramètre est vide, ca appaelle donc la fonction de base qui est cercle4
    else:
        fonction()                          #si pas de paramètres, ca appelle la fonction 


    #création de la ligne du bas
    ligne1=Canvas(master_mind,width=400, height=30)#largeur et hauteur du canvas 
    a=(0, 30)
    b=(400,30)
    ligne1.create_line(a, b)
    ligne1.place(x = 20, y = 480)#placer le canvas

    #création de la ligne du haut
    ligne1=Canvas(master_mind,width=400, height=1,bg='black')#largeur et hauteur du canvas 
    a=(0, 30)
    b=(400,30)
    ligne1.create_line(a, b)
    ligne1.place(x = 20, y = 50)

    #creation de la frame et des boutons de couleurs 
    frameb1 = Frame(master_mind, width=400, height=600, borderwidth=2)
    frameb1.place(x= 60, y=535)

    #ouvrir les images 
    img = Image.open('boutonrose.PNG')
    img1 = Image.open('boutonviolet.PNG')
    img2 = Image.open('boutonbleuf.PNG')
    img3 = Image.open('boutonbleuciel.PNG')
    img4 = Image.open('boutonturquoise.PNG')
    img5 = Image.open('boutonjeune.PNG')
    img6 = Image.open('boutonorange1.PNG')
    img7 = Image.open('boutonrouge.PNG')

    #redimentionner les images
    taille0= img.resize((35,35))
    a = ImageTk.PhotoImage(taille0)

    taille1 = img1.resize((35,35))
    b = ImageTk.PhotoImage(taille1)

    taille2 = img2.resize((35,35))
    c = ImageTk.PhotoImage(taille2)

    taille3 = img3.resize((35,35))
    d = ImageTk.PhotoImage(taille3)

    taille4 = img4.resize((35,35))
    e = ImageTk.PhotoImage(taille4)

    taille5 = img5.resize((35,35))
    f = ImageTk.PhotoImage(taille5)

    taille6 = img6.resize((35,35))
    g = ImageTk.PhotoImage(taille6)

    taille7 = img7.resize((35,35))
    h = ImageTk.PhotoImage(taille7)

    #boutons
    B0 = Button(frameb1, image=a,)
    B1 = Button(frameb1, image=b)
    B2 = Button(frameb1, image=c)
    B3 = Button(frameb1, image=d)
    B4 = Button(frameb1, image=e)
    B5 = Button(frameb1, image=f)
    B6 = Button(frameb1, image=g)
    B7 = Button(frameb1, image=h)

    #affichage des boutons
    B0.grid()
    B1.grid(row =0, column=1)
    B2.grid(row =0,column=2)
    B3.grid(row =0,column=3)
    B4.grid(row =0,column=4)
    B5.grid(row =0,column=5)
    B6.grid(row =0,column=6)
    B7.grid(row =0,column=7)
    

    #Canvas de la grille de jeu 
    grille = Canvas(master_mind,width=145, height=400)
    #ligne 1 des cercles pour le plateau de jeux 
    c1 = grille.create_oval(10,10,40,40)
    c2 = grille.create_oval(45,10,75,40)
    c3= grille.create_oval(80,10,110,40)
    c4 = grille.create_oval(115,10,145,40)

    #ligne 2 des cercles pour le plateau de jeux 
    c5= grille.create_oval(10,50,40,80)
    c6 = grille.create_oval(45,50,75,80)
    c7 = grille.create_oval(80,50,110,80)
    c8 = grille.create_oval(115,50,145,80)

    #ligne 3 des cercles pour le plateau de jeux 
    c9= grille.create_oval(10,90,40,120)
    c10 = grille.create_oval(45,90,75,120)
    c11 = grille.create_oval(80,90,110,120)
    c12 = grille.create_oval(115,90,145,120)

    #ligne 4 des cercles pour le plateau de jeux 
    c13= grille.create_oval(10,130,40,160)
    c14 = grille.create_oval(45,130,75,160)
    c15 = grille.create_oval(80,130,110,160)
    c16 = grille.create_oval(115,130,145,160)

    #ligne 5 des cercles pour le plateau de jeux 
    c17= grille.create_oval(10,170,40,200)
    c18 = grille.create_oval(45,170,75,200)
    c19 = grille.create_oval(80,170,110,200)
    c20 = grille.create_oval(115,170,145,200)

    #ligne 6 des cercles pour le plateau de jeux 
    c21 = grille.create_oval(10,210,40,240)
    c22 = grille.create_oval(45,210,75,240)
    c23 = grille.create_oval(80,210,110,240)
    c24 = grille.create_oval(115,210,145,240)

    #ligne 7 des cercles pour le plateau de jeux 
    c25 = grille.create_oval(10,250,40,280)
    c26 = grille.create_oval(45,250,75,280)
    c27 = grille.create_oval(80,250,110,280)
    c28 = grille.create_oval(115,250,145,280)

    #ligne 8 des cercles pour le plateau de jeux
    c29 = grille.create_oval(10,290,40,320)
    c30 = grille.create_oval(45,290,75,320)
    c31 = grille.create_oval(80,290,110,320)
    c32 = grille.create_oval(115,290,145,320)

    #ligne 9 des cercles pour le plateau de jeux
    c33 = grille.create_oval(10,330,40,360)
    c34 = grille.create_oval(45,330,75,360)
    c35 = grille.create_oval(80,330,110,360)
    c36 = grille.create_oval(115,330,145,360)

    #ligne 10 des cercles pour le plateau de jeux
    c37 = grille.create_oval(10,370,40,400)
    c38 = grille.create_oval(45,370,75,400)
    c39 = grille.create_oval(80,370,110,400)
    c40 = grille.create_oval(115,370,145,400)

    gun = grille.place(x = 50, y=75)

    #création 1 des canvas pions bien placé ou non    
    aide1 = Canvas(master_mind,width=90, height=25)
    a1 = aide1.create_oval(4,9,20,25)
    a2 = aide1.create_oval(27,9,43,25)
    a3 = aide1.create_oval(50,9,65,25)
    a4 = aide1.create_oval(71,9,87,25)
    aide1.place(x = 280, y = 83)

    #création 2 des canvas pions bien placé ou non    
    aide2 = Canvas(master_mind,width=90, height=25)
    a6 = aide2.create_oval(4,9,20,25)
    a7 = aide2.create_oval(27,9,43,25)
    a8 = aide2.create_oval(50,9,65,25)
    a9 = aide2.create_oval(71,9,87,25)
    aide2.place(x = 280, y = 122)

    #création 3 des canvas pions bien placé ou non    
    aide3 = Canvas(master_mind,width=90, height=25)
    a10 = aide3.create_oval(4,9,20,25)
    a11 = aide3.create_oval(27,9,43,25)
    a12 = aide3.create_oval(50,9,65,25)
    a13 = aide3.create_oval(71,9,87,25)
    aide3.place(x = 280, y = 163)

    #création 4 des canvas pions bien placé ou non    
    aide4 = Canvas(master_mind,width=90, height=25)
    a14 = aide4.create_oval(4,9,20,25)
    a15 = aide4.create_oval(27,9,43,25)
    a16 = aide4.create_oval(50,9,65,25)
    a17 = aide4.create_oval(71,9,87,25)
    aide4.place(x = 280, y = 203)

    #création 5 des canvas pions bien placé ou non    
    aide5 = Canvas(master_mind,width=90, height=25)
    a18 = aide5.create_oval(4,9,20,25)
    a19 = aide5.create_oval(27,9,43,25)
    a20 = aide5.create_oval(50,9,65,25)
    a21 = aide5.create_oval(71,9,87,25)
    aide5.place(x = 280, y = 245)

    #création 6 des canvas pions bien placé ou non   
    aide6 = Canvas(master_mind,width=90, height=25)
    a22 = aide6.create_oval(4,9,20,25)
    a23 = aide6.create_oval(27,9,43,25)
    a24 = aide6.create_oval(50,9,65,25)
    a25 = aide6.create_oval(71,9,87,25)
    aide6.place(x = 280, y = 285)

    #création 7 des canvas pions bien placé ou non   
    aide7 = Canvas(master_mind, width=90, height=25)
    a26 = aide7.create_oval(4,9,20,25)
    a27 = aide7.create_oval(27,9,43,25)
    a28 = aide7.create_oval(50,9,65,25)
    a29 = aide7.create_oval(71,9,87,25)
    aide7.place(x = 280, y = 325)

    #création 8 des canvas pions bien placé ou non   
    aide8 = Canvas(master_mind, width=90, height=25)
    a30 = aide8.create_oval(4,9,20,25)
    a31 = aide8.create_oval(27,9,43,25)
    a32 = aide8.create_oval(50,9,65,25)
    a33 = aide8.create_oval(71,9,87,25)
    aide8.place(x = 280, y = 365)

    #création 9 des canvas pions bien placé ou non   
    aide9 = Canvas(master_mind, width=90, height=25)
    a34 = aide9.create_oval(4,9,20,25)
    a35 = aide9.create_oval(27,9,43,25)
    a36 = aide9.create_oval(50,9,65,25)
    a37 = aide9.create_oval(71,9,87,25)
    aide9.place(x = 280, y = 405)

    #création 10 des canvas pions bien placé ou non   
    aide10 = Canvas(master_mind, width=90, height=25)
    a38 = aide10.create_oval(4,9,20,25)
    a39 = aide10.create_oval(27,9,43,25)
    a40 = aide10.create_oval(50,9,65,25)
    a41 = aide10.create_oval(71,9,87,25)
    aide10.place(x = 280, y = 443)


def preferencebouton2 () :
    """Création de la fonction permettant de choisir les préférences du jeu, c'est à dire :
    - la taille du code secret (nombre de pion)
    - le nombre de couleurs
    - le nombre d'essai afin de trouver le code secret""" 
    preference = Toplevel(bouton2)
    preference.title ("Préferences")
    preference.geometry ("300x300")
    global listeCombo4
    global listeCombo5
    global listeCombo6
    labelpreference4 = Label (preference, text = 'Choississez un nombre de pions', fg = ('black'), font = ('helvetica', '10'))
    labelpreference4.pack(side ='top')
    listeCombo4 = ttk.Combobox (preference, values = nombrepions)
    listeCombo4.pack()
    labelpreference5 = Label (preference, text = 'Choississez un nombre de couleurs', fg = ('black'), font = ('helvetica', '10'))
    labelpreference5.pack(side = 'top')
    listeCombo5 = ttk.Combobox (preference, values = nombrecouleurs)
    listeCombo5.pack()
    labelpreference6 = Label (preference, text = "Choississez un nombre d' essai", fg = ('black'), font = ('helvetica', '10'))
    labelpreference6.pack(side = 'top')
    listeCombo6 = ttk.Combobox (preference, values = nombreessai)
    listeCombo6.pack()
    appliquer = tkinter.Button(preference, text="Appliquer", fg = ("black"), font =("helvetica", "10"), command = appliquerparametres2)
    appliquer.pack(side = "bottom")


def appliquerparametres2 () :
    """fonction qui va permettre d'appliquer les paramètres choisi sur l'interface graphique en cliquant sur le 
    bouton appliquer"""
    if int(listeCombo4.get()) == 3:          # .get c'est pour appeler la valeur qu'on a choisi dans la combobox
        master_mind.destroy()                   # il faut ensuite mettre la veleur récupéré en nombre entier, d'ou le int
        bouton2fonction(cercletrois)
    elif int(listeCombo4.get()) == 4:
        master_mind.destroy()
        bouton2fonction(cerclequatre)
    elif int(listeCombo4.get()) == 5:
        master_mind.destroy()
        bouton2fonction(cerclecinq)
    elif int(listeCombo4.get()) == 6:
        master_mind.destroy()
        bouton2fonction(cerclesix)
    elif int(listeCombo4.get()) == 7:
        master_mind.destroy()
        bouton2fonction(cerclesept)
    elif int(listeCombo4.get()) == 8:
        master_mind.destroy()
        bouton2fonction(cerclehuit)
    if int(listeCombo5.get()) == 4 :
        pass
    elif int(listeCombo5.get()) == 5:
        pass
    elif int(listeCombo5.get()) == 6:
        pass
    elif int(listeCombo5.get()) == 7:
        pass
    elif int(listeCombo5.get()) == 8:
        pass
    elif int(listeCombo6.get()) == 6:
        pass
    elif int(listeCombo6.get()) == 7:
        pass
    elif int(listeCombo6.get()) == 8:
        pass
    elif int(listeCombo6.get()) == 9:
        pass
    elif int(listeCombo6.get()) == 10:
        pass
    elif int(listeCombo6.get()) == 15:
        pass
    elif int(listeCombo6.get()) == 20:
        pass

def cercletrois():
    global cercle1
    global cercle2
    global cercle3
    cercle1 = canvascs.create_oval(50,10,80,40)
    cercle2 = canvascs.create_oval(90,10,120,40)
    cercle3 = canvascs.create_oval(130,10,160,40)

def cerclequatre():
    cercletrois()
    global cercle4
    cercle4 = canvascs.create_oval(170,10,200,40)

def cerclecinq():
    cerclequatre()
    global cercle5
    cercle5 = canvascs.create_oval (210, 10, 240, 40)

def cerclesix():
    cerclecinq()
    global cercle6
    cercle6 = canvascs.create_oval (10, 10, 40, 40)

def cerclesept():
    cerclesix()
    global cercle7
    cercle7 = canvascs.create_oval (240, 10, 270, 40)

def cerclehuit():
    cerclesept()
    global cercle8
    cercle8 = canvascs.create_oval (270, 10, 300, 40)


def aproposbouton2 () : 
    """Création de la fonction permettant d'afficher les règles du jeu""" 
    showinfo ('À propos',
             message="Bienvenue dans Mastermind.\n\n"
                     "Ce jeu consiste à trouver un code secret composé de plusieurs couleurs, sachant que "
                     "chaque couleur peut apparaître plusieurs fois.\n\n"
                     "Vous pouvez configurer le nombre de couleurs différentes, la taille du code secret "
                     "et le nombre de tentatives que vous pouvez effectuer dans le menu Préférences.")
    

def timerbouton2 () :
    start = time.time()
    
    end = time.time()
    print(format(end-start))    
    

def sauvergarderjeu () :
    print ("bonjour")


# Bouton mode 2 joueurs 
bouton2 = tkinter.Button(racine, text = 'mode 2 joueurs', bd = '5', command=bouton2fonction)          # On peut aussi mettre un bg... comme sur les labels
bouton2.pack(side = 'left', fill='x', expand = True)




racine.mainloop()      # pour que le fenetre reste ouverte, boucle infinie
