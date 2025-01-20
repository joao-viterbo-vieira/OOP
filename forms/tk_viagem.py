# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 18:52:04 2022

@author: costa
"""

#from viagem import Viagem
from tkinter import *
from tkinter import ttk
import pandas as pd
from forms.tk_lugares import Lugares_tk
from classes.viagem import Viagem
from classes.Voo import Voo
class Viagem_tk(Tk):
    
    def __init__(self):
        super().__init__()
        self.geometry('420x450+300+200')
        self.title('Viagens')
        self.create_menu()
        self.create_frames()
        self.create_buttons()
        self.create_entries()
        self.create_treeview()
        self.lotes = dict()
        self.mainloop()        

    def app_end(self):
		# ends the application
        self.destroy()
    
    def pesquisar(self):
        
        for record in self.tv.get_children():
            self.tv.delete(record)
        
        cb_selected=self.combo_box.get()
        fh= open('dados/viagens.csv','r')
        
        for line in fh :
            lista=line.strip().split(";")
            if lista[3] == cb_selected:
                self.tv.insert("", index="end", values=(lista[1],lista[2],lista[0],lista[4]))
                

    def marcar(self):
        cb_selected=self.combo_box.get()
        Viagem.list_dest.append(cb_selected)
        
        try:
            vg_selec=self.tv.selection()[0]
            valores=self.tv.item(vg_selec, "values")
            
            Viagem.list_data.append(valores[0])
            Viagem.list_hora.append(valores[1])
            Viagem.list_cod.append(valores[2])
            Viagem.list_prec.append(valores[3])
            self.destroy()
            Voo.lugares = []
            app = Lugares_tk()
            
            
        except:
            messagebox.showinfo(title="Erro", message="Selecione primeiro uma viagem!")
        
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
        
        self.frame_lotes = LabelFrame(self.frame, text='Viagem')
        self.frame_lotes.grid(row=0, column=0, padx=10, pady=10)
        
        self.frame_lista = LabelFrame(self.frame, text='Lista Viagens')
        self.frame_lista.grid(row=1, column=0, padx=10, pady=10)

        self.frame_conf = Frame(self)
        self.frame_conf.grid(row=0, column=1, padx=10, pady=10)
        
        self.configure(background='SkyBlue1')
        self.frame.configure(background='SkyBlue1')
        
    
    def create_buttons(self):
        # creates the buttons
        self.btn_pesquisar = Button(self.frame_lotes, text='Pesquisar viagens', command = self.pesquisar, bg="snow")
        self.btn_pesquisar.grid(row=4,column=1,padx=10, pady=10)
        
        self.btn_marcar_viagem = Button(self.frame, text='Marcar viagem', command = self.marcar, bg="snow")
        self.btn_marcar_viagem.grid(row=40,column=0,padx=10, pady=10)
    
        
    def create_entries(self):
        # creates the form labels and entries
       
        lbl_box=Label(self.frame_lotes, text = 'Destinos:')
        lbl_box.grid(row=2, column=0, padx=10, pady=10)
        lista_types = []
        fh=open("dados/viagens.csv", "r")
        
        for line in fh:
            aux=line.strip().split(";")
            if aux[3] not in lista_types:
                lista_types.append(aux[3])
        lista_types.pop(0)
        
        self.selectedValue = StringVar()
        #print (self.selectedValue)
        
        self.combo_box = ttk.Combobox(self.frame_lotes, textvariable = self.selectedValue, value = lista_types, state="readonly")
        self.combo_box.grid(row=2,column =1, sticky = W)
        
    def create_treeview(self):
        self.tv = ttk.Treeview(self.frame_lista, show='headings', height=8)
        self.tv.pack(side=LEFT)
        self.tv['columns'] = [ 'data', 'hora', 'código',"preco"]
      
        self.tv.column('data', width=80)
        self.tv.column('hora', width=80)
        self.tv.column('código', width=80)
        self.tv.column('preco', width=80)
        
        
        self.tv.heading('data', text='Data')
        self.tv.heading('hora', text='Hora')
        self.tv.heading('código', text='Código')
        self.tv.heading('preco', text='Preço (€)')
        self.sb = Scrollbar(self.frame_lista, orient=VERTICAL)
        self.sb.pack(side=RIGHT, fill=Y)
        self.tv.config(yscrollcommand=self.sb.set)
        self.sb.config(command=self.tv.yview)

        

#if __name__ == '__main__':
 #  ap = Viagem_tk()


    