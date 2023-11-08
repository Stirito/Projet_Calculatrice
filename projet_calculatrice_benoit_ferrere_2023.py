import tkinter as tk
from Piles import *


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




class Calculatrie(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculatrice")
        self.geometry("700x700")
        self.config(background="#292929")
        self.default_font = ("Arial", 26, "bold")
        self.grid_style = {"padx":10, "pady":10,"sticky": "nsew"}   
        self.button_style = {"bg": "#595959", "fg": "white", "highlightthickness": 0, "font": self.default_font}
        
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
      
      negatif = tk.Button(self,text="-()",**self.button_style,)
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
      
      g = 1
      for i in range(3):
        
        for j in range(3):
          bouton_chiffre = tk.Button(self,text =str(g),**self.button_style,command=lambda t= g: self.AjouterValeurEntree(t))
          bouton_chiffre.grid(**self.grid_style,column=j,row=5-i)
          g+=1
      
    def AjouterValeurNPI(self,valeur:str):
      
      Empiler(self.valeurNPI,str(valeur))
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
      if self.is_memoire_plein == False:
        valeur = Depiler(self.valeurNPI)
      
        Empiler(self.memoire,str(valeur))
        print(self.memoire,self.valeur_entree)
        self.AffichageMemoire()
        self.NettoyerNPI()
        self.is_memoire_plein = True
      
      else:
        valeur = Depiler(self.memoire)
        self.AjouterValeurNPI(str(valeur))
        
        self.NettoyerMemoire()
        self.is_memoire_plein = False
      
        
    def AffichageMemoire(self):
      
      self.affichage_memoire.set("MEMOIRE : "+str(self.memoire[0]))
    def NettoyerMemoire(self):
      self.memoire = Creer_Pile()
      self.affichage_memoire.set("MEMOIRE : ")
    def Negatif(self):
      if self.valeurNPI[-1] not in "+*/-" and self.valeurNPI[-1] != "**":
        return
        
if __name__ == "__main__":
    app = Calculatrie()
    
    app.mainloop()