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

label1 = Label(racine, text="Choisissez un mode", fg = ("black"), bg=("pink3"), font =("helvetica", "14"))
label1.place(x='210', y='220')




# Création boutons 
# Fonction bouton 1
def bouton1fonction ():                     
    bouton1=Toplevel(racine)                # touver chez StackLima.com
    bouton1.title("Mode 1 joueur")
    bouton1.geometry("600x600")
    bouton1["bg"] = 'oldlace'
    labelbouton1 = Label(bouton1, text = 'Mode 1 joueur', fg = ("black"), bg=("oldlace"), font =("helvetica", "15"))
    labelbouton1.pack (side = "top")

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
    bouton2=Toplevel(racine)
    bouton2.title("Mode 2 joueurs")
    bouton2.geometry("400x700") #message de jessica, j'ai agrandit la fenetre 
    bouton2["bg"] = 'oldlace'
    labelbouton2 = Label(bouton2, text = 'Mode 2 joueurs', fg = ("black"), bg=("oldlace"), font =("helvetica", "15"))
    labelbouton2.pack (side = "top")
    

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








