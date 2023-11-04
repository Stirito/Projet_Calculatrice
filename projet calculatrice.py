# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 09:57:17 2023

@author: benoi
"""
import tkinter as tk
from tkinter import ttk
from Exercices_pile import *


#Valeurs couleurs,texte des boutons
default_font = ("Arial", 26, "bold")
button_dict = {"bg": "grey", "fg": "white", "font": default_font}
grid_dict = {"sticky": "nswe", "padx":10, "pady":10}    
valeur_ecran = ""
operateur_en_cours = ""
is_point = False
H = Creer_Pile()

def Evaluer_calculatrice(E):
    P = Creer_Pile()
    


    for el in E:
        print(P)
        if el in "*/-+" or el == "**":
            
            a1 = float(Depiler(P))
            a2 = float(Depiler(P))
            
            if el == "+":
                a = a2+a1
            
            elif el == "-":
                a = a2-a1
                
            elif el == "*":
                a = a2*a1
                
            elif el == "/":
                a = a2/a1
                
            elif el == "**":
                a = a2**a1
                
            Empiler(P,a)
            
            
        elif el == "cos" or el == "sin" or el =="tan":
          
            a1 = float(Depiler(P))
            if el == "cos":
                a = cos(a1)
               
            elif el == "sin":
                a = sin(a1)
            elif el == "tan":
                a = tan(a1)
            Empiler(P,a)
        else:
            Empiler(P,float(el))

    return Premier(P)




def AjouterPoint(texte):
    global valeur_ecran,H,operateur_en_cours,is_point
    if "." not in valeur_ecran:
        H+="."
        valeur_ecran+="."
        
        texte.set(str(valeur_ecran))
        is_point = True
        
def AjouterValeurEcran(v,texte):
    global valeur_ecran,H,operateur_en_cours
    Empiler(H,str(v))
    valeur_ecran+=str(v)
    print("ajouter",H)
    texte.set(str(v))

def ResetValeurEcran(texte):
    global valeur_ecran,is_point
    texte.set("")
    is_point = False
    
    
def Egale(texte):
    print("Egale")

def can_Update():
    global H,operateur_en_cours
    
    return Longueur(H) == 2 and operateur_en_cours != ""
    
def Operateur(op,texte):
    
    global operateur_en_cours,H,valeur_ecran
    if operateur_en_cours == "":
        operateur_en_cours = op
    ResetValeurEcran(texte)
    print("OPERATEUR",H,"/",valeur_ecran,"/",operateur_en_cours,can_Update())
    if can_Update():
        Empiler(H,operateur_en_cours)
        h = Evaluer_calculatrice(H)
        
        AjouterValeurEcran(h,texte)
    
        H = Creer_Pile()
        Empiler(H,str(h))
        operateur_en_cours = ""

    
    
    

  


#Creation fenetre evaluation#
def Creer_Bouton_evaluation(frame,grid_dict,var):
    texteLabel = tk.Label(frame, textvariable=var, bg ="lightgreen",padx=10,anchor="e",font=default_font)
    texteLabel.grid(**grid_dict,column=0,row=0,columnspan=3)


#Création des Boutons opérations#
def Creer_Bouton_operateur(frame,button_dict,grid_dict,texte):
    
    

    tk.Button(frame,text="+",**button_dict,command=lambda:(Operateur("+",texte))).grid(**grid_dict,column=3,row=0)
    tk.Button(frame,text="-",**button_dict,command=lambda:(Operateur("-",texte))).grid(**grid_dict,column=3,row=1)
    tk.Button(frame,text="x",**button_dict,command=lambda:(Operateur("*",texte))).grid(**grid_dict,column=3,row=2)
    tk.Button(frame,text="/",**button_dict,command=lambda:(Operateur("/",texte))).grid(**grid_dict,column=3,row=3)
    tk.Button(frame,text="^",**button_dict,command=lambda:(Operateur("**",texte))).grid(**grid_dict,column=3,row=4)
    tk.Button(frame,text="=",**button_dict,command=lambda:(Egale(texte))).grid(**grid_dict,column=2,row=4)


#Création des Boutons principaux#
def Creer_Bouton_0_virgule(frame,button_dict,grid_dict,texte):   
    global is_point
    tk.Button(frame,text="0",**button_dict,command=lambda:AjouterValeurEcran(0,texte)).grid(**grid_dict,column=0,row=4)
    tk.Button(frame,text=".",**button_dict,command=lambda:AjouterPoint(texte) if is_point == False else print("deja point") ).grid(**grid_dict,column=1,row=4)


def Creer_Bouton_chiffre(frame,button_dict,grid_dict,texte):
    g = 1
    
    for i in range(3):
        for j in range(3):
            tk.Button(frame, text=str(g), **button_dict,command=lambda t= g: AjouterValeurEcran(t,texte)).grid(**grid_dict,column=j,row=3-i)

            g+=1


def Demarrage():

    window = tk.Tk()
    window.title("Project Calculatrice - Benoit Ferrere 2eme année")
    window.geometry("400x400")
    window.config(background="black")
    frame = ttk.Frame(window, padding=10)
    frame.grid()
    
    
    textede= tk.StringVar()
   
    Creer_Bouton_evaluation(frame, grid_dict,textede)
    
    Creer_Bouton_chiffre(frame,button_dict,grid_dict,textede)
    Creer_Bouton_0_virgule(frame,button_dict,grid_dict,textede)
    Creer_Bouton_operateur(frame, button_dict, grid_dict,textede)
    
    ttk.Button(frame, text="Quit", command=window.destroy)
    window.mainloop()   
    
Demarrage()