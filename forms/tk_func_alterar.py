# -*- coding: utf-8 -*-
"""
@author: costa


#%%
"""""


from forms.tk_alt_viagem import viagens
from classes.passageiro import Passageiro
from forms.openform import OpenForm
from tkinter import *

class Alterar(Tk):
    def __init__(self):
        super().__init__()
        # Set the window title
        self.title('Funcionario')
        self.eval('tk::PlaceWindow . center')
        self.create_buttons()
        self.geometry('500x100+300+200')
        self.path = 'dados/'
        self.mode = 1# edit off (editmode = 0)
        self.mode2 = 1
        # if login is off (user='') or user group equal to admin -> edit on
        
        
            
        # Reads the objects from all the classes
        viagens.read(self.path)
        
        # Reads the objects from all the classes
        Passageiro.read(self.path) 
        
        
        
    def call_utente(self):
        labels = ['Código:', 'Data:', 'Hora:', 'Destino:', 'Preço:']
        s1 = OpenForm(self, viagens, labels, 
                      filePath=self.path, editmode = self.mode)
  
        
    def call_passageiro(self):
        labels = ['Número CC:', 'Nome:', 'Data nascimento:', 'Telefone:']
        s1 = OpenForm(self, Passageiro, labels, 
                      filePath=self.path, editmode = self.mode)
   
    
        
    def call_exit(self):
        self.destroy()
        
    def create_buttons(self):
        # Creates the buttons
        btn_p = Button(self, text='Alterar Viagens', command=self.call_utente, bg='light blue')
        btn_p.grid(row=0, column=20, padx = 100, pady = 10)
        
        btn_q = Button(self, text='Exit', command=self.call_exit, bg='light blue')
        btn_q.grid(row=0, column=40, padx = 0, pady = 0)

        btn_K = Button(self, text='Alterar Passageiros', command=self.call_passageiro, bg='light blue')
        btn_K.grid(row=1, column=20, padx = 100, pady = 10)

#if __name__ == '__main__':
 #  ap = Alterar()
   #Loop until it is closed by the user
  # ap.mainloop()
     
