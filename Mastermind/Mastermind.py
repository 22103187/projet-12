from tkinter import CENTER, RIGHT, Frame, Label, Menu, Tk, Toplevel, ttk, Canvas, Button
import tkinter
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image


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
nombrecouleurs = ["4", "5", "6", "7", "8"]
nombrepions = ["3", "4", "5", "6", "7", "8"]
nombreessai = ["6", "7", "8", "9", "10", "15", "20"]

# Fonction bouton 1
def bouton1fonction ():  
    """Création de la fonction permettant l'affichage du plateau de jeu lorsqu'on 
        clique sur le bouton du mode 1 joueur""" 


    master_mind=Toplevel(racine)
    master_mind.geometry("450x660")#taille de la fenetre

    master_mind.title("Master mind mode 1 joueurs")#titre de la fenetre 
    master_mind.resizable(height=False, width=False)

    master_mind.title("Master mind mode 1 joueurs")#titre de la fenetre  

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
    bvalide = Button(master_mind,text = 'Validé', height=1, width=8)
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

    #création du canvas qui va révéler le code secret  
    canvascs = Canvas(master_mind,width = 200, height = 40)
    canvascs.place(x = 100, y= 8) 
    canvascs.create_oval(50,10,80,40)
    canvascs.create_oval(90,10,120,40)
    canvascs.create_oval(130,10,160,40)
    canvascs.create_oval(170,10,200,40)

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
    B0 = Button(frameb1, image=a)
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
def bouton2fonction () :
    """Création de la fonction permettant l'affichage du plateau de jeu lorsqu'on 
    clique sur le bouton du mode 2 joueur"""  
    master_mind=Toplevel(racine)
    master_mind.geometry("450x660")#taille de la fenetre
    master_mind.title("Master mind mode 2 joueurs")#titre de la fenetre 
    palette = Label(master_mind, text='palette de couleurs :')
    master_mind.resizable(height=False, width=False)
    c = Label(master_mind, text='trouver le code ')
    s = Label(master_mind,text='secret ;)') 
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
    l7.place(x = 35, y = 335)
    l8.place(x = 35, y = 380)
    l9.place(x = 35, y = 420)
    l10.place(x = 30, y = 460)
    #création du canvas qui va révéler le code secret  
    canvascs = Canvas(master_mind,width = 300, height = 40)
    canvascs.place(x = 100, y= 8) 
    canvascs.create_oval(50,10,80,40)
    canvascs.create_oval(90,10,120,40)
    canvascs.create_oval(130,10,160,40)
    canvascs.create_oval(170,10,200,40)

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
    B0 = Button(frameb1, image=a)
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

    #ligne 1 des cercles pour le plateau de jeux 
    grille1 = Canvas(master_mind,width=145, height=40)

    c1 = grille1.create_oval(10,10,40,40)
    c2 = grille1.create_oval(45,10,75,40)
    c3= grille1.create_oval(80,10,110,40)
    c4 = grille1.create_oval(115,10,145,40)
    grille1.place(x = 50, y=70)

    #ligne 2 des cercles 
    grille2 = Canvas(master_mind,width=145, height=40)

    c5= grille2.create_oval(10,10,40,40)
    c6 = grille2.create_oval(45,10,75,40)
    c7 = grille2.create_oval(80,10,110,40)
    c8 = grille2.create_oval(115,10,145,40)
    grille2.place(x = 50, y=113)

    # ligne 3 des cercles 
    grille3 = Canvas(master_mind,width=145, height=40)

    c9= grille3.create_oval(10,10,40,40)
    c10 = grille3.create_oval(45,10,75,40)
    c11 = grille3.create_oval(80,10,110,40)
    c12 = grille3.create_oval(115,10,145,40)
    grille3.place(x = 50, y=156)

    #ligne 4 des cercles 
    grille4 = Canvas(master_mind,width=145, height=40)

    c13= grille4.create_oval(10,10,40,40)
    c14 = grille4.create_oval(45,10,75,40)
    c15 = grille4.create_oval(80,10,110,40)
    c16 = grille4.create_oval(115,10,145,40)
    grille4.place(x = 50, y=198)

    #ligne 5 des cercles
    grille4 = Canvas(master_mind,width=145, height=40)

    c17= grille4.create_oval(10,10,40,40)
    c18 = grille4.create_oval(45,10,75,40)
    c19 = grille4.create_oval(80,10,110,40)
    c20 = grille4.create_oval(115,10,145,40)
    grille4.place(x = 50, y=240)

    #ligne 6 des cercles
    grille6 = Canvas(master_mind,width=145, height=40)

    c21 = grille6.create_oval(10,10,40,40)
    c22 = grille6.create_oval(45,10,75,40)
    c23 = grille6.create_oval(80,10,110,40)
    c24 = grille6.create_oval(115,10,145,40)
    grille6.place(x = 50, y=283)

    #ligne 7 des cercles
    grille7 = Canvas(master_mind,width=145, height=40)

    c25 = grille7.create_oval(10,10,40,40)
    c26 = grille7.create_oval(45,10,75,40)
    c27 = grille7.create_oval(80,10,110,40)
    c28 = grille7.create_oval(115,10,145,40)
    grille7.place(x = 50, y=325)

    #ligne 8 des cercles
    grille8 = Canvas(master_mind,width=145, height=40)

    c29 = grille8.create_oval(10,10,40,40)
    c30 = grille8.create_oval(45,10,75,40)
    c31 = grille8.create_oval(80,10,110,40)
    c32 = grille8.create_oval(115,10,145,40)
    grille8.place(x = 50, y=367)

    #ligne 9 des cercles
    grille9 = Canvas(master_mind,width=145, height=40)

    c33 = grille9.create_oval(10,10,40,40)
    c34 = grille9.create_oval(45,10,75,40)
    c35 = grille9.create_oval(80,10,110,40)
    c36 = grille9.create_oval(115,10,145,40)
    grille9.place(x = 50, y=409)

    #ligne 10 des cercles 
    grille10 = Canvas(master_mind,width=145, height=40)

    c37 = grille10.create_oval(10,10,40,40)
    c38 = grille10.create_oval(45,10,75,40)
    c39 = grille10.create_oval(80,10,110,40)
    c40 = grille10.create_oval(115,10,145,40)
    grille10.place(x = 50, y = 450)

    #création 1 des canvas pions bien placé ou non    
    aide1 = Canvas(master_mind,width=90, height=25)

    a1 = aide1.create_oval(4,9,20,25)
    a2 = aide1.create_oval(27,9,43,25)
    a3 = aide1.create_oval(50,9,65,25)
    a4 = aide1.create_oval(71,9,87,25)
    aide1.place(x = 280, y = 80)

    #création 2 des canvas pions bien placé ou non    
    aide2 = Canvas(master_mind,width=90, height=25)

    a6 = aide2.create_oval(4,9,20,25)
    a7 = aide2.create_oval(27,9,43,25)
    a8 = aide2.create_oval(50,9,65,25)
    a9 = aide2.create_oval(71,9,87,25)
    aide2.place(x = 280, y = 120)

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
    aide4.place(x = 280, y = 207)

    #création 5 des canvas pions bien placé ou non    
    aide5 = Canvas(master_mind,width=90, height=25)

    a18 = aide5.create_oval(4,9,20,25)
    a19 = aide5.create_oval(27,9,43,25)
    a20 = aide5.create_oval(50,9,65,25)
    a21 = aide5.create_oval(71,9,87,25)
    aide5.place(x = 280, y = 250)

    #création 6 des canvas pions bien placé ou non   
    aide6 = Canvas(master_mind,width=90, height=25)

    a22 = aide6.create_oval(4,9,20,25)
    a23 = aide6.create_oval(27,9,43,25)
    a24 = aide6.create_oval(50,9,65,25)
    a25 = aide6.create_oval(71,9,87,25)
    aide6.place(x = 280, y = 290)

    #création 7 des canvas pions bien placé ou non   
    aide7 = Canvas(master_mind,width=90, height=25)

    a26 = aide7.create_oval(4,9,20,25)
    a27 = aide7.create_oval(27,9,43,25)
    a28 = aide7.create_oval(50,9,65,25)
    a29 = aide7.create_oval(71,9,87,25)
    aide7.place(x = 280, y = 333)

    #création 8 des canvas pions bien placé ou non   
    aide8 = Canvas(master_mind,width=90, height=25)

    a30 = aide8.create_oval(4,9,20,25)
    a31 = aide8.create_oval(27,9,43,25)
    a32 = aide8.create_oval(50,9,65,25)
    a33 = aide8.create_oval(71,9,87,25)
    aide8.place(x = 280, y = 375)

    #création 9 des canvas pions bien placé ou non   
    aide9 = Canvas(master_mind,width=90, height=25)

    a34 = aide9.create_oval(4,9,20,25)
    a35 = aide9.create_oval(27,9,43,25)
    a36 = aide9.create_oval(50,9,65,25)
    a37 = aide9.create_oval(71,9,87,25)
    aide9.place(x = 280, y = 415)

    #création 10 des canvas pions bien placé ou non   
    aide10 = Canvas(master_mind,width=90, height=25)

    a38 = aide10.create_oval(4,9,20,25)
    a39 = aide10.create_oval(27,9,43,25)
    a40 = aide10.create_oval(50,9,65,25)
    a41 = aide10.create_oval(71,9,87,25)
    aide10.place(x = 280, y = 457)
    
    master_mind.mainloop()
 

