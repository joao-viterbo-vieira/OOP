# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 18:08:03 2022

@author: costa
"""
from classes.passageiro import Passageiro
from forms.tk_viagem import Viagem_tk
from classes.viagem import Viagem
from tkinter import *
from tkinter import ttk

class Passageiro_tk(Tk):
    def __init__(self):
        super().__init__()
        self.eval('tk::PlaceWindow . center')
        self.geometry('470x510+300+200')
        self.title('Passageiros')
        self.create_menu()
        self.create_frames()
        self.create_buttons()
       
        self.create_entries()
        self.create_treeview()
        self.passageiros = dict()
        self.mainloop()        

    def app_end(self):
# ends the application
        self.destroy()
   
    def adicionar_pessoa(self):
        p = Passageiro(self.ent_numeroCC.get(),self.ent_nome.get(),self.ent_sata.get(),self.ent_telefone.get())
        self.passageiros[p.numeroCC] = p
        self.tv.insert('',index='end',iid=p.numeroCC, values=(p.numeroCC,p.nome,p.data,p.telefone))
        Passageiro.list_cc.append(p.numeroCC)
        Passageiro.list_nome.append(p.nome)
        Passageiro.list_data.append(p.data)
        Passageiro.list_telefone.append(p.telefone)
        #lista para adicionar os passageiros ao cliente
        
        
    def remover_pessoa(self):
        numeroCC = self.ent_numeroCC.get()
        del self.passageiros[numeroCC]
        self.tv.delete(numeroCC)
   
    def destino(self):
        if len(self.tv.get_children()) != 0:
            self.destroy()
            Viagem.list_dest=[]
            Viagem.list_data=[]
            Viagem.list_hora=[]
            Viagem.list_cod=[]
            Viagem.list_prec=[]
            ap = Viagem_tk()
        else:
            messagebox.showinfo('Erro!', 'Insira os dados de um passageiro', icon='warning')
           
   
   
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
       
        self.frame_passageiros = LabelFrame(self.frame, text='Passageiro')
        self.frame_passageiros.grid(row=0, column=0, padx=10, pady=10)
       
        self.frame_lista = LabelFrame(self.frame, text='Lista de Passageiros')
        self.frame_lista.grid(row=1, column=0, padx=10, pady=10)

        self.configure(background='light blue')
        self.frame.configure(background='light blue')
       
       
       
   
    def create_buttons(self):
        # creates the buttons
        self.btn_adicionar_passageiro = Button(self.frame_passageiros, text='Adicionar Passageiro', command = self.adicionar_pessoa, bg="snow")
        self.btn_adicionar_passageiro.grid(row=7,column=0,padx=10, pady=10)

        self.btn_remover_passageiro = Button(self.frame_passageiros, text='Remover Passageiro', command = self.remover_pessoa, bg="snow")
        self.btn_remover_passageiro.grid(row=7,column=1,padx=10, pady=10)
        
        self.btn_destino = Button(self.frame_passageiros, text='Escolher Destino', command = self.destino, bg="snow")
        self.btn_destino.grid(row=7,column=2,padx=10, pady=10)
       

    def create_entries(self):
        # creates the form labels and entries
        lbl_numeroCC = Label(self.frame_passageiros, text='numeroCC:')
        lbl_numeroCC.grid(row=0,column=0, padx=10,pady=10)
        self.ent_numeroCC = Entry(self.frame_passageiros)
        self.ent_numeroCC.grid(row=0,column=1, padx=10,pady=10)
       
        lbl_nome = Label(self.frame_passageiros, text='nome:')
        lbl_nome.grid(row=1,column=0, padx=10,pady=10)
        self.ent_nome = Entry(self.frame_passageiros)
        self.ent_nome.grid(row=1,column=1, padx=10,pady=10)

        lbl_sata = Label(self.frame_passageiros, text='data de nascimento:')
        lbl_sata.grid(row=2,column=0, padx=10,pady=10)
        self.ent_sata = Entry(self.frame_passageiros)
        self.ent_sata.grid(row=2,column=1, padx=10,pady=10)

        lbl_telefone = Label(self.frame_passageiros, text='telefone:')
        lbl_telefone.grid(row=3,column=0, padx=10,pady=10)
        self.ent_telefone = Entry(self.frame_passageiros)
        self.ent_telefone.grid(row=3,column=1, padx=10,pady=10)


       
    def create_treeview(self):
        self.tv = ttk.Treeview(self.frame_lista, show='headings', height=8)
        self.tv.pack(side=LEFT)
        self.tv['columns'] = ['numeroCC', 'nome', 'data de nascimento', 'telefone']
        self.tv.column('numeroCC', width=80)
        self.tv.column('nome', width=120)
        self.tv.column('data de nascimento', width=80)
        self.tv.column('telefone', width=80)
        self.tv.heading('numeroCC', text='numeroCC')
        self.tv.heading('nome', text='nome')
        self.tv.heading('data de nascimento', text='data de nascimento')
        self.tv.heading('telefone', text='telefone')
        self.sb = Scrollbar(self.frame_lista, orient=VERTICAL)
        self.sb.pack(side=RIGHT, fill=Y)
        self.tv.config(yscrollcommand=self.sb.set)
        self.sb.config(command=self.tv.yview)

       

#if __name__ == '__main__':
 #   ap = Passageiro_tk()