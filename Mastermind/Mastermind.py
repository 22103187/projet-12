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
M = Label(racine, text='sur le jeu Mastermind',bg=('pink3'),font='23')
M.place(x = 230, y=50)



# Création boutons 
nombrecouleurs = ["4", "5", "6", "7", "8"]
nombrepions = ["3", "4", "5", "6", "7", "8"]
nombreessai = ["6", "7", "8", "9", "10", "15", "20"]
# Fonction bouton 1

def bouton1fonction ():                     
    master_mind=Toplevel(racine)
    
    master_mind.geometry("450x660")#taille de la fenetre

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



   
    #création du bouton validé, supprimer et quitter 
    bvalide = Button(master_mind,text = 'Validé', height=1, width=8)
    bsupprimer = Button(master_mind,text = 'Supprimer',height=1, width=8)
    bquitter = Button(master_mind,text = 'Quitter',height=1, width=8,command=master_mind.destroy)

    #placement des boutons validé,supprimer,quitter et le label code
    bvalide.place(x = 175, y = 600)
    bsupprimer.place(x =50, y = 600)
    bquitter.place(x = 300, y = 600)
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
    #bouton bleu ciel
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

    # Création Menu
    bouton1_menu = Menu(bouton1)               
    bouton1['menu'] = bouton1_menu
    main_cascade = Menu(bouton1_menu)
    bouton1_menu.add_cascade(label='Menu', menu = main_cascade)
    main_cascade.add_command(label='Préférences', command = preferencebouton1)
    main_cascade.add_separator()
    main_cascade.add_separator()
    main_cascade.add_command(label='À propos', command = aproposbouton1)

nombrecouleurs = ["4", "5", "6", "7", "8"]
nombrepions = ["3", "4", "5", "6", "7", "8"]
nombreessai = ["6", "7", "8", "9", "10", "15", "20"]


def preferencebouton1 () :
    preference = Toplevel(bouton1)
    preference.title ("Préferences")
    preference.geometry ("300x300")
    preference['bg'] = 'oldlace'
    labelpreference1 = Label (preference, text = 'Choississez un nombre de pions', fg = ('black'), bg = ('oldlace'), font = ('helvetica', '10'))
    labelpreference1.pack(side ='top')
    listeCombo1 = ttk.Combobox (preference, values = nombrepions)
    listeCombo1.pack()
    labelpreference2 = Label (preference, text = 'Choississez un nombre de couleurs', fg = ('black'), bg = ('oldlace'), font = ('helvetica', '10'))
    labelpreference2.pack(side = 'top')
    listeCombo2 = ttk.Combobox (preference, values = nombrecouleurs)
    listeCombo2.pack()
    labelpreference3 = Label (preference, text = 'Choississez un nombre d esssai', fg = ('black'), bg = ('oldlace'), font = ('helvetica', '10'))
    labelpreference3.pack(side = 'top')
    listeCombo3 = ttk.Combobox (preference, values = nombreessai)
    listeCombo3.pack()
    appliquer = tkinter.Button (preference, text="Appliquer", fg = ("black"), font =("helvetica", "10"), command = appliquerparametres1)
    appliquer.pack(side = "bottom")
    

def aproposbouton1 () :             #https://www.invivoo.com/realiser-mastermind-tkinter-python-part-3/
    showinfo ('À propos',
             message = "Bienvenue dans Mastermind.\n\n"
                     "Ce jeu consiste à trouver un code secret composé de plusieurs couleurs, sachant que "
                     "chaque couleur peut apparaître plusieurs fois.\n\n"
                     "Vous pouvez configurer le nombre de couleurs différentes, la taille du code secret "
                     "et le nombre de tentatives que vous pouvez effectuer dans le menu Préférences.")
    
def appliquerparametres1 () : 
    print ("boujour")
   
# Bouton mode 1 joueur 
bouton1 = tkinter.Button(racine, text = 'mode 1 joueur', bd = '5', command=bouton1fonction)
bouton1.pack(side = 'left', fill='x', expand = True)            # .pack = pour afficher le bouton       SAVOIR EXPLIQUER LE RESTE 
   




