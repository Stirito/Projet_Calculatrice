
import tkinter as tk 
from tkinter import messagebox
from Piles import *
from math import *
import random 
import string

#Test de si l'element est un opérateur Cette fonction est juste utile dans le cas de la calculatrice pour eviter de se repeter#
def is_tout_operateur(el):
  return el in "*/-+" or el == "**"

#Test de si l'element est une fonction connus. Pareil que is_tout_operateur#
def is_toute_fonction(el):
  return el == "cos" or el == "sin" or el =="tan" or el == "exp" or el == "log10" or el == "sin-1" or el == "cos-1" or el =="tan-1" or el == "sqrt" or el == "10**" or el=="ln"


#Evaluer adapté à la calculatrice avec racine,exp,log etc à noter que je fais directement 
# une pile et non un string avec les espaces#

def Evaluer_calculatrice(E :list):
    P = Creer_Pile()
    
    for el in E:
        
        if is_tout_operateur(el):
              
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
            
            
        elif is_toute_fonction(el):
           
          a1 = float(Depiler(P))
          if el == "cos":
            a = cos(a1)
              
          elif el == "sin":
            a = sin(a1)
            
          elif el == "tan":
            a = tan(a1)
          elif el == "sin-1":
            a = asin(a1)
          elif el == "tan-1":
            a = atan(a1)
          elif el == "cos-1":
            a = acos(a1)
          elif el == "exp":
            a = exp(a1)
          elif el == "ln":
         
            a = log(a1)
          elif el == "log10":
         
            a = log10(a1)
          elif el == "10**":
            a = 10**a1
          elif el == "sqrt":
            a = sqrt(a1)
          Empiler(P,a)
        else:
          Empiler(P,el)

    return Premier(P)



