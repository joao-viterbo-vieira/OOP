# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 14:52:00 2022

@author: costa
"""

from forms.tk_funcionario import Funcionario_tk
from forms.tk_cliente import Cliente_tk
from classes.cliente import Cliente
from classes.funcionario import Funcionario
from classes.passageiro import Passageiro
from tkinter import *
from tkinter import ttk

class Inicio_tk(Tk):
    dadosimp= False
    def __init__(self):
        super().__init__()
        self.eval('tk::PlaceWindow . center')
        self.geometry('300x200')
        self.title('Aviões')
        self.create_menu()
        self.create_frames()
        self.create_buttons()
        self.mainloop()      

    def app_end(self):
		# ends the application
        self.destroy()
    
    def openfuncionario(self):
        self.destroy()
        ap2 = Funcionario_tk()
        
    def opencliente(self):
        self.destroy()
        ap3 = Cliente_tk()
        
    def importardados(self):
        if Inicio_tk.dadosimp==False:
            
           #importar clientes:
            fclientes = open('dados/Clientes.csv', 'r')
            for line in fclientes:
                linha=line.strip('\n')
                Cliente.from_string(linha)
            fclientes.close()
            #importar funcionarios
            ffuncionarios = open('dados/funcionarios.csv', 'r')
            for line in ffuncionarios:
                linha=line.strip('\n')
                Funcionario.from_string(linha)
            #importar passageiros
            fpassageiros = open('dados/Passageiro.csv', 'r')
            for line in fpassageiros:
                linha=line.strip('\n')
                Passageiro.from_string(linha)
            
            #final da importação
            messagebox.showinfo(title='Atualizado', message="Os dados foram importados")
            Inicio_tk.dadosimp=True
            
        else:
            messagebox.showwarning(title='Atualizado', message="Os dados já foram importados")
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
        
        self.frame_lotes = LabelFrame(self.frame, text='Funcionário')
        self.frame_lotes.grid(row=0, column=0, padx=10, pady=10)
        
        self.frame_conf = Frame(self)
        self.frame_conf.grid(row=0, column=1, padx=10, pady=10)
        
        self.configure(background='DodgerBlue2')
        self.frame.configure(background='light blue')
        
        
    def create_buttons(self):
        # creates the buttons
        self.btn_func = Button(self.frame, text='Funcionário', command= self.openfuncionario, bg='light yellow')
        self.btn_func.grid(row=1,column=0,padx=10, pady=30)
        
        self.btn_cli = Button(self.frame, text='Cliente', command= self.opencliente, bg='light blue')
        self.btn_cli.grid(row=1,column=2,padx=10, pady=30)
        
        self.btn_imp = Button(self.frame, text='Importar dados', command= self.importardados, bg='snow')
        self.btn_imp.grid(row=2,column=1,padx=10, pady=10)
              
        

if __name__ == '__main__':
    ap = Inicio_tk()