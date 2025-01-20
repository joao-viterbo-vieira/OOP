# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 20:56:46 2022

@author: costa
"""

from classes.Voo import Voo
from classes.passageiro import Passageiro
from classes.viagem import Viagem
#from forms.tk_inicio import Inicio_tk
from tkinter import *
from tkinter import ttk
import tkinter as tk

class Lugares_tk(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500+300+200')
        self.eval('tk::PlaceWindow . center')
        self.title('Lugares')
        self.create_menu()
        self.create_frames()
        self.create_buttons()
        self.mainloop()        

    def app_end(self):
		# ends the application
        self.destroy()
   
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
        

    
    def create_buttons(self):
        # creates the buttons
    
        lbl_A = Label(self.frame, text='A')
        lbl_A.grid(row=0,column=0, padx=10,pady=10)
        
        lbl_B = Label(self.frame, text='B')
        lbl_B.grid(row=0,column=1, padx=10,pady=10)
        
        lbl_C = Label(self.frame, text='C')
        lbl_C.grid(row=0,column=2, padx=10,pady=10)
        
        lbl_D = Label(self.frame, text='D')
        lbl_D.grid(row=0,column=4, padx=10,pady=10)
        
        lbl_E = Label(self.frame, text='E')
        lbl_E.grid(row=0,column=5, padx=10,pady=10)
        
        lbl_F = Label(self.frame, text='F')
        lbl_F.grid(row=0,column=6, padx=10,pady=10)
        
        lbl_corredor = Label(self.frame, text='   ')
        lbl_corredor.grid(row=0,column=3, padx=10,pady=10) 
        
        lbl_1 = Label(self.frame, text='1')
        lbl_1.grid(row=1,column=7, padx=10,pady=10) 
        
        lbl_2 = Label(self.frame, text='2')
        lbl_2.grid(row=2,column=7, padx=10,pady=10) 
        
        lbl_3 = Label(self.frame, text='3')
        lbl_3.grid(row=3,column=7, padx=10,pady=10) 
        
        lbl_4 = Label(self.frame, text='4')
        lbl_4.grid(row=4,column=7, padx=10,pady=10) 
        
        lbl_5 = Label(self.frame, text='5')
        lbl_5.grid(row=5,column=7, padx=10,pady=10) 
        
        lbl_espaco1 = Label(self.frame, text='   ')
        lbl_espaco1.grid(row=6,column=3, padx=10,pady=10)
        
        lbl_verde = Label(self.frame, text='  livre  ', bg="green")
        lbl_verde.grid(row=7,column=1, padx=10,pady=10) 
        
        lbl_amarelo = Label(self.frame, text='reservado', bg="yellow")
        lbl_amarelo.grid(row=7,column=5, padx=10,pady=10) 
        
        self.btn_confirmar = Button(self.frame, text='Confimar', command = self.confirmar)
        self.btn_confirmar.grid(row=8,column=3,padx=10, pady=10)
        
        self.btn_fim = Button(self.frame, text='Terminar', command = self.terminar)
        self.btn_fim.grid(row=9,column=3,padx=10, pady=10)
        
        self.btn_A1 = Button(self.frame, text='      ', command = self.changeText_A1, bg="green")
        self.btn_A1.grid(row=1,column=0,padx=10, pady=10)
        
        self.btn_B1 = Button(self.frame, text='      ', command = self.changeText_B1, bg="green")
        self.btn_B1.grid(row=1,column=1,padx=10, pady=10)

        self.btn_C1= Button(self.frame, text='      ', command = self.changeText_C1, bg="green")
        self.btn_C1.grid(row=1,column=2,padx=10, pady=10)
        
        self.btn_D1 = Button(self.frame, text='      ', command = self.changeText_D1, bg="green")
        self.btn_D1.grid(row=1,column=4,padx=10, pady=10)
                
        self.btn_E1 = Button(self.frame, text='      ', command = self.changeText_E1, bg="green")
        self.btn_E1.grid(row=1,column=5,padx=10, pady=10)
        
        self.btn_F1 = Button(self.frame, text='      ', command = self.changeText_F1, bg="green")
        self.btn_F1.grid(row=1,column=6,padx=10, pady=10)

        self.btn_A2 = Button(self.frame, text='      ', command = self.changeText_A2, bg="green")
        self.btn_A2.grid(row=2,column=0,padx=10, pady=10)
        
        self.btn_B2 = Button(self.frame, text='      ', command = self.changeText_B2, bg="green")
        self.btn_B2.grid(row=2,column=1,padx=10, pady=10)

        self.btn_C2= Button(self.frame, text='      ', command = self.changeText_C2, bg="green")
        self.btn_C2.grid(row=2,column=2,padx=10, pady=10)
        
        self.btn_D2 = Button(self.frame, text='      ', command = self.changeText_D2, bg="green")
        self.btn_D2.grid(row=2,column=4,padx=10, pady=10)
        
        self.btn_E2 = Button(self.frame, text='      ', command = self.changeText_E2, bg="green")
        self.btn_E2.grid(row=2,column=5,padx=10, pady=10)
        
        self.btn_F2 = Button(self.frame, text='      ', command = self.changeText_F2, bg="green")
        self.btn_F2.grid(row=2,column=6,padx=10, pady=10)
        
        self.btn_A3 = Button(self.frame, text='      ', command = self.changeText_A3, bg="green")
        self.btn_A3.grid(row=3,column=0,padx=10, pady=10)
        
        self.btn_B3 = Button(self.frame, text='      ', command = self.changeText_B3, bg="green")
        self.btn_B3.grid(row=3,column=1,padx=10, pady=10)

        self.btn_C3 = Button(self.frame, text='      ', command = self.changeText_C3, bg="green")
        self.btn_C3.grid(row=3,column=2,padx=10, pady=10)
        
        self.btn_D3 = Button(self.frame, text='      ', command = self.changeText_D3, bg="green")
        self.btn_D3.grid(row=3,column=4,padx=10, pady=10)
        
        self.btn_E3 = Button(self.frame, text='      ', command = self.changeText_E3, bg="green")
        self.btn_E3.grid(row=3,column=5,padx=10, pady=10)
        
        self.btn_F3 = Button(self.frame, text='      ', command = self.changeText_F3, bg="green")
        self.btn_F3.grid(row=3,column=6,padx=10, pady=10)
        
        self.btn_A4 = Button(self.frame, text='      ', command = self.changeText_A4, bg="green")
        self.btn_A4.grid(row=4,column=0,padx=10, pady=10)
        
        self.btn_B4 = Button(self.frame, text='      ', command = self.changeText_B4, bg="green")
        self.btn_B4.grid(row=4,column=1,padx=10, pady=10)

        self.btn_C4 = Button(self.frame, text='      ', command = self.changeText_C4, bg="green")
        self.btn_C4.grid(row=4,column=2,padx=10, pady=10)
        
        self.btn_D4 = Button(self.frame, text='      ', command = self.changeText_D4, bg="green")
        self.btn_D4.grid(row=4,column=4,padx=10, pady=10)
        
        self.btn_E4 = Button(self.frame, text='      ', command = self.changeText_E4, bg="green")
        self.btn_E4.grid(row=4,column=5,padx=10, pady=10)
        
        self.btn_F4 = Button(self.frame, text='      ', command = self.changeText_F4, bg="green")
        self.btn_F4.grid(row=4,column=6,padx=10, pady=10)
    
        self.btn_A5 = Button(self.frame, text='      ', command = self.changeText_A5, bg="green")
        self.btn_A5.grid(row=5,column=0,padx=10, pady=10)
        
        self.btn_B5 = Button(self.frame, text='      ', command = self.changeText_B5, bg="green")
        self.btn_B5.grid(row=5,column=1,padx=10, pady=10)

        self.btn_C5 = Button(self.frame, text='      ', command = self.changeText_C5, bg="green")
        self.btn_C5.grid(row=5,column=2,padx=10, pady=10)
        
        self.btn_D5 = Button(self.frame, text='      ', command = self.changeText_D5, bg="green")
        self.btn_D5.grid(row=5,column=4,padx=10, pady=10)
        
        self.btn_E5 = Button(self.frame, text='      ', command = self.changeText_E5, bg="green")
        self.btn_E5.grid(row=5,column=5,padx=10, pady=10)
        
        self.btn_F5 = Button(self.frame, text='      ', command = self.changeText_F5, bg="green")
        self.btn_F5.grid(row=5,column=6,padx=10, pady=10)
        
    def aviso(self):
        return messagebox.showerror("Atenção!", "Este lugar já está reservado. Escolha outro!")   

    def confirmar(self):
        if len(Voo.lugares) == len(Passageiro.list_cc):
            with open("dados/dados_globais.csv", "a") as arquivo:
                for i in range(len(Passageiro.list_cc)):
                    arquivo.write(str(Passageiro.list_cc[i]) + ";" + str(Passageiro.list_nome[i]) + ";" + str(Passageiro.list_data[i]) + ";" + str(Passageiro.list_telefone[i]) + ";" + str(Viagem.list_dest[0]) + ";" + str(Viagem.list_data[0]) + ";" + str(Viagem.list_hora[0]) + ";" + str(Viagem.list_cod[0]) + ";" + str(Viagem.list_prec[0]) + ";" + str(Voo.lugares[i]) + "\n")
            total = len(Passageiro.list_cc) * int(Viagem.list_prec[0])
            return messagebox.showinfo("Confirmado!",f"Seleção de lugares confimada! \n Destino:{Viagem.list_dest[0]}   Total:{total}")
            
        #messagebox.showinfo('Erro!', 'Insira os dados de um passageiro', icon='warning')
        else:
            dif = int(len(Passageiro.list_cc)) - int(len(Voo.lugares))
            return messagebox.showerror("Atenção!", f"Ainda precisa de escolher os lugares de {dif} Passageiro")
        
    def terminar(self):
       self.destroy()
     
        
    def changeText_A1 (self):
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else:  
            self.btn1_A1 = Button(self.frame, text='      ',command=self.aviso, bg="yellow")
            self.btn1_A1.grid(row=1,column=0,padx=10, pady=10)
            Voo.lugares_dict["A1"] = "reservado"
            Voo.lugares.append("A1")
        
    def changeText_B1(self):  
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_B1 = Button(self.frame, text='      ',command=self.aviso, bg="yellow")
            self.btn_B1.grid(row=1,column=1,padx=10, pady=10)
            Voo.lugares_dict["B1"] = "reservado"
            Voo.lugares.append("B1")
        
    def changeText_C1(self): 
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_C1 = Button(self.frame, text='      ',command=self.aviso,   bg="yellow")
            self.btn_C1.grid(row=1,column=2,padx=10, pady=10)
            Voo.lugares_dict["C1"] = "reservado"
            Voo.lugares.append("C1")
        
    def changeText_D1(self):    
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_D1 = Button(self.frame, text='      ',command=self.aviso,   bg="yellow")
            self.btn_D1.grid(row=1,column=4,padx=10, pady=10)
            Voo.lugares_dict["D1"] = "reservado"
            Voo.lugares.append("D1")
        
    def changeText_E1(self):   
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_E1 = Button(self.frame, text='      ',command=self.aviso,   bg="yellow")
            self.btn_E1.grid(row=1,column=5,padx=10, pady=10)
            Voo.lugares_dict["E1"] = "reservado"
            Voo.lugares.append("E1")
        
    def changeText_F1(self):    
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_F1 = Button(self.frame, text='      ',command=self.aviso,  bg="yellow")
            self.btn_F1.grid(row=1,column=6,padx=10, pady=10)
            Voo.lugares_dict["F1"] = "reservado"
            Voo.lugares.append("F1")
        
    def changeText_A2 (self):
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn1_A2 = Button(self.frame, text='      ',command=self.aviso, bg="yellow")
            self.btn1_A2.grid(row=2,column=0,padx=10, pady=10)
            Voo.lugares_dict["A2"] = "reservado"
            Voo.lugares.append("A2")
        
    def changeText_B2(self):   
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_B2 = Button(self.frame, text='      ',command=self.aviso, bg="yellow")
            self.btn_B2.grid(row=2,column=1,padx=10, pady=10)
            Voo.lugares_dict["B2"] = "reservado"
            Voo.lugares.append("B2")
        
    def changeText_C2(self): 
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_C2 = Button(self.frame, text='      ',command=self.aviso,   bg="yellow")
            self.btn_C2.grid(row=2,column=2,padx=10, pady=10)
            Voo.lugares_dict["C2"] = "reservado"
            Voo.lugares.append("C2")
        
    def changeText_D2(self):    
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_D2 = Button(self.frame, text='      ',command=self.aviso,   bg="yellow")
            self.btn_D2.grid(row=2,column=4,padx=10, pady=10)
            Voo.lugares_dict["D2"] = "reservado"
            Voo.lugares.append("D2")
        
    def changeText_E2(self):    
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_E2 = Button(self.frame, text='      ',command=self.aviso,   bg="yellow")
            self.btn_E2.grid(row=2,column=5,padx=10, pady=10)
            Voo.lugares_dict["E2"] = "reservado"
            Voo.lugares.append("E2")
        
    def changeText_F2(self):  
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else:
            self.btn_F2 = Button(self.frame, text='      ',command=self.aviso,  bg="yellow")
            self.btn_F2.grid(row=2,column=6,padx=10, pady=10)
            Voo.lugares_dict["F2"] = "reservado"
            Voo.lugares.append("F2")
        
    def changeText_A3 (self):
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn1_A3 = Button(self.frame, text='      ',command=self.aviso, bg="yellow")
            self.btn1_A3.grid(row=3,column=0,padx=10, pady=10)
            Voo.lugares_dict["A3"] = "reservado"
            Voo.lugares.append("A3")
        
    def changeText_B3(self):   
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_B3 = Button(self.frame, text='      ',command=self.aviso, bg="yellow")
            self.btn_B3.grid(row=3,column=1,padx=10, pady=10)
            Voo.lugares_dict["B3"] = "reservado"
            Voo.lugares.append("B3")
        
    def changeText_C3(self): 
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_C3 = Button(self.frame, text='      ',command=self.aviso,   bg="yellow")
            self.btn_C3.grid(row=3,column=2,padx=10, pady=10)
            Voo.lugares_dict["C3"] = "reservado"
            Voo.lugares.append("C3")
        
    def changeText_D3(self):    
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_D3 = Button(self.frame, text='      ',command=self.aviso,   bg="yellow")
            self.btn_D3.grid(row=3,column=4,padx=10, pady=10)
            Voo.lugares_dict["D3"] = "reservado"
            Voo.lugares.append("D3")
        
    def changeText_E3(self):   
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_E3 = Button(self.frame, text='      ',command=self.aviso,   bg="yellow")
            self.btn_E3.grid(row=3,column=5,padx=10, pady=10)
            Voo.lugares_dict["E3"] = "reservado"
            Voo.lugares.append("E3")
        
    def changeText_F3(self):    
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_F3 = Button(self.frame, text='      ',command=self.aviso,  bg="yellow")
            self.btn_F3.grid(row=3,column=6,padx=10, pady=10)
            Voo.lugares_dict["F3"] = "reservado"
            Voo.lugares.append("F3")
        
    def changeText_A4 (self):
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn1_A4 = Button(self.frame, text='      ',command=self.aviso, bg="yellow")
            self.btn1_A4.grid(row=4,column=0,padx=10, pady=10)
            Voo.lugares_dict["A4"] = "reservado"
            Voo.lugares.append("A4")
        
    def changeText_B4(self):  
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else:
            self.btn_B4 = Button(self.frame, text='      ',command=self.aviso, bg="yellow")
            self.btn_B4.grid(row=4,column=1,padx=10, pady=10)
            Voo.lugares_dict["B4"] = "reservado"
            Voo.lugares.append("B4")
        
    def changeText_C4(self): 
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_C4 = Button(self.frame, text='      ',command=self.aviso,   bg="yellow")
            self.btn_C4.grid(row=4,column=2,padx=10, pady=10)
            Voo.lugares_dict["C4"] = "reservado"
            Voo.lugares.append("C4")
        
    def changeText_D4(self):    
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_D4 = Button(self.frame, text='      ',command=self.aviso,   bg="yellow")
            self.btn_D4.grid(row=4,column=4,padx=10, pady=10)
            Voo.lugares_dict["D4"] = "reservado"
            Voo.lugares.append("D4")
        
    def changeText_E4(self):    
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_E4 = Button(self.frame, text='      ',command=self.aviso,   bg="yellow")
            self.btn_E4.grid(row=4,column=5,padx=10, pady=10)
            Voo.lugares_dict["E4"] = "reservado"
            Voo.lugares.append("E4")
        
    def changeText_F4(self):    
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_F4 = Button(self.frame, text='      ',command=self.aviso,  bg="yellow")
            self.btn_F4.grid(row=4,column=6,padx=10, pady=10)
            Voo.lugares_dict["F4"] = "reservado"
            Voo.lugares.append("F4")
        
    def changeText_A5 (self):
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn1_A5 = Button(self.frame, text='      ',command=self.aviso, bg="yellow")
            self.btn1_A5.grid(row=5,column=0,padx=10, pady=10)
            Voo.lugares_dict["A5"] = "reservado"
            Voo.lugares.append("A5")
        
    def changeText_B5(self): 
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_B5 = Button(self.frame, text='      ',command=self.aviso, bg="yellow")
            self.btn_B5.grid(row=5,column=1,padx=10, pady=10)
            Voo.lugares_dict["B5"] = "reservado"
            Voo.lugares.append("B5")
        
    def changeText_C5(self): 
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_C5 = Button(self.frame, text='      ',command=self.aviso,   bg="yellow")
            self.btn_C5.grid(row=5,column=2,padx=10, pady=10)
            Voo.lugares_dict["C5"] = "reservado"
            Voo.lugares.append("C5")
        
    def changeText_D5(self): 
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_D5 = Button(self.frame, text='      ',command=self.aviso,   bg="yellow")
            self.btn_D5.grid(row=5,column=4,padx=10, pady=10)
            Voo.lugares_dict["D5"] = "reservado"
            Voo.lugares.append("D5")
        
    def changeText_E5(self):    
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_E5 = Button(self.frame, text='      ',command=self.aviso,   bg="yellow")
            self.btn_E5.grid(row=5,column=5,padx=10, pady=10)
            Voo.lugares_dict["E5"] = "reservado"
            Voo.lugares.append("E5")
        
    def changeText_F5(self):
        if len(Voo.lugares) == len(Passageiro.list_cc):
            return messagebox.showerror(" Atenção!!!","Já escolheu os lugares necessários")
        else: 
            self.btn_F5 = Button(self.frame, text='      ',command=self.aviso,  bg="yellow")
            self.btn_F5.grid(row=5,column=6,padx=10, pady=10)
            Voo.lugares_dict["F5"] = "reservado"
            Voo.lugares.append("F5")
    
        

#if __name__ == '__main__':
 #   ap = Lugares_tk()