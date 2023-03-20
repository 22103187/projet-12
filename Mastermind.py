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

<<<<<<< HEAD
#création de la fenetre mode 2 joueurs 

def acces_mode2joueurs(self,):
    mode_2_joueurs = tkinter.Tk
    mode_2_joueurs.mainloop()
    
   


#Création boutons
#Bouton mode 1 joueur
bouton1 = tkinter.Button(racine,text='mode 1 joueur',bd='5')
bouton1.pack(side='left',fill='x',expand = True)


#Bouton mode 2 joueurs
bouton2 = tkinter.Button(racine,text='mode 2 joueurs', bd = '5',command=acces_mode2joueurs)
bouton2.pack(side='left',fill='x',expand = True)
=======
label1 = Label(racine, text="Choisissez un mode", fg = ("black"), bg=("pink3"), font =("helvetica", "14"))
label1.place(x='210', y='220')




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






racine.mainloop()      # pour que le fenetre reste ouverte, boucle infinie






   


#Interphase
=======
print("-----------------------------------------")
print("\t\tMenu")
print("-----------------------------------------")
print("Enter code using numbers.")
print("1 - rouge, 2 - vert, 3 - jaune, 4 - bleu, 5 - blanc, 6 - orange, 7 - violet, 8 - rose")
print("Example: RED YELLOW ORANGE BLACK ---> 1 3 6 5")
print("-----------------------------------------")
print_mastermind_board(show_passcode, guess_codes, guess_flags)
couleurs = ['rouge', 'rose', 'bleu', 'vert', 'jaune', 'orange', 'violet', 'blanc']
essais = 10    # nbr d'essai pour trouver le code secret


