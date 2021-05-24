#############################
#groupe td4
#Elsa Fernandez-Antolin
#Luciano Rincon 
#Ilian Rondey
#Killian Le Bonhomme 
#Halima Cherif 
#https://github.com/uvsq21912390/projet2_terrain_jeu/edit/main/projet%20final.py
#### LES BIBLIOTHEQUES ####

import tkinter as tk
import random as rd

import tkinter
from tkinter import *
from tkinter import Canvas
import random
from random import *
import numpy as np
import copy
from pickle import *

#### VARIABLES ####

cpt = 0
LARGEUR, HAUTEUR = 1000, 1000
easy = HAUTEUR/50
z =[] #tous les carrés
liste_cercle_vert = [] #tous les carrés vert
i = 0
NB_COL = 50
NB_LINE = 50
tableau = []
liste_move = []
present = 0
retour_arrière=0

#### FENETRES ####

mainapp = tk.Tk()
canvas = tk.Canvas(mainapp, height=HAUTEUR, width=LARGEUR, bg="WHITE")
canvas.grid(column=0 , row=0)
canvas2 = tk.Canvas(mainapp, height=HAUTEUR, width=LARGEUR/2, bg="GREY")
canvas2.grid(column=1, row=0)

#### GRILLE ####

def ligne():
    x = 0
    while(x<=50):
        canvas.create_line(0,(HAUTEUR/50)*x,LARGEUR,(HAUTEUR/50)*x,fill="black",width="2")
        x = x + 1
    y = 0
    while(y<=50):
        canvas.create_line((LARGEUR/50)*y,0,(LARGEUR/50)*y,HAUTEUR,fill="black",width="2")
        y = y + 1


def matrice():
    global ma_matrice
    ma_matrice = np.random.rand(50, 50)
    
    
###################

def creer_tableau():
    global tableau
    tableau = []
    for i in range(NB_COL):
        tableau.append([-1] * NB_LINE)
    
    # tableau = [tableau_col for i in range(NB_COL)]

###### FONCTION PERMETTANT DE GENERER DES CASES VERTES ET BLEUES ######

def terre_ou_eau():
    global z , oval, liste_cercle_vert, tableau
    valeur_p_utilisateur()
    p = 0.5
    matrice()
    creer_tableau()
    
    x = 0
    for i in range(0,50):
        x = x + 1
        for ii in range(0,50):  
            a = ma_matrice[i][ii]
            
            
            if(a < p):
                oval = canvas.create_rectangle((easy*(x-1)),(easy*ii+easy),(easy*x),(easy*ii),fill="green")
                
                z.append(canvas.coords(oval))
                liste_cercle_vert.append(canvas.coords(oval))
                
                
            else:
                oval = canvas.create_rectangle((easy*(x-1)),(easy*ii+easy),(easy*x),(easy*ii),fill="blue")
                z.append(canvas.coords(oval))
                
                tableau[i][ii] = 0
    

def compte_vivant(i, j):
    """Retourne le nombre de cases voisines vivantes
       autour de la case (i, j)"""
    cpt = 0
    for k in range(max(0, i-1), min(NB_COL, i+2)):
        for el in range(max(0, j-1), min(NB_LINE, j+2)):
            if tableau[k][el] != -1 and [k, el] != [i, j]:
                cpt += 1
    
    return cpt

def traite_case(i, j):
    """Traite la case à la colonne i et ligne j en
       retournant la nouvelle valeur du tableau"""
    T = 5
    valeur_T_utilisateur()
    global tableau , compte_vivant
    nb_vivant = compte_vivant(i, j)

    if tableau[i][j] == -1:
        if nb_vivant > T:
            x, y = i * easy, j * easy
            carre = canvas.create_rectangle(x, y, x + easy,
                                            y + easy, fill="blue",
                                            outline="black")
            
            tableau[i][j]= 0
            
            
            return carre
        else:
            return -1
    
   
