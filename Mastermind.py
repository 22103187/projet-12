from tkinter import CENTER, RIGHT, Frame, Label, Tk, Toplevel
import tkinter




# Paramètres fenetre racine
racine = Tk()    # création de la fenetre racine
racine.geometry("600x600")    # régler la taille de la fenetre
racine.title("Mastermind")     # nom fenetre
racine["bg"] = 'pink3'      # couleur arrière plan 
racine.resizable(height=False, width=False)   # = fenetre pas redimensionnable dans longeur et largeur, figer les dimenssions
racine.grid_columnconfigure(4, weight=4)        # C'EST QUOIIIIIIIII

label = Label(racine, text="Bienvenue", fg = ("black"), bg=("pink3"), font =("helvetica", "25"))
label.pack(side="top")
label1 = Label(racine, text="Choisissez un mode", fg = ("black"), bg=("pink3"), font =("helvetica", "14"))
label1.place(x='235', y='220')



# Création boutons 
# Fonction bouton 1
def bouton1fonction ():                     # Code de chez StackLima.com
    bouton1=Toplevel(racine)
    bouton1.title("Mode 1 joueur")
    bouton1.geometry("600x600")
    bouton1["bg"] = 'rosybrown1'
    labelbouton1 = Label(bouton1, text = 'Mode 1 joueur', fg = ("black"), bg=("rosybrown1"), font =("helvetica", "15"))
    labelbouton1.pack (side = "top")
# Bouton mode 1 joueur 
bouton1 = tkinter.Button(racine, text = 'mode 1 joueur', bd = '5', command=bouton1fonction)
bouton1.pack(side = 'left', fill='x', expand = True)            # .pack = pour afficher le bouton       SAVOIR EXPLIQUER LE RESTE 


# Fonction bouton 2 
def bouton2fonction () :
    bouton2=Toplevel(racine)
    bouton2.title("Mode 1 joueur")
    bouton2.geometry("600x600")
    bouton2["bg"] = 'rosybrown1'
    labelbouton2 = Label(bouton2, text = 'Mode 2 joueurs', fg = ("black"), bg=("rosybrown1"), font =("helvetica", "15"))
    labelbouton2.pack (side = "top")

# Bouton mode 2 joueurs 
bouton2 = tkinter.Button(racine, text = 'mode 2 joueurs', bd = '5', command=bouton2fonction)          # On peut aussi mettre un bg... comme sur les labels
bouton2.pack(side = 'left', fill='x', expand = True)




racine.mainloop()  # pour que le fenetre reste ouverte, boucle infinie

#Interphase
# en cours de programation 
#création de la fenetre master mind
master_mind = Tk()#création de la fenetre master mind
master_mind.geometry("400x600")#taille de la fenetre
master_mind.title("Master mind mode 2 joueurs")#titre de la fenetre 
labelcode = Label(master_mind, text = "Trouver le code secret : )",fg = ('black'), font =("helvetica", "14"))
labelcode.place(x = "125", y = "30")#emplacement du labelcode
#création des lignes 
canvasligne.create_line(master_mind,x = 400, y = 600, width = 3 #épaisseur de la ligne)







