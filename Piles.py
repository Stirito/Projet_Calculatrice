# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 07:40:59 2023

@author: benoi
"""

def Creer_Pile():
    return []
def Empiler(P : list, e : object):
    P.append(e)
    
def Depiler(P:list):
    assert P != [],  "Erreur Pile vide je ne peux enlever un element"
    return P.pop()
def Pile_Vide(P):
    return P == []

def Longueur(P):
    return len(P)
def Premier(P):
    if not Pile_Vide(P):
        return P[0]
    else:
        assert False, ("ERREUR Liste Vide je ne peux vous renvoyer le premier element")
        
        