def etape():
    """Fait une étape du jeu de la vie"""
    n = 4
    valeur_n_utilisateur()
    global tableau
    x = 0
    while(x <= n):
        for i in range(NB_COL):
            for j in range(NB_LINE):
                traite_case(i, j)
                x = x + 1


###### LE PERSONNAGE #########

def ballle(x, y):
    """Dessine un rond bleu et retourne son identifiant 
     et les valeurs de déplacements dans une liste"""
    global z , oval, liste_cercle_vert , i , cercle, tableau,present
    
    if(present == 0):
        while x % 20 != 0 :
            x-=1
        while y % 20 != 0 :
            y-=1
        z = x//20
        e = y //20
        if tableau[z][e]== -1:
            cercle = canvas.create_oval(x, y, x+easy , y + easy, fill="red")
            present = 1

        dx, dy = 0, 0
    
        #le cercle sera donc inscrit dans un des carrés
        return [cercle, dx, dy]

def supprimer_personnage(event): # PRESSER LA TOUCHE S DU CLAVIER AFIN DE SUPPRIMER LE PERSONNAGE 
    global present
    if(present==1):
        canvas.delete(cercle)
        present = 0

def tre(event): # AVEC CLIC GAUCHE FAIRE APPARAITRE LE PERSONNAGE 
    global ballle, balle
    x = event.x 
    y = event.y
    balle = ballle(x,y)

    
###### LES DEPLACEMENTS DU PERSONNAGES ######

def tourne_droit(event):
    global  cercle , liste_cercle_bleu, tableau, balle,retour_arrière
    balle[1]= 20
    balle[2] = 0
    a , b , c , d = canvas.coords(cercle)
    e , f , g , h = (a +20) , b , (c+20), d
    i = int(e/ 20)
    j = int(f /20)
    retour_arrière=1
    if tableau[i][j]== -1 :
        canvas.move(balle[0], balle[1], balle[2])
        canvas.after(20)
        balle[1]= -20
        balle[2] = 0
        liste_move.append([balle[1]])
        liste_move.append([balle[2]])
       
    
def tourne_gauche(event):
    global cercle , liste_cercle_bleu, balle,retour_arrière
    balle[1]= -20
    balle[2] = 0
    a , b , c , d = canvas.coords(cercle)
    e , f , g , h = (a -20) , b , (c-20), d
    i = int(e/ 20)
    j = int(f /20)

    retour_arrière=1
    if tableau[i][j]== -1  :
        canvas.move(balle[0], balle[1], balle[2])
        canvas.after(20)
        balle[1]= 20
        balle[2] = 0
        liste_move.append([balle[1]])
        liste_move.append([balle[2]])
    
   

def tourne_bas(event):
    global cercle , liste_cercle_bleu,retour_arrière
    balle[1]= 0
    balle[2]= 20
    a , b , c , d = canvas.coords(cercle)
    e , f , g , h = a , (b +20) , c, (d+20)
    i = int(e/ 20)
    j = int(f /20)
    retour_arrière=1
    if tableau[i][j]== -1 :
        canvas.move(balle[0], balle[1], balle[2])
        canvas.after(20)
        balle[1]= 0
        balle[2]= -20
        liste_move.append([balle[1]])
        liste_move.append([balle[2]])
        
       
    

def tourne_haut (event):
    global cercle , liste_cercle_bleu,retour_arrière
    balle[1]= 0
    balle[2]= -20
    
    
    a , b , c , d = canvas.coords(cercle)
    e , f , g , h = a , (b -20) , c, (d-20)
    i = int(e/ 20)
    j = int(f /20)
    retour_arrière=1
    if tableau[i][j]== -1 :
        canvas.move(balle[0], balle[1], balle[2])
        canvas.after(20)
        balle[1]= 0
        balle[2]= 20
        liste_move.append([balle[1]])
        liste_move.append([balle[2]])
        
        

