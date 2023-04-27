import random
from tkinter import CENTER, RIGHT, Frame, Label, Menu, Tk, Toplevel, ttk, Canvas, Button
import tkinter
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
import time


# Paramètres fenetre racine

# création de la fenetre racine
racine = Tk() 

# régler la taille de la fenetre
racine.geometry("600x600")

 # nom fenetre
racine.title("Mastermind")    

# couleur arrière plan 
racine["bg"] = 'pink3'      

# = fenetre pas redimensionnable dans longeur et largeur, figer les dimenssions
racine.resizable(height=False, width=False)  

#label de la fenetre racine 
label = Label(racine, text="Bienvenue", fg = ("black"), bg=("pink3"), font =("helvetica", "20"))
label.pack(side="top")

label1 = Label(racine, text="Choisissez un mode de jeu", fg = ("black"), bg=("pink3"), font =("helvetica", "20"))
label1.place(x='140', y='230')

M = Label(racine, text='sur le jeu Mastermind',bg=('pink3'),font='20')
M.place(x = 210, y=40)





CPT=0
nombredetentative=0
combinaison_max=4
combinaison_secrete=[]

def creer_combinaison_secrete():
    combinaison_secrete=[]
    for i in range(0,combinaison_max):
        couleurs=["rose","bleu","jaune","orange","turquoise", "violet","bleuciel","rouge"]
        index=random.randint(0,len(couleurs)-1)
        combinaison_secrete.append(couleurs[index])#je ne comprends pas
    return combinaison_secrete
a=creer_combinaison_secrete()
combinaison=a
L=[]
# CPT

def get_couleur(couleur, master_mind, canvas, color):
    global CPT
    if len(L)>=combinaison_max:
        Labelcouleur=Label(master_mind, text="Tu as dépassé le nombre maximum!", font =("helvetica", "12"))
        Labelcouleur.place(x=95, y=250)
    else:
        L.append(couleur)
        cpt=len(L)-1
        print(CPT)
        canvas.create_oval(10+cpt*35,10+CPT*40,40+cpt*35,40+CPT*40, fill=color)
        canvas.place(x = 50, y=75)       
     

def get_couleur2(couleur, master_mind,canvas,color):
    global CPT
    if len(L)>=combinaison_max:
        Labelcouleur=Label(master_mind, text="Tu as dépassé le nombre maximum!", font =("helvetica", "12"))
        Labelcouleur.place(x=95, y=250)
    else:
        L.append(couleur)
        cpt=len(L)-1
        print(CPT)
        # label_image = Label(master_mind, image=image)
        # label_image.grid(row=0, column=cpt)
        canvas.create_oval(10+cpt*35,10+CPT*40,40+cpt*35,40+CPT*40, fill=color)
        canvas.place(x = 50, y=75)       
         
     
    
    print(L) 

def supprimer () :
    pass


longueur_combinaison=4
def comparer_combinaison(combinaison_entree, combinaison_secrete, master_mind):
    nb_couleurs_bien_placees=0
    nb_couleurs_mal_placees=0
    for i in range (longueur_combinaison):
        if combinaison_entree[i]==combinaison_secrete[i]:
            nb_couleurs_bien_placees+=1
        elif combinaison_entree[i] in combinaison_secrete:
            nb_couleurs_mal_placees+=1
            
    

    return (nb_couleurs_bien_placees, nb_couleurs_mal_placees)

  
Nombre_tentativesmaximum= 10

def fonctionvalider(canvas,Nombre_tentativesmaximum):
    global CPT
    global nombredetentative
    if len(L)<combinaison_max:
        Labelerreur=Label(master_mind, text="Tu n'as pas fini ta combinaison!", font =("helvetica", "12"))
        Labelerreur.place(x=95, y=250)
    else:
        (bienplace, malplace) = comparer_combinaison(L, combinaison, master_mind)
        print(bienplace)
        print(malplace)
        print(combinaison)
        if bienplace==4:
            print("tu as gagne")
            Labelvictoire=Label(master_mind, text="Bravo, tu as gagné!", font =("helvetica", "12"),fg='green')
            Labelvictoire.place(x=100, y=250)
        if bienplace!=4:
            nombredetentative+=1
        if nombredetentative==Nombre_tentativesmaximum:
            Labelcouleur=Label(master_mind, text="Tu as perdue :(", font =("helvetica", "12"), fg='red')
            Labelcouleur.place(x=155, y=250)
            print("tu as perdue")

        cpt=0
        while bienplace>0:
            canvas.create_oval(4+cpt*23,13+CPT*40,20+cpt*23,30+CPT*40, fill='red')
            cpt+=1
            bienplace-=1
        while malplace>0:
            canvas.create_oval(4+cpt*23,13+CPT*40,20+cpt*23,30+CPT*40, fill='black')
            cpt+=1
            malplace-=1
        CPT+=1
        canvas.place(x = 280, y = 80)
        # del L
        L.pop()
        L.pop()
        L.pop()
        L.pop()






