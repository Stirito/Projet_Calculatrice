
import tkinter as tk 
from tkinter import messagebox
from Piles import *
from math import *

def Evaluer_calculatrice(E :list):
    P = Creer_Pile()
    
    for el in E:
        print(el)
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
            
            
        elif el == "cos" or el == "sin" or el =="tan" or el == "exp" or el == "log" or el == "sin-1" or el == "cos-1" or el =="tan-1":
           
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
          elif el == "log":
            a = log(a1)
          elif el == "√":
            a = sqrt(a1)
          Empiler(P,a)
        else:
          Empiler(P,el)

    return Premier(P)




class Calculatrie(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculatrice")
        self.geometry("700x700")
        self.config(background="#292929")
        self.default_font = ("Arial", 26, "bold")
        self.grid_style = {"padx":10, "pady":10,"sticky": "nsew"}   
        self.button_style = {"bg": "#595959", "fg": "white", "highlightthickness": 0, "font": self.default_font}
        self.button_style_vert = {"bg": "#21a80a", "fg": "white", "highlightthickness": 0, "font": self.default_font}
        self.button_style_bleu = {"bg": "#127DEA", "fg": "white", "highlightthickness": 0, "font": self.default_font}

        self.affichage_NPI = tk.StringVar()
        self.valeurNPI = Creer_Pile()
        
        self.affichage_entree = tk.StringVar()
        self.valeur_entree = ""
        
        self.is_point = False
        
        self.memoire = Creer_Pile()
        self.affichage_memoire = tk.StringVar()
        self.affichage_memoire.set("MEMOIRE : ")
        self.is_memoire_plein = False
        
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)
        self.grid_rowconfigure(5, weight=0)
        self.grid_columnconfigure(0, weight=1, uniform="same_group")
        self.grid_columnconfigure(1, weight=1, uniform="same_group")
        self.grid_columnconfigure(2, weight=1, uniform="same_group")
        self.grid_columnconfigure(3, weight=1, uniform="same_group")
        self.grid_columnconfigure(4, weight=2, uniform="same_group")
        self.creer_bouton()
        
        
    def creer_bouton(self):
      self.grid()
      
      label_NPI = tk.Label(self, textvariable=self.affichage_NPI, anchor='e',bg="darkgreen", fg="white", font=self.default_font, padx=10)
      label_NPI.grid(column=0, row=0, columnspan=4, **self.grid_style)
      label_Entree = tk.Label(self, textvariable=self.affichage_entree, anchor='e',bg="darkgreen", fg="white", font=self.default_font, padx=10)
      label_Entree.grid(column=0, row=1, columnspan=4, **self.grid_style)
      
      label_Memoire = tk.Label(self, textvariable=self.affichage_memoire, anchor='e',bg="darkred", fg="white", font=self.default_font, padx=10)
      label_Memoire.grid(column=4, row=0,columnspan=4, **self.grid_style)
      
      
      zero = tk.Button(self,text="0",**self.button_style,command=lambda :self.AjouterValeurEntree("0"))
      zero.grid(**self.grid_style,column=0,row=6)
      
      virgule = tk.Button(self,text=".",**self.button_style,command=lambda :self.AjouterValeurEntree(".") if self.is_point == False else None)
      virgule.grid(**self.grid_style,column=1,row=6)
      
      negatif = tk.Button(self,text="-()",**self.button_style)
      negatif.grid(**self.grid_style,column=1,row=7)
      
      
      evaluer = tk.Button(self,text="Evaluer",**self.button_style,command=lambda :self.EvaluerNPI())
      evaluer.grid(**self.grid_style,column=2,row=7,columnspan=2)
      
      
      entree = tk.Button(self,text="Entrée",**self.button_style,command=lambda : self.AjouterValeurNPI(self.valeur_entree))
      entree.grid(**self.grid_style,column=2,row=6,columnspan=2)
      
      M = tk.Button(self,text="M",**self.button_style,command=lambda : self.Memoire())
      M.grid(**self.grid_style,column=0,row=2)
      
      C = tk.Button(self,text="C",**self.button_style,command=lambda : self.NettoyerNPI())
      C.grid(**self.grid_style,column=1,row=2)
      
      CA = tk.Button(self,text="CA",**self.button_style,command=lambda : self.NettoyerEntree())
      CA.grid(**self.grid_style,column=2,row=2)
      
      
      #Bouton opérateurs#
      
      divise = tk.Button(self,text="/",**self.button_style,command=lambda : self.AjouterValeurEntree("/"))
      divise.grid(**self.grid_style,column=3,row=2)
      multiplier = tk.Button(self,text="x",**self.button_style,command=lambda : self.AjouterValeurEntree("*"))
      multiplier.grid(**self.grid_style,column=3,row=3)
      soustraire = tk.Button(self,text="-",**self.button_style,command=lambda : self.AjouterValeurEntree("-"))
      soustraire.grid(**self.grid_style,column=3,row=4)
      additionner = tk.Button(self,text="+",**self.button_style,command=lambda : self.AjouterValeurEntree("+"))
      additionner.grid(**self.grid_style,column=3,row=5)
      
      #Boutons verts
      racine = tk.Button(self,text="√",**self.button_style_vert,command=lambda: self.AjouterValeurEntree("√") )
      racine.grid(**self.grid_style,column=4,row=2)

      puissance = tk.Button(self,text="^",**self.button_style_vert,command=lambda: self.AjouterValeurEntree("**") )
      puissance.grid(**self.grid_style,column=5,row=2)

      exponentielle = tk.Button(self,text="exp",**self.button_style_vert,command=lambda: self.AjouterValeurEntree("exp"))
      exponentielle.grid(**self.grid_style,column=4,row=3)

      logarithme = tk.Button(self,text="log",**self.button_style_vert,command=lambda: self.AjouterValeurEntree("log") )
      logarithme.grid(**self.grid_style,column=5,row=3)

      sin = tk.Button(self,text="sin",**self.button_style_vert,command=lambda: self.AjouterValeurEntree("sin") )
      sin.grid(**self.grid_style,column=4,row=4)

      cos = tk.Button(self,text="cos",**self.button_style_vert,command=lambda: self.AjouterValeurEntree("cos") )
      cos.grid(**self.grid_style,column=5,row=4)

      tan = tk.Button(self,text="tan",**self.button_style_vert,command=lambda: self.AjouterValeurEntree("tan") )
      tan.grid(**self.grid_style,column=4,row=5)

      arcsin = tk.Button(self,text="sin-1",**self.button_style_vert,command=lambda: self.AjouterValeurEntree("sin-1"))
      arcsin.grid(**self.grid_style,column=5,row=5)

      arccos = tk.Button(self,text="cos-1",**self.button_style_vert,command=lambda: self.AjouterValeurEntree("cos-1"))
      arccos.grid(**self.grid_style,column=4,row=6)

      arctan = tk.Button(self,text="tan−1",**self.button_style_vert,command=lambda: self.AjouterValeurEntree("tan-1") )
      arctan.grid(**self.grid_style,column=5,row=6)

      #Boutons Bleus#
      valeur_exponetielle = tk.Button(self,text="e",**self.button_style_bleu,command=lambda: self.AjouterValeurEntree(str(exp(1))) )
      valeur_exponetielle.grid(**self.grid_style,column=4,row=7)

      pi = tk.Button(self,text="π",**self.button_style_bleu,command=lambda: self.AjouterValeurEntree(str(pi)) )
      pi.grid(**self.grid_style,column=5,row=7)


      g = 1
      for i in range(3):
        
        for j in range(3):
          bouton_chiffre = tk.Button(self,text =str(g),**self.button_style,command=lambda t= g: self.AjouterValeurEntree(t))
          bouton_chiffre.grid(**self.grid_style,column=j,row=5-i)
          g+=1
      
    def AjouterValeurNPI(self,valeur:str):
      
      Empiler(self.valeurNPI,str(valeur))
      print(valeur,self.valeurNPI,"calc")
      self.AfficherValeurNPI()
      self.NettoyerEntree()
      
    def AfficherValeurNPI(self):
      
      texte = ""
      for val in self.valeurNPI:
        texte+=str(val)+" "
      self.affichage_NPI.set(texte)
    
    def NettoyerNPI(self):
      self.affichage_NPI.set("")
      self.valeurNPI = Creer_Pile()
      
  
    def EvaluerNPI(self):
        
        
      new_valeurNPI = Creer_Pile()
     
      Empiler(new_valeurNPI,str(Evaluer_calculatrice(self.valeurNPI)))
      self.valeurNPI = new_valeurNPI
      self.affichage_NPI.set(self.valeurNPI)

    
        
    
      
    def AjouterValeurEntree(self,valeur):
      if valeur == ".":
        self.is_point = True
      self.valeur_entree+=str(valeur)
      self.affichage_entree.set(self.valeur_entree)
      print(self.valeurNPI)
    
    def NettoyerEntree(self):
      self.affichage_entree.set("")
      
      self.valeur_entree = ""
      self.is_point = False
      
    def Memoire(self):
      op = None
      if not Pile_Vide(self.valeurNPI) and self.valeurNPI[-1] in "+-/*":
        op = Depiler(self.valeurNPI)
      
      if self.is_memoire_plein == False:
        valeur = Depiler(self.valeurNPI)
        Empiler(self.memoire,valeur)
        if op != None:
          Empiler(self.valeurNPI,op)
        
        self.AffichageMemoire()
        self.AfficherValeurNPI()
        self.is_memoire_plein = True
      else:
        valeur = Depiler(self.memoire)
        Empiler(self.valeurNPI,str(valeur))
        if op != None:
          Empiler(self.valeurNPI,str(op))
        self.NettoyerMemoire()
        self.AfficherValeurNPI()
        self.is_memoire_plein = False
    
        
    def AffichageMemoire(self):
      
      self.affichage_memoire.set("MEMOIRE : "+str(self.memoire[0]))
    def NettoyerMemoire(self):
      self.memoire = Creer_Pile()
      self.affichage_memoire.set("MEMOIRE : ")
    def Negatif(self):
      if self.valeurNPI[-1] not in "+*/-" and self.valeurNPI[-1] != "**":
        return

    def Appliquer(self,fonction):
      a = Depiler(self.valeurNPI)
      if a not in "*+/-" or a == "**":
        valeur = fonction(float(a))
        self.AjouterValeurNPI(str(valeur))
      else:
         b = Depiler(self.valeurNPI)
         valeur_bis = fonction(float(b))   
         self.AjouterValeurNPI(str(valeur_bis))
         self.AjouterValeurNPI(str(a))

    def Message_Erreur(self,message):
       self.NettoyerEntree()
       self.NettoyerNPI()
       messagebox.showerror("ERREUR : ",message)
          
          
if __name__ == "__main__":
    app = Calculatrie()
    app.mainloop()