def preferencebouton2 () :
    """Création de la fonction permettant de choisir les préférences du jeu, c'est à dire :
    - la taille du code secret (nombre de pion)
    - le nombre de couleurs
    - le nombre d'essai afin de trouver le code secret"""
    preference2 = Toplevel(bouton2)
    preference2.title ("Préferences")
    preference2.geometry ("300x300")
    labelpreference4 = Label (preference2, text = 'Choississez un nombre de pions', fg = ('black'), font = ('helvetica', '10'))
    labelpreference4.pack(side ='top')
    listeCombo4 = ttk.Combobox (preference2, values = nombrepions)
    listeCombo4.pack()
    labelpreference5 = Label (preference2, text = 'Choississez un nombre de couleurs', fg = ('black'), font = ('helvetica', '10'))
    labelpreference5.pack(side = 'top')
    listeCombo5 = ttk.Combobox (preference2, values = nombrecouleurs)
    listeCombo5.pack()
    lebelpreference6 = Label (preference2, text = "Choississez un nombre d' essai", fg = ('black'), font = ('helvetica', '10'))
    lebelpreference6.pack(side = 'top')
    listeCombo6 = ttk.Combobox (preference2, values = nombreessai)
    listeCombo6.pack()
    appliquer = tkinter.Button(preference2, text="Appliquer", fg = ("black"), font =("helvetica", "10"), command = appliquerparametres2)
    appliquer.pack(side = "bottom")
    

def aproposbouton2 () : 
    """Création de la fonction permettant d'afficher les règles du jeu""" 
    showinfo ('À propos',
             message="Bienvenue dans Mastermind.\n\n"
                     "Ce jeu consiste à trouver un code secret composé de plusieurs couleurs, sachant que "
                     "chaque couleur peut apparaître plusieurs fois.\n\n"
                     "Vous pouvez configurer le nombre de couleurs différentes, la taille du code secret "
                     "et le nombre de tentatives que vous pouvez effectuer dans le menu Préférences.")
    

def appliquerparametres2 () :
    print ("bonjour")


def timerbouton2 () :
    print ('Bonjour')    
    
def sauvergarderjeu () :
    print ("bonjour")


# Bouton mode 2 joueurs 
bouton2 = tkinter.Button(racine, text = 'mode 2 joueurs', bd = '5', command=bouton2fonction)          # On peut aussi mettre un bg... comme sur les labels
bouton2.pack(side = 'left', fill='x', expand = True)




racine.mainloop()      # pour que le fenetre reste ouverte, boucle infinie