def bouton1fonction ():  
    """Création de la fonction permettant l'affichage du plateau de jeu lorsqu'on
        clique sur le bouton du mode 1 joueur"""
    global master_mind
    master_mind=Toplevel(racine)
    master_mind.geometry("450x660")#taille de la fenetre
    master_mind.title("Master mind mode 1 joueurs")#titre de la fenetre
    master_mind.resizable(height=False, width=False)
    c = Label(master_mind, text='trouver le code ')
    s = Label(master_mind,text='secret ;)')

    bouton3_menu = Menu(master_mind)               
    master_mind['menu'] = bouton3_menu
    main_cascade = Menu(bouton3_menu)
    bouton3_menu.add_cascade(label='Menu', menu = main_cascade)
    main_cascade.add_command(label='À propos', command = aproposbouton_mode1)
    main_cascade.add_separator()
    main_cascade.add_separator()
    main_cascade.add_command(label='Ajouter un timer', command = timerbouton)

    #création du bouton validé, supprimer et quitter
    bvalide = Button(master_mind,text = 'Validé', height=1, width=8, command=lambda: fonctionvalider(aide1,Nombre_tentativesmaximum))
    bsupprimer = Button(master_mind,text = 'Supprimer',height=1, width=8, command=supprimer)
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
    grille = Canvas(master_mind,width=145, height=500)
    gun = grille.place(x = 50, y=75)
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
    aide1 = Canvas(master_mind,width=90, height=400)
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
    B0 = Button(frameb1, image=a, command=lambda : get_couleur("rose", master_mind, grille, 'fuchsia'))
    B1 = Button(frameb1, image=b, command=lambda : get_couleur("violet", master_mind, grille,'blueviolet'))
    B2 = Button(frameb1, image=c, command=lambda : get_couleur("bleu", master_mind, grille,'blue'))
    B3 = Button(frameb1, image=d,command=lambda : get_couleur("bleuciel", master_mind, grille, 'deepskyblue'))
    B4 = Button(frameb1, image=e,command=lambda : get_couleur("turquoise", master_mind, grille,'cyan'))
    B5 = Button(frameb1, image=f,command=lambda : get_couleur("jaune", master_mind, grille, 'yellow'))
    B6 = Button(frameb1, image=g,command=lambda : get_couleur("orange", master_mind, grille,'darkorange'))
    B7 = Button(frameb1, image=h,command=lambda : get_couleur("rouge", master_mind, grille, 'crimson'))
    
    #affichage des boutons
    B0.grid()
    B1.grid(row =0, column=1)
    B2.grid(row =0,column=2)
    B3.grid(row =0,column=3)
    B4.grid(row =0,column=4)
    B5.grid(row =0,column=5)
    B6.grid(row =0,column=6)
    B7.grid(row =0,column=7)
  

    master_mind.mainloop()

   
def aproposbouton_mode1 () : 
    """Création de la fonction permettant d'afficher les règles du jeu""" 
    showinfo ('À propos',
             message="Bienvenue dans Mastermind.\n\n"
                     "Ce jeu consiste à trouver un code secret composé de huit couleurs, sachant que "
                     "chaque couleur peut apparaître plusieurs fois.\n\n"
                     "Le code secret est choisi au hasard au début de la partie, à vous de le trouver"
                     "Vous disposerez pour cela de 10 tentatives. A chaque essai, vous aurez accès aux informations suivante : \n\n"
                     "- le nombre de pions bien placés (pion rouge); c'est à dire qui a la même couleur et la même position que le pions du code secret;\n\n"
                     "- et le nombre de pions mal placés (pion noir); c'est à dire qu'il a la même "
                     "couleur qu’un pion du du code secret, mais n'est pas à la bonne position.\n\n"
                     " De plus chaque pion du code secret peut compter pour au plus un pion mal placé. \n\n"
                      "Maintenant, à vous de jouer ! ")


def sauvegarderjeu () :
    """fonction permettant de sauvegarder la partie joué """
    print ("bonjour")

 
# Bouton mode 1 joueur
bouton1 = tkinter.Button(racine, text = 'mode 1 joueur', bd = '5', command=bouton1fonction)
bouton1.pack(side = 'left', fill='x', expand = True)            # .pack = pour afficher le bouton       SAVOIR EXPLIQUER LE RESTE


def codesecret() :
    """Création de la fenetre permettant de choisir le code secret"""
    #création de la fenetre, taille et titre
    global code_secret
    code_secret=Toplevel(master_mind)
    code_secret.geometry("400x250")
    code_secret.title(":)")

    #création des label + placement dans la fenetre 
    choisir = Label(code_secret, text='Choisir le code secret : )')
    choisir.place(x=120, y=10)
    pal = Label(code_secret, text="palette de couleurs : ")
    pal.place(x= 130, y=110)

    #création du bouton validé 
    valider1 = Button(code_secret, text='Validé') 
    valider1.place(x =165, y=200)

    #création du canvas et des cercles qui révèle le code secrert
    canvasbis = Canvas(code_secret,width=245, height=50)
    canvasbis.create_oval(40,10,80,50)
    canvasbis.create_oval(90,10,130,50)
    canvasbis.create_oval(140,10,180,50)
    canvasbis.create_oval(190,10,230,50)
    canvasbis.place(x= 60 , y= 40)

    #creation de la frame qui contient les boutons de couleurs
    frameb2 = Frame(code_secret, width=400, height=600)
    frameb2.place(x= 25, y=145)

    #ouvrir les images
    img8 = Image.open('rose.PNG')
    img9 = Image.open('violet.PNG')
    img10 = Image.open('bleu1.PNG')
    img11 = Image.open('bleu2.PNG')
    img12 = Image.open('turquoise.PNG')
    img13 = Image.open('jaune.PNG')
    img14 = Image.open('orange.PNG')
    img15 = Image.open('rouge.PNG')

    #redimentionner les images
    taille8 = img8.resize((35,35))
    i = ImageTk.PhotoImage(taille8)

    taille9 = img9.resize((35,35))
    j = ImageTk.PhotoImage(taille9)

    taille10 = img10.resize((35,35))
    k = ImageTk.PhotoImage(taille10)

    taille11 = img11.resize((35,35))
    l = ImageTk.PhotoImage(taille11)

    taille12 = img12.resize((35,35))
    m = ImageTk.PhotoImage(taille12)

    taille13 = img13.resize((35,35))
    n = ImageTk.PhotoImage(taille13)

    taille14 = img14.resize((35,35))
    o = ImageTk.PhotoImage(taille14)

    taille15 = img15.resize((35,35))
    p = ImageTk.PhotoImage(taille15)

    #création des bouton + ajout des parametre 
    B8 = Button(frameb2, image=i)
    B9 = Button(frameb2, image=j)
    B10 = Button(frameb2, image=k)
    B11 = Button(frameb2, image=l)
    B12 = Button(frameb2, image=m)
    B13 = Button(frameb2, image=n)
    B14 = Button(frameb2, image=o)
    B15 = Button(frameb2, image=p)

    #placement des bouton
    B8.grid()
    B9.grid(row =0, column=1)
    B10.grid(row =0,column=2)
    B11.grid(row =0,column=3)
    B12.grid(row =0,column=4)
    B13.grid(row =0,column=5)
    B14.grid(row =0,column=6)
    B15.grid(row =0,column=7)

    
    code_secret.mainloop()


  