def retour(event): #PRESSER LA TOUCHE Z AFIN D'ANNULER LE DEPLACEMENT DU PERSONNAGE
    global liste_move 
    global retour_arrière
    if(retour_arrière==1):
        balle[1] = liste_move[-2]
        balle[2] = liste_move[-1]
        canvas.move(balle[0], balle[1], balle[2])
        canvas.after(20)
        retour_arrière==0
        return retour_arrière
   
###### SAUVEGARDER LE TERRAIN ######

#def sauvegarder_le_terrain ():
#    """ sauvegarder un terrain qui a été généré"""
#   fichier = open("sauvegarder.txt, w")
#   pickle.dump (liste_move, fichier)
#    
#   fichier.close()

##### RECHARGER UN TERRAIN #######
#def recharger ():
#   """Charger un terrain depuis le fichier txt """
#   liste_move= pickle.load(input)
#   print (liste_move)

######## BOUTONS #######

def valeur_p_utilisateur():
  p = myEntry.get()

myEntry = tk.Entry(canvas2, width=40)
myEntry.insert(0,"entrer une valeur entre 0 et 1, 0.5 par défaut")
myEntry.place(x = 50,y= 100)
button = tk.Button(canvas2, height=1, width=20, text="nouvelle valeur pour p",command= valeur_p_utilisateur)
button.place(x=130,y=130)

def valeur_n_utilisateur():
  n = myEntry2.get()

myEntry2 = tk.Entry(canvas2, width=40)
myEntry2.insert(0,"l'automate tourne 4 fois par défaut")
myEntry2.place(x = 50 ,y=175)
button2 = tk.Button(canvas2, height=1, width=20, text="nouvelle valeur pour n",command= valeur_n_utilisateur)
button2.place(x=130,y=205)

def valeur_T_utilisateur():
  T = myEntry3.get()
 
myEntry3 = tk.Entry(canvas2, width=40)
myEntry3.insert(0,"nombre de voisin pour case eau, 5 par défaut")
myEntry3.place(x = 50,y=250)

button = tk.Button(canvas2, height=1, width=20, text="nouvelle valeur pour T",command= valeur_T_utilisateur)
button.place(x=130,y=280)

def valeur_k_utilisateur():
  k = myEntry.get()

myEntry4 = tk.Entry(canvas2, width=40)
myEntry4.insert(0,"entrer une valeur , 1 par défaut")
myEntry4.place(x = 50,y= 325)
button = tk.Button(canvas2, height=1, width=20, text="nouvelle valeur pour k ",command= valeur_k_utilisateur)
button.place(x=130,y=355)








bouton_terraind = tk.Button(mainapp, text="Génération de terrain par défaut", font=("helvetica", "20"))
bouton_terraind.place(x = 1050 , y = 500)

bouton_sauvegarder = tk.Button(mainapp, text="Sauvegarde du terrain",font=("helvetica", "20"))#command=sauvegarder_le_terrain)
bouton_sauvegarder.place(x=1050, y=550)

bouton_recharger = tk.Button(mainapp, text="Recharger un terrain", font=("helvetica", "20"))#command= recharger)
bouton_recharger.place(x=1050, y=600)





#######


matrice()
terre_ou_eau()
ligne()
#sauvegarde ()
#recharger ()

canvas.create_rectangle(0, 0, 1 , 1, fill="red")
mainapp.bind("<Button-1>", tre)
mainapp.bind("<Right>", tourne_droit)
mainapp.bind("<Left>", tourne_gauche)
mainapp.bind("<Down>", tourne_bas)
mainapp.bind("<Up>", tourne_haut)
mainapp.bind
mainapp.bind("s",supprimer_personnage)  # appuyer sur S pour suprimer personnage
etape()
mainapp.bind("z", retour)    # appuyer sur Z pour faire marche arrière


mainapp.mainloop()
