# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 11:02:56 2022

@author: costa
"""
from classes.cliente import Cliente
from classes.passageiro import Passageiro
from forms.tk_passageiro import Passageiro_tk
from tkinter import *
from tkinter import ttk

class Cliente_tk(Tk):
    def __init__(self):
        super().__init__()
        self.eval('tk::PlaceWindow . center')
        self.geometry('300x200+300+200')
        self.title('Cliente')
        self.create_menu()
        self.create_frames()
        self.create_buttons()
        self.create_entries()
        #self.pessoas = dict()
        self.mainloop()        

    def app_end(self):
		# ends the application
        self.destroy()
    
    def login(self):
        loginin= str(self.ent_nome.get())
        passin = str(self.ent_datan.get())

        if loginin in Cliente.clientes.keys():
            
                if passin == str(Cliente.clientes[loginin]):
                    self.destroy()
                    Passageiro.list_cc=[]
                    Passageiro.list_nome=[]
                    Passageiro.list_data=[]
                    Passageiro.list_telefone=[]
                    app= Passageiro_tk()
                    self._loginin=loginin
                elif str(Cliente.clientes[loginin]) != passin :
                    messagebox.showinfo('Erro!', 'Password incorreta', icon='error') 
            
        if loginin not in Cliente.clientes.keys():
            messagebox.showinfo('Erro!', 'Não existe nenhum Cliente com esse username', icon='warning') 

    def criar(self):
        novo_login= str(self.ent_nome.get())
        novo_pass = str(self.ent_datan.get())
        Cliente.clientes[novo_login] = novo_pass
   
    def create_menu(self):
        # creates the menus
        my_menu = Menu(self)
        self.config(menu = my_menu)
        menu = Menu(my_menu)
        my_menu.add_cascade(label='Sair', menu=menu)
        menu.add_command(label='quit', command = self.app_end)
    
    def create_frames(self):
        # creates the frames
        self.frame = Frame(self)
        self.frame.grid(row=0, column=0, padx=10, pady=10)
        
        self.frame_lotes = LabelFrame(self.frame, text='Cliente')
        self.frame_lotes.grid(row=0, column=0, padx=10, pady=10)
        
        self.frame_conf = Frame(self)
        self.frame_conf.grid(row=0, column=1, padx=10, pady=10)

        self.configure(background='light blue')
        self.frame.configure(background='light blue')
        
    def create_buttons(self):
        # creates the buttons
        self.btn_adicionar_lote = Button(self.frame_lotes, text='Login', command = self.login)
        self.btn_adicionar_lote.grid(row=4,column=0,padx=10, pady=10)

        self.btn_remover_lote = Button(self.frame_lotes, text='Criar novo cliente', command = self.criar)
        self.btn_remover_lote.grid(row=4,column=1,padx=10, pady=10)

    def create_entries(self):
        # creates the form labels and entries
        lbl_nome = Label(self.frame_lotes, text='Username:')
        lbl_nome.grid(row=0,column=0, padx=10,pady=10)
        self.ent_nome = Entry(self.frame_lotes)
        self.ent_nome.grid(row=0,column=1, padx=10,pady=10)
        
        lbl_datan = Label(self.frame_lotes, text='Password:')
        lbl_datan.grid(row=1,column=0, padx=10,pady=10)
        self.ent_datan = Entry(self.frame_lotes)
        self.ent_datan.grid(row=1,column=1, padx=10,pady=10)


#if __name__ == '__main__':
 #  ap = Cliente()
    
