# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 07:52:08 2023

@author: benoi
"""

def Creer_File():
    return []

def Enfiler(F:list,e:object):
    L = []
    while F != []:
        L.append(F.pop())
    F.append(e)
    while L != []:
        F.append(L.pop())
        

    
        
def Defiler(F:list):
    assert F != [], "Erreur File vide je ne peux enlever un element"
    return F.pop()
def File_Vide(F:list):
    return F == []
def Longueur(F:list):
    return len(F)
def Premier(F:list):
    if not File_Vide(F):
        return F[Longueur(F)-1]
    else:
        assert False, ("ERREUR File Vide je ne peux vous renvoyer le premier element")
    