# Fonction bouton 2
def bouton2fonction () :
    """Création de la fonction permettant l'affichage du plateau de jeu lorsqu'on
    clique sur le bouton du mode 2 joueurs"""  
    global master_mind
    master_mind=Toplevel(racine)
    master_mind.geometry("450x660")#taille de la fenetre
    master_mind.title("Master mind mode 2 joueurs")#titre de la fenetre
    master_mind.resizable(height=False, width=False)
    c = Label(master_mind, text='trouver le code ')
    s = Label(master_mind,text='secret ;)')

    bouton3_menu = Menu(master_mind)               
    master_mind['menu'] = bouton3_menu
    main_cascade = Menu(bouton3_menu)
    bouton3_menu.add_cascade(label='Menu', menu = main_cascade)
    main_cascade.add_command(label='À propos', command = aproposbouton_mode2)
    main_cascade.add_separator()
    main_cascade.add_separator()
    main_cascade.add_command(label='Ajouter un timer', command = timerbouton)

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
    bvalide = Button(master_mind,text = 'Validé', height=1, width=8, command=lambda: fonctionvalider(aide1,Nombre_tentativesmaximum))
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
    canvascs.place(x = 100, y= 8)
    global cercle1
    global cercle2
    global cercle3
    global cercle4
    cercle1 = canvascs.create_oval(50,10,80,40)
    cercle2 = canvascs.create_oval(90,10,120,40)
    cercle3 = canvascs.create_oval(130,10,160,40)
    cercle4 = canvascs.create_oval(170,10,200,40)

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
    img16 = Image.open('ro.PNG')
    img17 = Image.open('v.PNG')
    img18 = Image.open('bl1.PNG')
    img19 = Image.open('bl2.PNG')
    img20 = Image.open('t.PNG')
    img21 = Image.open('j.PNG')
    img22 = Image.open('rou.PNG')
    img23 = Image.open('r.PNG')
 
    #redimentionner les images
    taille16= img16.resize((35,35))
    q = ImageTk.PhotoImage(taille16)

    taille17 = img17.resize((35,35))
    r = ImageTk.PhotoImage(taille17)

    taille18 = img18.resize((35,35))
    s = ImageTk.PhotoImage(taille18)

    taille19 = img19.resize((35,35))
    t = ImageTk.PhotoImage(taille19)

    taille20 = img20.resize((35,35))
    u = ImageTk.PhotoImage(taille20)

    taille21 = img21.resize((35,35))
    v = ImageTk.PhotoImage(taille21)

    taille22 = img22.resize((35,35))
    w = ImageTk.PhotoImage(taille22)

    taille23 = img23.resize((35,35))
    x = ImageTk.PhotoImage(taille23)

    #boutons
    B16 = Button(frameb1, image=q, command=lambda : get_couleur2("rose", master_mind, grille, 'fuchsia'))
    B17 = Button(frameb1, image=r, command=lambda : get_couleur2("violet", master_mind, grille,'blueviolet'))
    B18 = Button(frameb1, image=s, command=lambda : get_couleur2("bleu", master_mind, grille,'blue'))
    B19 = Button(frameb1, image=t,command=lambda : get_couleur2("bleuciel", master_mind, grille, 'deepskyblue'))
    B20 = Button(frameb1, image=u,command=lambda : get_couleur2("turquoise", master_mind, grille,'springgreen'))
    B21 = Button(frameb1, image=v,command=lambda : get_couleur2("jaune", master_mind, grille, 'yellow'))
    B22 = Button(frameb1, image=w,command=lambda : get_couleur2("orange", master_mind, grille,'darkorange'))
    B23 = Button(frameb1, image=x,command=lambda : get_couleur2("rouge", master_mind, grille, 'crimson'))
        
    #affichage des boutons
    B16.grid()
    B17.grid(row =0, column=1)
    B18.grid(row =0,column=2)
    B19.grid(row =0,column=3)
    B20.grid(row =0,column=4)
    B21.grid(row =0,column=5)
    B22.grid(row =0,column=6)
    B23.grid(row =0,column=7)
  
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
    

    aide1 = Canvas(master_mind,width=90, height=400)

    a1 = aide1.create_oval(4,13,20,30)
    a2 = aide1.create_oval(27,13,43,30)
    a3 = aide1.create_oval(50,13,65,30)
    a4 = aide1.create_oval(71,13,87,30)

    a6 = aide1.create_oval(4,53,20,70)
    a7 = aide1.create_oval(27,53,43,70)
    a8 = aide1.create_oval(50,53,65,70)
    a9 = aide1.create_oval(71,53,87,70)

    a10 = aide1.create_oval(4,93,20,110)
    a11 = aide1.create_oval(27,93,43,110)
    a12 = aide1.create_oval(50,93,65,110)
    a13 = aide1.create_oval(71,93,87,110)

    a14 = aide1.create_oval(4,133,20,150)
    a15 = aide1.create_oval(27,133,43,150)
    a16 = aide1.create_oval(50,133,65,150)
    a17 = aide1.create_oval(71,133,87,150)

    a18 = aide1.create_oval(4,173,20,190)
    a19 = aide1.create_oval(27,173,43,190)
    a20 = aide1.create_oval(50,173,65,190)
    a21 = aide1.create_oval(71,173,87,190)

    a22 = aide1.create_oval(4,213,20,230)
    a23 = aide1.create_oval(27,213,43,230)
    a24 = aide1.create_oval(50,213,65,230)
    a25 = aide1.create_oval(71,213,87,230)

    a26 = aide1.create_oval(4,253,20,270)
    a27 = aide1.create_oval(27,253,43,270)
    a28 = aide1.create_oval(50,253,65,270)
    a29 = aide1.create_oval(71,253,87,270)

    a30 = aide1.create_oval(4,293,20,310)
    a31 = aide1.create_oval(27,293,43,310)
    a32 = aide1.create_oval(50,293,65,310)
    a33 = aide1.create_oval(71,293,87,310)

    a34 = aide1.create_oval(4,333,20,350)
    a35 = aide1.create_oval(27,333,43,350)
    a36 = aide1.create_oval(50,333,65,350)
    a37 = aide1.create_oval(71,333,87,350)

    a38 = aide1.create_oval(4,373,20,390)
    a39 = aide1.create_oval(27,373,43,390)
    a40 = aide1.create_oval(50,373,65,390)
    a41 = aide1.create_oval(71,373,87,390)

    aide1.place(x = 280, y = 80)

 
    codesecret()
    master_mind.mainloop()  



    



