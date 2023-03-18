from tkinter import Tk, CENTER, RIGHT, Label
import tkinter
#Paramètres fenetre racine 
racine = Tk() # création de la fenetre racine 
racine.geometry("600x600") #régler la taille de la fenetre 
racine.title("Masterminnd") #nom fenetre 
racine["bg"] = 'pink' #couleur arrière plan 
racine.resizable(height= False, width= False) 
racine.grid_columnconfigure(4,weight=4)
label=Label(racine, text="Bienvenue", fg=("white"), bg=("pink"), font=("helvetica", "30"))
label.pack(side="top")
#
label1=Label(racine,text="Choissisez un mode", fg=("black"), bg=("pink"), font=("helvetica", "20"))
label1.place(x='210',y='220')

#Création boutons
#Bouton mode 1 joueur
bouton1 = tkinter.Button(racine,text='mode 1 joueur',bd='5')
bouton1.pack(side='left',fill='x',expand = True)

#Bouton mode 2 joueurs
bouton2 = tkinter.Button(racine,text='mode 2 joueurs', bd = '5')
bouton2.pack(side='left',fill='x',expand = True)

#Fonction bouton 1

#Fonction bouton 2 

#Interphase

racine.mainloop() #pour que la fenetre reste ouverte, boucle infinie
label1.pack(side='bottom')
