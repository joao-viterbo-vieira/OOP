# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 15:59:41 2022

@author: costa
"""

from classes.gclass import Gclass
from tkinter import messagebox
import datetime

class Cliente(Gclass):
    clientes = {}
    listaclientes=[]
    def __init__(self,nome, username, password):
        self._nome = nome
        self._username = username
        self._password = password
        self._listapassageiros=[]
        self._func = False
        Cliente.listaclientes.append(self)
        Cliente.clientes[username] = password
        
    @property 
    def username(self):
        return self._username
    
    @property 
    def password(self):
        return self._password 
    @password.setter 
    def password(self, novapass):
        return 
    
    @property 
    def numpassageiros(self):
        return self._numpassageiros
    
    def passageiros(self, numpassageiros):
        self._numpassageiros = numpassageiros
        return
    

#c1 = Cliente('ccc', 123)
#c1.clienteexiste('ccc')
#c1.clienteexiste('cbo')