def aproposbouton_mode2 () : 
    """Création de la fonction permettant d'afficher les règles du jeu""" 
    showinfo ('À propos',
             message="Bienvenue dans Mastermind.\n\n"
                     "Ce jeu consiste à trouver un code secret composé de huit couleurs, sachant que "
                     "chaque couleur peut apparaître plusieurs fois.\n\n"
                     "Vous devez dans un premier temps choisir le code secret, qu'un autre joueur devra trouver. "
                     "Celui-ci aura 10 tentatives. A chaque essai, le joueur acquiert l'information suivante : \n\n"
                     "- le nombre de pions bien placés (pion rouge); c'est à dire qui a la même couleur et la même position que le pions du code secret;\n\n"
                     "- et le nombre de pions mal placés (pion noir); c'est à dire qu'il a la même couleur qu’un pion du du code secret, mais n'est pas "
                     "à la bonne position.\n\n"
                     " De plus chaque pion du code secret peut compter pour au plus un pion mal placé. \n\n"
                      "Maintenant, à vous de jouer ! ")


def sauvergarderjeu2 () :
    """fonction permettant de sauvegarder la partie"""
    print ("bonjour")


# Bouton mode 2 joueurs
bouton2 = tkinter.Button(racine, text = 'mode 2 joueurs', bd = '5', command=bouton2fonction)          # On peut aussi mettre un bg... comme sur les labels
bouton2.pack(side = 'left', fill='x', expand = True)







# variables combobox 
nombrepions = ["3", "4", "5", "6"]
nombrecouleurs = ["4", "5", "6", "7", "8"]
nombreessai = ["6", "7", "8", "9", "10"]

# Fonction bouton 3
def bouton3fonction (fonction={}) :
    """Création de la fonction permettant l'affichage du plateau de jeu lorsqu'on 
    clique sur le bouton du mode préférences"""  
    global master_mind
    master_mind=Toplevel(racine)
    master_mind.geometry("500x800")
    master_mind.title("Master mind mode préférences")
    master_mind.resizable(height=False, width=False)
    c = Label(master_mind, text='trouver le code ')
    s = Label(master_mind,text='secret ;)') 

    # Création Menu
    bouton3_menu = Menu(master_mind)               
    master_mind['menu'] = bouton3_menu
    main_cascade = Menu(bouton3_menu)
    bouton3_menu.add_cascade(label='Menu', menu = main_cascade)
    main_cascade.add_command(label='Préférences', command = preferencebouton)
    main_cascade.add_separator()
    main_cascade.add_separator()
    main_cascade.add_command(label='À propos', command = aproposbouton)
    main_cascade.add_separator()
    main_cascade.add_separator()
    main_cascade.add_command(label='Ajouter un timer', command = timerbouton)
    
    #création de la ligne du bas
    ligne1=Canvas(master_mind,width=600, height=80) 
    a=(0, 30)
    b=(450,30)
    ligne1.create_line(a, b)
    ligne1.place(x = 20, y = 480)

    #création de la ligne du haut
    ligne1=Canvas(master_mind,width=400, height=1,bg='black')               
    a=(0, 30)
    b=(450,30)
    ligne1.create_line(a, b)
    ligne1.place(x = 20, y = 50)

    #création du bouton validé,supprimer et quitter
    bvalide = Button(master_mind,text = 'Validé', height=1, width=8)
    bsupprimer = Button(master_mind,text = 'Supprimer',height=1, width=8)
    bquitter = Button(master_mind,text = 'Quitter',height=1, width=8,command=master_mind.destroy)
    bsauvegarder = Button(master_mind,text= 'Sauvegarder', height=1, width=8, command = sauvergarderjeu)

    #placement des boutons validé,supprimer,quiter + label
    bvalide.place(x = 90, y = 585)
    bsupprimer.place(x = 190, y = 585)
    bquitter.place(x = 290, y = 585)
    bsauvegarder.place(x =190, y=620)
    c.place(x= 5, y=5)
    s.place(x=20, y=23) 

    #placer les pions du code secret
    global canvascs
    canvascs = Canvas(master_mind,width = 300, height = 40)
    canvascs.place(x = 100, y= 8)

     #creation de la frame et des boutons de couleurs 
    frameb = Frame(master_mind, width=400, height=600, borderwidth=2)
    frameb.place(x= 60, y=535)

    #ouvrir les images 
    img22 = Image.open('boutonrose.PNG')
    img23 = Image.open('boutonviolet.PNG')
    img24 = Image.open('boutonbleuf.PNG')
    img25 = Image.open('boutonbleuciel.PNG')
    img26 = Image.open('boutonturquoise.PNG')
    img27 = Image.open('boutonjeune.PNG')
    img28 = Image.open('boutonorange1.PNG')
    img29 = Image.open('boutonrouge.PNG')

    #redimentionner les images
    taille22= img22.resize((35,35))
    y = ImageTk.PhotoImage(taille22)

    taille23 = img23.resize((35,35))
    z = ImageTk.PhotoImage(taille23)

    taille24 = img24.resize((35,35))
    z1 = ImageTk.PhotoImage(taille24)

    taille25 = img25.resize((35,35))
    z2 = ImageTk.PhotoImage(taille25)

    taille26 = img26.resize((35,35))
    z3 = ImageTk.PhotoImage(taille26)

    taille27 = img27.resize((35,35))
    z4 = ImageTk.PhotoImage(taille27)

    taille28 = img28.resize((35,35))
    z5 = ImageTk.PhotoImage(taille28)

    taille29 = img29.resize((35,35))
    z6 = ImageTk.PhotoImage(taille29)

    #boutons
    B22 = Button(frameb, image=y)
    B23 = Button(frameb, image=z)
    B24 = Button(frameb, image=z1)
    B25 = Button(frameb, image=z2)
    B26 = Button(frameb, image=z3)
    B27 = Button(frameb, image=z4)
    B28 = Button(frameb, image=z5)
    B29 = Button(frameb, image=z6)

    #affichage des boutons
    B22.grid()
    B23.grid(row =0, column=1)
    B24.grid(row =0,column=2)
    B25.grid(row =0,column=3)
    B26.grid(row =0,column=4)
    B27.grid(row =0,column=5)
    B28.grid(row =0,column=6)
    B29.grid(row =0,column=7)


    if fonction == {}:                         #fonction prend en paramètre un élément
        appliquerparametres()   # si le paramètre est vide, ca appaelle donc la fonction de base qui est appliquerparametres             
    else:
        fonction()                          #si pas de paramètres, ca appelle la fonction


