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
H = ""


def AjouterValeurEcran(v,texte):
    global valeur_ecran,H,operateur_en_cours
  
    
    H+=str(v)
    print(H)
    valeur_ecran+=str(v)
    
    print(H,valeur_ecran,operateur_en_cours)
    texte.set(str(valeur_ecran))

def ResetValeurEcran(texte):
    global valeur_ecran
    texte.set("")
    valeur_ecran = ""

def Egale(texte):
    global valeur_ecran,operateur_en_cours,H

    if operateur_en_cours !="":
        if valeur_ecran != "":
            H+=" "+operateur_en_cours+" "
    
        ResetValeurEcran(texte)
        
        AjouterValeurEcran(Evaluer(H),texte)
        H = str(Evaluer(H))
        operateur_en_cours = ""
    else:
        ResetValeurEcran(texte)
    


def Operateur(op,texte):
    global valeur_ecran,operateur_en_cours,H
    H+=" "
    operateur_en_cours = op
    ResetValeurEcran(texte)
    
    
    
  


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
    
    tk.Button(frame,text="0",**button_dict,command=lambda:AjouterValeurEcran(0,texte)).grid(**grid_dict,column=0,row=4)
    tk.Button(frame,text=".",**button_dict,command=lambda:AjouterValeurEcran(".",texte)).grid(**grid_dict,column=1,row=4)


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