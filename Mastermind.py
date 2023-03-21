from tkinter import CENTER, RIGHT, Frame, Label, Tk, Toplevel, Canvas,PhotoImage, Frame, Button
import tkinter
from PIL import ImageTk, Image



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
master_mind.geometry("400x620")#taille de la fenetre
#création des lignes 
master_mind.title("Master mind mode 2 joueurs")#titre de la fenetre 

#création du bouton validé et supprimer
bvalide = Button(master_mind,text = 'Validé')
bsupprimer = Button(master_mind,text = 'Supprimer')

#placement des boutons validé et supprimer
bvalide.place(x = 175, y = 520)
bsupprimer.place(x = 165, y = 550)

#création de la ligne du bas
ligne1=Canvas(master_mind,width=400, height=20)#largeur et hauteur du canvas 
a=(0, 15)
b=(400,15)
ligne1.place(x = 1, y = 500)#placer le canvas
ligne1.create_line(a, b)

#création de la ligne à la verticale 
ligne2=Canvas(master_mind,width=0.5, height=500, bg = 'black')
ligne2.place(x = 320, y = 9)


master_mind.mainloop()