def timerbouton () :
    pass


def sauvergarderjeu () :
        pass


def preferencebouton () :
    """Création de la fonction permettant de choisir les préférences du jeu, c'est à dire :
    - la taille du code secret (nombre de pion)
    - le nombre de couleurs
    - le nombre d'essai afin de trouver le code secret""" 
    global preference
    preference = Toplevel(bouton3)
    preference.title ("Préferences")
    preference.geometry ("300x300")
    global listeCombo4, listeCombo5, listeCombo6
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
    appliquer = tkinter.Button(preference, text="Appliquer", fg = ("black"), font =("helvetica", "10"), command=  appliquerparametres)
    appliquer.pack(side = "bottom")


def appliquerparametres () :
    """fonction qui va permettre d'appliquer les paramètres choisi sur l'interface graphique en cliquant sur le 
    bouton appliquer"""
    if int(listeCombo4.get()) == 3:          # .get c'est pour appeler la valeur qu'on a choisi dans la combobox;il faut ensuite mettre la veleur récupéré en nombre entier, d'ou le int                  
        master_mind.destroy()
        bouton3fonction(cercletrois)            
    elif int(listeCombo4.get()) == 4:
        master_mind.destroy()
        bouton3fonction(cerclequatre)
    elif int(listeCombo4.get()) == 5:
        master_mind.destroy()
        bouton3fonction(cerclecinq)
    elif int(listeCombo4.get()) == 6:
        master_mind.destroy()
        bouton3fonction(cerclesix)
    if int(listeCombo5.get()) == 4 :
        master_mind.destroy()
        bouton3fonction (nbrcouleur4)
    elif int(listeCombo5.get()) == 5:
        master_mind.destroy()
        bouton3fonction (nbrcouleur5)
    elif int(listeCombo5.get()) == 6:
        master_mind.destroy()
        bouton3fonction (nbrcouleur6)
    elif int(listeCombo5.get()) == 7:
        master_mind.destroy()
        bouton3fonction (nbrcouleur7)
    elif int(listeCombo5.get()) == 8:
        master_mind.destroy()
        bouton3fonction (nbrcouleur8)
    if int(listeCombo6.get()) == 6:
        bouton3fonction(ligne6)
    elif int(listeCombo6.get()) == 7:
        bouton3fonction(ligne7)
    elif int(listeCombo6.get()) == 8:
        bouton3fonction(ligne8)
    elif int(listeCombo6.get()) == 9:
        bouton3fonction(ligne9)
    elif int(listeCombo6.get()) == 10:
        bouton3fonction(ligne10)
    preference.destroy()


def cercletrois():
    """fonction appellée lorsqu'on choisi un nombre de pion égal à 3 dans les paramètres"""
    #création du canvas qui va révéler le code secret  
    global cercle1, cercle2, cercle3
    cercle1 = canvascs.create_oval(50,10,80,40)
    cercle2 = canvascs.create_oval(90,10,120,40)
    cercle3 = canvascs.create_oval(130,10,160,40)

def cerclequatre():
    """fonction appellée lorsqu'on choisi un nombre de pion égal à 4 dans les paramètres"""
    cercletrois()
    global cercle4
    cercle4 = canvascs.create_oval(170,10,200,40)

def cerclecinq():
    """fonction appellée lorsqu'on choisi un nombre de pion égal à 5 dans les paramètres"""
    cerclequatre()
    global cercle5
    cercle5 = canvascs.create_oval (210, 10, 240, 40)

def cerclesix():
    """fonction appellée lorsqu'on choisi un nombre de pion égal à 6 dans les paramètres"""
    cerclecinq()
    global cercle6
    cercle6 = canvascs.create_oval (10, 10, 40, 40)



#ligne 1 des cercles pour le plateau de jeux 
def ligne1 () :  
    """fonction appellée qui place le même nombre de pions (essai et pions rouges et noirs) sur la ligne 1 que le nombre de pions du code secret"""
    #Canvas de la grille de jeu 
    global grille 
    grille = Canvas(master_mind,width=250, height=400)
    global gun
    gun = grille.place(x = 50, y=75)
    if int(listeCombo4.get()) == 3:
        ovalsligne1_pions3 ()
    elif int(listeCombo4.get()) == 4:
        ovalsligne1_pions4 ()
    elif int(listeCombo4.get()) == 5:
        ovalsligne1_pions5 ()
    elif int(listeCombo4.get()) == 6:
        ovalsligne1_pions6 () 

def ovalsligne1_pions3 () :
    """fonction appellée pour que le nombre de pions de la ligne 1 soit égal à 3, qui est le nombre de pions du code secret
    appelle la fonction cercletrois pour que tous les cercles soient sur la même page"""
    cercletrois()
    #Création de la grille des petits cercles
    global aide1, aide2, aide3, aide4, aide5, aide6, aide7, aide8, aide9, aide10
    aide1 = Canvas(master_mind,width=180, height=25)
    aide2 = Canvas(master_mind,width=180, height=25)
    aide3 = Canvas(master_mind,width=180, height=25)
    aide4 = Canvas(master_mind,width=180, height=25)
    aide5 = Canvas(master_mind,width=180, height=25)
    aide6 = Canvas(master_mind,width=180, height=25)
    aide7 = Canvas(master_mind, width=180, height=25)
    aide8 = Canvas(master_mind, width=180, height=25)
    aide9 = Canvas(master_mind, width=180, height=25)
    aide10 = Canvas(master_mind, width=180, height=25)
    global c1, c2, c3, a1, a2, a3
    c1 = grille.create_oval(10,10,40,40)
    c2 = grille.create_oval(45,10,75,40)
    c3= grille.create_oval(80,10,110,40)
    #création 1 des canvas pions bien placé ou non 
    a1 = aide1.create_oval(4,9,20,25)
    a2 = aide1.create_oval(27,9,43,25)
    a3 = aide1.create_oval(50,9,65,25)
    aide1.place(x = 280, y = 83)

def ovalsligne1_pions4 () :
    """fonction appellée pour que le nombre de pions de la ligne 1 soit égal à 4, qui est le nombre de pions du code secret
    appelle la fonction cerclequatre pour que les pions du code secret et des essais soient sur la même page
    appelle la fonction ovalsligne1_pions3 parce que les trois premiers cercles sont crées dans cette fonction"""
    cerclequatre()
    ovalsligne1_pions3 ()
    global c4, a4
    c4 = grille.create_oval(115,10,145,40)
    a4 = aide1.create_oval(71,9,87,25)
    
