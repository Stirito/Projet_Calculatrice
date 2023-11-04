# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 08:33:05 2023

@author: benoi
"""
from Piles import *
from math import *
#2.3

def Renverse(P):
    G = Creer_Pile()
    
    while P != []:
        Empiler(G, Depiler(P))
        
    return G

def Renverse_2(P):
    G = Creer_Pile()
    temp = Creer_Pile()
    while P != []:
        a = Depiler(P)
        Empiler(G,a)
        Empiler(temp,a)
    
        
    P = Renverse(G)
        
    return temp,P
   

def Verif2(E :str):
    pao = Creer_Pile()
    paf = Creer_Pile()
    aao = Creer_Pile()
    aaf = Creer_Pile()
    cao = Creer_Pile()
    caf = Creer_Pile()
    for el in E:
        if el == "(":
            Empiler(pao,el) 
        elif el == "{":
            Empiler(cao,el)
        elif el == "[":
            Empiler(aao,el)
        elif el == "}":
            Empiler(caf,el)
        elif el == "]":
            Empiler(aaf,el)
        elif el == ")":
            Empiler(paf,el)
        
    return Longueur(pao) == Longueur(paf) and Longueur(cao) == Longueur(caf) and Longueur(aao) == Longueur(aaf) 
    
def Verif(E :str):        
    pao = Creer_Pile()
    paf = Creer_Pile()
    for el in E:
        if el == "(" :
            Empiler(pao,el) 
        if el == ")":
            Empiler(paf,el)
    return Longueur(pao) == Longueur(paf)
    
def Clean(A:str):
    g = ""
    L = []
    for el in A:
        if el == " ":
            L.append(g)
            g=""
        else:
            g+=el
    return L

def Evaluer(E :str):
    P = Creer_Pile()
    


    for el in Clean(E):
    
        if el in "*/-+" or el == "**":
            print(P)
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