# Fonction bouton 2 
def bouton2fonction () :
    master_mind=Toplevel(racine)
    
    master_mind.geometry("450x660")#taille de la fenetre

    master_mind.title("Master mind mode 2 joueurs")#titre de la fenetre 
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

    #création du bouton validé,supprimer et quitter
    bvalide = Button(master_mind,text = 'Validé', height=1, width=8)
    bsupprimer = Button(master_mind,text = 'Supprimer',height=1, width=8)
    bquitter = Button(master_mind,text = 'Quitter',height=1, width=8,command=master_mind.destroy)
    

    #placement des boutons validé,supprimer,quiter + label
    bvalide.place(x = 175, y = 600)
    bsupprimer.place(x =50, y = 600)
    bquitter.place(x = 300, y = 600)
    c.place(x= 5, y=5)
    s.place(x=20, y=23)

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
    ligne1.place(x = 20, y = 470)#placer le canvas

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
    #bouton bleu ciel
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
    # création d'une nouvelle frame pour les grilles d'esssais 



    palette.place(x=170, y=509)



    master_mind.mainloop()

    # Création Menu
    bouton2_menu = Menu(bouton2)               
    bouton2['menu'] = bouton2_menu
    main_cascade = Menu(bouton2_menu)
    bouton2_menu.add_cascade(label='Menu', menu = main_cascade)
    main_cascade.add_command(label='Préférences', command = preferencebouton2)
    main_cascade.add_separator()
    main_cascade.add_separator()
    main_cascade.add_command(label='À propos', command = aproposbouton2)

 

def preferencebouton2 () :
    preference2 = Toplevel(bouton2)
    preference2.title ("Préferences")
    preference2.geometry ("300x300")
    preference2['bg'] = "oldlace"
    labelpreference4 = Label (preference2, text = 'Choississez un nombre de pions', fg = ('black'), bg = ('oldlace'), font = ('helvetica', '10'))
    labelpreference4.pack(side ='top')
    listeCombo4 = ttk.Combobox (preference2, values = nombrepions)
    listeCombo4.pack()
    labelpreference5 = Label (preference2, text = 'Choississez un nombre de couleurs', fg = ('black'), bg = ('oldlace'), font = ('helvetica', '10'))
    labelpreference5.pack(side = 'top')
    listeCombo5 = ttk.Combobox (preference2, values = nombrecouleurs)
    listeCombo5.pack()
    lebelpreference6 = Label (preference2, text = 'Choississez un nombre d essai', fg = ('black'), bg = ('oldlace'), font = ('helvetica', '10'))
    lebelpreference6.pack(side = 'top')
    listeCombo6 = ttk.Combobox (preference2, values = nombreessai)
    listeCombo6.pack()
    appliquer = tkinter.Button(preference2, text="Appliquer", fg = ("black"), font =("helvetica", "10"), command = appliquerparametres2)
    appliquer.pack(side = "bottom")
    

def aproposbouton2 () :             #https://www.invivoo.com/realiser-mastermind-tkinter-python-part-3/
    showinfo ('À propos',
             message="Bienvenue dans Mastermind.\n\n"
                     "Ce jeu consiste à trouver un code secret composé de plusieurs couleurs, sachant que "
                     "chaque couleur peut apparaître plusieurs fois.\n\n"
                     "Vous pouvez configurer le nombre de couleurs différentes, la taille du code secret "
                     "et le nombre de tentatives que vous pouvez effectuer dans le menu Préférences.")
    
def appliquerparametres2 () :
    print ("bonjour")


# Bouton mode 2 joueurs 
bouton2 = tkinter.Button(racine, text = 'mode 2 joueurs', bd = '5', command=bouton2fonction)          # On peut aussi mettre un bg... comme sur les labels
bouton2.pack(side = 'left', fill='x', expand = True)




racine.mainloop()      # pour que le fenetre reste ouverte, boucle infinie