def ovalsligne1_pions5 () :
    cerclecinq()
    ovalsligne1_pions4 ()
    global c5, a5
    c5 = grille.create_oval(150,10,180,40)
    a5 = aide1.create_oval(92,9,108,25)

def ovalsligne1_pions6 () :
    cerclesix()
    ovalsligne1_pions5 () 
    global c6, a6
    c6 = grille.create_oval(185,10,215,40)
    a6 = aide1.create_oval(113,9,129,25)


#ligne 2 des cercles pour le plateau de jeux 
def ligne2 () :
    ligne1 ()
    if int(listeCombo4.get()) == 3:
        ovalsligne2_pions3 ()
    elif int(listeCombo4.get()) == 4:
        ovalsligne2_pions4 ()
    elif int(listeCombo4.get()) == 5:
        ovalsligne2_pions5 ()
    elif int(listeCombo4.get()) == 6:
        ovalsligne2_pions6 ()

def ovalsligne2_pions3 () :
    global c1b, c2b, c3b, a1b, a2b, a3b
    c1b = grille.create_oval(10,50,40,80)
    c2b = grille.create_oval(45,50,75,80)
    c3b = grille.create_oval(80,50,110,80)
    a1b = aide2.create_oval(4,9,20,25)
    a2b = aide2.create_oval(27,9,43,25)
    a3b = aide2.create_oval(50,9,65,25)
    aide2.place(x = 280, y = 122)

def ovalsligne2_pions4 () :
    ovalsligne2_pions3 ()
    global c4b, a4b
    c4b = grille.create_oval(115,50,145,80)
    a4b = aide2.create_oval(71,9,87,25)

def ovalsligne2_pions5 () :
    ovalsligne2_pions4 ()
    global c5b, a5b
    c5b = grille.create_oval(150,50,180,80)
    a5b = aide2.create_oval(92,9,108,25)

def ovalsligne2_pions6 () :
    ovalsligne2_pions5 () 
    global c6b, a6b
    c6b = grille.create_oval(185,50,215,80)
    a6b = aide2.create_oval(113,9,129,25)


#ligne 3 des cercles pour le plateau de jeux 
def ligne3 () :
    ligne2 ()
    if int(listeCombo4.get()) == 3:
        ovalsligne3_pions3 ()
    elif int(listeCombo4.get()) == 4:
        ovalsligne3_pions4 ()
    elif int(listeCombo4.get()) == 5:
        ovalsligne3_pions5 ()
    elif int(listeCombo4.get()) == 6:
        ovalsligne3_pions6 ()

def ovalsligne3_pions3 () :
    global c1c, c2c, c3c, a1c, a2c, a3c
    c1c= grille.create_oval(10,90,40,120)
    c2c = grille.create_oval(45,90,75,120)
    c3c = grille.create_oval(80,90,110,120)
    a1c = aide3.create_oval(4,9,20,25)
    a2c = aide3.create_oval(27,9,43,25)
    a3c = aide3.create_oval(50,9,66,25)
    aide3.place(x = 280, y = 163)

def ovalsligne3_pions4 () :
    ovalsligne3_pions3 ()
    global c4c, a4c
    c4c = grille.create_oval(115,90,145,120)
    a4c = aide3.create_oval(71,9,87,25)

def ovalsligne3_pions5 () :
    ovalsligne3_pions4 ()
    global c5c, a5c
    c5c = grille.create_oval(150,90,180,120)
    a5c = aide3.create_oval(92,9,108,25)

def ovalsligne3_pions6 () :
    ovalsligne3_pions5 () 
    global c6c, a6c
    c6c = grille.create_oval(185,90,215,120)
    a6c = aide3.create_oval(113,9,129,25)


#ligne 4 des cercles pour le plateau de jeux 
def ligne4 () :
    ligne3 ()
    if int(listeCombo4.get()) == 3:
        ovalsligne4_pions3 ()
    elif int(listeCombo4.get()) == 4:
        ovalsligne4_pions4 ()
    elif int(listeCombo4.get()) == 5:
        ovalsligne4_pions5 ()
    elif int(listeCombo4.get()) == 6:
        ovalsligne4_pions6 ()

def ovalsligne4_pions3 () :
    global c1d, c2d, c3d, c4d, a1d, a2d, a3d, a4d
    c1d= grille.create_oval(10,130,40,160)
    c2d = grille.create_oval(45,130,75,160)
    c3d = grille.create_oval(80,130,110,160)
    a1d = aide4.create_oval(4,9,20,25)
    a2d = aide4.create_oval(27,9,43,25)
    a3d = aide4.create_oval(50,9,65,25)
    aide4.place(x = 280, y = 203)

def ovalsligne4_pions4 () :
    ovalsligne4_pions3 ()
    global c4d, a4d
    c4d = grille.create_oval(115,130,145,160)
    a4d = aide4.create_oval(71,9,87,25)

def ovalsligne4_pions5 () :
    ovalsligne4_pions4 ()
    global c5d, a5d
    c5d = grille.create_oval(150,130,180,160)
    a5d = aide4.create_oval(92,9,108,25)

def ovalsligne4_pions6 () :
    ovalsligne4_pions5 () 
    global c6d, a6d
    c6d = grille.create_oval(185,130,215,160)
    a6d = aide4.create_oval(113,9,129,25)


#ligne 5 des cercles pour le plateau de jeux 
def ligne5 () :
    ligne4 ()
    if int(listeCombo4.get()) == 3:
        ovalsligne5_pions3 ()
    elif int(listeCombo4.get()) == 4:
        ovalsligne5_pions4 ()
    elif int(listeCombo4.get()) == 5:
        ovalsligne5_pions5 ()
    elif int(listeCombo4.get()) == 6:
        ovalsligne5_pions6 ()

def ovalsligne5_pions3 () :
    global c1e, c2e, c3e, a1e, a2e, a3e
    c1e= grille.create_oval(10,170,40,200)
    c2e = grille.create_oval(45,170,75,200)
    c3e = grille.create_oval(80,170,110,200)
    a1e = aide5.create_oval(4,9,20,25)
    a2e = aide5.create_oval(27,9,43,25)
    a3e = aide5.create_oval(50,9,65,25)
    aide5.place(x = 280, y = 245)