#Classe de la calculatrice base du programme en TKINTER #
class Calculatrie(tk.Tk):
    def __init__(self):
        super().__init__()

        #Parametre classique -> Nom de la fenetre, taille, couleur du fond, et style de la grid, des boutons et la police d'écriture#
        self.title("Calculatrice")
        self.geometry("700x700")
        self.config(background="#292929")
        self.default_font = ("Arial", 26, "bold")
        self.grid_style = {"padx":10, "pady":10,"sticky": "nsew"}   
        
        self.button_style = {"bg": "#3b3b3b", "fg": "white", "highlightthickness": 0, "font": self.default_font}
        
        self.style_ca_c_m = {"bg": "#3b3b3b", "fg": "white", "highlightthickness": 0, "font": self.default_font}
        
        self.style_evaluer_entree = {"bg": "#595959", "fg": "white", "highlightthickness": 0, "font": self.default_font}
        
        self.style_operateur_fonction = {"bg": "#323232", "fg": "white", "highlightthickness": 0, "font": self.default_font}
        
        self.style_pi_expo = {"bg": "#127DEA", "fg": "white", "highlightthickness": 0, "font": self.default_font}
        
        self.historique_style ={"bg": "#464747", "fg": "white", "highlightthickness": 0, "font": self.default_font}
     
        self.all_boutons = []
        #Stockage de la valeur NPI sous forme d'une pile. 
        # tk.StringVar() permet de stocker une variable qui va changer au cours du programme (C'est une ecriture Tkinter à connaitre)#
        self.affichage_NPI = tk.StringVar()
        self.valeurNPI = Creer_Pile()
        
        #Pareil mais pour l'affiche de l'entrée#
        self.affichage_entree = tk.StringVar()
        self.valeur_entree = ""
        
        #Un bool de is_point qui servira à ne pas pouvoir écrire plusieurs points dans la barre d'entrée#
        self.is_point = False
        

        #Pile de la Mémoire. Pareil que affichage_NPI. La fonction set() permet d'ecrire dans le StringVar() (SEULE MANIERE DE MODIFIER LE STRINGVAR) à connaitre aussi#
        #is_memore_plein va permettre de vider notre pile ssi on à un element dedans -> elle sert de flag pour ceux qui voient#
        self.memoire = Creer_Pile()
        self.affichage_memoire = tk.StringVar()
        
        self.is_memoire_plein = False
        
        self.historique = {}
        #On force la taille des lignes à etre de meme dimension et prendre 100% de l'espace qu'elle peut prendre 
        # -> Ce qui permet que quand on agrandit l'ecran que les boutons s'adaptent à la taille de la fenetre  (C'est pour un confort de l'utilisateur et pratique)#
        #le weight est de 1 car les ligne vertes d'affichage doivent prendre beaucoup plus d'espace que les boutons gris de la calculatrice 123456789#
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        

        #Configuration de l'espace pour les boutons gris #
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)
        self.grid_rowconfigure(5, weight=0)

        #Ici pareil que les autre toutes les colonnes doivent être de la même taille mais uniform = "same_group" permet un texte libre#
        self.grid_columnconfigure(0, weight=1, uniform="same_group")
        self.grid_columnconfigure(1, weight=1, uniform="same_group")
        self.grid_columnconfigure(2, weight=1, uniform="same_group")
        self.grid_columnconfigure(3, weight=1, uniform="same_group")

        #La memoire prenant plus d'espace d'ou weight = 2 en colonne que les autres
        self.grid_columnconfigure(4, weight=2, uniform="same_group")
        self.grid_columnconfigure(7, weight=2, uniform="same_group")
        
        #Les Labels sont des espaces pour pouvoir ecrire des choses dedans. 
        # textvariable est obligatoire si vous voulez changer les valeurs durant le programme (NE PAS UTILISER text= qui est DIFFERENT)#
        #anchor = "e" permet d'encrer notre texte sur le coté "Est" soit à droite de notre affichage en vert#
        #padx c'est les écarts entre les autres objets de la grid suivant x#
        #bg = background et fg = foreground c'est pour les couleurs
        #font = police police d'ecriture basique
        #columnspan permet de prendre 4 taille de notre grid#
        #Pour utiliser grid voyez le comme une grille (NE PAS HESITER A DESSINER POUR COMPRENDRE)
        #en sachant que on commence tout en haut à gauche a (column=0,row =0) -> Comme une matrice#
        
        self.label_Entree = tk.Label(self, textvariable=self.affichage_entree, anchor='e',width=1,bg="#202020", fg="white", font=self.default_font, padx=10)
        self.label_Entree.grid(column=0, row=1, columnspan=4, **self.grid_style)

        self.label_NPI = tk.Label(self, textvariable=self.affichage_NPI, anchor='e',bg="#202020",width=1, fg="white", font=self.default_font, padx=10)
        self.label_NPI.grid(column=0, row=0, columnspan=4, **self.grid_style)
        
        self.label_Memoire = tk.Label(self, textvariable=self.affichage_memoire, anchor='w',width=1,bg="#2C0404", fg="white", font=self.default_font, padx=10)
        self.label_Memoire.grid(column=4, row=0,columnspan=3, **self.grid_style)
        #Fonction pour tout regrouper#
        self.creer_bouton()
        self.bind_touche()
    
    def bind_touche(self):
      self.bind('<KeyPress>',self.couleur_aleatoire)  
    
    def couleur_aleatoire(self,event:tk.Event):
      if event.char.lower()=='r':
       
        self.config(bg=self.generer_couleur_aleatoire())

        self.supprimer_tout_les_boutons()

        self.button_style["bg"] = self.generer_couleur_aleatoire()
        self.creer_bouton_chiffre(self.button_style)
        self.style_operateur_fonction["bg"] = self.generer_couleur_aleatoire()
        self.creer_bouton_operateur_fonction(self.style_operateur_fonction)
        self.style_pi_expo["bg"] = self.generer_couleur_aleatoire()
        self.creer_bouton_expo_pi(self.style_pi_expo)
        self.style_evaluer_entree["bg"] = self.generer_couleur_aleatoire()
        self.creer_bouton_evaluer_entree(self.style_evaluer_entree)
        self.style_ca_c_m["bg"] = self.generer_couleur_aleatoire()
        self.creer_bouton_ca_c_m(self.style_ca_c_m)
    def generer_couleur_aleatoire(self):
   
      color = '#' + ''.join(random.choices(string.hexdigits[:16], k=6))
      
      return color
    def creer_bouton(self):
      #On crée une grid pour baser tout notre affichage et nos boutons dessus#
      self.grid()
      
      self.creer_bouton_ca_c_m(self.style_ca_c_m)
      
      self.creer_bouton_evaluer_entree(self.style_evaluer_entree)

    
      #Bouton opérateurs et fonctions#
      
      self.creer_bouton_operateur_fonction(self.style_operateur_fonction)

      #Boutons Bleus#
      self.creer_bouton_expo_pi(self.style_pi_expo)

      #Création des boutons 1,2,3,4,5,6,7,8,9 #
      #Petite Astuce (IMPORTANT SAVOIR BIEN VISUALISER LA GRID POUR COMPRENDRE CELA)#
      #Je fais une double boucle en commencant en bas a gauche à 1 (d'ou 5-i) et je vais de bas en haut en augmentant de 1 a chaque fois#
      #Et je vais de gauche à droite d'ou la colonne la plus basse soit j#
      #Noté : le lambda est différent j'ai affecté un paramètre t qui sera g à chaque passage de boucle#
      #Sans ca le g ne varie pas et cela va vous renvoyer 10 pour chaque bouton#
      #Le bouton zero,virgule et négatif sont fait à part car ma petite astuce ne marche pas pour ceux la#
      #command permet d'appliquer une fonction quand on appuie sur le bouton#
      #lambda n'est pas à comprendre ici réellement il le faut pour pouvoir invoquer la fonction c'est tout#
      
      self.creer_bouton_chiffre(self.button_style)
      
    def supprimer_tout_les_boutons(self):
      for bouton in self.all_boutons:
        bouton.destroy()


    def creer_bouton_chiffre(self,style_bouton):
      
      zero = tk.Button(self,text="0",**style_bouton,command=lambda :self.AjouterValeurEntree("0"))
      zero.grid(**self.grid_style,column=0,row=6)
      
      virgule = tk.Button(self,text=".",**style_bouton,command=lambda :self.AjouterValeurEntree(".") if self.is_point == False else None)
      virgule.grid(**self.grid_style,column=1,row=6)
      
      negatif = tk.Button(self,text="-()",**style_bouton,command=lambda:self.Negatif())
      negatif.grid(**self.grid_style,column=1,row=7)
      
      self.all_boutons.append(zero)
      self.all_boutons.append(virgule)
      self.all_boutons.append(negatif)

      g = 1
      for i in range(3):
        
        for j in range(3):
          bouton_chiffre = tk.Button(self,text =str(g),**style_bouton,command=lambda t= g: self.AjouterValeurEntree(t))
          bouton_chiffre.grid(**self.grid_style,column=j,row=5-i)
          self.all_boutons.append(bouton_chiffre)
          g+=1
    def creer_bouton_operateur_fonction(self,style_operateur_fonction):
      divise = tk.Button(self,text="/",**style_operateur_fonction,command=lambda : self.AjouterValeurEntree("/"))
      divise.grid(**self.grid_style,column=3,row=2)

      multiplier = tk.Button(self,text="x",**style_operateur_fonction,command=lambda : self.AjouterValeurEntree("*"))
      multiplier.grid(**self.grid_style,column=3,row=3)

      soustraire = tk.Button(self,text="-",**style_operateur_fonction,command=lambda : self.AjouterValeurEntree("-"))
      soustraire.grid(**self.grid_style,column=3,row=4)

      additionner = tk.Button(self,text="+",**style_operateur_fonction,command=lambda : self.AjouterValeurEntree("+"))
      additionner.grid(**self.grid_style,column=3,row=5)
      
      #Boutons verts
      racine = tk.Button(self,text="√",**style_operateur_fonction,command=lambda: self.AjouterValeurEntree("sqrt") )
      racine.grid(**self.grid_style,column=4,row=2)

      puissance = tk.Button(self,text="^",**style_operateur_fonction,command=lambda: self.AjouterValeurEntree("**") )
      puissance.grid(**self.grid_style,column=5,row=2)

      exponentielle = tk.Button(self,text="exp",**style_operateur_fonction,command=lambda: self.AjouterValeurEntree("exp"))
      exponentielle.grid(**self.grid_style,column=4,row=3)

      logarithme = tk.Button(self,text="log10",**style_operateur_fonction,command=lambda: self.AjouterValeurEntree("log10") )
      logarithme.grid(**self.grid_style,column=5,row=3)

      ln = tk.Button(self,text="ln",**style_operateur_fonction,command=lambda: self.AjouterValeurEntree("ln") )
      ln.grid(**self.grid_style,column=7,row=2)
      
      puissance_10 = tk.Button(self,text="10**",**style_operateur_fonction,command=lambda: self.AjouterValeurEntree("10**") )
      puissance_10.grid(**self.grid_style,column=7,row=3)
      
      sin = tk.Button(self,text="sin",**style_operateur_fonction,command=lambda: self.AjouterValeurEntree("sin") )
      sin.grid(**self.grid_style,column=4,row=4)

      cos = tk.Button(self,text="cos",**style_operateur_fonction,command=lambda: self.AjouterValeurEntree("cos") )
      cos.grid(**self.grid_style,column=5,row=4)

      tan = tk.Button(self,text="tan",**style_operateur_fonction,command=lambda: self.AjouterValeurEntree("tan") )
      tan.grid(**self.grid_style,column=4,row=5)

      arcsin = tk.Button(self,text="sin-1",**style_operateur_fonction,command=lambda: self.AjouterValeurEntree("sin-1"))
      arcsin.grid(**self.grid_style,column=5,row=5)

      arccos = tk.Button(self,text="cos-1",**style_operateur_fonction,command=lambda: self.AjouterValeurEntree("cos-1"))
      arccos.grid(**self.grid_style,column=4,row=6)

      arctan = tk.Button(self,text="tan−1",**style_operateur_fonction,command=lambda: self.AjouterValeurEntree("tan-1") )
      arctan.grid(**self.grid_style,column=5,row=6)


      self.all_boutons.extend([arctan,arccos,arcsin,cos,sin,tan,puissance_10,ln,logarithme,exponentielle,puissance,racine,multiplier,divise,additionner,soustraire])

    def creer_bouton_expo_pi(self,style_pi_expo):
      valeur_exponetielle = tk.Button(self,text="e",**style_pi_expo,command=lambda: self.AjouterValeurEntree(str(exp(1))) )
      valeur_exponetielle.grid(**self.grid_style,column=4,row=7)

      valeur_pi = tk.Button(self,text="π",**style_pi_expo,command=lambda: self.AjouterValeurEntree(str(pi)) )
      valeur_pi.grid(**self.grid_style,column=5,row=7)

      self.all_boutons.append(valeur_exponetielle)
      self.all_boutons.append(valeur_pi)
      
    def creer_bouton_evaluer_entree(self,style_evaluer):
      evaluer = tk.Button(self,text="Evaluer",**style_evaluer,command=lambda :self.EvaluerNPI())
      evaluer.grid(**self.grid_style,column=2,row=7,columnspan=2)
      
      
      entree = tk.Button(self,text="Entrée",**style_evaluer,command=lambda : self.AjouterValeurNPI(self.valeur_entree))
      entree.grid(**self.grid_style,column=2,row=6,columnspan=2)
      
      self.all_boutons.append(evaluer)
      self.all_boutons.append(entree)
      
    def creer_bouton_ca_c_m(self,style_ca_c_m):
      M = tk.Button(self,text="M",**style_ca_c_m,command=lambda : self.Memoire())
      M.grid(**self.grid_style,column=0,row=2)
      
      C = tk.Button(self,text="C",**style_ca_c_m,command=lambda : self.NettoyerNPI())
      C.grid(**self.grid_style,column=1,row=2)
      
      CA = tk.Button(self,text="CA",**style_ca_c_m,command=lambda : self.NettoyerEntree())
      CA.grid(**self.grid_style,column=2,row=2)


      self.all_boutons.append(M)
      self.all_boutons.append(C)
      self.all_boutons.append(CA)
      
    #Fonction qui empile une valeur passé en paramètre#
    #Qui affiche cette valeur sur le premier écran vert#
    #Qui nettoie l'entrée car sinon ce que vous avez écrit reste sur le deuxième affichage vert#
    def AjouterValeurNPI(self,valeur:str):
      
      Empiler(self.valeurNPI,str(valeur))
      
      self.AfficherValeurNPI()
      
      self.NettoyerEntree()
    
    #Changement des valeurs dans ma pile valeur NPI en texte pour pouvoir l'afficher dans le StringVar() #
    def AfficherValeurNPI(self):
      
      texte = ""
      for val in self.valeurNPI:
        texte+=str(val)+" "
      self.Ajuster_taille(self.label_NPI,texte)
      self.affichage_NPI.set(texte)

    #Tout simplement on Nettoie ce qui est écrit à l'écran#
    #Et on rénitialise valeur NPI#
    def NettoyerNPI(self):
      self.affichage_NPI.set("")
      self.valeurNPI = Creer_Pile()
      
    #le new_valeurNPI permet d'update la nouvelle pile pour garder la pile évalué après en affichage#
    #le try except permet de contenir les erreur de valeurs impossible comme log(0) our racine d'un nombre négatif#
    #Si erreur de ce domaine la j'envoie un message d'erreur#

    def EvaluerNPI(self):
      
      try:
        
        new_valeurNPI = Creer_Pile()
        Empiler(new_valeurNPI,str(Evaluer_calculatrice(self.valeurNPI)))
        if Premier(new_valeurNPI) != Premier(self.valeurNPI):
          self.Ajouter_a_historique(self.valeurNPI)
        self.valeurNPI = new_valeurNPI
        self.affichage_NPI.set(self.valeurNPI)
        self.Ajuster_taille(self.label_NPI,self.valeurNPI)
        
        
      except ValueError:
        self.Message_Erreur("Domaine Impossible ou vous avez mal écrit")
      except AssertionError:
        self.Message_Erreur("Ecriture polonaise non respecté")
   
    #Fonction qui permet d'écrire dans le second affichage vert#
    #je fais change le bool du is_point ce qui permet de ne plus pouvoir écrire si il y en a deja un#
    #j'ajoute à valeur_entree et je l'affiche#

    def AjouterValeurEntree(self,valeur):
      if valeur == ".":
        
        self.is_point = True
      self.valeur_entree+=str(valeur)
      
      self.affichage_entree.set(self.valeur_entree)
      self.Ajuster_taille(self.label_Entree,self.valeur_entree)
    
    def is_operateur_dans_entree(self):
      return
    
    #Pareil que NettoyerNPI#
    #Je remet le paramètre is_point = False car il n'y à plus de point dans la valeur d'entrée#
    def NettoyerEntree(self):
      self.affichage_entree.set("")
      
      self.valeur_entree = ""
      self.is_point = False

    #Op = opérateur#
    #Si le dernier element de la pile est un opérateur ou une fonction 
    # je prend pas cette valeur en mémoire mais celle juste avant#
    #is_memoire_plein : permet de vider la mémoire si il y a une valeur de dans sinon la mettre en mémoire
    # quand on appuie sur le bouton M #

    def Memoire(self):
      op = None
      if not Pile_Vide(self.valeurNPI) and (is_tout_operateur(self.valeurNPI[-1]) or is_toute_fonction(self.valeurNPI[-1])):
        op = Depiler(self.valeurNPI)
      
      if self.is_memoire_plein == False:
        valeur = Depiler(self.valeurNPI)
        Empiler(self.memoire,valeur)
        self.Ajuster_taille(self.label_Memoire,float(valeur))
        if op != None:
          Empiler(self.valeurNPI,op)
        
        self.AffichageMemoire()
        self.AfficherValeurNPI()
        self.is_memoire_plein = True
      else:
        valeur = Depiler(self.memoire)
        Empiler(self.valeurNPI,str(valeur))
        self.Ajuster_taille(self.label_NPI,float(valeur))
        if op != None:
          Empiler(self.valeurNPI,str(op))
        self.NettoyerMemoire()
        self.AfficherValeurNPI()
        self.is_memoire_plein = False
    
    #Affiche la mémoire#    
    def AffichageMemoire(self):
      self.affichage_memoire.set(str(self.memoire[0]))
      self.Ajuster_taille(self.label_Memoire,str(self.memoire[0]))
      

    #Nettoie la memoire comes les autres fonctions NettoyerEntree(),NettoyerNPI()#
    def NettoyerMemoire(self):
      self.memoire = Creer_Pile()
      self.affichage_memoire.set("")

    #Meme fonctionnement que mémoire#
    #Si il y un opérateur ou fonction en dernier element je prendre la deuxieme valeur dans valeur NPI
    # et je mets la valeur l'opposé 

    def Negatif(self):
      op = None
      if not Pile_Vide(self.valeurNPI):

        if is_toute_fonction(self.valeurNPI[-1]) or is_tout_operateur(self.valeurNPI[-1]):
         
          op = Depiler(self.valeurNPI)
        
        valeur = Depiler(self.valeurNPI)

        if op !=  None:
          
          Empiler(self.valeurNPI,str(-float(valeur)))
          Empiler(self.valeurNPI,str(op))
        else:
            Empiler(self.valeurNPI,str(-float(valeur)))
     
        self.AfficherValeurNPI() 
     
    def Ajouter_a_historique(self,valeurNPI):
      texte = str(self.valeur_npi_en_texte_historique(valeurNPI))
      bouton_historique = tk.Button(self,text =texte,**self.historique_style,padx=10)
      
      self.historique[bouton_historique]= valeurNPI
      
      bouton_historique.config(command=lambda: self.Mettre_Historique_dans_NPI(bouton_historique),font=("Arial",max(30-len(texte),10),"bold"))
      
      self.Mise_a_Jour_Position_historique()

    def Mettre_Historique_dans_NPI(self,bouton):
      self.NettoyerNPI()
      self.valeurNPI = self.historique[bouton]
      self.AfficherValeurNPI()
      self.Supprimer_Historique(bouton)
      self.Mise_a_Jour_Position_historique()
  
    def Supprimer_Historique(self,bouton):
      boutons_a_supprimer = []
      trouve = False

      for btn in self.historique.keys():
          if trouve:
              boutons_a_supprimer.append(btn)
          if btn == bouton:
              trouve = True
              
      for b in boutons_a_supprimer:
        b.destroy()
        del self.historique[b]
        
   
    def Mise_a_Jour_Position_historique(self):
      
      for (bouton,valeurNPI) in self.historique.items():
        bouton.grid(**self.grid_style, columnspan=3,column=8,row=list(self.historique.items())[::-1].index((bouton,valeurNPI)))
    
    def valeur_npi_en_texte_historique(self,valeurNPI):
      texte = ""
      for el in valeurNPI:
        texte+=str(el)+" "
      return texte
    
    def Nettoyer_Historique(self):
      self.historique = {}
    #Je nettoie tout -> Je réinitialise tout#
    #MessageBox permet de créer un pop up #
    #showerror() permet de faire une pop up d'une erreur#
    #Avec un message passé en paramètre#
    
    def Ajuster_taille(self,label,nombre):
     
  
      taille_police = max(30 - len(str(nombre)),10) 
      label.config(font=("Arial", taille_police,"bold"))
    

    def Message_Erreur(self,message):
       self.NettoyerEntree()
       self.NettoyerNPI()
       self.Nettoyer_Historique()
       messagebox.showerror("ERREUR : ",message)
          

#Je crée une variable avec la classe Calculatrice#
#mainloop() permet de lancer votre application
# __name__ == "__main__ permet simplement de lancer un script que si il n'est pas importé en module"
# Il n'est pas important on pourrait l'enlever#       
if __name__ == "__main__":
    app = Calculatrie()
    app.mainloop()
   
    