def ovalsligne5_pions4 () :
    ovalsligne5_pions3 ()
    global c4e, a4e
    c4e = grille.create_oval(115,170,145,200)
    a4e = aide5.create_oval(71,9,87,25)

def ovalsligne5_pions5 () :
    ovalsligne5_pions4 ()
    global c5e, a5e
    c5e = grille.create_oval(150,170,180,200)
    a5e = aide5.create_oval(92,9,108,25)

def ovalsligne5_pions6 () :
    ovalsligne5_pions5 () 
    global c6e, a6e
    c6e = grille.create_oval(185,170,215,200)
    a6e = aide5.create_oval(113,9,129,25)


#ligne 6 des cercles pour le plateau de jeux 
def ligne6 () :
    ligne5 ()
    if int(listeCombo4.get()) == 3:
        ovalsligne6_pions3 ()
    elif int(listeCombo4.get()) == 4:
        ovalsligne6_pions4 ()
    elif int(listeCombo4.get()) == 5:
        ovalsligne6_pions5 ()
    elif int(listeCombo4.get()) == 6:
        ovalsligne6_pions6 ()

def ovalsligne6_pions3 () :
    global c1f, c2f, c3f, a1f, a2f, a3f
    c1f = grille.create_oval(10,210,40,240)
    c2f = grille.create_oval(45,210,75,240)
    c3f = grille.create_oval(80,210,110,240)
    a1f = aide6.create_oval(4,9,20,25)
    a2f = aide6.create_oval(27,9,43,25)
    a3f = aide6.create_oval(50,9,65,25)
    aide6.place(x = 280, y = 285)

def ovalsligne6_pions4 () :
    ovalsligne6_pions3 ()
    global c4f, a4f
    c4f = grille.create_oval(115,210,145,240)
    a4f = aide6.create_oval(71,9,87,25)

def ovalsligne6_pions5 () :
    ovalsligne6_pions4 ()
    global c5f, a5f
    c5f = grille.create_oval(150,210,180,240)
    a5f = aide6.create_oval(92,9,108,25)

def ovalsligne6_pions6 () :
    ovalsligne6_pions5 () 
    global c6e, a6e
    c6e = grille.create_oval(185,210,215,240)
    a6e = aide6.create_oval(113,9,129,25)


#ligne 7 des cercles pour le plateau de jeux 
def ligne7 () :  
    ligne6 ()
    if int(listeCombo4.get()) == 3:
        ovalsligne7_pions3 ()
    elif int(listeCombo4.get()) == 4:
        ovalsligne7_pions4 ()
    elif int(listeCombo4.get()) == 5:
        ovalsligne7_pions5 ()
    elif int(listeCombo4.get()) == 6:
        ovalsligne7_pions6 ()

def ovalsligne7_pions3 () :
    global c1g, c2g, c3g, a1g, a2g, a3g
    c1g = grille.create_oval(10,250,40,280)
    c2g = grille.create_oval(45,250,75,280)
    c3g = grille.create_oval(80,250,110,280)
    a1g = aide7.create_oval(4,9,20,25)
    a2g = aide7.create_oval(27,9,43,25)
    a3g = aide7.create_oval(50,9,65,25)
    aide7.place(x = 280, y = 325)

def ovalsligne7_pions4 () :
    ovalsligne7_pions3 ()
    global c4g, a4g
    c4g = grille.create_oval(115,250,145,280)
    a4g = aide7.create_oval(71,9,87,25)

def ovalsligne7_pions5 () :
    ovalsligne7_pions4 ()
    global c5g, a5g
    c5g = grille.create_oval(150,250,180,280)
    a5g = aide7.create_oval(92,9,108,25)

def ovalsligne7_pions6 () :
    ovalsligne7_pions5 () 
    global c6g, a6g
    c6g = grille.create_oval(185,250,215,280)
    a6g = aide7.create_oval(113,9,129,25)


#ligne 8 des cercles pour le plateau de jeux
def ligne8 () :
    ligne7 ()
    if int(listeCombo4.get()) == 3:
        ovalsligne8_pions3 ()
    elif int(listeCombo4.get()) == 4:
        ovalsligne8_pions4 ()
    elif int(listeCombo4.get()) == 5:
        ovalsligne8_pions5 ()
    elif int(listeCombo4.get()) == 6:
        ovalsligne8_pions6 ()

def ovalsligne8_pions3 () :
    global c1h, c2h, c3h, a1h, a2h, a3h
    c1h = grille.create_oval(10,290,40,320)
    c2h = grille.create_oval(45,290,75,320)
    c3h = grille.create_oval(80,290,110,320)
    a1h = aide8.create_oval(4,9,20,25)
    a2h = aide8.create_oval(27,9,43,25)
    a3h = aide8.create_oval(50,9,65,25)
    aide8.place(x = 280, y = 365)

def ovalsligne8_pions4 () :
    ovalsligne8_pions3 ()
    global c4h, a4h
    c4h = grille.create_oval(115,290,145,320)
    a4h = aide8.create_oval(71,9,87,25)

def ovalsligne8_pions5 () :
    ovalsligne8_pions4 ()
    global c5h, a5h
    c5h = grille.create_oval(150,290,180,320)
    a5h = aide8.create_oval(92,9,108,25)

def ovalsligne8_pions6 () :
    ovalsligne8_pions5 () 
    global c6h, a6h
    c6h = grille.create_oval(185,290,215,320)
    a6h = aide8.create_oval(113,9,129,25)


#ligne 9 des cercles pour le plateau de jeux
def ligne9 () : 
    ligne8 ()
    if int(listeCombo4.get()) == 3:
        ovalsligne9_pions3 ()
    elif int(listeCombo4.get()) == 4:
        ovalsligne9_pions4 ()
    elif int(listeCombo4.get()) == 5:
        ovalsligne9_pions5 ()
    elif int(listeCombo4.get()) == 6:
        ovalsligne9_pions6 ()

def ovalsligne9_pions3 () :
    global c1i, c2i, c3i, a1i, a2i, a3i
    c1i = grille.create_oval(10,330,40,360)
    c2i = grille.create_oval(45,330,75,360)
    c3i = grille.create_oval(80,330,110,360)
    a1i = aide9.create_oval(4,9,20,25)
    a2i = aide9.create_oval(27,9,43,25)
    a3i = aide9.create_oval(50,9,65,25)
    aide9.place(x = 280, y = 405)

def ovalsligne9_pions4 () :
    ovalsligne9_pions3 ()
    global c4i, a4i
    c4i = grille.create_oval(115,330,145,360)
    a4i = aide9.create_oval(71,9,87,25)

def ovalsligne9_pions5 () :
    ovalsligne9_pions4 ()
    global c5i, a5i
    c5i = grille.create_oval(150,330,180,360)
    a5i = aide9.create_oval(92,9,108,25)

def ovalsligne9_pions6 () :
    ovalsligne9_pions5 () 
    global c6i, a6i
    c6i = grille.create_oval(185,330,215,360)
    a6i = aide9.create_oval(113,9,129,25)


#ligne 10 des cercles pour le plateau de jeux
def ligne10 () :
    ligne9 () 
    if int(listeCombo4.get()) == 3:
        ovalsligne10_pions3 ()
    elif int(listeCombo4.get()) == 4:
        ovalsligne10_pions4 ()
    elif int(listeCombo4.get()) == 5:
        ovalsligne10_pions5 ()
    elif int(listeCombo4.get()) == 6:
        ovalsligne10_pions6 ()

def ovalsligne10_pions3 () :
    global c1j, c2j, c3j, a1j, a2j, a3j
    c1j = grille.create_oval(10,370,40,400)
    c2j = grille.create_oval(45,370,75,400)
    c3j = grille.create_oval(80,370,110,400)
    a1j = aide10.create_oval(4,9,20,25)
    a2j = aide10.create_oval(27,9,43,25)
    a3j = aide10.create_oval(50,9,65,25)
    aide10.place(x = 280, y = 443)

def ovalsligne10_pions4 () :
    ovalsligne10_pions3 ()
    global c4j, a4j
    c4j = grille.create_oval(115,370,145,400)
    a4j = aide10.create_oval(71,9,87,25)

def ovalsligne10_pions5 () :
    ovalsligne10_pions4 ()
    global c5j, a5j
    c5j = grille.create_oval(150,370,180,400)
    a5j = aide10.create_oval(92,9,108,25)

def ovalsligne10_pions6 () :
    ovalsligne10_pions5 () 
    global c6j, a6j
    c6j = grille.create_oval(185,370,215,400)
    a6j = aide10.create_oval(113,9,129,25)


def nbrcouleur4 () :
    """fonction qui permet d'avoir seulement 4 couleurs à disposition lorsque le nombre de couleur choisi dans les paramètres 
    est égal à 4"""
    #creation de la frame et des boutons de couleurs 
    
    frameb3 = Frame(master_mind, width=0, height=200, borderwidth=1)
    frameb3.place(x= 60, y=535)
        #ouvrir les images 
    img30 = Image.open('a3.PNG')
    img31 = Image.open('a7.PNG')
    img32 = Image.open('a2.PNG')
    img33 = Image.open('a1.PNG')

        #redimentionner les images
    taille30 = img30.resize((35,35))
    z7 = ImageTk.PhotoImage(taille30)

    taille31 = img31.resize((35,35))
    z8 = ImageTk.PhotoImage(taille31)

    taille32 = img32.resize((35,35))
    z9 = ImageTk.PhotoImage(taille32)

    taille33 = img33.resize((35,35))
    z10 = ImageTk.PhotoImage(taille33)
        #boutons
    global B30, B31, B32, B33
    B30 = Button(frameb3, image=z7)
    B31 = Button(frameb3, image=z8)
    B32 = Button(frameb3, image=z9)
    B33 = Button(frameb3, image=z10)
        # affichage des boutons
    B30.grid(row =0,column=2)
    B31.grid(row =0,column=3)
    B32.grid(row =0,column=4)
    B33.grid(row =0,column=5)

def nbrcouleur5 () :
    """fonction qui permet d'avoir 5 couleurs à disposition lorsque le nombre de couleur choisi dans les paramètres 
    est égal à 5
    appelle la fonction nbrcouleur4 car les 4 premières couleurs sont déjà placés dans cette fonction"""
    nbrcouleur4 ()
    frameb4 = Frame(master_mind, width=0, height=200, borderwidth=1)
    frameb4.place(x= 60, y=535)

    img34 = Image.open('a8.PNG')

    taille34 = img34.resize((35,35))
    z11 = ImageTk.PhotoImage(taille34)

    B34 = Button(frameb3, image=z11)

    B34.grid(row =0,column=6)

def nbrcouleur6 () :
    nbrcouleur5 ()
    img35 = Image.open('a5.PNG')

    taille35 = img35.resize((35,35))

    z12 = ImageTk.PhotoImage(taille35)

    B35 = Button(frameb4, image=z12)

    B35.grid(row =0, column=1)

def nbrcouleur7 () :
    nbrcouleur6 ()
    img36 = Image.open('a8.PNG')

    taille36 = img36.resize((35,35))

    z13 = ImageTk.PhotoImage(taille36)

    B36 = Button(frameb4, image=z13)

    B36.grid(row =0,column=7)

def nbrcouleur8 () :
    nbrcouleur7 ()
    img37 = Image.open('a6.PNG')

    taille37= img.resize((35,35))

    z14 = ImageTk.PhotoImage(taille37)

    B37 = Button(frameb4, image=z14)

    B37.grid()



def aproposbouton () : 
    """Création de la fonction permettant d'afficher les règles du jeu""" 
    showinfo ('À propos',
             message="Bienvenue dans Mastermind.\n\n"
                     "Ce jeu consiste à trouver un code secret composé de plusieurs couleurs, sachant que "
                     "chaque couleur peut apparaître plusieurs fois.\n\n"
                     "Vous pouvez configurer le nombre de couleurs différentes, la taille du code secret "
                     "et le nombre de tentatives que vous pouvez effectuer dans le menu Préférences.\n\n"
                     "Maintenant, à vous de jouer ! ")
    


# Bouton mode préférences 
bouton3 = tkinter.Button(racine, text = 'mode préférences', bd = '5', command=bouton3fonction)          # On peut aussi mettre un bg... comme sur les labels
bouton3.pack(side = 'left', fill='x', expand = True)

racine.mainloop()
